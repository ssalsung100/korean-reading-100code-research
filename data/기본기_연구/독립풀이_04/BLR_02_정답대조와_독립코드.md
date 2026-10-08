

<!-- luna-raw:BLR-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G467",
  "selected_answer": 2,
  "official_answer": 2,
  "match": true,
  "original_blind_preserved": true,
  "group_blind_barrier_verified": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2020/2020_answer_2020_LEET_언어이해_정답표.hwp",
  "minimal_logic_without_codes": "큰원궤도는지구에서멀고중력이약해원궤도속력이더느리므로지름이클수록빠르다는②가부적절하다.",
  "sdss_seen": false,
  "strict_blind_eligible": false,
  "source_restoration_before_disclosure": true,
  "background_knowledge_limit_preserved": "거리증가에따른중력약화라는기존물리지식을원궤도중력-속력문장에연결했다.본문의복원식에는힘의역제곱법칙이나원궤도속력식이명시돼있지않으므로그식이원문에있었다고기록하지않는다."
}
```


<!-- luna-raw:BLR-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G467",
  "minimal_logic_without_codes": "원궤도반경이증가할때공전속력이감소하는방향을②의증가주장과대조한다.",
  "primary": [
    {
      "code": 49,
      "reason": "원궤도크기와속력의변화방향을판독한다.통계적공변으로만제한하지않는다."
    }
  ],
  "auxiliary": [
    {
      "code": 91,
      "reason": "④의같은힘아래질량-가속도반비례를적용한다."
    },
    {
      "code": 43,
      "reason": "작용반작용의같은힘을고정한채기체와우주선의질량차이를비교한다.실험설계주장아님."
    },
    {
      "code": 46,
      "reason": "⑤는분사→일시감속→작은궤도→짧은주기의연쇄를복원한다."
    }
  ],
  "surface": [
    {
      "code": 92,
      "reason": "식은관계확인에쓰이고수치대입계산은없다."
    }
  ],
  "competing_codes": [
    {
      "code": 86,
      "rejection": "단순수치대소보다반경변화에따른속력방향이핵심이며정량속력비는주어지지않는다."
    },
    {
      "code": 45,
      "rejection": "반경에서속력으로의대응으로표상가능해49와국소중첩한다.유일주우선유보."
    },
    {
      "code": 5,
      "rejection": "개별우주선의시간상변화만이아니라서로다른원궤도조건의관계비교다."
    }
  ],
  "source_limit": "거리-중력약화의배경지식사용을보존.본문에원궤도속력식이직접있었다고간주하지않는다.",
  "confidence": 0.91,
  "sdss_seen": false
}
```
