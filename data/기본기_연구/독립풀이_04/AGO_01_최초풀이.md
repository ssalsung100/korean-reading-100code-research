

<!-- luna-raw:AGO-blind-20260920-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G200",
  "selected_answer": 2,
  "confidence": 0.98,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "required_information_and_location": [
    "4~5문단고유DNA·이분분열·박테리아막의카디오리핀·박테리아와유사한리보솜이기원근거.",
    "ㄴ은진핵세포리보솜,ㄷ은일반막과수송단백질만제시."
  ],
  "minimal_logic_without_codes": "ㄱ은고유DNA와박테리아같은이분분열,ㄹ은박테리아막특성카디오리핀을확인해본문기원판단근거와맞는다.ㄴ·ㄷ은핵심박테리아특징이부족하여ㄱㄹ②.",
  "intermediate_reasoning": [
    "ㄴ고유DNA하나에더해진핵세포리보솜이라는반대유형정보가주어짐.",
    "ㄷ막과수송단백질이라는일반특징은진핵세포에도있어박테리아기원을식별하지못함.",
    "ㄹ단순막존재가아니라막성분의특정종류가중요."
  ],
  "most_attractive_wrong_answer": 1,
  "exact_error": "미토막에포린이있다는특정수송단백질근거를모든수송단백질존재라는일반특성으로완화하면ㄷ을잘못승인한다.",
  "scope_limit": "본문이제시한기원판단근거의전이를판정하며이특성만으로현실의모든진화기원이논리적으로유일입증된다고일반화하지않음.",
  "quota_status": "unavailable"
}
```
