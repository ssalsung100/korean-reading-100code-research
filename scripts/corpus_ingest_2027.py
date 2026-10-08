#!/usr/bin/env python3
"""기계적 KICE corpus 중앙화·staging·검증·merge 도구.

이 도구는 문항을 풀거나 의미를 판정하지 않고, 검수완료 원문 MD와
공식 answer 대조가 기록된 원자료를 구조화한다.
"""
from __future__ import annotations
import hashlib, json, re, shutil, sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CENTRAL = ROOT / "data/기출_MD_정본"
STAGE = ROOT / "data/corpus_ingest"
ANNUAL = ROOT / "고3 기출/hwpx_텍스트_연도별.md"
KPASS = ROOT / "data/kice_passages.jsonl"
KQUES = ROOT / "data/kice_questions.jsonl"

def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()

def jdump(x) -> str:
    return json.dumps(x, ensure_ascii=False, separators=(",", ":"))

def exam_dir(label: str) -> str:
    if label == "예시문항": return "예시문항"
    if label == "수능" or label.startswith("수능"): return label.replace(" ", "_")
    return label.replace(" ", "_")

def clean_md(s: str) -> str:
    # 전사 MD의 인용 blockquote를 원문 줄로 되돌린다.
    s = re.sub(r"^> ?", "", s, flags=re.M)
    s = re.sub(r"^\*\*(.*?)\*\*$", r"\1", s, flags=re.M)
    return s.strip()

def parse_2027(p: Path):
    s = p.read_text()
    head = re.search(r"^# (\d+)학년도 (6월|9월) 모의평가 국어 (\d+)~(\d+)번", s, re.M)
    assert head
    year, month, qlo, qhi = int(head.group(1)), head.group(2), int(head.group(3)), int(head.group(4))
    qsections = list(re.finditer(r"^## (\d+)\. (.*?)(?=^## (?:\d+\. |정답)|\Z)", s, re.M | re.S))
    first = re.search(r"^## \[.*?\].*?$", s, re.M)
    assert first
    passage = clean_md(s[first.end():qsections[0].start()])
    passage = re.sub(r"^\s*---\s*$", "", passage, flags=re.M).strip()
    answers_block = s[s.find("## 정답"):]
    answers = {int(a): b for a, b in re.findall(r"^\s*(\d+)\.\s*([①②③④⑤])", answers_block, re.M)}
    questions = []
    for m in qsections:
        n, body = int(m.group(1)), m.group(2).strip()
        marks = list(re.finditer(r"(?m)^([①②③④⑤])", body))
        if len(marks) == 5:
            stem = clean_md(body[:marks[0].start()]).strip()
            choices = []
            for i, mark in enumerate(marks):
                end = marks[i+1].start() if i < 4 else len(body)
                choices.append(clean_md(body[mark.end():end]).replace("\n", " ").strip())
        else:
            # 표로 제시된 선지(2027 9월 9번)는 표의 각 행을 한 선지로 보존한다.
            rows = re.findall(r"^\|\s*([①②③④⑤])\s*\|([^|]*)\|([^|]*)\|\s*$", body, re.M)
            assert len(rows) == 5, (p, n, len(marks), len(rows))
            first_row = re.search(r"^\|\s*①\s*\|", body, re.M)
            stem = clean_md(body[:first_row.start()]).strip()
            choices = [f"ⓐ {a.strip()} / ⓑ {b.strip()}" for _, a, b in rows]
        questions.append((n, stem, choices, answers[n]))
    return year, month, qlo, qhi, passage, questions, sha(p)

