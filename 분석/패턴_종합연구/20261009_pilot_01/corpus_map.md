# 코퍼스 연결과 이번 실행의 범위

이 실행은 완료된 개별 풀이를 재사용하는 후속 종합 연구다. 기존 연구의 새로운 blind 수행이나 100코드 재정의가 아니다. 모든 새 파일은 이 실행 폴더에만 두었다. 기존 원본·raw·manifest·meta_state·인덱스·코드 파일에는 쓰지 않았다.

## 분석 단위와 최종 산출물

`case_id`는 연구 작업 식별자, `passage_group`은 공개 장벽을 공유하는 운영 묶음, `question_id`·`passage_id`는 원문 연결 식별자다. 세 종류의 수는 같지 않다. 한 문항에는 최초 풀이·공식답 대조·독립 코드·SDSS 대조 및 후속 수정·보강이 여럿 붙을 수 있다. 이번의 `event_id`는 문항 안에서 특정 선지를 판단하는 국소 장면이다. 한 문항의 여러 장면을 문항 여러 개로 세지 않는다.

최종 판단은 `data/기본기_연구/astra_handoff_queue.jsonl`의 해당 case 단계와 후속 정정·backfill을 우선한다. `astra_handoff_processed.jsonl`은 반영 여부를 기록할 뿐 판단을 추가하지 않는다. 사람이 읽는 `독립풀이_04/{CASE}_01/02/03` 파일은 그 반영본이다. `분석/기본기_연구/문항별_완성본/`은 2026-09-15 기준 177개를 담은 과거 부분 뷰여서 현재 전체 완료 자산을 대표하지 않는다.

## 실제 상태 집계

아래 숫자는 기존 검증을 재실행하여 의미를 전수 재판정한 값이 아니다. 원장 ID·stage·manifest 상태·인덱스의 비어 있지 않은 식별자만 코드로 계산했다. `corpus_counts.json`과 `prepare_sample.py`에 재현 근거가 있다.

|단위|현재 관측값|해석|
|---|---:|---|
|raw 처리 작업|7,605행 / 7,605 ID|hold·meta·audit·수정도 포함|
|processed|7,605행|pending 0; 출제 문항 수 아님|
|manifest|1,671 cases / 499 groups|prepared 8, consumed_sdss 1,663|
|meta_state 완료|497 groups / 1,663 cases|완료 운영 사례 수; 의미의 전역 확정·고유 기출 수 아님|
|현재 인덱스의 저장 식별자|497 passage_id / 1,671 question_id|hold 포함; 학년도 오표기·legacy 중복 문제까지 해결된 고유 원문 수 아님|
|consumed 사례의 저장 식별자|495 passage_id / 1,663 question_id|2개 지문이 여러 작업 group에 나뉨|
|이번 발견 표본|12 고유 지문 / 39 고유 문항|한 지문 전체와 관련 문항 전체 열람|
|이번 검증 표본|6세트 / 21문항|메타데이터로만 선정. G095 한 문항 요약 우발 노출 별도 기록|

raw 단계별 기록 수: answer_check 1,689, independent_code 1,672, sdss_compare 1,676, blind 1,674, boundary_revision 21, induction 388, hold 180, meta_induction 162, manual_parity_audit 54, depth_backfill 89. `independent_code` 1,672행은 분석 기록 수이고 `blind` 1,674행·`answer_check` 1,689행은 각각 다른 작업 기록 수다. 이를 합하거나 파일 수로 나눠 출제 횟수를 만들지 않는다.

`TARGET_COMPLETION_RECONCILIATION_V1.md`는 과거 903건/366 연결을 보고하지만 현재 crosswalk 파일은 research-side 1,156행(619 target, 537 non-target), target-side 1,147행(619 completed, 511 ready, 4 hold, 5 source missing, 8 ambiguous)이다. 이 crosswalk도 현재 manifest 1,671행 전체의 완료 현황을 포괄하지 않는다. 따라서 후속 완료 기록을 무시하고 511건을 새 연구 대상으로 재개하지 않았다.

## 원문과 풀이의 연결

`research_data_index_enriched_v2.json`에서 case → group → question/passage ID → canonical source → stage record ID → reflected target을 따른다. KICE는 `data/kice_passages.jsonl`과 `data/kice_questions.jsonl`, LEET는 검수 Markdown 또는 공식 HWP 추출 텍스트, MEET는 공식 지면 검수 전사와 정본 JSONL을 이용한다. 그림은 기존 보충 파일의 provenance를 따른다.

