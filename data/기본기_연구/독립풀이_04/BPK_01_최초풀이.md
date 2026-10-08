

<!-- luna-raw:BPK-blind-20261004-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G499",
  "selected_answer": 4,
  "confidence": 0.96,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "necessary_information": [
    {
      "location": "보기 단계2·3",
      "evidence": "출력 조건은120초과/이하, 경력 조건은3년초과 등 단일 경계 비교다. 단계3의짧은경력 규칙과스크랩카 규칙은그대로두면중복된다."
    },
    {
      "location": "공식 그림2 및FEEL 설명",
      "evidence": "<2와>=5 같은크기비교, [2..5[ 및[천만..일억] 같은숫자구간, -의항상참을구분해표기한다."
    }
  ],
  "minimal_logic_without_codes": "④의두조건은한경계와값을비교하는조건이지그림에서별도로구분한양끝경계의숫자구간표기를요구하지않는다. 본문의조건식구문구분에따라④를배제한다.",
  "intermediate_reasoning": [
    "① 자동차유형결정과위험도결정의두노드가단계2·3으로구체화된다.",
    "② 유형은가격·출력두입력, 위험도는경력·유형두입력에각결과하나다.",
    "③ 스포츠카의경력>5와3<경력≤5는출력2/3이다르므로두규칙행이필요하다.",
    "⑤ 경력≤3만쓰면스크랩카도위험5와위험1에동시에걸린다. 유일정책에서는스크랩제외등유형조건과경력조건을함께써야한다."
  ],
  "most_attractive_wrong": {
    "choice": 5,
    "exact_error": "단계3A의경력조건만분리해쓰고D의스크랩우선예외를놓치면같은입력이두결과를산출하는오버랩을만든다."
  },
  "source_restoration": {
    "crop": "data/기본기_연구/prepared_backlog/blind_sources/G499_official_figures_crop.png",
    "astra_direct_seen": true,
    "resolved_before_answer_disclosure": true,
    "original_hold_preserved": true
  },
  "scope_limit": "수학적으로부등식해집합도구간으로표현할수있다는사실을부정하지않는다.④는본문이구분한FEEL크기비교구문과숫자구간구문이라는범위에서판정했다."
}
```