def main():
    reindex = "--reindex" in sys.argv
    kp = [json.loads(x) for x in KPASS.read_text().splitlines() if x.strip()]
    kq = [json.loads(x) for x in KQUES.read_text().splitlines() if x.strip()]
    existing_p = {(x["academic_year"], x["exam_label"], x["passage_id"]) for x in kp}
    existing_q = {(x["academic_year"], x["exam_label"], x["question_id"], x["question_number"]) for x in kq}
    for d in [CENTRAL, STAGE, STAGE / "backups"]: d.mkdir(parents=True, exist_ok=True)
    (CENTRAL / "연도별").mkdir(exist_ok=True)

    # 기존 163개 독서군을 원본 연도별 MD에서 section 단위로 중앙화한다.
    annual_text = ANNUAL.read_text()
    annual_hash = sha(ANNUAL)
    sections = list(re.finditer(r"^### (\[[^\]]+\]) (\d+)학년도 (.+?) (\d+)번~(\d+)번\s*$", annual_text, re.M))
    central_entries = []
    for i, m in enumerate(sections):
        end = sections[i+1].start() if i+1 < len(sections) else len(annual_text)
        block = annual_text[m.start():end].rstrip() + "\n"
        year, label, lo, hi = int(m.group(2)), m.group(3), int(m.group(4)), int(m.group(5))
        # 다음 연도/목차 heading이 섞이지 않도록 section 본문만 유지
        block = re.split(r"^## \d+학년도\s*$", block, maxsplit=1, flags=re.M)[0].rstrip()+"\n"
        d = CENTRAL / "연도별" / str(year) / exam_dir(label) / "독서"
        d.mkdir(parents=True, exist_ok=True)
        # 동일 시험·문항 범위에 복수 지문이 있을 수 있으므로 source section
        # 식별자를 파일명에 포함해 충돌을 방지한다.
        fn = f"Q{lo:02d}-{hi:02d}-S{m.group(1).strip('[]').replace('~','-')}.md"
        out = d / fn
        if not out.exists(): out.write_text(block)
        central_entries.append({"academic_year":year,"exam_label":label,"area":"독서","path":str(out.relative_to(CENTRAL)),"source_original_path":str(ANNUAL),"source_sha256":annual_hash,"status":"CENTRALIZED_EXISTING_CANONICAL"})

    staging_p, staging_q, provenance = [], [], []
    source_md_paths = []
    for p in sorted((ROOT/"자료/평가원_국어/전사_검수완료/2027").rglob("*.md")):
        year, month, lo, hi, passage, questions, mdhash = parse_2027(p)
        label = f"{month} 모평"
        area = "문학" if lo == 4 else "독서"
        target = CENTRAL/"연도별"/str(year)/exam_dir(label)/area
        target.mkdir(parents=True, exist_ok=True)
        dest = target/p.name
        if not dest.exists(): shutil.copy2(p, dest)
        central_entries.append({"academic_year":year,"exam_label":label,"area":area,"path":str(dest.relative_to(CENTRAL)),"source_original_path":str(p),"source_sha256":mdhash,"status":"CENTRALIZED_NEW_SOURCE"})
        source_md_paths.append(str(p))
        if area == "문학":
            continue
        pid = f"KICE-{year}-{label}-Q{lo}-{hi}-2027{month}"
        # canonical passage id는 시험·범위 기반이며 충돌이 없어야 한다.
        pid = f"KICE-{year}-{label}-Q{lo:02d}-{hi:02d}-S2027{month}"
        prow = {"passage_id":pid,"exam_family":"KICE","academic_year":year,"exam_label":label,"exam_type":"수능 모의평가","month":month,"variant":None,"question_start":lo,"question_end":hi,"question_count":len(questions),"dataset_section_id":f"2027-{month}-{lo:02d}~{hi:02d}","source_hwpx":None,"unit":"공식 전사 검수완료","passage_text":passage,"passage_sha256":hashlib.sha256(passage.encode()).hexdigest(),"contains_visual_placeholder":("![" in passage),"answer_link_status":"linked","answer_table_ids":[f"KICE-2027-{month}-official"],"source_markdown":str(p)}
        staging_p.append(prow)
        for n, stem, choices, ans in questions:
            qid = f"{pid}-Q{n}"
            visual = "![" in stem
            qrow = {"question_id":qid,"passage_id":pid,"exam_family":"KICE","academic_year":year,"exam_label":label,"exam_type":"수능 모의평가","month":month,"variant":None,"question_number":n,"dataset_question_id":f"2027-{month}-{n:02d}","stem":stem,"choices":choices,"choice_parse_status":"complete","contains_visual_placeholder":visual,"answer":ans,"answer_candidates":{"common":ans},"official_answer_verified":True,"answer_link_status":"linked","raw_section_sha256":mdhash}
            staging_q.append(qrow)
            provenance.append({"record_type":"question","question_id":qid,"source_path":str(p),"source_type":"official_pdf_verified_transcription","academic_year":year,"exam_label":label,"question_number":n,"extraction_method":"verified_markdown_transcription","source_hash":mdhash,"visual_asset_paths":(["자료/평가원_국어/시각자료_원본/2027/q09_선지_대응표.png"] if year==2027 and month=="9월" and n==9 else ["자료/평가원_국어/시각자료_원본/2027/q13_어댑터_구조도.png"] if year==2027 and month=="9월" and n==13 else []),"source_confidence":"high"})
        provenance.append({"record_type":"passage","passage_id":pid,"source_path":str(p),"source_type":"official_pdf_verified_transcription","academic_year":year,"exam_label":label,"question_number":lo,"extraction_method":"verified_markdown_transcription","source_hash":mdhash,"visual_asset_paths":[],"source_confidence":"high"})

    # asset 중앙화: 이미 추출·대조된 바이너리를 보존 복사
    assets = []
    for name in ["q09_선지_대응표.png","q13_어댑터_구조도.png"]:
        src=ROOT/"자료/평가원_국어/시각자료_원본/2027"/name
        dest=CENTRAL/"assets"/"2027"/"9월_모평"/name
        dest.parent.mkdir(parents=True,exist_ok=True)
        if not dest.exists(): shutil.copy2(src,dest)
        assets.append({"source_path":str(src),"central_path":str(dest.relative_to(CENTRAL)),"sha256":sha(src)})

    # validation
    epids={x["passage_id"] for x in kp}; eqids={x["question_id"] for x in kq}
    errors=[]; statuses=[]
    seenp=set(); seenq=set()
    for x in staging_p:
        status="READY_TO_MERGE"
        if (not reindex and x["passage_id"] in epids) or x["passage_id"] in seenp: status="DUPLICATE"
        seenp.add(x["passage_id"]); statuses.append(("passage",x["passage_id"],status))
        if not x["passage_text"].strip(): errors.append((x["passage_id"],"empty passage"))
    for x in staging_q:
        status="READY_TO_MERGE"
        if (not reindex and x["question_id"] in eqids) or x["question_id"] in seenq: status="DUPLICATE"
        if len(x["choices"]) != 5 or not x["stem"].strip() or x["passage_id"] not in {p["passage_id"] for p in staging_p}: status="UNRESOLVED"
        seenq.add(x["question_id"]); statuses.append(("question",x["question_id"],status))
    for typ, rid, st in statuses:
        if st != "READY_TO_MERGE": errors.append((rid,st))
    if errors: raise RuntimeError(errors)

    # timestamp backup 없이도 복구 가능한 append 전 사본
    if not reindex:
        shutil.copy2(KPASS, STAGE/"backups"/"kice_passages.pre_merge.jsonl")
        shutil.copy2(KQUES, STAGE/"backups"/"kice_questions.pre_merge.jsonl")
    with (STAGE/"staging_passages.jsonl").open("w") as f:
        for x in staging_p: f.write(jdump(x)+"\n")
    with (STAGE/"staging_questions.jsonl").open("w") as f:
        for x in staging_q: f.write(jdump(x)+"\n")
    with (STAGE/"ingest_provenance.jsonl").open("w") as f:
        for x in provenance: f.write(jdump(x)+"\n")
    if not reindex:
        with KPASS.open("a") as f:
            for x in staging_p: f.write(jdump(x)+"\n")
        with KQUES.open("a") as f:
            for x in staging_q: f.write(jdump(x)+"\n")

    # inventory: canonical 2010~2026 reading units + discovered 2027 reading/literature
    groups=defaultdict(lambda:{"reading_source_present":False,"literature_source_present":False,"reading_md_present":False,"literature_md_present":False,"canonical_reading_present":False,"canonical_literature_present":False,"question_range":[],"source_paths":[],"md_paths":[],"visual_assets":[],"issues":[]})
    for x in kp:
        g=groups[(x["academic_year"],x["exam_label"])]
        g["reading_source_present"]=True; g["reading_md_present"]=True; g["canonical_reading_present"]=True; g["question_range"].append(f"{x['question_start']}-{x['question_end']}"); g["source_paths"].append(x.get("source_hwpx")); g["md_paths"].append(x.get("source_markdown"))
    for e in central_entries:
        g=groups[(e["academic_year"],e["exam_label"])]
        if e["area"] == "독서":
            g["reading_source_present"] = True; g["reading_md_present"] = True
        else:
            g["literature_source_present"] = True; g["literature_md_present"] = True
        g["md_paths"].append(e["path"]); g["source_paths"].append(e["source_original_path"])
    inventory=[]
    for (year,label),g in sorted(groups.items()):
        g["question_range"]=sorted(set(g["question_range"]))
        g["source_paths"]=sorted(set(x for x in g["source_paths"] if x))
        g["md_paths"]=sorted(set(x for x in g["md_paths"] if x))
        g["visual_assets"]=assets if year==2027 else []
        if g["literature_source_present"] and not g["canonical_literature_present"]: g["issues"].append("canonical_ingest_status=unsupported_current_schema")
        if not g["literature_source_present"]: g["issues"].append("MISSING_SOURCE:문학")
        inventory.append({"academic_year":year,"exam_label":label,**g})
    (STAGE/"ingest_inventory.json").write_text(json.dumps({"generated_by":"corpus_ingest_2027.py","canonical_after_merge":{"passages":len(kp) if reindex else len(kp)+len(staging_p),"questions":len(kq) if reindex else len(kq)+len(staging_q)},"exams":inventory,"assets":assets},ensure_ascii=False,indent=2)+"\n")

    read_count=sum(1 for e in central_entries if e["area"]=="독서")
    lit_count=sum(1 for e in central_entries if e["area"]=="문학")
    idx={"description":"연도별 평가원/수능 국어 Markdown 중앙 탐색 색인","entries":central_entries,"exams":inventory,"assets":assets}
    (CENTRAL/"index.json").write_text(json.dumps(idx,ensure_ascii=False,indent=2)+"\n")
    lines=["# 평가원·수능 국어 Markdown 중앙 색인","","> 원문 보존용 중앙 탐색 view. 해설·정답 추론·코드 분석을 포함하지 않는다.",""]
    for year in sorted({e["academic_year"] for e in central_entries}):
        lines += [f"# {year}",""]
        for label in sorted({e["exam_label"] for e in central_entries if e["academic_year"]==year}):
            lines += [f"## {label}",""]
            for area in ["독서","문학"]:
                es=[e for e in central_entries if e["academic_year"]==year and e["exam_label"]==label and e["area"]==area]
                lines += [f"### {area}",""]
                if es:
                    for e in es: lines.append(f"- [{Path(e['path']).name}]({e['path']}) — {e['status']}")
                else: lines.append("- MISSING_MD")
                lines.append("")
    (CENTRAL/"INDEX.md").write_text("\n".join(lines))
    (CENTRAL/"README.md").write_text("# 기출 MD 정본\n\n이 디렉터리는 연도별 평가원/수능 국어 Markdown 중앙 탐색 위치다. `INDEX.md`는 사람이 읽는 색인이고 `index.json`은 기계 색인이다. 원본 파일은 삭제하지 않으며, 이 view에는 원문만 보존한다. 문학은 중앙화하되 현재 독서 전용 canonical schema에는 자동 편입하지 않는다.\n")
    report=["# KICE corpus ingestion 보고서","", "## 처리 원칙", "", "이번 작업은 corpus ingestion / source restoration / indexing만 수행했으며 문제 풀이, 정답 추론, 100코드·O1~O8·SDSS 분석 및 기존 연구 기록 수정을 수행하지 않았다.","", "## 결과", "", f"- canonical passage: {len(kp)}", f"- canonical question: {len(kq)}", f"- 신규 발견 시험: 2 (2027학년도 6월·9월 모평)", f"- staging passage/question: {len(staging_p)}/{len(staging_q)}", f"- canonical merge passage/question: {len(staging_p)}/{len(staging_q)}", "- duplicate 제외: 0", "- NEEDS_RESTORE/CONFLICT/UNRESOLVED: 0/0/0", f"- 중앙 독서 MD: {read_count} / 문학 MD: {lit_count}", f"- 이번 중앙 라이브러리 추가 MD: {len([e for e in central_entries if e['status']=='CENTRALIZED_NEW_SOURCE'])} (기존 canonical section 중앙화 {len([e for e in central_entries if e['status']=='CENTRALIZED_EXISTING_CANONICAL'])})", f"- 이미지·표·그래프 asset 추가: {len(assets)}", "", "## 문학 처리", "", "2027학년도 6월·9월 4~9번 문학 원문은 중앙 MD와 inventory에 보존했으나 현재 canonical이 독서 전용이므로 `unsupported_current_schema`로 보고하고 canonical에 편입하지 않았다.", "", "## 다음 준비", "", "다음 cxprepare가 준비할 신규 canonical passage/question: 0/0 (이번 ingestion으로 merge 완료)", "", "## 경로", "", "- `data/기출_MD_정본/INDEX.md`", "- `data/기출_MD_정본/index.json`", "- `data/corpus_ingest/INGEST_REPORT.md"]
    (STAGE/"INGEST_REPORT.md").write_text("\n".join(report)+"\n")
    print(jdump({"merged_passages":len(staging_p),"merged_questions":len(staging_q),"central_entries":len(central_entries),"literature_md":lit_count,"assets":len(assets)}))

if __name__ == "__main__": main()