각 이벤트에는 원문 짧은 인용, 원본 파일과 JSONL 행/Markdown 줄, blind source의 필드·문자 구간·빈 줄 기준 문단, 선택지 ID와 전문, 최초 풀이 raw ID·행·인용, 후속 공식답 기록 ID를 연결했다. JSON의 문단 번호는 원 지면의 단락 번호가 아니라 해당 전사 필드의 빈 줄 분할 번호다. 원문의 정확한 쪽을 모르면 만들지 않았다.

발견용 39문항의 지문·발문·선지와 canonical 텍스트 사이 정규화 대조는 모두 일치했다. 공백·문장부호·HTML 태그를 제외한 문자열 대조로, OCR의 의미 정확성·원 배포 지면 일치의 새로운 보증은 아니다. `reading_coverage.json`에 문항별 출처와 승계한 검증 수준을 보존한다. 원 배포본 전면 재검수나 정답표 재수집은 하지 않았다.

G014 CA의 그림은 `CA_supplement_20260910.json`에 연결된 기술 HWPX 060쪽 표식, `BinData/image21.bmp` 추출본을 직접 보았다. G039 GL의 장치 그림도 직접 보았다. GL의 `2f1₁` 중복첨자와 원 배포본 수식 미검증은 유지하며 GL①의 선후 장면만 근거로 쓴다.

## 중복·반복 분석·변형 구분

- 동일 원 시험·형·문항·본문의 수록 컨테이너 차이는 중복 수록이다. source 경로·최초 ID는 모두 남기고 원문 단위로 한 번 센다.
- 동일 문항의 여러 stage, 후속 답 정정, depth_backfill, legacy case 재연구는 반복 분석이다. 원장의 레코드는 보존하되 출제 사례를 늘리지 않는다.
- 같은 지문에 문항 번호가 다른 경우는 고유 문항이지만 하나의 지문 묶음이다. G013/G059 및 G031/G520은 같은 저장 passage_id를 여러 group으로 나눠 처리한 실제 예다.
- 발문·선지를 연구자가 바꾼 probe는 변형 문항이다. 예컨대 GK backfill의 전달 경로 발문 교체는 synthetic_not_corpus이며 본 실행의 실제 기출 수에 포함하지 않는다.
- 저장 ID의 연도·S구간 제거만으로 실제 중복을 확정하지 않는다. G160/G162는 같은 2025-Q01~03 좌표로 보이나 본문 문자열이 다르고, G160은 후속 원장에서 2026학년도6월로 정정되었다. 표본의 alias 집합은 보수적 분할 금지 범위로만 유지한다.
- 기존 03·04 초기 legacy 자산과 전체 코퍼스를 통합한 완전한 원문 중복 제거 수는 이번에 확정하지 않았다. 1,663을 평가원/전체 고유 기출 수라고 주장하지 않는다.

## 선정·분할·노출

기존 공통 sample_manifest를 파일명 검색으로 찾지 못해 최초로 고정했다. 발견 KICE 8·LEET 2·MEET 2, 검증 KICE 4·LEET 1·MEET 1이다. 발견 자료의 실제 연도는 2006~2026, KICE는 2010~2026이다. 논리적으로 풍부한 독서 자료와 짧은 독서론·서사 자료를 함께 읽되, 연구 group의 크기나 코드 빈도로 확률 표집하지 않았다.

법·사상·사회 관련 자료의 비중이 크고 경제 수치 모형, 그래프·표 집중형, KICE 문학을 대표하지 못한다. 그림 2문항과 MEET 문학 1세트가 있지만 균형·통계적 충분성을 보장하지 않는다. 소재·분야는 발견용 내용을 읽은 뒤 아래처럼 주석화했고 검증용 분야를 맞추기 위해 내용을 열지 않았다. 유형은 내용 일치·보기 적용·근거 찾기·비판/대책·논지 전개·서술 방식·어휘가 포함된다.

