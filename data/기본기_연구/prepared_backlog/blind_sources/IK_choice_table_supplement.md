# IK 선택표 원문 XML 전사 보충

이 파일은 blind source의 선택표 구조를 기계적으로 보강하기 위한 supplement다. 정답·곡선과 기체의 대응·해설·SDSS·코드 판정은 포함하지 않는다.

## 원문 앵커와 추출 경로

- source container: `고3 기출/2027 고3 국어 독서_Ⅲ. 과학.hwpx`
- XML part: `Contents/section0.xml`
- XML 요소: `hp:tbl` 내부의 `hp:tr` / `hp:tc` / `hp:cellAddr` / `hp:t`
- 확인 기준: 열 제목 셀과 번호별 셀의 `colAddr`, `rowAddr`, 텍스트를 직접 추출
- source status: 로컬 HWPX 편집본 XML 확인
- 원배포 PDF 직접 검증: 수행하지 않음

## 열 순서

| XML `colAddr` | 열 제목 (`rowAddr=0`) |
|---:|---|
| 1 | 아르곤(25℃) |
| 2 | 아르곤(727℃) |
| 3 | 크립톤(25℃) |

`colAddr=0`은 번호 열이며, 열 제목은 비어 있다.

## 번호별 셀 전사

| 번호 셀 (`colAddr=0`) | `colAddr=1` | `colAddr=2` | `colAddr=3` |
|---|---|---|---|
| ① (`rowAddr=1`) | A | B | C |
| ② (`rowAddr=2`) | A | C | B |
| ③ (`rowAddr=3`) | B | C | A |
| ④ (`rowAddr=4`) | B | A | C |
| ⑤ (`rowAddr=5`) | C | B | A |

이 전사는 표의 열·행과 기호를 보존한 구조 기록이며, 어느 행이 정답인지 판단하지 않는다.

## 이전 근거와 구분

기존 `IK_graph_provenance.json`의 선택표 행 순서는 blind packet 텍스트 앵커에 근거했다. 이 supplement는 그 기록을 덮어쓰지 않고, 같은 행 순서를 실제 로컬 HWPX `section0.xml`에서 별도로 확인한 기계 근거다.
