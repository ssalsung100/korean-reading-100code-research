# GitHub Private 백업 검증 보고서

작성일: 2026-10-08
상태: **PRIVATE 확인 대기 — 로컬 보안·LFS·원장 검증 완료**

## A. GitHub 저장소

- 계정 / 저장소: `ssalsung100/korean-reading-100code-research`
- 원격: `git@github.com:ssalsung100/korean-reading-100code-research.git`
- 브랜치: `main`
- SSH 계정 인증: `ssalsung100` 확인
- `git ls-remote`: 종료 코드 0, 원격 ref 조회 성공
- Visibility: 사용자의 GitHub 웹 Private 확인 응답 대기. 익명 웹/API 응답만으로 Private 여부를 입증하지 않음.
- commit / push: 로컬 커밋은 검증 후 준비 가능, push는 Private 확인 후 수행

## B. 백업 대상 및 LFS

- 작업 트리 파일 수: 약 16,213개 (`.git` 제외, ripgrep 파일 목록 기준)
- 예상 전체 자료 크기: 약 4.0 GiB
- 실제 staged LFS 포인터: 4,780개 파일, 4,022,980,786 bytes (3.7467 GiB)
- 중복 제거 LFS 객체: 3,561개, 3,210,576,670 bytes (약 2.989 GiB). 로컬 LFS 저장소 파일 수 3,561개 확인.
- staged 경로: 16,225개. 고유 Git 객체 데이터 약 205,900,045 bytes이며, LFS 포인터 크기를 포함한 값.
- 100 MiB 초과 파일: `통합사회/JIHAKSA_통합사회1_고_교과서.pdf` (118,315,728 bytes). `*.pdf` 규칙에서 `filter=lfs`, `diff=lfs`, `merge=lfs` 적용 확인.
- LFS 원격 quota/저장 공간: 계정 인증 API를 통한 확인 미완료.
- 주요 ignore 경로: `.tools/`(로컬 도구 설치 캐시), `.playwright-cli/`(브라우저 실행 자료). `.aws/`는 비어 있음. Python 캐시와 실행 로그 규칙은 기존 `.gitignore`를 유지.
- 실제 Git 추적 파일 수 및 일반 Git 크기: staging 이전이므로 미산출.

## C. 보안 검사

- 업로드 후보 전체의 바이너리 포함 패턴 검색에서 AWS access key 형식과 일치하는 바이트열이 3개 BMP에서 검출됨.
- 대상 파일:
  - `자료/통합사회_문항이미지_완전판/원본/통합사회1-3단원-Q024_01_image26.bmp`
  - `자료/통합사회_문항이미지/원본/통합사회1-3단원-Q023_01_image26.bmp`
  - `자료/통합사회_문항이미지/원본/통합사회1-4단원-Q019_01_image25.bmp`
- 일치 지점은 비압축 BMP의 pixel data 영역에만 있음. 첫 두 이미지는 SHA-256 동일한 중복 파일임. 세 이미지 모두 로컬 한국어·영어 OCR에서 AWS 키 형식 문자열이 검출되지 않음.
- 분류: **B — 이미지 픽셀 바이트에서의 우연한 패턴**. 일치 문자열 자체는 어떤 로그·보고서에도 기록하지 않음.
- 앞서 지정된 11개 의심 파일을 포함한 전체 후보의 정규식 검사에서 토큰 문자열·개인키 블록·서비스 토큰 형식은 검출되지 않았고, named-secret assignment 패턴도 검출되지 않음.
- 조치: 원본 이미지 변경 없이 보안 검사 통과로 기록.

## D. 연구 원장 검증

- queue: `record_id` 기준 7,605행 / 고유 ID 7,605 / 중복 0
- processed: `source_record_id` 기준 7,605행 / 고유 ID 7,605 / 중복 0
- pending: 0
- orphan: 0
- `research_data_index_enriched_v2.json`의 `case_to_group`: 1,671건
- `meta_state.json`: `meta_due=false`, `manual_parity_audit_due=false`, `depth_backfill_pending=[]`, `semantic_state_review=[]`
- G024/G370 hold 파일은 수정하지 않음.
- 아래 SHA-256 기준값은 push 전 현재 파일에서 산출했으며, 파일을 수정하지 않음.

| 파일 | SHA-256 |
|---|---|
| `astra_handoff_queue.jsonl` | `74b1e630ddb3808a1fc25d5d047514b8558ddd8f271d1d41a5d629fd568b4195` |
| `astra_handoff_processed.jsonl` | `c49e67a393b517671b94b6e0267689f8250fe55f6d4f2cd38e0cd954ef311818` |
| `prepared_backlog/manifest.jsonl` | `29bbdf41af019151d0342a846b3cfa48cec22142f41f24f5d895c4b8e4392e48` |
| `meta_state.json` | `2ac212abe6f83b7d2e97f9b2ef0b706bca92bd8bda7dfafb1a2482044be480fc` |
| `research_data_index.json` | `72401d0439e83c0c2dfce954a6c754df50a42322a117301b6852954e19097c01` |
| `research_data_index_enriched.json` | `4eea7dfa54d83253bd93c40923eb8ee13e52d57e7e68074d6a910ca0914ea806` |
| `research_data_index_enriched_v2.json` | `5bda68f7de147006c5ed87096a66439a4f120b0d106ebdb3f03a89035b34b414` |
| `G508_official_answer_recovery_20261008.json` | `bd842345be73305dfcec77f314a1f702793eb1ef91317b3b75e1c39721e5d1d5` |

## E. 백업 결과 및 후속 조치

- 결과: **로컬 staged / Private 확인 전 push 보류**
- 원격 HEAD 일치 및 LFS 업로드: 해당 없음 (push 미실행)
- `git diff --cached --check`: exit 2, 107,239개 진단(939개 파일; trailing whitespace 107,128건, blank-at-EOF 111건). 기존 원본 형식으로 판단해 연구 자료를 수정하지 않음.
- 핵심 연구 파일 제외: 없음. 전체 파일 staging 자체를 수행하지 않음.
- 재개 조건: 사용자가 GitHub 웹에서 저장소 Private 설정을 확인했다고 응답하거나 인증된 GitHub 조회로 Private을 입증할 것.
- Private 확인 전 원격 push 금지. 기존 연구 파일, provenance, G024/G370 hold는 변경하지 않음.
