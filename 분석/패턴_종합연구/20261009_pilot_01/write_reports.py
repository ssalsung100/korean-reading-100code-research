import json,hashlib,re
from pathlib import Path
from collections import Counter
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[2]
def j(p):return json.loads(p.read_text())
manifest=j(OUT/'sample_manifest.json');coverage=j(OUT/'reading_coverage.json');counts=j(OUT/'pilot_counts.json');corpus=j(OUT/'corpus_counts.json')
titles={
'G001':('입증 책임과 공해 소송','법','2014학년도 6월 A형'),
'G002':('슈퍼문·이심률·조차','천문 과학','2015학년도 수능 B형'),
'G004':('믿음의 정도와 조건화','인식론','2020학년도 수능'),
'G010':('베카리아의 형벌론','법·사회사상','2022학년도 6월'),
'G014':('차량 주변 영상의 왜곡 보정과 시점 변환','기술','2022학년도 수능'),
'G039':('귀의 소리와 청력 측정','생리 과학·측정 기술','2010학년도 6월'),
'G103':('아리스토텔레스 목적론에 대한 비판과 재평가','철학','2018학년도 수능'),
'G160':('동형이의어의 의미 확정','독서론·언어','2026학년도 6월(기존 후속 정정 승계)'),
'G222':('부랑인 정책의 법제·명분·운영','사회·법제사','2022학년도 LEET'),
'G260':('프랑스 제3공화국의 대의제와 국가 확대','정치사','2011학년도 LEET'),
'G284':('최승로의 광종 평가','역사 사료·통치 비판','2006학년도 MEET'),
'G329':('서하진 「추일 서정」','문학·서사','2012학년도 MEET')}
annotations={
 'manifest_sha256':hashlib.sha256((OUT/'sample_manifest.json').read_bytes()).hexdigest(),
 'immutable_selection':True,'sample_count_change':False,
 'identity_corrections':[dict(group='G160',legacy_year=2025,resolved_year=2026,
 evidence='data/기본기_연구/astra_handoff_queue.jsonl:2620-2622',
 note='동일 사례를 유지하고 표시 연도만 후속 기록에 따라 해석. 원 sample_manifest·canonical·sealed 필드는 수정하지 않음')],
 'alias_cluster_review':[dict(groups=['G160','G162'],same_passage=False,
 evidence='발견용 ZD와 좌표 충돌 별칭 ZJ의 본문 문자열 동일성만 기계 비교: false. ZJ 본문은 모델에 출력·분석하지 않음.',
 note='표본 고정 당시의 alias_groups는 실제 중복 확정이 아니라 보수적인 분할 금지 집합이다. 이 집합 전체를 검증용에서 배제하여 혼입 방지.')],
 'validation_contamination':[dict(group='G095',case='NM',question='2017학년도 수능 18번',
 exposed='기존 절차·연구03 요약표에 있던 legacy K의 정답⑤·주 코드 #2·간단 상태',
 source='분석/기본기_연구/코드심층_03_독립풀이_증거와경쟁.md:37',
 scope='검증 원문·전체 선지·상세 해설은 열람하지 않음. 검증용 내용 무노출이라고 주장할 수 없음.',
 action='공통 표본 재추첨 없음. G095는 이 실행 주체의 독립 검증에 부적격 표시. 다음 검증에서 다른 미노출 독자/세션에 분리하고 요약 노출 이력도 제공.')],
 'runtime':manifest['runtime'],
 'discovery_topics':{g:dict(topic=t[0],domain=t[1],resolved_exam=t[2]) for g,t in titles.items()}}
# 정확한 노출 줄을 실제 파일에서 식별한다.
path=ROOT/'분석/기본기_연구/코드심층_03_독립풀이_증거와경쟁.md'
for n,l in enumerate(path.read_text().splitlines(),1):
 if '[K: 2017 수능 18]' in l:annotations['validation_contamination'][0]['source']=str(path.relative_to(ROOT))+f':{n}'
(OUT/'sample_annotations.json').write_text(json.dumps(annotations,ensure_ascii=False,indent=2)+'\n')

