"""고정 세트의 형식·근거 추적·입력 불변·산출물 해시만 검사한다."""
from pathlib import Path
import json, hashlib, datetime, argparse, collections

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[2]
EXPECTED_SHA='cb25b7b5438863c4c0f437f5f2e115cc30865183202edd79b0e7a8de5b5c9dff'
EXPECTED={'G064':['JN','JO'],'G095':['NK','NL','NM','NN','NO'],
 'G119':['RV','RW','RX','RY'],'G157':['YR','YS','YT','YU'],
 'G350':['AYE','AYF','AYG'],'G310':['ATN','ATO','ATP']}
REQUIRED=['case_annotations.jsonl','evidence_links.jsonl','pattern_residuals.md',
 'text_item_solution_matrix.md','teaching_item_design_notes.md','application_limitations.md']

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def readjl(p):return [json.loads(line) for line in p.read_text().splitlines() if line]
def check(c,msg):
    if not c:raise AssertionError(msg)

def validate():
    for n in REQUIRED:check((OUT/n).is_file() and (OUT/n).stat().st_size>0,'산출물 누락: '+n)
    baseline=json.loads((OUT/'input_baseline.json').read_text())
    for r in baseline['inputs']+baseline['frozen_folder_baseline']:
        check(sha(ROOT/r['path'])==r['sha256'],'입력 변경: '+r['path'])
    frozen_root=ROOT/'분석/패턴_종합연구/20261010_codebook_v0_2_01'
    check({str(p.relative_to(ROOT)) for p in frozen_root.rglob('*') if p.is_file()}==
          {r['path'] for r in baseline['frozen_folder_baseline']},'기존 동결 폴더 파일 목록 변경')
    cp=ROOT/'분석/패턴_종합연구/20261010_codebook_v0_2_01/codebook_v0.2.json'
    check(sha(cp)==EXPECTED_SHA,'코드북 해시 불일치')
    book=json.loads(cp.read_text());cards={r['pattern_id']:r for r in book['cards']}
    types={a['subtype_id']:r['pattern_id'] for r in book['cards'] for a in r['sub_operations']}
    rows=readjl(OUT/'case_annotations.jsonl');evidence=readjl(OUT/'evidence_links.jsonl')
    items=[r for r in rows if r['record_type']=='item_application']
    passages=[r for r in rows if r['record_type']=='passage_application']
    check(len(passages)==6 and len(items)==21 and len(rows)==27,'지문·문항 수 불일치')
    check({r['group_id'] for r in passages}==set(EXPECTED),'지문 ID 불일치')
    check(collections.Counter(r['case_id'] for r in items)==collections.Counter(c for cs in EXPECTED.values() for c in cs),'case 중복·누락')
    for r in items:check(r['case_id'] in EXPECTED[r['group_id']],'group/case 대응 불일치')
    raw=readjl(OUT/'initial_solution_raw.jsonl')
    check(len(raw)==21,'최초 풀이 누락')
    rawmap={r['case_id']:r for r in raw}
    check(len(rawmap)==21,'최초 풀이 중복')
    snapshot=json.loads((OUT/'source_snapshot.json').read_text())
    check(snapshot['groups']==EXPECTED,'원문 스냅샷 범위 불일치')
    blind_root=ROOT/'data/기본기_연구/prepared_backlog/blind_sources'
    for g,cs in EXPECTED.items():
        for c in cs:
            src=json.loads((blind_root/f'{c}.json').read_text())
            check(src.get('blind_only') is True and src['passage_group']==g,'blind 원문 식별 불일치')
            check(snapshot['sources'][c]==src,'원문 스냅샷 내용 불일치')
        check(len({snapshot['sources'][c]['passage_text'] for c in cs})==1,'group 공통 지문 상이')
    for n,t in snapshot['supplements'].items():check((blind_root/n).read_text()==t,'보강표 스냅샷 불일치')
    ids=[r['evidence_id'] for r in evidence];check(len(ids)==len(set(ids)),'근거 ID 중복')
    ids=set(ids)
    for e in evidence:
        p=ROOT/e['source_path'];check(sha(p)==e['source_sha256'],'근거 원문 해시 변경')
        if e.get('evidence_kind')=='image_observation':
            check(bool(e['image_region_description']) and bool(e['observed_content_transcription']),'시각 근거 위치·전사 누락')
            continue
        pointer=e['json_pointer']
        if pointer:
            v=json.loads(p.read_text())
            for token in pointer.strip('/').split('/'):
                v=v[int(token)] if isinstance(v,list) else v[token]
        else:v=p.read_text()
        check(v[e['char_start']:e['char_end_exclusive']]==e['exact_quote'],'원문 인용 불일치: '+e['evidence_id'])
        check(v[:e['char_start']].count('\n\n')+1==e['paragraph_index_1_based'],'문단 위치 불일치')
    used_ids=set()
    for r in rows:
        check(bool(r['evidence_ids']),'사례 근거 누락')
        used_ids.update(r['evidence_ids'])
        for a in r['pattern_decisions']:
            check(a['pattern_id'] in cards,'코드북에 없는 패턴')
            if a['subtype_id']:check(types.get(a['subtype_id'])==a['pattern_id'],'하위형 대응 불일치')
            check(a['decision'] in ['적용','구조상 존재','경계·비적용','불확실'],'판정 상태 불일치')
            check(a['evidence_ids'] and a['reason'],'패턴 최소 서술 누락')
            check(not a['necessary_for_all_solutions'],'필수 경로 과장')
            check(set(a['codebook_relations'])<=set(book['pattern_relation_definitions']),'원 관계 이름 불일치')
            used_ids.update(a['evidence_ids'])
        if r['record_type']=='passage_application':
            check(r['functional_organization'] and r['source_defects_and_limits'],'지문 기능·결손 기록 누락')
            for a in r['functional_organization']:used_ids.update(a['evidence_ids'])
            continue
        check(r['initial_solution']==rawmap[r['case_id']],'최초 풀이 덮어쓰기 또는 불일치')
        check(r['initial_solution']['official_answer_checked'] is False,'답 미대조 상태 불일치')
        for field in ['information_actually_used','present_but_not_used','recognition_during_reading',
          'recognition_after_choices','alternative_valid_route','unnecessary_procedures','boundary_or_counterexample']:
            check(bool(r[field]),'문항 심층 필드 누락: '+r['case_id']+' '+field)
        check(len(r['choice_analyses'])==5 and {x['choice_number'] for x in r['choice_analyses']}==set(range(1,6)),'선지 누락')
        for ch in r['choice_analyses']:
            check(ch['content_status'] and ch['item_transformation'] and ch['evidence_ids'],'선지 분석 누락')
            check(set(ch['minimum_argument'])=={'source_premise','needed_intermediate_inference','difference_or_match','conclusion'},'최소 논증 사슬 필드 불일치')
            check(all(ch['minimum_argument'].values()),'논증 사슬 공백')
            used_ids.update(ch['evidence_ids'])
        coverage=[a['pattern_id'] for a in r['pattern_decisions']]+[a['pattern_id'] for a in r['not_applicable_patterns']]
        check(collections.Counter(coverage)==collections.Counter(cards.keys()),'13개 카드의 적용·유보 범위 기록 불일치')
        for residual in r['residual_candidate_ids']:
            check(residual in (OUT/'pattern_residuals.md').read_text(),'잔여 후보 연결 누락')
    check(used_ids<=ids,'존재하지 않는 근거 ID')
    # 문항·근거·상태 개수는 기술 통계이며 적용 의미의 타당성을 검증하지 않는다.
    return {'status':'pass','validation_scope':'형식·추적성·입력 불변 검사',
      'semantic_validity_certified':False,'official_answers_checked':False,
      'checked':{'passages':6,'items':21,'choices':105,'evidence_links':len(evidence),
                 'text_evidence_links':sum(e.get('evidence_kind')!='image_observation' for e in evidence),
                 'image_links':sum(e.get('evidence_kind')=='image_observation' for e in evidence),
                 'initial_solution_preserved':True,'input_baselines_unchanged':True,'frozen_codebook_unchanged':True},
      'limits':['자동 검사 통과는 의미적 타당성 완료가 아님',
                '시각 전사의 의미 일치는 자동 검사 대상 아님','실제 런타임 모델 ID와 effort는 미확인']}

