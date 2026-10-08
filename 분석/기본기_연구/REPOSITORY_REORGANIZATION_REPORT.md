# 저장소 자료 재구성 검증 보고서

작성일: 2026-10-06

이번 실행은 계획·인벤토리·기계적 index 작성으로 한정했다. 기존 파일 이동·이름 변경·삭제·경로 rewrite는 0건이다. 아래 전후값은 작성 직전/직후의 저장소 원장 상태를 다시 읽어 비교했다.

## 불변성 및 상태 확인

- queue: 7605 rows, SHA-256 `74b1e630ddb3808a1fc25d5d047514b8558ddd8f271d1d41a5d629fd568b4195`; processed: 7605 rows, SHA-256 `c49e67a393b517671b94b6e0267689f8250fe55f6d4f2cd38e0cd954ef311818`.
- pending: 0; duplicate `record_id`: 0; orphan processed: 0.
- manifest: 1671 rows/cases; 상태 분포 {'consumed_sdss': 1663, 'prepared': 8}.
- meta_state: completed groups=497, completed cases=1663, meta_due=False, manual_parity_audit_due=False, depth_backfill_pending=[].
- 현재 미완료 manifest cases: DR, DS, DT, DU (G024); BAP, BAQ, BAR, BAS (G370).
- blind source 미존재: 0; 목록: [].
- blind/sealed structural key leakage 후보: 0; 목록: [].
- 후보 경로 누락 토큰: 725. 자동 수정하지 않았으며 후보 전체는 inventory에 기록.
- 완전 동일 SHA-256 파일군: 9. 격리/삭제하지 않음.

## 제한 및 판정

- 원장 무결성: queue/processed를 변경하지 않았으며 hash/row count를 유지했다.
- manifest case 수와 meta_state 완료/hold 관련 값은 수정하지 않았다.
- leakage 확인은 blind JSON의 필드명 구조 검색만 수행했다. 자유 텍스트 안의 공식 답/태그를 의미적으로 판독하지 않았으므로 이는 구조 검사 결과이며 의미적 누출 0의 보증으로 확대하지 않는다.
- 경로 참조는 스캔 대상 텍스트에서 저장소 상대경로 토큰의 정확 일치를 확인했다. 템플릿/기록/외부 절대 경로에 따른 오탐 가능성이 있어 dangling 후보는 모두 사람 확인 대상으로 남겼다.
- verifier와 restore script는 실행하지 않았다. 이번 작업은 경로 및 원장에 변화가 없어 기준선 영향은 없으나, 향후 실제 이동 계획의 통과 여부는 이 결과로 승인되지 않는다.
- 실제 이동·삭제·reference rewrite: 0.
