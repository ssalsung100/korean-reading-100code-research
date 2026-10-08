

<!-- luna-raw:AFA-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G192",
  "blind_answer": 3,
  "official_answer": 3,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "수소 추출 방식으로 쓰임을 활용됨이 보존.",
  "official_answer_source": "sealed canonical answer 기계 연결; 공식 배포 답표 직접 대조 아님",
  "group_barrier": "AEX/AEY/AEZ/AFA 전체 blind raw 저장 후 answer 필드만 공개",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AFA-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G192",
  "primary": [
    96
  ],
  "auxiliary": [],
  "surface": [
    16
  ],
  "logic_without_codes_fixed": "많이 쓰이는 열분해 방식은 많이 활용되는 방식으로 바꿀 수 있다. 다른 교체는 목적어 종류나 사건의 의미를 바꾼다.",
  "evidence": [
    "ⓒ 쓰이는 열분해는 수소 추출에 방법을 사용한다는 뜻.",
    "ⓑ 분자 결합 만들기는 물건 제작과 다르고ⓓ 전환율 얻기는 물건을 주워 얻는 습득(拾得)과 다름."
  ],
  "primary_scope": "문맥의 목적어·행위 유형을 보존하는 어휘 치환",
  "competitors_rejected": [
    {
      "code": 16,
      "reason": "과학 개념의 정의조건을 판별하는 것이 아니라 다의적 동사의 사용 적합성 검사."
    },
    {
      "code": 17,
      "reason": "목적어 종류 제약을 대상범주로 기술할 수 있지만 학술 대상집합의 귀속을 바꾸는 문제는 아니다.96의 구체 치환 연산을 대체할 이유 부족."
    },
    {
      "code": 98,
      "reason": "A의B라는 소유·주체 관계가 교환되는 문장이 아니다."
    }
  ],
  "counterfactual_test": "얻다의 목적어를 길에 떨어진 물건으로 바꾸면 습득이 가능해지지만 현재 전환율에서는 부적합하다. 동일 동사라도 논항과 문맥을 고정해야 한다.",
  "boundary_note": "ACN의 분별/깨달음처럼 가까운 의미를 비교하는 문제와 달리 AFA는 목적어·사건 유형 제약이 명확한 선택지가 많다. 같은96이라도 오답 매력과 근거의 깊이가 다르다.",
  "confidence": 0.98,
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