def freeze():
    check(not (OUT/'freeze_manifest.json').exists(),'이미 동결됨; 덮어쓰지 않음')
    report=validate();report['validated_at']=datetime.datetime.now(datetime.timezone.utc).isoformat()
    (OUT/'validation_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    baseline=json.loads((OUT/'input_baseline.json').read_text())
    excluded={'freeze_manifest.json','freeze_manifest.sha256','hashes.sha256'}
    files=[p for p in sorted(OUT.iterdir()) if p.is_file() and p.name not in excluded]
    artifacts=[{'path':p.name,'sha256':sha(p),'size_bytes':p.stat().st_size} for p in files]
    manifest={'schema_version':'external-application-freeze-1.0','frozen_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
      'application_id':'20261010_codebook_external_application_01',
      'scope':{'group_ids':list(EXPECTED),'case_ids':EXPECTED,'passages':6,'items':21,'choices':105,
               'scope_exhaustive_classification_of_repository':False},
      'codebook':{'path':'분석/패턴_종합연구/20261010_codebook_v0_2_01/codebook_v0.2.json','sha256':EXPECTED_SHA,'modified':False},
      'executor':baseline['runtime_identity'],
      'execution':{'other_model_calls':0,'subagents_spawned':0,'git_push':False,'official_answers_read':False,
        'previous_sol_analysis_or_candidates_read':False,'previous_100code_answers_or_judgments_read':False,
        'sdss_read':False,'source_and_frozen_folder_modified':False},
      'independence':{'G095':'사용자 보고의 이전 노출 이력 있음; 문항별 범위와 기억 여부 미확인',
        'other_groups':'이번 세션의 과거 분석·정답 사전 열람 없음; 세션 밖 노출 여부 미확인',
        'codebook_exposure':'풀이 전에 동결 코드북을 열람한 적용 연구; 코드북 미노출 발견 실험 아님'},
      'semantic_read_scope':['AGENTS.md','지정 코드북의 13개 카드 핵심 필드','21 blind-only 원문 JSON',
        'RX_choice_table.md','G350_visual01.md','G350_visual02.md','G350_emphasis_restored.md',
        'G350 공식 인쇄2·3쪽 이미지','manifest의 해당 group 라우팅·결손 메타데이터'],
      'read_scope_note':'codebook 전체 최초 출력 일부 잘림; 이후 13개 카드의 원칙·하위형·최소 증거·조건·경계 필드를 재확인. 다른 동결 파일은 해시만 계산.',
      'source_defects':{'G064':'공식 조판 전체 재대조 미실시',
        'G095':'문장 중간 P4/P5 분리·NO 발문 선택지 중복 혼입; 이전 노출 범위 미확인',
        'G119':'RX B열 누락을 blind-only 보강표로 복원; 이번 세션의 원본 스캔 재대조 없음',
        'G157':'실험 데이터·실제 심리 효과 증거 없음; 원문 모형에 한정',
        'G350':'강조구·발문·보기 표 평탄화/placeholder를 공식2·3쪽 이미지로 직접 확인',
        'G310':'u 태그·선택지 번호 포함; 원본 전체 조판·시험 계열 정본 확인 미실시'},
      'collateral_exposure':'G350 공식2쪽의 앞 지문 문항2·3은 화면에 부수 노출; 분석 대상에 편입하지 않음',
      'inputs':baseline['inputs'],'frozen_folder_baseline':baseline['frozen_folder_baseline'],
      'validation_report':'validation_report.json','automated_validation_passed':True,
      'semantic_validity_verified':False,'external_independent_semantic_review':False,
      'education_outcomes_observed':False,'new_item_quality_empirically_validated':False,
      'residual_status':'구체적 후보·경계 기록만; 코드북 개정 또는 확정 신규 패턴 승격 없음',
      'artifacts':artifacts,'hash_policy':'manifest는 artifacts의 해시를 담는다. manifest 자체는 freeze_manifest.sha256과 hashes.sha256에서 검증한다. hashes.sha256은 자기 자신을 포함하지 않는다.'}
    mp=OUT/'freeze_manifest.json';mp.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    (OUT/'freeze_manifest.sha256').write_text(sha(mp)+'  freeze_manifest.json\n')
    allfiles=files+[mp,OUT/'freeze_manifest.sha256']
    (OUT/'hashes.sha256').write_text(''.join(sha(p)+'  '+p.name+'\n' for p in sorted(allfiles)))
    return {'status':'frozen','manifest_sha256':sha(mp),'artifacts':len(artifacts),'validation':report}

def verify():
    report=validate();manifest=json.loads((OUT/'freeze_manifest.json').read_text())
    for a in manifest['artifacts']:check(sha(OUT/a['path'])==a['sha256'],'동결 산출물 변경: '+a['path'])
    for line in (OUT/'hashes.sha256').read_text().splitlines():
        h,n=line.split('  ',1);check(sha(OUT/n)==h,'해시 기록 불일치: '+n)
    check((OUT/'freeze_manifest.sha256').read_text().split('  ',1)[0]==sha(OUT/'freeze_manifest.json'),'manifest 해시 불일치')
    return {'status':'verified','semantic_validity_certified':False,'manifest_sha256':sha(OUT/'freeze_manifest.json'),
            'counts':report['checked']}

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--freeze',action='store_true');parser.add_argument('--verify',action='store_true')
    args=parser.parse_args();check(not(args.freeze and args.verify),'freeze와 verify는 별도 실행')
    result=freeze() if args.freeze else verify() if args.verify else validate()
    print(json.dumps(result,ensure_ascii=False,indent=2))
