

<!-- luna-raw:BGZ-answer_check-20261002-r4-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G425",
  "blind_answer": 3,
  "official_answer": 3,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "sdss_seen": false,
  "official_answer_source": "자료/LEET_언어이해/원본/2011/2011_answer_2011_법학적성시험_언어이해_정답표.hwp",
  "logic_without_codes_fixed": "㉠의 상위 신적 질서/자연법과 (나)의 현행 성문·관습 인정법 사이의 위계를 보존한다.",
  "limitations": [
    "봉인 공식 전사 답과 대조. 원정답표 독립 시각 대조 미실시. 과거노출unknown 유지."
  ]
}
```


<!-- luna-raw:BGZ-independent_code-20261002-r4-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G425",
  "sdss_seen": false,
  "general_task": "네 주체의 법적 근거와 입장 비교",
  "decisive_relation": "자연법에 반하는 인정법은 효력이 없다는 상하 관계를㉠의 근거법과(나)의 현행법 비교에 적용",
  "primary": {
    "code": 9,
    "scope": "정답③",
    "reason": "두 법적 근거의 위계가 직접 정답 내용이다."
  },
  "auxiliary": [
    {
      "codes": [
        74,
        75
      ],
      "scope": "문항 전체",
      "reason": "기존 통합군을 적용하여㉠·㉡·(가)·(나)의 결론/근거/요건을 주체별로 보존한다."
    },
    {
      "code": 12,
      "scope": "정답③",
      "reason": "자연법 위반이면 인정법 무효라는 조건이 상위성을 뒷받침한다."
    },
    {
      "code": 10,
      "scope": "오답②",
      "reason": "동물 권리 인정에 법 변경이 필요한지라는 추가 요건을 기존법 해석과 분리한다."
    }
  ],
  "surface": [
    {
      "code": 79,
      "reason": "법적 권리 논쟁이지만 이 문항은 현실적으로 무엇을 허용해야 하는지 판단하지 않는다."
    }
  ],
  "competing_codes": [
    {
      "code": 39,
      "verdict": "포괄 작업 보조",
      "refutation": "비교라는 과제명은 맞지만 정답의 구체 위계를 따로 남겨야 한다."
    },
    {
      "code": 20,
      "verdict": "②에서 후보, 주로는 기각",
      "refutation": "현행법 해석으로 권리 주체 인정이 가능하다는 것은 법 변경의 비필수성을 시사하지만 정답③의 상하 관계가 핵심이다. 복수수단의 전면 나열이 있는 것도 아니다."
    },
    {
      "code": 58,
      "verdict": "⑤배제 보조",
      "refutation": "㉠㉡은 신의 질서를 공통 출발점으로 삼지만 결론은 인간 지배/동물 권리로 다르다. 공통전제만으로(나)와의 위계는 설명되지 않는다."
    }
  ],
  "falsification_attempt": "동물 권리를 인정한다는 결론이 같아도 근거가 자연법일 수도 현행법 해석일 수도 있다. 결론 일치→근거/변경요건 일치라는 추론은 성립하지 않는다.",
  "confidence": 0.97
}
```