lines=['# 코퍼스 연결과 이번 실행의 범위','',
'이 실행은 완료된 개별 풀이를 재사용하는 후속 종합 연구다. 기존 연구의 새로운 blind 수행이나 100코드 재정의가 아니다. 모든 새 파일은 이 실행 폴더에만 두었다. 기존 원본·raw·manifest·meta_state·인덱스·코드 파일에는 쓰지 않았다.','',
'## 분석 단위와 최종 산출물','',
'`case_id`는 연구 작업 식별자, `passage_group`은 공개 장벽을 공유하는 운영 묶음, `question_id`·`passage_id`는 원문 연결 식별자다. 세 종류의 수는 같지 않다. 한 문항에는 최초 풀이·공식답 대조·독립 코드·SDSS 대조 및 후속 수정·보강이 여럿 붙을 수 있다. 이번의 `event_id`는 문항 안에서 특정 선지를 판단하는 국소 장면이다. 한 문항의 여러 장면을 문항 여러 개로 세지 않는다.','',
'최종 판단은 `data/기본기_연구/astra_handoff_queue.jsonl`의 해당 case 단계와 후속 정정·backfill을 우선한다. `astra_handoff_processed.jsonl`은 반영 여부를 기록할 뿐 판단을 추가하지 않는다. 사람이 읽는 `독립풀이_04/{CASE}_01/02/03` 파일은 그 반영본이다. `분석/기본기_연구/문항별_완성본/`은 2026-09-15 기준 177개를 담은 과거 부분 뷰여서 현재 전체 완료 자산을 대표하지 않는다.','',
'## 실제 상태 집계','',
'아래 숫자는 기존 검증을 재실행하여 의미를 전수 재판정한 값이 아니다. 원장 ID·stage·manifest 상태·인덱스의 비어 있지 않은 식별자만 코드로 계산했다. `corpus_counts.json`과 `prepare_sample.py`에 재현 근거가 있다.','',
'|단위|현재 관측값|해석|','|---|---:|---|',
f'|raw 처리 작업|{corpus["queue_rows"]:,}행 / {corpus["queue_unique_ids"]:,} ID|hold·meta·audit·수정도 포함|',
f'|processed|{corpus["processed_rows"]:,}행|pending {corpus["pending"]}; 출제 문항 수 아님|',
f'|manifest|{corpus["manifest_rows"]:,} cases / {corpus["manifest_groups"]} groups|prepared 8, consumed_sdss 1,663|',
'|meta_state 완료|497 groups / 1,663 cases|완료 운영 사례 수; 의미의 전역 확정·고유 기출 수 아님|',
'|현재 인덱스의 저장 식별자|497 passage_id / 1,671 question_id|hold 포함; 학년도 오표기·legacy 중복 문제까지 해결된 고유 원문 수 아님|',
'|consumed 사례의 저장 식별자|495 passage_id / 1,663 question_id|2개 지문이 여러 작업 group에 나뉨|',
'|이번 발견 표본|12 고유 지문 / 39 고유 문항|한 지문 전체와 관련 문항 전체 열람|',
'|이번 검증 표본|6세트 / 21문항|메타데이터로만 선정. G095 한 문항 요약 우발 노출 별도 기록|','',
'raw 단계별 기록 수: '+', '.join(f'{k} {v:,}' for k,v in corpus['stages'].items())+'. `independent_code` 1,672행은 분석 기록 수이고 `blind` 1,674행·`answer_check` 1,689행은 각각 다른 작업 기록 수다. 이를 합하거나 파일 수로 나눠 출제 횟수를 만들지 않는다.','',
'`TARGET_COMPLETION_RECONCILIATION_V1.md`는 과거 903건/366 연결을 보고하지만 현재 crosswalk 파일은 research-side 1,156행(619 target, 537 non-target), target-side 1,147행(619 completed, 511 ready, 4 hold, 5 source missing, 8 ambiguous)이다. 이 crosswalk도 현재 manifest 1,671행 전체의 완료 현황을 포괄하지 않는다. 따라서 후속 완료 기록을 무시하고 511건을 새 연구 대상으로 재개하지 않았다.','',
'## 원문과 풀이의 연결','',
'`research_data_index_enriched_v2.json`에서 case → group → question/passage ID → canonical source → stage record ID → reflected target을 따른다. KICE는 `data/kice_passages.jsonl`과 `data/kice_questions.jsonl`, LEET는 검수 Markdown 또는 공식 HWP 추출 텍스트, MEET는 공식 지면 검수 전사와 정본 JSONL을 이용한다. 그림은 기존 보충 파일의 provenance를 따른다.','',
'각 이벤트에는 원문 짧은 인용, 원본 파일과 JSONL 행/Markdown 줄, blind source의 필드·문자 구간·빈 줄 기준 문단, 선택지 ID와 전문, 최초 풀이 raw ID·행·인용, 후속 공식답 기록 ID를 연결했다. JSON의 문단 번호는 원 지면의 단락 번호가 아니라 해당 전사 필드의 빈 줄 분할 번호다. 원문의 정확한 쪽을 모르면 만들지 않았다.','',
'발견용 39문항의 지문·발문·선지와 canonical 텍스트 사이 정규화 대조는 모두 일치했다. 공백·문장부호·HTML 태그를 제외한 문자열 대조로, OCR의 의미 정확성·원 배포 지면 일치의 새로운 보증은 아니다. `reading_coverage.json`에 문항별 출처와 승계한 검증 수준을 보존한다. 원 배포본 전면 재검수나 정답표 재수집은 하지 않았다.','',
'G014 CA의 그림은 `CA_supplement_20260910.json`에 연결된 기술 HWPX 060쪽 표식, `BinData/image21.bmp` 추출본을 직접 보았다. G039 GL의 장치 그림도 직접 보았다. GL의 `2f1₁` 중복첨자와 원 배포본 수식 미검증은 유지하며 GL①의 선후 장면만 근거로 쓴다.','',
'## 중복·반복 분석·변형 구분','',
'- 동일 원 시험·형·문항·본문의 수록 컨테이너 차이는 중복 수록이다. source 경로·최초 ID는 모두 남기고 원문 단위로 한 번 센다.',
'- 동일 문항의 여러 stage, 후속 답 정정, depth_backfill, legacy case 재연구는 반복 분석이다. 원장의 레코드는 보존하되 출제 사례를 늘리지 않는다.',
'- 같은 지문에 문항 번호가 다른 경우는 고유 문항이지만 하나의 지문 묶음이다. G013/G059 및 G031/G520은 같은 저장 passage_id를 여러 group으로 나눠 처리한 실제 예다.',
'- 발문·선지를 연구자가 바꾼 probe는 변형 문항이다. 예컨대 GK backfill의 전달 경로 발문 교체는 synthetic_not_corpus이며 본 실행의 실제 기출 수에 포함하지 않는다.',
'- 저장 ID의 연도·S구간 제거만으로 실제 중복을 확정하지 않는다. G160/G162는 같은 2025-Q01~03 좌표로 보이나 본문 문자열이 다르고, G160은 후속 원장에서 2026학년도6월로 정정되었다. 표본의 alias 집합은 보수적 분할 금지 범위로만 유지한다.',
'- 기존 03·04 초기 legacy 자산과 전체 코퍼스를 통합한 완전한 원문 중복 제거 수는 이번에 확정하지 않았다. 1,663을 평가원/전체 고유 기출 수라고 주장하지 않는다.','',
'## 선정·분할·노출','',
'기존 공통 sample_manifest를 파일명 검색으로 찾지 못해 최초로 고정했다. 발견 KICE 8·LEET 2·MEET 2, 검증 KICE 4·LEET 1·MEET 1이다. 발견 자료의 실제 연도는 2006~2026, KICE는 2010~2026이다. 논리적으로 풍부한 독서 자료와 짧은 독서론·서사 자료를 함께 읽되, 연구 group의 크기나 코드 빈도로 확률 표집하지 않았다.','',
'법·사상·사회 관련 자료의 비중이 크고 경제 수치 모형, 그래프·표 집중형, KICE 문학을 대표하지 못한다. 그림 2문항과 MEET 문학 1세트가 있지만 균형·통계적 충분성을 보장하지 않는다. 소재·분야는 발견용 내용을 읽은 뒤 아래처럼 주석화했고 검증용 분야를 맞추기 위해 내용을 열지 않았다. 유형은 내용 일치·보기 적용·근거 찾기·비판/대책·논지 전개·서술 방식·어휘가 포함된다.','',
'기존 연구를 재사용하므로 코드명과 기존 판정에 대한 완전 무노출 귀납을 주장하지 않는다. 일부 안내·색인에서 답·코드를 먼저 보았고, 판정 장면은 직접 원문을 읽어 작성한 다음 해당 case 독립 코드 원장을 다시 확인해 대응을 기록했다. 검증용의 원문·전체 선지·상세 풀이·다른 후보 모델 결과는 열람하지 않았다. 다만 필수 절차 자료의 과거 요약표에서 G095/K 한 문항의 답·코드 요약이 우발 노출되었다. 독립 검증 무노출 위반을 `sample_annotations.json`에 명시하고 표본을 임의 교체하지 않았다.','',
'`sample_manifest.json`은 선정 후 불변이다. G160 표시 정정, G160/G162 alias 오해 방지, G095 노출 주석은 별도 `sample_annotations.json`에 두었다. 후속 모델은 공통 manifest와 이 주석을 함께 사용해야 한다.','',
'## 발견용 실제 열람 목록','',
'|group|실제 시험·분야·소재|case|문항 수|','|---|---|---|---:|']
for s in manifest['samples']:
 if s['split']=='discovery':
  t=titles[s['passage_group']];lines.append(f'|{s["passage_group"]}|{t[2]} / {t[1]} / {t[0]}|{", ".join(s["case_ids"])}|{len(s["case_ids"])}|')
