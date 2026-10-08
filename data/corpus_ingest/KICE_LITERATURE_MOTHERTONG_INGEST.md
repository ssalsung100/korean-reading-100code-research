# KICE 문학 마더텅 로컬 원자료 재감사·중앙화 보고서

- 감사일: 2026-09-20
- authoritative 후보: `/mnt/d/국어/평가원 선지 빼먹기/2027_마더텅_수능기출문제집_국어_문학_문제편_한글_파일`
- 조사 범위: 하위 디렉터리 재귀 inventory, HWP/HWPX/PDF/MD/이미지 파일 목록·signature·내부 텍스트·학년도·시험명·문항 범위·작품명 교차 확인
- 검사한 마더텅 파일 수: 15개(원본 HWPX 7개 + 추출 MD 8개; HWP/PDF/이미지 0개)
- 파일별 signature·SHA-256·내부 학년도/시험 header는 [KICE_LITERATURE_MOTHERTONG_SOURCE_INVENTORY.json](KICE_LITERATURE_MOTHERTONG_SOURCE_INVENTORY.json)에 저장했다.

## 원자료 판정

7개 HWPX는 모두 ZIP signature(`50 4B 03 04`)였고, `Contents/section*.xml`을 직접 읽어 문단·표·도형 텍스트를 추출했다. 외부 폴더의 파일명은 2027 마더텅이지만 내부에는 2020~2026학년도 기출이 포함되어 있었다. 문제편 추출본에는 지문, 발문, 선택지, <보기>, [A]/[B], ㉠·㉡이 보존되어 있으며 마더텅 해설·정답·작품 해설은 중앙 MD에 넣지 않았다.

대상 문항 블록에 평가 판단에 필요한 그림·표 asset은 없었다. 따라서 새 asset은 0개다. 공식 정답은 마더텅 자료가 아니라 기존 평가원 정답표 경로를 연결했다.

## 회차별 source 상태

| 학년도 | 시험 | 대상 문항 | source HWPX | 중앙 문학 MD | 상태 | 추가 다운로드 |
|---:|---|---:|---|---|---|---|
| 2026 | 수능 | Q18–34 | Ⅴ 고전산문·Ⅲ 갈래복합·Ⅳ 현대소설·Ⅱ 고전시가/시복합 | Q18-21, Q22-26, Q27-30, Q31-34 | LOCAL_COMPLETE | 없음 |
| 2024 | 수능 | Q22–29, Q32 | Ⅲ 갈래복합·Ⅳ 현대소설·Ⅱ 고전시가/시복합 | Q22-27, Q28-31, Q32-34 | LOCAL_COMPLETE | 없음 |
| 2023 | 수능 | Q31–34 | Ⅰ 현대시 | Q31-34 | LOCAL_COMPLETE | 없음 |
| 2023 | 9월 모평 | Q28–31 | Ⅳ 현대소설 | Q28-31 | LOCAL_COMPLETE | 없음 |
| 2023 | 6월 모평 | Q32–34 | Ⅰ 현대시 | Q32-34 | LOCAL_COMPLETE | 없음 |
| 2022 | 수능 | Q28–31 | Ⅴ 고전산문 | Q28-31 | LOCAL_COMPLETE | 없음 |
| 2021 | 수능 | Q43 | Ⅰ 현대시 | Q43-45 원문 블록 | LOCAL_COMPLETE | 없음 |
| 2020 | 수능 | Q43–45 | Ⅰ 현대시 | Q43-45 | LOCAL_COMPLETE | 없음 |

2024 수능 Q28–29는 실제 원문 지문군이 Q28–31로 묶여 있어 중앙 MD도 Q28-31 블록으로 보존했다. 2021 수능 Q43은 실제 원문 블록 Q43–45 안에서 보존했다.

## 중앙화 원칙과 provenance

중앙 MD 13개 각각에 다음을 기록했다.

- `source_original_path`: 외부 마더텅 원본 HWPX 절대 경로
- `source_filename`, 원본 SHA-256
- `extraction_method`: HWPX ZIP `Contents/section*.xml` 문단·표·도형 텍스트 추출 후 문항 블록 절취
- `source_type`: `mother_tong_hwp_or_hwpx_transcription`
- 학년도·시험·문항 범위
- 기존 평가원 공식 정답표 경로

문항별 `candidate_id`·작품명·source path·SHA-256·중앙 MD·정답 source·canonical/preparation status는 [kice_literature_local_audit_target_mapping.json](kice_literature_local_audit_target_mapping.json)에 45개 레코드로 갱신했다. 현재 독서 전용 JSON에 문학을 강제 병합하지 않고 `LITERATURE_CANONICAL_SCHEMA_NEEDED`와 `READY_LOCAL_LITERATURE_SOURCE`로 표시했다.

## 최종 집계

- 검사한 마더텅 파일 수: 15
- target 45문항 중 source 찾은 수: 45
- LOCAL_COMPLETE: 45
- LOCAL_RESTORABLE: 0
- LOCAL_PARTIAL: 0
- EXTERNAL_SOURCE_NEEDED: 0
- 생성한 중앙 문학 MD: 13
- 추출한 asset: 0
- 실제로 남은 KICE 다운로드 회차: 0
- 2008 LEET 예비시험 다운로드 후보: 기존 상태 유지(별도 대상)

검산: `45 = 45 + 0 + 0 + 0`.

문항을 풀거나 정답·100코드를 추론하지 않았고, 연구 queue·processed·meta_state·기존 semantic 판정은 수정하지 않았다.
