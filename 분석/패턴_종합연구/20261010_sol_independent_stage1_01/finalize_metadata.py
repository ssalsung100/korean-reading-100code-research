from pathlib import Path
import json,hashlib
from datetime import datetime,timezone

RUN=Path(__file__).resolve().parent
ROOT=RUN.parents[2]
def dump(name,obj):
 (RUN/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
hist=json.loads((RUN/'read_history.json').read_text())
hist['runtime_note']='이번 실행은 주 세션에서만 수행. 외부 모델 호출·subagent·cx1m 호출 없음. 요청 모델·effort의 API 실행 식별값은 직접 검증하지 못함.'
hist['events'] += [
 {'paths':['자료/평가원_국어','자료/평가원_독서_시각자료_원본','data/기출_MD_정본'],
  'mode':'rg --files 및 경로명 검사','scope':'RX의 누락 B열 원문 위치 탐색','content_exposure':'원문·정답표 파일명만. 정답표 본문 미열람.'},
 {'paths':['data/기출_MD_정본/연도별/2019/6월_모평/독서/Q35-38.md','data/기출_MD_정본/연도별/2019/6월_모평/독서/Q35-38-S084-087.md'],
  'mode':'기계적 구조 필터','scope':'줄 수·제목 수준·숫자 식별·원본 HWP 파일명만 출력','content_exposure':'문서의 정답·해설 및 기존 분석 값 출력 없음.'},
 {'path':'data/기출_MD_정본/연도별/2019/6월_모평/독서/Q35-38-S084-087.md',
  'mode':'문항 부분만 모델 출력','scope':'A와 B라는 발문부터 다음 문항 전까지·금지 문자열 직전에서 중단',
  'content_exposure':'RX 발문·보기·A열 5선지·문항 식별 숫자 087. B열 누락 확인. 정답·해설 출력 없음.'},
 {'scope':'저장소 전체 PDF/HWP 경로 열거 및 두 /tmp PDF 존재 여부',
  'mode':'파일명·존재 여부만','content_exposure':'정답표 경로명 일부 보였으나 정답표를 열지 않음. /tmp 후보 PDF 2개 모두 없음.'},
 {'scope':'새 실행 폴더의 analysis 6파일·분리한 원문 사본·직접 작성한 스크립트',
  'mode':'독립 판단 기록 및 연결 산출','content_exposure':'자신의 독립 풀이와 원문만. 기존 보고·코드북·정답 대조 없음.'}
]
hist['chronology_note']='사례 본문 열람에는 실제 시각을 남겼다. 초기 기계적 조회 및 RX 진단 조회는 최종 정리에 추가하여 사건 배열은 정확한 전체 시간순 로그가 아니다. 실행한 명령의 필터·출력 범위를 기록한 수동 열람 원장이다.'
hist['completed_at_utc']=datetime.now(timezone.utc).isoformat()
dump('read_history.json',hist)

baseline=json.loads((RUN/'preservation_baseline.json').read_text())
inventory=json.loads((RUN/'source_inventory.json').read_text())
for name in ('Q35-38.md','Q35-38-S084-087.md'):
 rel='data/기출_MD_정본/연도별/2019/6월_모평/독서/'+name
 sha=hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()
 baseline.append({'path':rel,'sha256':sha,'baseline_timing':'RX 조회 후 기록·우리 작업은 읽기만 수행'})
 inventory.append({'path':rel,'sha256':sha,'scope':'RX 누락 B열 진단: 구조만'+(' 및 RX 문항 부분' if '-S' in name else ''),
                   'model_content_viewed':'-S' in name,'copied':False,'role':'출처 결손 진단·추가 독립 정답 정보 아님'})
dump('preservation_baseline.json',baseline);dump('source_inventory.json',inventory)

(RUN/'검증대상과_열람자료.md').write_text('''# 검증 대상과 실제 열람 자료

고정 표본 목록의 validation 6행에서 ID·출처 경로만 분리했다. 표본의 선정 이유, 예상 패턴, 기존 분류 값은 출력하거나 분석하지 않았다. `targets.json`에 6세트·21문항의 전체 ID와 원문 위치가 있다.

|지문|시험|문항 ID|case ID|독립성 표시|
|---|---|---|---|---|
|G064|2014학년도 KICE 6월 B형|28–29|JN, JO|이번 세션 정답·기존 판정 비노출|
|G095|2017학년도 KICE 수능|16–20|NK, NL, NM, NN, NO|이전 Astra 노출 이력·5문항 별도|
|G119|2019학년도 KICE 6월|35–38|RV, RW, RX, RY|RX 선지 B열 누락|
|G157|2024학년도 KICE 6월|4–7|YR, YS, YT, YU|이번 세션 정답·기존 판정 비노출|
|G350|2015학년도 LEET 홀수형|4–6|AYE, AYF, AYG|시각자료의 blind 전사 사용·원본 이미지 미대조|
|G310|2010학년도 MEET|5–7|ATN, ATO, ATP|이번 세션 정답·기존 판정 비노출|

본문으로 읽은 핵심 자료는 prepared_backlog/blind_sources의 해당 21개 JSON과 G350_visual01.md·G350_visual02.md이다. JSON에서는 지문·발문·선지와 시각자료 경로만 새 폴더로 분리했다. 동일 그룹의 지문 중복은 별도로 동등성을 검증한다. `source_inventory.json`은 원본 경로·SHA-256·사본 경로·열람 범위를 제공한다.

RX의 B열 복구 가능성을 확인하기 위해 정본 MD 두 파일의 구조만 출력했고, 그중 Q35-38-S084-087.md에서는 RX 질문 부분만 추가 열람했다. 역시 B열이 없었다. 정답표는 파일명만 발견했으며 본문을 열지 않았다. LEET 전체 연도 텍스트, meet_questions.jsonl, kice_questions.jsonl, sealed 자료는 읽지 않았다.

기존 연구 폴더의 파일은 보존 검증용 바이트 해시 계산에만 사용했다. 이 처리는 의미 내용의 모델 열람과 구분하며 read_history.json에 기록했다. 기존 패턴 카드·분석 보고·코드북의 본문 값은 모델에 출력하지 않았다.
''')

(RUN/'정보노출과_검증한계.md').write_text('''# 정보 노출과 검증 한계

이번 세션에서 공식 정답, 기존 풀이, 기존 코드 정의·적용 결과, 검증 표본의 예상 패턴 값은 열람하지 않았다. 코드북 대조는 0회다. 현재 독립 선택 20개는 정답 검증 결과가 아니라 원문에서 직접 판단한 선택이다.

자동으로 제공된 정보는 사용자 메시지 속 AGENTS.md 운영 지침, 최신 작업 지시, 시스템·개발자 지침, 스킬 목록·환경 정보다. 연구 절차와 G095의 이전 노출 이력, G024/G370 hold, 기존 코드북의 식별자를 알게 되었지만 기존 13개 정의·정답·풀이 값은 이 입력에 없었다. 디스크의 AGENTS.md, CURRENT, ASTRA_START, 인수인계·G095 상세 기록을 추가로 열지 않았다. 최신 독립 검증 범위가 이전 연속 연구 절차를 대체한다.

파일 검색에서는 기존 연구 보고와 정답표의 경로명이 보였다. metadata 구조 검사에서는 discovery, validation, exposure_history 등의 키와 개수만 보였다. 검증 대상의 ID·경로를 확보할 때는 코드로 허용 필드만 출력했다. 금지 자료가 프로세스에서 바이트 해시 또는 구조 필터를 위해 읽힌 경우도 숨기지 않고 원장에 남겼다. 모델에 의미 내용을 출력해 분석한 것과 동일한 열람으로 주장하지 않는다.

G095는 이전 Astra의 정답·코드 노출 이력이 있다고 사용자가 명시했다. 그 상세 문서와 정답 값은 이번 세션에서 열지 않았지만, 5문항은 엄격 비노출 성과에서 제외한다. 다른 16문항은 이번 세션에 정답·기존 판정이 표시되지 않은 비노출 후보로 집계한다. 그중 15개는 독립 선택, RX 1개는 번호 보류다. G095 5개는 모두 독립 선택했다. 이 집계가 모델의 사전학습 기출 기억이나 보이지 않는 자동 삽입까지 증명하는 것은 아니므로 절대적 완전 blind는 보장하지 않는다.

요청 모델은 GPT-6.1 Sol, 요청 effort는 xhigh이다. 이 주 세션 밖에서 다른 모델을 호출하지 않았다. 실제 API 모델 ID와 reasoning effort를 검증하는 런타임 수단은 사용하지 못했으므로 설정값 준수를 확인했다고 보고하지 않는다.

RX는 준비 원문과 정본의 모든 선지 B열이 누락되었다. A=위음성, B=진음성은 본문 정의로 판단했지만 ④/⑤의 B값을 구분할 수 없다. 번호를 보류했다. 105개 선지 슬롯을 분석했으나 RX의 5슬롯은 완전한 A/B 선지를 읽은 것이 아니다. 결손을 기존 정답 기억으로 메우지 않았다.

G350의 필수 표는 blind_sources의 두 텍스트 전사로 읽었다. 기호 정의와 네 과세 상태는 확인했지만 원본 이미지의 배치·기호를 직접 렌더링해 대조하지 않았다. 초반 지문과 AYE의 [시각 자료 1] 표지에 대응하는 차선의 문제라는 구는 후속 문맥에서 추정했으며 원본 확인으로 복원했다고 하지 않는다. AYG는 전사 해석에 의존한다. 그밖에 읽은 blind JSON에는 필수 그림 참조가 없었다. 원본 PDF/HWP 전체와 전사 정확성의 전수 대조는 하지 않았다.

판단 보류와 논리적 미확정은 다르다. RX는 자료 결손 때문에 문항 번호를 보류했다. AYF③의 A-B 비용 서열, YT 집단1·2의 효능감 배치는 완전한 문항 안에서 원문이 결정하지 않는 값이다. 독립 후보에서 두 종류를 구분했다.

20개 후보는 이번 소표본의 관찰을 연결한 잠정 목록이다. 서로 중복될 수 있고 기존 코드와 독립적으로 이름 붙였다. 단일 사례 후보 및 G095에 의존하는 근거를 표시했다. 시험별 빈도, 난도, 학습 효과, 재현도, 신규 문항의 타당도는 측정하지 않았다. KICE/LEET/MEET의 차이는 구현 예로만 관찰했고 일반적인 시험 특성 차이로 확정하지 않았다.

원본과 기존 연구는 수정하지 않았으며 G024/G370은 읽거나 재개하지 않았다. 새 폴더에만 기록했다. 외부 모델 호출, 전수 분류, Git push, 신규 지문·문항 제작은 모두 하지 않았다. 1단계 해시 고정 후 작업을 끝낸다.
''')

(RUN/'00_1단계_결과.md').write_text('''# 독립 검증 1단계 결과

고정 검증 표본 6지문·21문항을 직접 읽고 독립 분석했다. KICE 4지문 15문항, LEET 1지문 3문항, MEET 1지문 3문항이다. 20문항에서 독립 답을 선택했고 RX 1문항은 선지 B열 결손으로 번호를 보류했다. 공식 정답·기존 풀이·기존 코드북과 대조하지 않았다.

지문 6개와 문항 21개를 별도 단위로 기록하고, 전체 풀이 장면 21개와 선지 판독 슬롯 105개를 근거에 연결했다. 총 75개 원문 근거에 문자 위치를 붙이고 254개 판단-근거 연결을 남겼다. RX의 5선지 슬롯은 B열 미확인 분석이며 완전 선지 5개로 세지 않는다.

독립 후보는 지문 4개, 문항 설계 6개, 풀이 행동 10개다. 대표 관찰은 정의의 입력 역할 대응, 가능·필요·전체 범위 검사, 표시와 현실 및 지표 분모 분리, 주장과 증거의 적합성 검사, 발화자·시점·지시 대상과 평가의 분리다. 단일 문항·지문에서만 관찰한 후보는 반복 미검증으로 표시했다. 지문에 등장한 구조와 문항에서 실제 활용한 구조를 구분했다.

G095 5문항은 과거 Astra 노출 이력으로 별도 집계한다. 나머지 16문항은 이번 세션 정답·기존 판정 비노출 후보이며, 15선택·1보류다. 자동으로 제공된 프로젝트 지침에는 정의·정답 값이 없었다. 검색 경로명, 기계적 구조 검사, 보존용 바이트 해시는 열람 원장에 기록했다. 모델의 사전학습 기억 및 보이지 않는 자동 삽입까지 완전 blind로 증명하지는 못한다.

G350은 시각자료 텍스트 전사를 사용했고 원본 이미지를 대조하지 않았다. RX 결손과 함께 원문 충실도 한계로 별도 표시했다. 요청 모델·effort는 기록했지만 실제 API 실행값은 독립 검증하지 못했다.

주요 파일:

- `targets.json`, `source_inventory.json`, `read_history.json`: 대상·원문·열람 이력.
- `문항별_독립풀이.md`, `independent_solutions.jsonl`, `passage_analyses.jsonl`: 직접 판단과 별도 분석 단위.
- `decision_scenes.jsonl`, `evidence_anchors.jsonl`, `evidence_links.jsonl`: 선지·풀이 장면과 원문 위치 연결.
- `independent_candidates.json`, `독립후보_목록.md`: 독립 후보와 적용·제외·경계 사례.
- `활용가능성_잠정분석.md`: 교재·강의·창작 설계 원리.
- `정보노출과_검증한계.md`: 노출 집계·결손·독립성의 한계.
- `validation_report.json`, `preservation_report.json`: 연결 구조와 기존 파일 보존 검증.
- `freeze_manifest.json`, `freeze_manifest.sha256`, `freeze_record.json`: 결과 파일별 SHA-256과 고정 시점. 순환 해시를 피하려고 manifest·고정 기록은 본문 파일 목록에서 제외하고 마지막 고정 기록이 이들의 해시를 연결한다.

원본 및 기존 연구를 수정하지 않았다. G024/G370 hold 유지, 다른 모델 호출·전수 분류·Git push·신규 지문 제작 없음. 해시 고정으로 이번 1단계를 종료하며 기존 체계와의 대조는 수행하지 않는다.
''')
print('대상·열람 원장·노출 한계·결과 보고 저장')
