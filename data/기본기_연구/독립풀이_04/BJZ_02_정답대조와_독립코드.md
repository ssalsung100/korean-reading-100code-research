

<!-- luna-raw:BJZ-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G452",
  "selected_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "group_blind_barrier_verified": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2019/2019_answer_2019_LEET_언어이해_정답표.hwp",
  "minimal_logic_without_codes": "제정 초기 문화 존중에 따른 그리스 지식인의 자존·정체성 유지가 ④와 일치한다. 시기·평가 주체·정책 동기를 바꾼 나머지 선지는 배제한다.",
  "sdss_seen": false,
  "strict_blind_eligible": false,
  "exposure_note": "과거 노출 여부 unknown 보존; 이번 풀이 전에 정답·태그는 읽지 않았다."
}
```


<!-- luna-raw:BJZ-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G452",
  "minimal_logic_without_codes": "문화 존중을 받으며 그리스 정체성을 유지한 제정 초기 지식인의 태도를 정확히 귀속하고, 다른 시기·주체·동기를 끼워 넣은 진술을 구별한다.",
  "primary": [
    {
      "code": 75,
      "name": "경쟁입장",
      "reason": "④의 타협주의 태도 귀속 및 ③의 속주 지식인/로마 전통 지배층 견해 교환을 판별하는 작업 대표. 실제 대립 논쟁의 존재까지 주장하지 않는다."
    }
  ],
  "auxiliary": [
    {
      "code": 3,
      "name": "선후",
      "reason": "①은 서기 2세기 중엽의 통치 평가를 공화정 말기에 옮긴다. 시기 보존이 독립된 오답 배제 근거다."
    },
    {
      "code": 44,
      "name": "수단/목적",
      "reason": "⑤의 정책 목적을 지배 비결에서 보편 시민 양성으로 교환했는지 확인한다."
    },
    {
      "code": 80,
      "name": "인식론적도식",
      "reason": "로마 정책에 대한 외부 해석과 로마인의 실용적 인식을 구별한다. 75와 주체별 평가 귀속에서 중첩하며 별도 연산으로 중복 계수하지 않는다."
    }
  ],
  "surface": [
    {
      "code": 5,
      "reason": "태도 변화는 지문 구성이나 정답 직접 근거는 특정 시기의 태도 귀속이다."
    }
  ],
  "competing_codes": [
    {
      "code": 80,
      "rejection": "인식 주체·평가 귀속에서는 75와 중첩하므로 유일 주를 확정하는 반증은 실패. 75를 작업 대표로만 둔다."
    },
    {
      "code": 46,
      "rejection": "문화 존중→자존 유지의 배경 인과는 있으나 새 인과 경로의 계산·효과 검증을 하지 않는다."
    },
    {
      "code": 97,
      "rejection": "연설문이 존재하지만 ⑤는 발화의 의도를 묻는 것이 아니라 통치 정책의 실제 목적과 해석을 혼동한다."
    }
  ],
  "boundary_note": "정답 직접 수용과 오답 배제의 연산은 다르다. 75/80 유일 주 우선은 유보한다.",
  "confidence": 0.86,
  "sdss_seen": false
}
```
