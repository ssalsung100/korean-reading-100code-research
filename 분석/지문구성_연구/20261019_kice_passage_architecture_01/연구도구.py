"""새 연구 폴더 내부에만 파생 자료를 작성한다. 정답·태그는 읽어 출력하지 않는다."""
import json
from pathlib import Path
from datetime import datetime, timezone

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[2]
SELECTION = [
    (121, "이중차분법", "사회·측정"),
    (84, "BIS 자기자본 규제", "사회·제도"),
    (0, "천 개념의 변화", "인문·사상사"),
    (3, "영화의 몽타주", "예술·영화"),
    (7, "비트겐슈타인의 그림 이론", "인문·철학"),
    (12, "기악의 의미와 음악의 자율성", "예술·음악"),
    (13, "귀납의 정당화", "인문·논리"),
    (17, "나무의 수분 상승", "과학·생물"),
    (24, "본질과 반본질주의", "인문·철학"),
    (25, "공해 소송의 입증 책임", "사회·법"),
    (32, "CT의 영상 구성", "기술·영상"),
    (45, "헴펠의 설명 이론", "인문·과학철학"),
    (48, "수강료 계약과 판결", "사회·법"),
    (49, "항암제의 작용", "과학·생물"),
    (57, "보험과 고지 의무", "사회·경제법"),
    (110, "PCR의 증폭과 정량", "과학·측정"),
    (126, "검색 엔진의 평가", "기술·정보"),
    (137, "결측치와 이상치", "기술·통계"),
    (115, "아도르노의 예술론과 비판", "예술·철학"),
    (136, "촉매의 작용과 설계", "과학·화학"),
    (138, "압전 효과와 초정밀 저울", "기술·측정"),
    (122, "법령의 불확정 개념", "사회·법"),
]

def log(stage, sample_ids, content):
    record = {
        "at": datetime.now(timezone.utc).isoformat(),
        "stage": stage, "sample_ids": sample_ids, "content": content
    }
    with (BASE / "연구판단_raw.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")

def save_stage1(sid, content):
    path = BASE / f"03_지문별_심층분석/{sid}.md"
    with path.open("x", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    log("지문자체분석_고정", [sid], content.strip())

def append_stage2(sid, content):
    path = BASE / f"03_지문별_심층분석/{sid}.md"
    assert path.exists(), "지문 자체 분석 먼저 저장"
    with path.open("a", encoding="utf-8") as f:
        f.write("\n" + content.strip() + "\n")
    log("문항연결", [sid], content.strip())

def prepare():
    if (BASE / "02_평가원지문_표본목록.jsonl").exists():
        raise RuntimeError("초기 준비 완료: 기존 표본·상태를 덮어쓰지 않습니다. 재실행하지 마세요.")
    rows = [json.loads(x) for x in (ROOT / "data/kice_passages.jsonl").read_text().splitlines()]
    selected = []
    for n, (idx, title, domain) in enumerate(SELECTION, 1):
        r = rows[idx]
        sid = f"PA{n:02}"
        paragraphs = [x.strip() for x in r["passage_text"].split("\n\n") if x.strip()]
        target = BASE / f"근거/지문만/{sid}.md"
        target.write_text(f"# {sid} {title}\n\n{r['passage_id']}\n\n" +
                          "\n\n".join(f"## P{i}\n\n{p}" for i, p in enumerate(paragraphs, 1)))
        selected.append({
            "sample_id": sid, "title": title, "domain": domain,
            "role": "원리도출" if n <= 18 else "보류검증",
            "passage_id": r["passage_id"], "academic_year": r["academic_year"],
            "exam_label": r["exam_label"], "question_range": [r["question_start"], r["question_end"]],
            "source_kind": "저장소 기출 전사; AI 해설 아님; 공식 PDF 신규 전수 대조 아님",
            "source_jsonl": "data/kice_passages.jsonl", "source_line": idx + 1,
            "source_hwpx": r.get("source_hwpx"), "source_markdown": r.get("source_markdown"),
            "source_visual_flag": r.get("contains_visual_placeholder"),
            "paragraph_count_transcription": len(paragraphs),
            "paragraph_numbering": "전사 빈 줄 기준. 원PDF 단락과 다른 경우 별도 기록",
            "passage_only_copy": str(target.relative_to(BASE)),
            "past_exposure": "기존 연구 존재; 무노출·엄격한 blind 실적 주장 안 함",
            "stage1": "미검토", "stage2": "미검토",
        })
    (BASE / "02_평가원지문_표본목록.jsonl").write_text(
        "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in selected))
    log("범위고정", [], "최신 사용자 지시 우선: 타 모델 자동 호출 없음, 기존 원장 불변. 신규 판단은 이 폴더 raw에 즉시 저장. G024/G370 hold 유지. 18개 도출 표본과 4개 보류검증 표본 사전 선정. PA19~22 본문은 원리 v0 고정 전 열람하지 않음.")

if __name__ == "__main__":
    prepare()
