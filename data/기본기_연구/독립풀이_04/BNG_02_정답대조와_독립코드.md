

<!-- luna-raw:BNG-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G480",
  "selected_answer": 5,
  "official_answer": 5,
  "match": true,
  "original_blind_preserved": true,
  "group_blind_barrier_verified": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2024/2024_answer_2024언어이해정답.pdf",
  "minimal_logic_without_codes": "본문은 주변부 집단에게 우천 비용 장벽이 크게 작용한다고 설명하므로⑤의 비용 증가를 더 작게 느낀다는 방향은 맞지 않는다.",
  "sdss_seen": false,
  "strict_blind_eligible": false,
  "source_restoration_before_disclosure": true,
  "incidental_future_source_exposure": "공식crop의오른쪽및아래에다음10~12번진리개념지문일부가포함되어우연히보였다.해당지문의공식답·SDSS·선지전체는읽지않았다.다음관련그룹시작시이부분본문노출을추가로기록하고strictblind성과에서제외한다.",
  "exposure_scope_clarification": "다음10~12번의답·태그·선지전체가미노출이다.BNG자체의선지전체는blind때읽었고공식답은그후대조했다."
}
```


<!-- luna-raw:BNG-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G480",
  "minimal_logic_without_codes": "본문이 설명한 집단별 비용 장벽의 방향을⑤의 직접비용 증가 비교에 적용하고, 보상 차이를 구성하는 두 비용 항의 부호를 나누어 읽는다.",
  "primary": [
    {
      "code": 86,
      "reason": "⑤는 집단별로 체감하는 우천 비용 증가의 크기를 반대로 비교한다.기저 비용 수준과 증가량을 구분한다."
    }
  ],
  "auxiliary": [
    {
      "code": 88,
      "reason": "R은 기대 혜택·만족에서 직접비용과 기회비용을 뺀 순보상으로 주어진다."
    },
    {
      "code": 92,
      "reason": "R맑음-R비의 부호와 두 비용 차이의 합을 수식대로 판독한다."
    },
    {
      "code": 43,
      "reason": "두 날씨 식에 동일한P,B,S가 주어진 조건 아래 비용 항의 차이를 비교한다."
    },
    {
      "code": 2,
      "reason": "공휴일의 기회비용 차이가 음수일 수 있다는④를 모든 유권자에게 필연인 것으로 확대하지 않는다."
    }
  ],
  "surface": [
    {
      "code": 49,
      "reason": "R과 참여 가능성의 같은 방향 관계가 있지만⑤는 특정 집단의 비용 증가 비교가 직접 쟁점이다."
    }
  ],
  "competing_codes": [
    {
      "code": 85,
      "rejection": "직접비용과 기회비용의 합이 일정하다고 주어진 것은 아니다.두 항은 함께 또는 반대로 변할 수 있다."
    },
    {
      "code": 46,
      "rejection": "날씨의 전체 인과 효과를 새로 추정하기보다 주어진 모형과 본문의 방향을 맞춘다."
    },
    {
      "code": 84,
      "rejection": "확률P가 있지만 이 문항에서 분모 변화나 비율 계산을 수행하지 않는다."
    }
  ],
  "scope_limit": "집단별 차이는 본문이 제시한 모형에 한정하며 실제 인구집단의 비용 크기를 독립적으로 계측·확정하지 않는다.",
  "source_note": "부등호>0을 공식 이미지로 확인했다.verified_tight_crop에서 후속 지문이 제외됐음을 직접 확인했으며 원crop의 다음 지문 부분 노출 이력은 보존한다.",
  "confidence": 0.94,
  "sdss_seen": false
}
```
