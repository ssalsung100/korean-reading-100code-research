

<!-- luna-raw:AST-blind-20260927-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G303",
  "selected_answer": 5,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "needed_information_locations": [
    "결정/비결정둘중하나필연이라는본문",
    "각경우에서자유의지부정",
    "온건결정론은결정이면자유없음거부"
  ],
  "minimal_logic_without_codes": "두 경우가 모두 같은 결론으로 이어지고 경우를 망라하기 때문에 결론이 나오며 두 조건문이 반대 관계라서가 아니다.",
  "intermediate_reasoning": [
    "①반대관계로바꾸면둘다거짓인제3가능성으로망라성깨짐.②가의필연성이탈출막음.③온건은나를부정.④가나다이면라유도.⑤나와다는동시에수용가능하며같은결론을지지."
  ],
  "attractive_wrong_answer": 1,
  "exact_error": "반대 관계와 모순 관계를 같은 배타성으로만 보면 둘 다 거짓일 가능성과 경우 망라의 차이를 놓친다.",
  "quota_status": "unavailable"
}
```