lines.extend(['','## 보류와 제외의 승계','',
'G024 DR/DS/DT/DU: 그룹 원문 전 DR의 답·SDSS49 사전 노출로 최초 independent_code 생성이 금지된 상태다. 명시적 비독립 검토 절차 없이 재개하지 않는다. G370 BAP/BAQ/BAR/BAS: 공식 배포 렌더와 blind source에 실제 본문·[A][B] 문맥이 없으므로 원문 복원 전 풀이 불가다. 둘 다 표본에서 제외했지만 기존 연구에서 완료·제외 처리한 것으로 고쳐 쓰지 않았다.','',
'`consumed_sdss`는 모든 세부 의미가 확정됐다는 뜻이 아니다. OX의 유일 주 코드 우선순위 유보, GK의 대안 풀이, GL의 수식 정본 유보, G160의 최초 오연결과 후속 정정을 그대로 재사용했다. 과거 노출 unknown인 사례에 새 blind 자격을 부여하지 않았고 답 일치를 코드 의미 검증 성공률로 쓰지 않았다.','',
'## 재현과 실행 정보','',
'집계는 `build_outputs.py`가 `pilot_events.jsonl`에 대응하는 근거 연결 레코드에서 resolved passage/question 집합으로 계산한다. `pattern_cards.md`와 `pilot_counts.json`이 같은 계산을 사용한다. `prepare_sample.py`는 고정 manifest가 있으면 실패하도록 되어 있어 재선정에 사용하지 않는다.','',
'런타임에서 확인되는 값: GPT-6 기반 Codex. 정확한 모델 ID·effort·실시간 사용량은 이 인터페이스에서 확인하지 못해 null로 남겼다. 저장소의 Astra/Luna 과거 설정을 현재 값으로 쓰지 않았다. 다른 모델·에이전트 호출, 모델·인증·daemon 변경, commit/push는 수행하지 않았다.'])
(OUT/'corpus_map.md').write_text('\n'.join(lines)+'\n')

