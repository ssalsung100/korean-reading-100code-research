

<!-- luna-raw:BKI-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G455",
  "selected_answer": 2,
  "official_answer": 2,
  "match": true,
  "original_blind_preserved": true,
  "group_blind_barrier_verified": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2019/2019_answer_2019_LEET_언어이해_정답표.hwp",
  "minimal_logic_without_codes": "동물권리론은 의무를 지니는 데 행동 조절 능력이 필요한지를 검토하므로 인간의 도덕 행위자 여부를 고려한다는 ②가 맞는다.",
  "sdss_seen": false,
  "strict_blind_eligible": false,
  "source_restoration_before_disclosure": true
}
```


<!-- luna-raw:BKI-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G455",
  "minimal_logic_without_codes": "동물권리론은 의무를 지니는 주체의 행동 조절 능력을 고려하므로 인간이 도덕 행위자인지 여부는 의무 판단에 관련된다.",
  "primary": [
    {
      "code": 79,
      "reason": "의무는 실행 능력을 전제한다는 당위-능력 관계를 실제 의무 주체에 적용한다."
    }
  ],
  "auxiliary": [
    {
      "code": 10,
      "reason": "도덕 행위 능력은 의무를 지니기 위한 필요 요건이다. 79와 동일 관계의 논리적 표상이므로 중복 계수하지 않는다."
    },
    {
      "code": 75,
      "reason": "공리주의적 총효용과 의무론적 행위·주체 조건, 포식 비판의 입장을 구분한다."
    },
    {
      "code": 15,
      "reason": "⑤에서 총효용 계산과 자연 질서 보존 자체라는 평가 기준을 같게 만들지 않는다."
    }
  ],
  "surface": [
    {
      "code": 88,
      "reason": "공리주의의 계산은 오답 판독 배경이며 ②의 직접 조건 적용과는 범위가 다르다."
    }
  ],
  "competing_codes": [
    {
      "code": 10,
      "rejection": "79의 당위-능력 관계와 같은 연산이므로 완전한 반증·유일 주 분리는 불가능하다. 79를 의미 영역 대표로만 둔다."
    },
    {
      "code": 48,
      "rejection": "생태계 변화나 동물 보호가 공통 소재여도 ⑤가 묻는 것은 동일 결과 자체보다 평가 기준의 차이다."
    },
    {
      "code": 63,
      "rejection": "이론에 대한 비판이 지문에 있으나 ②의 선택은 새 근거의 지지 효과가 아닌 이론 내용의 정확한 재진술이다."
    }
  ],
  "confidence": 0.93,
  "sdss_seen": false
}
```
