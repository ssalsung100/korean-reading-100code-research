

<!-- luna-raw:BNR-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G484",
  "selected_answer": 4,
  "official_answer": 4,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2024/2024_answer_2024언어이해정답.pdf",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "무왕·문왕의 예는 아버지의 밝은 선택과 아들의 계승이 왕조의 기틀을 세운다는 관계를 인조·효종에 대응시킨다. 종통의 실질이 이미 확고하다는④이다.",
  "strict_blind_eligible": false,
  "sdss_seen": false
}
```


<!-- luna-raw:BNR-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G484",
  "minimal_logic_without_codes": "문왕의 자식 선택과 무왕의 계승으로 왕조 기반이 섰다는 관계를 인조의 선택과 효종의 계승에 대응시켜 종통의 실질을 강조한다.",
  "primary": [
    {
      "code": 69,
      "reason": "인물의 표면 동일성이 아니라 아버지의 선택→아들의 계승→왕조 기반이라는 관계를 옮기는 유추다."
    }
  ],
  "auxiliary": [
    {
      "code": 17,
      "reason": "인조-문왕, 효종-무왕의 역할을 바꾸지 않는다."
    },
    {
      "code": 97,
      "reason": "사례를 인용한 의도를 복제 결정이 아닌 이미 성립한 종통의 실질 확인으로 읽는다."
    },
    {
      "code": 62,
      "reason": "복제의 높낮이가 종통의 명확성을 결정한다는 관련성을 글쓴이는 부정한다."
    }
  ],
  "surface": [
    {
      "code": 86,
      "reason": "복제 기간의 높낮이라는 비교가 등장하지만④의 직접 행동은 유추의 대응 구조다."
    }
  ],
  "competing_codes": [
    {
      "code": 37,
      "rejection": "일반 규칙에 맞는 사례를 단순 확인하기보다 두 역사적 관계 구조의 대응을 논거로 쓴다."
    },
    {
      "code": 94,
      "rejection": "⑤의 지향 표현만으로 종통이 부재함을 필연적으로 함축한다고 일반화하지 않는다. 여기서 문제는 본문이 강조한 이미 확립된 종통과 사례 인용 목적의 불일치다."
    },
    {
      "code": 10,
      "rejection": "장자라는 신분을 종통 계승의 필수 조건으로 부여하는 유추가 아니다. 본문은 그 조건 의존을 거부한다."
    }
  ],
  "confidence": 0.94,
  "sdss_seen": false
}
```