기존 연구를 재사용하므로 코드명과 기존 판정에 대한 완전 무노출 귀납을 주장하지 않는다. 일부 안내·색인에서 답·코드를 먼저 보았고, 판정 장면은 직접 원문을 읽어 작성한 다음 해당 case 독립 코드 원장을 다시 확인해 대응을 기록했다. 검증용의 원문·전체 선지·상세 풀이·다른 후보 모델 결과는 열람하지 않았다. 다만 필수 절차 자료의 과거 요약표에서 G095/K 한 문항의 답·코드 요약이 우발 노출되었다. 독립 검증 무노출 위반을 `sample_annotations.json`에 명시하고 표본을 임의 교체하지 않았다.

`sample_manifest.json`은 선정 후 불변이다. G160 표시 정정, G160/G162 alias 오해 방지, G095 노출 주석은 별도 `sample_annotations.json`에 두었다. 후속 모델은 공통 manifest와 이 주석을 함께 사용해야 한다.

## 발견용 실제 열람 목록

|group|실제 시험·분야·소재|case|문항 수|
|---|---|---|---:|
|G001|2014학년도 6월 A형 / 법 / 입증 책임과 공해 소송|AA, AB|2|
|G002|2015학년도 수능 B형 / 천문 과학 / 슈퍼문·이심률·조차|AC, AD|2|
|G004|2020학년도 수능 / 인식론 / 믿음의 정도와 조건화|AF, AG, AH, AI, AJ|5|
|G010|2022학년도 6월 / 법·사회사상 / 베카리아의 형벌론|BI, BJ, BK, BL|4|
|G014|2022학년도 수능 / 기술 / 차량 주변 영상의 왜곡 보정과 시점 변환|BY, BZ, CA, CB|4|
|G039|2010학년도 6월 / 생리 과학·측정 기술 / 귀의 소리와 청력 측정|GK, GL, GM|3|
|G103|2018학년도 수능 / 철학 / 아리스토텔레스 목적론에 대한 비판과 재평가|OX, OY, OZ, PA|4|
|G160|2026학년도 6월(기존 후속 정정 승계) / 독서론·언어 / 동형이의어의 의미 확정|ZD, ZE, ZF|3|
|G222|2022학년도 LEET / 사회·법제사 / 부랑인 정책의 법제·명분·운영|AJP, AJQ, AJR|3|
|G260|2011학년도 LEET / 정치사 / 프랑스 제3공화국의 대의제와 국가 확대|ANV, ANW, ANX|3|
|G284|2006학년도 MEET / 역사 사료·통치 비판 / 최승로의 광종 평가|AQN, AQO, AQP|3|
|G329|2012학년도 MEET / 문학·서사 / 서하진 「추일 서정」|AVS, AVT, AVU|3|

## 보류와 제외의 승계

G024 DR/DS/DT/DU: 그룹 원문 전 DR의 답·SDSS49 사전 노출로 최초 independent_code 생성이 금지된 상태다. 명시적 비독립 검토 절차 없이 재개하지 않는다. G370 BAP/BAQ/BAR/BAS: 공식 배포 렌더와 blind source에 실제 본문·[A][B] 문맥이 없으므로 원문 복원 전 풀이 불가다. 둘 다 표본에서 제외했지만 기존 연구에서 완료·제외 처리한 것으로 고쳐 쓰지 않았다.

`consumed_sdss`는 모든 세부 의미가 확정됐다는 뜻이 아니다. OX의 유일 주 코드 우선순위 유보, GK의 대안 풀이, GL의 수식 정본 유보, G160의 최초 오연결과 후속 정정을 그대로 재사용했다. 과거 노출 unknown인 사례에 새 blind 자격을 부여하지 않았고 답 일치를 코드 의미 검증 성공률로 쓰지 않았다.

## 재현과 실행 정보

집계는 `build_outputs.py`가 `pilot_events.jsonl`에 대응하는 근거 연결 레코드에서 resolved passage/question 집합으로 계산한다. `pattern_cards.md`와 `pilot_counts.json`이 같은 계산을 사용한다. `prepare_sample.py`는 고정 manifest가 있으면 실패하도록 되어 있어 재선정에 사용하지 않는다.

런타임에서 확인되는 값: GPT-6 기반 Codex. 정확한 모델 ID·effort·실시간 사용량은 이 인터페이스에서 확인하지 못해 null로 남겼다. 저장소의 Astra/Luna 과거 설정을 현재 값으로 쓰지 않았다. 다른 모델·에이전트 호출, 모델·인증·daemon 변경, commit/push는 수행하지 않았다.
