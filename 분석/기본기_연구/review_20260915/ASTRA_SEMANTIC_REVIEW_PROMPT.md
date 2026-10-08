AGENTS.md, CURRENT.md, ASTRA_START.md를 먼저 읽어라.

그다음
분석/기본기_연구/review_20260915/implementation_tasks.md
중 "B. Astra High에게 전달할 의미적 연구 작업"을 읽고 수행하라.

review_report.md와 evidence.md는 문제 제기와 anchor 선택의 근거일 뿐,
그 결론을 정답으로 받아들이지 마라.

authoritative source는 기존 raw queue와 각 case의 blind/source asset이다.
문항별_완성본은 탐색용 derived view로만 사용한다.

이번 작업은 새 blind corpus 진행이 아니라,
이미 완료된 사례에 대한 사후 semantic audit이다.

중요:
- 기존 blind/answer_check/independent_code/sdss_compare record는 수정하거나 덮어쓰지 않는다.
- 새 판단은 depth_backfill 또는 boundary_revision 등 기존 protocol의 적절한 append-only record로 남긴다.
- 내가 제안한 O1~O8 수행군은 가설이다. 맞지 않는 사례를 적극적으로 찾는다.
- 새 코드 번호를 만들려고 하지 않는다.
- 기존 100코드를 폐기하거나 통합하는 결론을 성급하게 내리지 않는다.
- 같은 passage의 여러 문항을 독립 표본 여러 개로 과대계상하지 않는다.
- SDSS 또는 기존 code name을 먼저 보고 원문의 풀이 구조를 억지로 맞추지 않는다.
- 각 비교에서는 가장 강한 경쟁 풀이를 실제로 구성한다.

우선 anchor:
DV, GA,
DZ, EO, EP,
EJ,
AB, BZ, CT, GC,
FH, FN, FT, GJ, ET,
FF, FL,
FX, EF,
FD, EI

반드시 검토할 항목:

1. 판정 단위 분리
- 발문의 과제
- 원문/선지 관계
- 실제 결정 수행
- 선지가 바꾼 부분
- 증거 종류
- 기존 code가 설명하는 층

2. 증거 종류
- 직접 함의
- 합성 함의
- 명시 반례
- 지지 부족
- 미해결

3. 경쟁 코드 관계
- 배제
- 같은 국소 수행의 다른 표현
- 상위/하위 층위
- 별개의 추가 수행
- 미결

4. 교차 사례 검증
- DV/GA
- DZ/EO/EP
- AB/BZ/CT/GC
- FH/FN/FT/GJ/ET
- FF/FL
- FX/EF
- FD/EI

5. 각 후보 규칙에 대해
- 유지
- 수정
- 유보
- 반례
- 다음 falsification target
을 남긴다.

6. 학생의 실제 독해 행동으로 번역한다.
단, 강의용 간명화가 논리적 보편 규칙으로 오해되지 않도록 적용 조건을 명시한다.

최종 산출물:
- 기존 code와 별도로 '수행 연산 후보' 문서를 작성할 수 있다.
- 예: 분석/기본기_연구/수행연산_후보_v1.md
- 이것은 검증 중 가설이라고 명시한다.
- raw에는 필요한 semantic backfill/boundary revision만 append한다.
- 기존 판정을 소급 수정하지 않는다.

이 작업이 끝난 뒤 새 corpus 연구는 시작하지 말고 종료하라.