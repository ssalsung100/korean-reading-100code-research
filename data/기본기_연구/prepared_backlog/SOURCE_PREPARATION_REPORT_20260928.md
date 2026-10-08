# Target universe source preparation — 2026-09-28

이 기록은 source preparation만 다룬다. semantic research, 정답 대조, SDSS 비교, 코드 판정은 수행하지 않았다.

## LEET source selection

LEET 문항 본문은 passage 단위 검수 완료 Markdown을 먼저 확인하고, exact passage 파일이 없을 때 연도별 홀수형 canonical Markdown을 사용한다. 두 Markdown에서 필요한 텍스트나 시각 정보가 빠진 경우에만 원본 HWP/HWPX 및 필요한 page-render crop을 fallback으로 쓴다. page PNG 전체를 blind source에 연결하지 않는다.

준비기 `scripts/prepare_target_universe.mjs`는 exact `전사_검수완료/{YEAR}/qXX-YY.md`를 먼저 선택하고, 없으면 `텍스트/{YEAR}/{YEAR}_question_odd.md`를 선택하도록 수정했다. target crosswalk에서 확인된 verified transcript 59건은 모두 기존 `COMPLETED_TARGET`이므로 보호 상태로 유지했고 재준비하지 않았다.

## Target status

| 상태 | 문항 수 | passage group 수 |
|---|---:|---:|
| COMPLETED_TARGET | 619 | — |
| NOT_COMPLETED_READY_LOCAL_SOURCE | 450 | 151 |
| NOT_COMPLETED_NEEDS_RESTORE | 61 | 22 |
| NOT_COMPLETED_SOURCE_MISSING | 5 | 1 |
| HOLD | 4 | 1 |
| AMBIGUOUS_COMPLETION | 8 | 5 |
| 합계 | 1,147 | — |

미완료 target은 528문항이다. 신규 준비로 `COMPLETED_TARGET` 수는 늘지 않았다. 가족별 READY는 KICE 4, LEET 352, MEET 94, DEET 0이다.

남은 `NEEDS_RESTORE` 61문항은 LEET 54문항/17 groups, MEET 6문항/4 groups, KICE 1문항/1 group이다. `SOURCE_MISSING`은 LEET 2008 예비 Q4–8의 5문항이다. 기존 HOLD 4문항과 completion 불명확 8문항은 보존했다.

## Prepared backlog

- READY: 450문항, 151 groups; G365–G515, AZZ–BRG.
- 이번에 추가: 20문항, 7 groups; G509–G515, BQN–BRG.
- 추가 가족 구성: LEET 20문항/7 groups.
- 전체 manifest의 `prepared` entry 454건에는 기존 HOLD G024 4건이 포함된다.

이번에 추가한 groups는 G509 2017 Q1–3, G510 2017 Q11–13, G511 2018 Q10–12, G512 2019 Q1–3, G513 2017 Q33/Q35, G514 2018 Q13–15, G515 2012 Q33–35다.

## Source restoration

- `<보기>` 0, `<가정>` 0.
- 강조·표적 구절: 5 groups에서 필요한 구간만 7개 crop asset으로 복원했다. canonical Markdown의 passage, stem, choices를 유지하고 crop에는 필요한 강조 구간만 담았다.
- Q33–35의 마지막 `<표>`가 문항 뒤 행정 확인란인 경우 2017 Q33/Q35와 2012 Q33–35에서 해당 꼬리표만 제외했다. 각 blind source의 질문 본문과 선지는 canonical Markdown에서 왔다.
- 2016 Q33–35에는 passage 안에 실제 `<표>`가 남아 있어 준비하지 않았다.
- 복원 원문, page/HWP hash, crop 범위, case linkage는 `sealed/source_restorations_v1.jsonl` 및 provenance mapping에 기록했다. 신규 answer/SDSS sidecar의 값은 읽지 않았으며 null 상태다.

## Verification

신규 G509–G515에 대한 별도 검증 결과:

- duplicate candidate/question/case: 0
- COMPLETED_TARGET/HOLD/AMBIGUOUS_COMPLETION overlap: 0
- blind answer 또는 SDSS leakage: 0
- source provenance/hash 및 passage/question linkage error: 0
- empty passage/stem, choice 오류, 남은 visual placeholder: 0
- 필수 visual 누락, output path conflict: 0
- queue/processed 변경: 없음; 각각 5,234건, pending 0

repository 전체 `verify_prepared_backlog.py`는 기존 사례에서 발생하는 24개 오류 때문에 exit 1이다. 이 오류 중 G509–G515 사례는 0건이다. 전체 content leakage, blind leak, question duplicate도 0이다.

Semantic research 누적은 1,156 cases이며 그대로다. 다음 Astra semantic start는 기존 frontier인 **G365 / AZZ**다.
