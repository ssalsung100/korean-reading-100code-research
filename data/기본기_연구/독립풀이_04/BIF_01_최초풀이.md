

<!-- luna-raw:BIF-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G437",
  "selected_answer": 5,
  "confidence": 0.98,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": "data/기본기_연구/prepared_backlog/blind_sources/BIF.json",
  "necessary_information": [
    {
      "location": "㉠문단",
      "evidence": "지불불능예상→인출쇄도→자산급매·가격하락→실제지불능력취약."
    },
    {
      "location": "㉣문단",
      "evidence": "상승지속예상→차입증가·가격상승→거품·취약성→거품붕괴위기."
    }
  ],
  "minimal_logic_without_codes": "㉠은파산우려가실현되는경로지만㉣의위기는계속상승하리라는낙관이깨지는결과다.둘다예상이그대로실현되어위기가온다는⑤는둘의예상내용을혼동한다.",
  "intermediate_reasoning": [
    "①은부분준비·만기없음·선착순지급에의한인출유인을정확히말한다.②는주주의고수익선호와채권자위험전가를은행행동에연결하는전제다.",
    "③은개인적이익을추구하는은행가의약탈이은행손실을초래하는구조.④는항상합리적이지않은경제행동의관찰에기초한다는㉣설명과맞는다.",
    "㉣에서도상승예상이일시적으로상승을강화할수는있지만최종붕괴를상승지속예상과같은내용이라고할수없다."
  ],
  "most_attractive_wrong": {
    "choice": 4,
    "exact_error": "이론전체를연역모형으로간주해④를배제하면㉣만경제주체의비합리적행동관찰에기초한다는본문의차이를놓친다."
  }
}
```
