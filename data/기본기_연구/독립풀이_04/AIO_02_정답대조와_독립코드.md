

<!-- luna-raw:AIO-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G214",
  "blind_answer": 3,
  "official_answer": 3,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "홀씨는버섯이참나무상처에피어나함께살아가는생성의계기이다.③의공존생명체가흩어짐은반대이다.",
  "official_answer_source": "자료/평가원_정답표/원본/수능/2023__국어_1교시_국어영역_정답표.pdf",
  "verification_scope": "sealed답필드대조,공식PDF정답셀직접검증아님.AIN범위crop은직접검증완료",
  "barrier_verified": "AIN해소후G214blind4저장후answer만공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AIO-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G214",
  "primary": [],
  "primary_candidates": [
    17,
    100
  ],
  "working_representative": 17,
  "auxiliary": [
    39,
    46
  ],
  "surface": [
    5
  ],
  "judgment_reason": "홀씨의생명생성·공존역할을생명체의흩어짐에귀속. 작품상징의의미대응100과역할귀속17이같은오류에반응.",
  "competing_codes": [
    {
      "code": 100,
      "verdict": "후보",
      "reason": "보기의생명공존지향에맞춰홀씨의새생성의미확인"
    },
    {
      "code": 46,
      "verdict": "보조",
      "reason": "홀씨일어남→상처에버섯이라는결과를보존하면흩어짐기각가능"
    },
    {
      "code": 39,
      "verdict": "보조",
      "reason": "(가)(나)감상의두절중후반만으로③기각가능.양쪽의전체대조가필수는아님"
    },
    {
      "code": 5,
      "verdict": "주 기각",
      "reason": "무언가변한다는것보다변화의결과를생성/해체중어디에귀속하는지가정답근거"
    }
  ],
  "minimal_change_test": "③흩어지게되는을새생명이피어나공존하게되는으로고치면보기와복원. 생물학상홀씨이동상식을외부에서보충하여흩어짐을정당화하지않음.",
  "sdss_seen": false,
  "confidence": 0.95,
  "quota_status": "unavailable"
}
```
