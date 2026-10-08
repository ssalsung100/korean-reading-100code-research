

<!-- luna-raw:AJY-answer_check-20260926-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G225",
  "blind_answer": 3,
  "official_answer": 3,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "정지 물체의 상은 안구 움직임에 따른 전체 이미지 이동과 같은 경로로 움직이므로 특정 종류 신경절세포가 신호를 내지 않는다. 따라서 그러한 세포가 존재한다는③이 맞다.",
  "official_answer_source": "자료/LEET_언어이해/원본/2022/2022_answer_2022_LEET_언어이해_정답표_배포용.pdf",
  "verification_scope": "정본 연결 sealed 공식답 필드 대조; 이번 단계에서 공식 PDF 답 셀 직접 판독은 아님",
  "barrier_verified": "G225 전체 blind raw 저장 후 공식답 필드만 공개",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AJY-independent_code-20260926-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    12
  ],
  "auxiliary": [
    17,
    1
  ],
  "surface": [
    4
  ],
  "judgment_reason": "정지 물체→안구 움직임에 의한 전체 이미지와 동일 경로→특정 신경절세포 무출력이라는 조건 적용으로③을 확인한다. 특정 종류의 반응 규칙을 모든 신경절세포로 확대하지 않는다.",
  "competing_codes": [
    {
      "code": 17,
      "verdict": "보조",
      "reason": "규칙 적용 대상을 특정 종류 신경절세포에 한정하고④의 칩/광수용체 역할을 분리한다. 그러나③에는 동일 경로 조건에서 무출력으로 가는 적용도 필요하다."
    },
    {
      "code": 1,
      "verdict": "보조",
      "reason": "출력 있음/없음은 결론 형태. 존재 여부만 읽어서는 정지 물체와 동일 경로의 연결을 복원하지 못함."
    },
    {
      "code": 4,
      "verdict": "표면",
      "reason": "존재한다는③ 양화는 일부 종류라는 본문과 맞으나 결정적인 오답이 모든/일부 치환에서 생긴 것은 아님."
    },
    {
      "code": 45,
      "verdict": "경쟁 후보·주 유보",
      "reason": "경로 일치 여부를 입력,출력 유무를 결과로 잡으면12와 국소 중첩한다. 동적 계산·연속 변환보다 명시 조건 적용이 최소 단위여서12를 작업 대표로 둔다."
    }
  ],
  "minimal_change_test": "③의 정지 물체를 배경과 다른 경로로 움직이는 물체로 바꾸면 특정 세포의 무출력 결론이 성립하지 않는다. 단순 대상명 교체만이 아니라 반응 조건 변화가 핵심.",
  "confidence": 0.92,
  "passage_group": "G225",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
