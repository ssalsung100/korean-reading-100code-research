

<!-- luna-raw:BEB-answer_check-20261002-r2-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G399",
  "all_group_blind_records_before_any_group_answer_check": true,
  "selected_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "fixed_logic_without_codes": "5개 지지점 사이 4칸, 내부3개에서 감주를 한 개 이상 실제 수행하면 잔여0~2개.",
  "unresolved": "공식답 일치는 보 사용→실제 감주라는 문맥 해석을 지지할 뿐, 중복 보를 단 구조의 물리적 불가능을 증명하지 않는다.",
  "sdss_disclosed": false
}
```


<!-- luna-raw:BEB-independent_code-20261002-r2-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G399",
  "primary": [
    {
      "code": 92,
      "reason": "5개 지지점→4칸, 내부3개에서 1개 이상 제거→0~2개라는 개수 상한 산출."
    }
  ],
  "auxiliary": [
    {
      "code": 44,
      "reason": "보를 기둥을 실제 대체하는 수단으로 읽어 감주량의 최소값1을 설정한다."
    },
    {
      "code": 40,
      "reason": "도리·대공·보·기둥의 지지 구조가 개수 산출의 전제다."
    }
  ],
  "surface": [
    {
      "code": 87,
      "reason": "③의 지붕 경사는 공간 소재이며 정답 결정 계산은 기울기가 아니다."
    }
  ],
  "competing_codes": [
    {
      "code": 90,
      "rejection": "가능한 잔여 개수의 범위이지 배치 조합수나 확률을 세지 않는다."
    },
    {
      "code": 31,
      "rejection": "원소 수와 집합 수를 혼동한 문제가 아니라 기둥 수와 칸수의 구조적 대응이다."
    },
    {
      "code": 10,
      "rejection": "보 사용의 의미에 감주 조건이 필요하지만 명시된 필요조건을 독립 추론하는 구조보다 산술 상한 판정이 직접적이다."
    }
  ],
  "uncertainty": "44에 의한 사용 의미 제한은 문맥적이다. 형식적 필연으로 강화하지 않는다.",
  "confidence": 0.83,
  "sdss_disclosed": false
}
```
