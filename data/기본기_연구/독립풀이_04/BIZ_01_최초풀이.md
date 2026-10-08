

<!-- luna-raw:BIZ-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G443",
  "selected_answer": 5,
  "confidence": 0.97,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": [
    "data/기본기_연구/prepared_backlog/blind_sources/BIZ.json",
    "data/기본기_연구/prepared_backlog/blind_sources/G443_visual01.md"
  ],
  "necessary_information": [
    {
      "location": "마지막문장㉠",
      "evidence": "연령에따른노동능력변화는모든사람에게불가피하므로연령차별금지는정당하지않다는입장."
    },
    {
      "location": "보기",
      "evidence": "ㄱ특정연령우대에따른고령기회제한,ㄴ계약정년45세,ㄷ50세초과직책배제."
    }
  ],
  "minimal_logic_without_codes": "지정입장㉠은연령에따른차등을차별금지원칙으로금지하는것에반대한다.세사례모두연령기준의고용차등이므로그입장에서는평등권·차별금지위반이아니라는ㄱㄴㄷ을수용한다.⑤.",
  "intermediate_reasoning": [
    "ㄱ은특정연령우대의반대편에고령기회제약이있어도연령기준차등이라는점에서㉠과부합한다.",
    "ㄴ자유계약의정년연령설정,ㄷ법규의직책연령상한도같은적용범위다.",
    "본문전체의연령차별금지입법가능성과마지막의별도반대주장을섞지않는다.발문은㉠과의부합만묻는다.",
    "해당입장이현행법이나보편적규범으로옳다는평가가아니다.주어진견해의논리적적용으로한정한다."
  ],
  "most_attractive_wrong": {
    "choice": 4,
    "exact_error": "ㄱ이노골적인연령우대·배제처럼보인다는일반적규범직관으로제외하면지정된㉠이바로연령차등금지의정당성을부정한다는범위를놓친다."
  }
}
```