evs=[json.loads(l) for l in (OUT/'pilot_events.jsonl').read_text().splitlines()]
unclassified=[e for e in evs if not e['pattern_ids']]
review=['# 파일럿 검토','',
'발견용 12개 고유 지문의 본문과 관련 39문항의 발문·보기·선지 전체, 보충 그림 2개, 연결된 기존 최초 풀이·공식답 후속 대조·독립 코드 및 필요한 GK depth_backfill을 읽었다. 같은 표본에서 43개 판정 장면을 추출했다. 검증용 6세트·21문항의 본문 분석과 전수 분류는 수행하지 않았다.','',
'## 실제 결과와 적용 범위','',
'복수 지문에서 확인한 반복 후보 7개와 한 지문에만 확인한 잠정 후보 6개를 `pattern_cards.md`에 남겼다. 숫자에 맞춘 목록이 아니며, 어느 것도 검증용 적용을 통과한 확정 규칙이라고 표시하지 않았다. 12개 장면은 미분류로 남겼다. 후보와 실제 풀이 활용이 연결된 고유 문항은 29개다. 나머지를 풀지 않았다는 뜻이 아니라 채택 카드의 활용 증거로 세지 않았다는 뜻이다.','',
'- **판단 축 보존(P02):** 입증 책임 주체와 입증 정도(AB), 과학성과 진릿값(OZ), 물질 구성과 환원 가능성(PA). 실제 두 지문·세 문항이다. PA와 OZ를 독립 지문 두 개로 부풀리지 않았다.',
'- **필요 전제 확인(P04):** 고의·과실 없는 손해배상(AA④), 양도되지 않는 생명과 형벌권(BK④), 청세포가 파괴된 인공 달팽이관 사례(GM⑤). 법과 생리 기술에서 전제 결손 확인이 반복된다. AA④는 오답 검토이지 정답① 선택의 필수 경로가 아니다.',
'- **비교 기준과 방향(P03):** 달·지구의 이심률 비교, 같은 달 위치에서 이심률 변화에 따른 1월 조차, A/B 상대 크기의 시점 변환 전후 비교. 단순 크기 단어가 아니라 무엇을 고정하고 어느 관계를 이어야 하는지 기록했다.',
'- **문맥 제약(P05):** AJ·BL·CB의 어휘 판정 및 ZF의 보기 해석을 연결했다. ZE는 그 행동을 설명하는 지문·내용 문항으로만 기록하여 직접 행동 활용 문항 수에서 제외했다.',
'- **고립 후보(S02·S04):** 메아리와 능동 발생을 가르는 관측(GK), 두 후보가 모두 맞아서 유보함과 모두 틀려서 유보함의 차이(ZF③). 서로 다른 지문에서 같은 조작이 반복되는지는 아직 확인하지 못했다.','',
'## 통합·분할·누락의 위험','',
'P01이 가장 넓다. 인물의 견해 귀속(AG), 기관 권한(BI·ANW), 관계 두 항(AJQ), 원인 종류(BY), 평가 대상 행동(AQP)을 한 대응 복원 규칙으로 묶었다. 뒷 세 사례가 별도 중간 추론을 요구한다면 분리해야 한다. 단순히 기존 #75·#98·#17의 이름을 합친 결과로 취급하지 않는다.','',
'P03의 역순 비교·조건부 연쇄·상대비 비교, P07의 기전 선후·중간 처리 상태·역사적 전후는 서로 전이 가능한 상위 규칙인지 아직 미확인이다. 카드 안에서 하위 조작을 숨기지 않았다. 이 두 묶음도 검증에서 우선 분할 가능성을 확인한다.','',
'반대로 S05의 규정/실행 분리와 P02의 축 보존은 과잉 분할일 수 있다. 규범 위반과 부재 구별이 단순 칸 분리로 충분한지, 규범의 효력·예외 해석이 추가로 필요한지를 새로운 실제 사례로 판단해야 한다. P04의 법적 허용과 기전 필요성도 통합·재분할 양쪽 가능성이 있다.','',
'문학의 시점·감정·공간 기능 장면은 대체로 미분류로 남았다. MEET 문학 한 지문으로 이를 독서 규칙에 강제로 합치면 누락을 숨기게 된다. 경제·복합 그래프·강한 수식 계산·KICE 문학도 표본에서 부족하다. 각 문항의 모든 원자 판정을 전수 추출한 것은 아니므로 43개 이벤트는 최소 기록이고, 등장 빈도나 표본 내 패턴 부재의 근거가 아니다.','',
'## 출처·검증 제한 및 우발 노출','',
'대표·경계 사례의 인용은 정본 전사와 연결 대조했다. 원 배포 페이지의 신규 전수 시각 검수는 하지 않았다. KICE 원천 중 다수는 분야별 편집 HWPX이며 이를 공식 배포 원본 컨테이너라고 쓰지 않는다. MEET는 기존 공식 페이지 검수 상태를 승계하고 LEET 2011은 공식 HWP 추출 텍스트 수준을 명시한다. GL④ 수식은 원 배포 정본 미검증이 남는다. G160의 연도·답은 원장 후속 정정을 우선하며 최초 기록을 덮어쓰지 않는다.','',
'표본 고정 뒤 절차 자료의 요약표에서 **검증용 G095의 2017 수능 18번 정답·코드 요약이 우발 노출**되었다. 검증 본문·전체 선지를 읽지는 않았으나 완전 미노출 검증으로 보고할 수 없다. 이 세트는 현재 실행 주체의 독립 검증에서 보류하고 다른 미노출 검토자에게 넘길 필요가 있다. 이번에는 다른 모델을 호출하지 않았다. 표본을 바꿔 오염을 숨기지도 않았다. 초기 CURRENT 통독 출력은 길이 제한으로 일부 생략되었으며, 그 출력·기존 학습까지 소급해 완전 무노출을 증명할 수는 없다.','',
'실제 학생 반응·정답률·시간 자료가 없다. 오답 장면은 원문과 선지의 차이이며 학생들이 많이 틀리는 원인을 관찰했다는 주장이 아니다. GK는 명시된 명제-근거 대응만으로도 풀리므로 경쟁 설명 생성이 필수라는 표현을 쓰지 않았다.','',
'## 다음 검증 작업','',
'1. 공통 `sample_manifest.json`과 `sample_annotations.json`을 승계한다. G095는 현재 실행의 독립성 제한을 보존한 채 미노출 검토자가 담당해야 한다. 사용자 지시 없이 다른 모델을 자동 실행하지 않는다.',
'2. 후보 규칙·적용 조건·제외 조건을 먼저 고정하고 검증용 지문과 관련 문항 전체에서 적용 가능, 비해당, 반례, 미분류를 구분한다. 결과에 맞추어 조건을 사후 수정하면 최초 예측과 수정본을 모두 남긴다.',
'3. 우선 P01·P03·P07의 과잉 통합, S05/P02의 과잉 분할을 검사한다. 같은 지문 여러 문항의 반복을 독립 증거로 부풀리지 않는다.',
'4. 보기의 실제 정답을 고르는 행동과 특정 오답을 설명하는 행동을 나누어 검증한다. ZE처럼 구조만 설명된 경우를 활용 수에 넣지 않는다.',
'5. 반례가 확보되면 기존 100코드는 유지하고 새 실행의 카드 조건만 수정한다. 전수 코퍼스 분류는 파일럿 검증 이후 별도 범위로 결정한다.','',
'## 미분류 장면 보존','',
'|event|case / 선지|미분류로 남긴 차이|','|---|---|---|']
for e in unclassified:review.append(f'|{e["event_id"]}|{e["case_id"]} / {e["choice_ids"]}|{e["decisive_difference"]}|')
review.extend(['','## 기계 점검과 집계 원칙','',
'`validate_outputs.py`는 표본 12/6 분할, 고유 지문·문항 단위 집계, 인용 문자열·선지 ID·기존 원장 참조, 정본 텍스트 대응, 보호 파일 hash와 manifest 불변을 검사한다. 결과는 `validation_report.json`에 남긴다. 이 점검은 풀이의 의미적 정당성을 자동 보증하지 않는다. 카드 의미는 본 실행에서 원문과 기존 풀이를 직접 대조한 판단이며 제2검토자는 아직 없다.','',
'현재 모델의 세부 ID·effort·사용량은 확인할 수 없어 null. 확인된 것은 GPT-6 기반 Codex라는 런타임 설명뿐이다. 다른 모델을 실행했다고 기록하지 않았다.'])
(OUT/'pilot_review.md').write_text('\n'.join(review)+'\n')
print('corpus_map.md / pilot_review.md / sample_annotations.json 저장')
