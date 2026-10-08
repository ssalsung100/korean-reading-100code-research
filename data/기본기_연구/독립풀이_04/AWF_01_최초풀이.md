

<!-- luna-raw:AWF-blind-20260928-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G333",
  "selected_answer": 5,
  "confidence": 0.95,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가",
    "incidental_adjacent_passage": "G333_visual01.png가공식전체페이지여서오른쪽16~18이민선문학지문일부사전노출. 해당후속group은strict blind제외필요.정답·SDSS노출없음."
  },
  "needed_information_locations": [
    "전후한국권위주의강함·X탈권위·완만보수화",
    "영국전후진보/대처보수",
    "기간효과모든세대·생애효과노화보수화"
  ],
  "minimal_logic_without_codes": "연령·시점·코호트 중 고정된 것을 확인하고 예상과 반대인 변화의 설명 후보를 기간 효과로 남긴다.",
  "intermediate_reasoning": [
    "ㄱ 같은시점X가전후보다젊고덜권위적인코호트라낮을것예상",
    "ㄴ 같은50대로연령고정,더보수적인대처코호트가오히려진보이면달라진시점효과가주요후보",
    "ㄷ 같은코호트노화가보수화예상인데오히려덜보수면진보적기간효과가능,다른세대도영향가능",
    "셋다수용하되기간효과의수치적유일식별을주장하지않음"
  ],
  "attractive_wrong_answer_and_error": "ㄴ: 코호트차이가있다는이유로기간설명을배제하기쉽지만변화방향이코호트예상과반대다.",
  "visuals_reviewed": [
    "G333_visual01.png"
  ],
  "quota_status": "unavailable"
}
```
