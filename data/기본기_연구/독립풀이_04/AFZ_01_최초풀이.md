

<!-- luna-raw:AFZ-blind-20260920-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G197",
  "selected_answer": 2,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "required_information_and_location": [
    "마지막문단다른조건동일시기초자산위험높을수록·보장매도자지급능력높을수록프리미엄큼.",
    "복원표:가BB+/AAA,나BB+/AA-,다BBB-/A-,라BBB-/AA-,마BBB-/A+.",
    "낮은기초자산등급은위험높음,높은매도자채권등급은지급능력높음."
  ],
  "minimal_logic_without_codes": "같은기초등급에서가>나. 같은매도자등급AA-에서나>라. 같은기초BBB-에서매도자등급AA->A+>A-이므로라>마>다. 전체가>나>라>마>다여서둘째나는②.",
  "intermediate_reasoning": [
    "기초자산등급은낮을수록프리미엄상승방향.",
    "매도자채권등급은높을수록프리미엄상승방향.",
    "서로영향반대인등급두개를한총점으로임의합산하지않고한조건씩같은행을연결."
  ],
  "most_attractive_wrong_answer": 4,
  "exact_error": "기초자산신용등급이높은것을매도자지급능력높은것과같이프리미엄상승요인으로읽으면라를나보다높게오인한다. 두등급의소유주와영향방향이다르다.",
  "source_verification": "AFZ_choice_table_parse_supplement_20260920.json의원HWPX XML행별두열및선지번호기계복원자료를직접읽음. 임의수치나가중치부여없음.",
  "quota_status": "unavailable"
}
```
