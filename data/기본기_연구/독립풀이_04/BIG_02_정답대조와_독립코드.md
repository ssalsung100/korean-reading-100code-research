

<!-- luna-raw:BIG-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G437",
  "blind_answer": 5,
  "official_answer": 5,
  "match": true,
  "original_blind_preserved": true,
  "all_group_blind_records_before_any_group_answer_check": true,
  "sdss_seen": false,
  "official_answer_source": "자료/LEET_언어이해/원본/2017/2017_answer_2017학년도_법학적성시험_언어이해_정답표.hwp",
  "logic_without_codes_fixed": "유한책임의하방손실제한과양의잔여가치상방증가가위험선호유인이다.잔여가치감소자체를목적으로삼는것이아니다.",
  "limitations": [
    "봉인 공식 전사 답 대조. 원정답표 시각 재대조 미실시. unknown strict 제외 유지."
  ]
}
```


<!-- luna-raw:BIG-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G437",
  "sdss_seen": false,
  "general_task": "비대칭 손익구조에서 위험선호 동기 해석",
  "decisive_relation": "성공시 잔여이익 상승과 파산시 손실상한이 위험수용을 유인",
  "primary": {
    "code": 78,
    "scope": "⑤",
    "reason": "주주의 위험사업 선호 이유를 잘못된 잔여가치 감소 목표로 바꾼 오류를 판별."
  },
  "auxiliary": [
    {
      "code": 45,
      "scope": "①②③",
      "reason": "자산A,부채D에서 주주 잔여청구액은 max(A-D,0)이라는 분기 구조.원투자액 기준 손실상한과 구분."
    },
    {
      "code": 88,
      "reason": "상방이익과 하방손실의 비대칭이 선택유인을 만든다."
    },
    {
      "code": 86,
      "scope": "②⑤",
      "reason": "A-D의 증가/감소 방향과0경계 비교."
    }
  ],
  "surface": [
    {
      "code": 90,
      "reason": "위험의확률이언급되어도구체적성공확률·기대수익계산은필요없다."
    }
  ],
  "competing_codes": [
    {
      "code": 92,
      "verdict": "보조표상",
      "refutation": "max함수로손익을표현하면도움되나구체숫자계산없이비대칭유인을판정할수있다."
    },
    {
      "code": 54,
      "verdict": "주기각",
      "refutation": "모든주주가언제나고위험사업을택한다는필연결정까지본문은요구하지않는다."
    },
    {
      "code": 83,
      "verdict": "주기각",
      "refutation": "경제적손익구조를도덕가치판단의옳고그름으로평가하는문항이아니다."
    }
  ],
  "countermodel": "가상의부채100에서자산80과50은모두잔여청구액0으로주주손실하한이같다.자산130이면잔여30을받는다.이는본문구조의예시이며현실기업수치가아니다.",
  "unresolved": "본문모형밖 평판·보증·별도책임은 도입하지 않는다.원투자손익과잔여청구액을동일량으로혼동하지않는다.",
  "confidence": 0.97
}
```
