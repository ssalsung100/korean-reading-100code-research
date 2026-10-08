

<!-- luna-raw:BJY-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G451",
  "selected_answer": 1,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": [
    "data/기본기_연구/prepared_backlog/blind_sources/BJY.json",
    "data/기본기_연구/prepared_backlog/blind_sources/G451_visual01.md"
  ],
  "necessary_information": [
    {
      "location": "1804/2006규정",
      "evidence": "1804상속포기자녀는계산자녀수에포함·형제자매유류분없음.2006포기자녀는계산수제외하여자유분증가."
    },
    {
      "location": "우리제도",
      "evidence": "직계비속법정분균분,유류분은각법정분의반."
    }
  ],
  "minimal_logic_without_codes": "ㄱ1804포기자녀수포함,ㄴ형제D권리없음은맞다.ㄷ2006포기로자유분증가하므로틀리고ㄹB/C법정분균분및같은유류분비율이라틀리다.ㄱㄴ인①.",
  "intermediate_reasoning": [
    "B의생활곤란과C의경제력은본문이제시한균분규칙을변경하는요건이아니다.",
    "D의고령생활위험이있어도1804형제자매배제규정을뒤집지않는다.",
    "두자녀만상속한다는본문사례에서는각법정상속분1/2,그반인각1/4이지만정답은두비율동일성만으로도판정된다.",
    "상속포기의권리자격효과와계산자녀수효과는시기별로다르므로별도로읽는다."
  ],
  "most_attractive_wrong": {
    "choice": 3,
    "exact_error": "2006상속포기도1804처럼계산자녀수에포함된다고옮겨ㄷ을맞다고읽는다.개정으로바뀐바로그조건을놓친다."
  }
}
```
