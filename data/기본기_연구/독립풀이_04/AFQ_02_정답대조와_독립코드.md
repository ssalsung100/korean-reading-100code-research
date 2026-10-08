

<!-- luna-raw:AFQ-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G195",
  "blind_answer": 2,
  "official_answer": 2,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "원문은경제주체가위험에처하는상태인데드러낼로바꾸면경제주체가무엇인가를드러내는행위가되어뜻과논항역할이바뀐다.②가부적절.",
  "official_answer_source": "sealed canonical answer 기계 연결; 공식 배포 답표 직접 대조는 이번 stage에서 수행하지 않음.",
  "group_barrier": "AFO 원그래프/범위/선지표 직접확인 후 전체6 blindraw 저장을 확인하여 answer필드만 공개.",
  "sdss_seen": false,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AFQ-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G195",
  "logic_without_codes_fixed": "위험에노출될은경제주체가위험에놓이는상태이고드러낼은행위주체가무엇인가를나타내는행위다. 어휘교체가뜻과주어·대상의관계를모두바꾸어②가틀린다.",
  "primary": [
    96
  ],
  "auxiliary": [
    17
  ],
  "surface": [
    39,
    78
  ],
  "evidence": [
    "경제주체들은과도한위험에노출될수있다.",
    "②교체어는드러낼이며드러날이아님."
  ],
  "competing_codes": [
    {
      "code": 39,
      "reason": "원표현과교체표현의뜻을비교하는넓은기술은96과겹친다. 비교대상이다르다는말만으로왜어색한지설명하지말고상태/행위와논항역할차이를명시한다. 유일주번호의전역배타성은유보."
    },
    {
      "code": 17,
      "reason": "경제주체를위험에놓인대상에서무언가를드러내는행위자로바꾼역할교체를보조로기록. 이것은별개사건의주체귀속이아니라해당어휘용법과결합한분석이다."
    },
    {
      "code": 78,
      "reason": "행위적뜻과상태적뜻을비교하지만행위자의욕구·동기·믿음으로행동을설명하는문제가아니다. 행위어가나온다고행위설명주를부여하지않음."
    }
  ],
  "falsification_probe": "드러낼을수동형드러날로바꾸면문법역할문제는완화될수있지만위험에노출됨의문맥뜻까지완전히같다고자동승인할수없다. 문법형태와문맥의미를각각확인한다.",
  "confidence": 0.98,
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
