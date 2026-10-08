

<!-- luna-raw:BJV-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G450",
  "selected_answer": 5,
  "confidence": 0.96,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": [
    "data/기본기_연구/prepared_backlog/blind_sources/BJV.json",
    "data/기본기_연구/prepared_backlog/blind_sources/G450_visual01.md"
  ],
  "necessary_information": [
    {
      "location": "본문목적일치/분리및결론",
      "evidence": "소선거구·동시선거·결선투표는일반적으로일치경향이나정치환경에따라효과다름."
    },
    {
      "location": "보기",
      "evidence": "4부족35/30/20/15,각거주지에서압도다수,부족정당지지.대통령전국단순다수,의회전국비례·분리선거.모두대통령제유지합의."
    }
  ],
  "minimal_logic_without_codes": "부족거주경계별소선거구면각지역의부족정당이계속우세하여의회가부족별로갈린다.일반소선거구경향을이환경에그대로적용해목적일치를보장하는⑤가부적절하다.",
  "intermediate_reasoning": [
    "①의회과반총리선출은어느부족도단독과반이없어연합을유도할수있다.대통령제유지와내치총리분담이원천적으로양립불가라고본문은말하지않는다.",
    "②목적분리상태에서대통령결정권을강화하면교착에도집행효율을높일수있다는기존권고와맞는다.③동시선거는일치성을높이는경향이라는본문규칙에부합.",
    "④결선과정의정당연합은과반지지확보와정치적협력을촉진할수있다.",
    "⑤각부족의지역별압도다수라는특수조건은선거방식이름만으로단일전국다수파가생긴다는추론을막는다.지역구수·인구배분의정확의석계산은미제시이므로특정의석수는만들지않는다."
  ],
  "most_attractive_wrong": {
    "choice": 1,
    "exact_error": "총리가있으면대통령제를없애는것이라고간주하여배제한다.제시안은내치분담과의회연합유도이며대통령제폐지를명시하지않는다."
  },
  "unresolved": "①~④는가능한개선기제이며실제성공필연이나구체의석비율을보장하지않는다.강한부족정체성이있어도동시선거의효과크기는별도실증문제다."
}
```
