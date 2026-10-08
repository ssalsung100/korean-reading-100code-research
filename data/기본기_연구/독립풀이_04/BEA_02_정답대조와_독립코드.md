

<!-- luna-raw:BEA-answer_check-20261002-r2-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G399",
  "all_group_blind_records_before_any_group_answer_check": true,
  "selected_answer": 3,
  "official_answer": 3,
  "match": true,
  "source": "sealed/answer_sdss.jsonl official_answer; 공식 페이지 검증 정본",
  "original_blind_preserved": true,
  "fixed_logic_without_codes": "지붕 확대→서까래 지지 한계→중도리 추가로 하중 분산. 대공→보→기둥의 간접 전달 보존.",
  "sdss_disclosed": false
}
```


<!-- luna-raw:BEA-independent_code-20261002-r2-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G399",
  "primary": [
    {
      "code": 46,
      "reason": "중도리 추가의 하중 분산 효과를 확인하는 것이 정답③의 직접 연산이다."
    }
  ],
  "auxiliary": [
    {
      "code": 19,
      "reason": "서까래의 하중 한계를 중도리 추가로 보완한다."
    },
    {
      "code": 40,
      "reason": "부재별 위치·연결을 복원하여 ②④를 검증한다."
    }
  ],
  "surface": [
    {
      "code": 44,
      "reason": "감주 목적은 ⑤의 일부 판정에 쓰이지만 정답③의 직접 근거는 하중 분산 기능이다."
    }
  ],
  "competing_codes": [
    {
      "code": 50,
      "rejection": "②에는 간접 전달 경로가 있지만 경로 차단 뒤 결과를 예측하지 않으므로 경로라는 말만으로 주 판정하지 않는다."
    },
    {
      "code": 87,
      "rejection": "①의 경사는 공간 기울기 소재일 뿐 변화율 계산은 없다."
    },
    {
      "code": 88,
      "rejection": "공간과 안정성의 장단점은 ⑤에 나타나나 비용·편익을 비교하여 최적 선택하지 않는다."
    }
  ],
  "boundary_note": "46/19는 효과 추적과 한계 보완이라는 서로 다른 설명 수준으로 중첩 가능. 강제 배타화하지 않는다.",
  "confidence": 0.91,
  "sdss_disclosed": false
}
```
