# 평가원 공식 국어·언어 정답표 수집본

## 수집 범위

한국교육과정평가원 수능 홈페이지의 공식 게시판에서 2010학년도 이후의 국어/언어 영역을 수집했다.

- 대학수학능력시험: [공식 기출문제 게시판](https://www.suneung.re.kr/boardCnts/list.do?boardID=1500234&m=0403&s=suneung)
- 수능 모의평가: [공식 모의평가 게시판](https://www.suneung.re.kr/boardCnts/list.do?boardID=1500236&m=0403&s=suneung)
- 각 게시물의 `문제 및 정답` 첨부파일에서 정답표를 내려받았다.

## 산출물

| 파일 | 역할 |
| --- | --- |
| `manifest.json` | 공식 게시물·파일 식별자, 원본 다운로드 URL, 등록일, SHA-256, 처리 상태 |
| `manifest.tsv` | 같은 목록의 표 형식 |
| `board_index_csats.json`, `board_index_mock.json` | 공식 게시판 전체 페이지에서 추출한 영역별 게시물 색인 |
| `normalized_answer_keys.json` | 추출된 정답표를 문항 번호→정답 기호로 정규화한 데이터 |
| `passage_answer_links.json` | `고3 기출/hwpx_텍스트_연도별.md`의 163개 지문 구간과 정답표 연결 결과 |
| `원본/수능/` | 수능 정답표 원본 PDF/구형 ZIP |
| `원본/모의평가/` | 모의평가 정답표 원본 PDF/구형 ZIP |
| `추출/모의평가/` | 구형 ZIP에서 풀어낸 PDF 원본 |

## 현재 검증 결과

- manifest 항목: 61개 (PDF 51, ZIP 10)
- 정규화된 정답표: 55개 (문항 수 45 또는 50)
- OCR 필요: 7개 (스캔 PDF라 텍스트 레이어가 없음)
- 기존 HWPX 지문 구간: 163개
- 정답표 자동 연결: 155개
- 미연결 8개는 정답표가 없어서가 아니라 OCR 대상이거나, 해당 회차의 지문 구간이 현재 HWPX 추출본에 없는 경우다.

## 처리 재현

```bash
python3 scripts/build_kice_answer_manifest.py
python3 scripts/extract_kice_answer_keys.py
python3 scripts/link_kice_answers_to_passages.py
```

정답표 원본은 평가원 저작권 자료이므로 프로젝트 내부 검토용으로만 사용하고, 외부 배포 시에는 평가원 이용 조건을 확인한다.
