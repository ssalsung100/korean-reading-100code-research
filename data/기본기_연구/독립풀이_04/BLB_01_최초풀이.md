

<!-- luna-raw:BLB-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G461",
  "selected_answer": 5,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "necessary_information": [
    {
      "location": "보기",
      "evidence": "노씨는혼례없이들였고김씨·허씨는혼서·혼례를갖춤.1402년후처혼인,1413년5월사망,소제기는첫문장1415년.허씨와평생동거."
    },
    {
      "location": "1413·1414규정",
      "evidence": "혼서·혼례로처첩을구분.사망한경우선처를적처로인정하는최초규정과은의·종신동거를반영한수정규정."
    }
  ],
  "minimal_logic_without_codes": "노씨는첩이고처는김씨·허씨두명이므로세명의처를둔경우의규정을적용한다는⑤는틀리다.",
  "intermediate_reasoning": [
    "① 1413년사망직후그해판결이면수정전규정에따라혼서·혼례를갖춘선처김씨에게작첩·수신전.",
    "② 후처혼인은1402년이므로1413년기준일뒤새중혼에대한처벌이아니다.",
    "③ 집안일주관여부는제시된적통·분급기준이아니다.",
    "④ 실제소제기1415년에는1414년수정기준에따라종신동거한허씨에게작첩·수신전."
  ],
  "most_attractive_wrong": {
    "choice": 4,
    "exact_error": "혼인순서만으로선처김씨를고정해,실제판결시점에적용되는수정기준의은의·동거요건을누락한다."
  },
  "scope_limit": "보기말미의이때는첫문장의소제기시점1415년으로읽고,명시된사망1413년과구분했다.노씨의신분만으로추정하지않고혼례없음이라는기준사실을사용한다."
}
```
