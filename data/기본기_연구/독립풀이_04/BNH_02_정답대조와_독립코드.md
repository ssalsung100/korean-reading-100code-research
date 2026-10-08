

<!-- luna-raw:BNH-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G481",
  "selected_answer": 4,
  "official_answer": 4,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2024/2024_answer_2024언어이해정답.pdf",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "일치의 두 방향에서 기준과 대상이 교환된다. 존재론적 진리에서 기준인 지성은 인식론적 진리에서는 사물과 비교되어 판정되는 대상이다. 따라서④.",
  "strict_blind_eligible": false,
  "sdss_seen": false,
  "exposure_note": "이전 crop의 지문 일부 노출 이력 보존; 정답 일치를 strict-blind 성과로 집계하지 않는다."
}
```


<!-- luna-raw:BNH-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G481",
  "minimal_logic_without_codes": "지성에 사물이 일치할 때의 기준인 지성이 사물에 지성이 일치할 때에는 판정 대상이 된다. 일치의 방향에 따라 관계항의 역할을 바꿔 추적한다.",
  "primary": [
    {
      "code": 17,
      "reason": "같은 지성이라는 항이 두 진리 차원에서 기준과 대상 중 어떤 역할을 맡는지 보존하는 것이④의 직접 판정이다."
    }
  ],
  "auxiliary": [
    {
      "code": 16,
      "reason": "사태적·명제적 진리의 정의를 방향까지 분해한다."
    },
    {
      "code": 80,
      "reason": "명제적 진리에서 인식 내용과 객관적 사물의 관계를 유지한다."
    },
    {
      "code": 81,
      "reason": "사태적 진리에서는 사물 존재의 참됨을 판단한다."
    },
    {
      "code": 3,
      "reason": "①②에서 맹아/보편화와 작품별 입장의 차이를 구별한다."
    }
  ],
  "surface": [
    {
      "code": 46,
      "reason": "③ 조건과 결과의 역전에는 쓰이나④의 주 연산은 인과효과 산출이 아니다."
    }
  ],
  "competing_codes": [
    {
      "code": 39,
      "rejection": "두 차원 비교라는 일반 표상은 맞지만 결정점은 기준/대상의 방향별 귀속이며 단순 공통점 찾기로 충분하지 않다."
    },
    {
      "code": 21,
      "rejection": "정의가 있지만④는 필요충분성을 양방향 적용해서 답을 내는 문제가 아니다."
    },
    {
      "code": 75,
      "rejection": "철학자 견해는 여럿이나④는 고전적 정식 내부의 두 방향 대응이며 견해 경쟁이 필수는 아니다."
    }
  ],
  "boundary_note": "17은 물건의 종별 범주에 한정하지 않고 관계항 역할 귀속이라는 작업 후보로 사용한다.80/81은 판정 차원의 실질 보조이며 번호 전체의 독립성·병합을 확정하지 않는다.",
  "confidence": 0.9,
  "sdss_seen": false
}
```
