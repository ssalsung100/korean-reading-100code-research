

<!-- luna-raw:AFK-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G194",
  "blind_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "④의오다는돈을구한뒤오는별도의이동행위를나타내어자립적서술기능을한다.①완료,②남을위한행위,③이후를위한준비,⑤시도·확인등의의미를앞용언에더하는쓰임과다르다.",
  "official_answer_source": "sealed canonical answer 기계 연결; 이번stage에서공식배포답표직접대조아님.",
  "group_barrier": "G194 전체 유효blindraw저장확인후 answer필드만공개. 원문범위·그림·밑줄hold는후속직접확인으로해소하고최초기록보존.",
  "sdss_seen": false,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가",
    "source_boundary_residue": "최초JSON말미##2018학년도잔재보존;group식별확정안함"
  },
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AFK-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G194",
  "logic_without_codes_fixed": "보기의 자립적 서술 기능/다른 용언 뒤에서 의미를 더하는 기능을 각 밑줄 용례에 적용한다.④ 오다는 돈을 구한 뒤 오는 행위 자체를 나타내고, 나머지는 완료·수혜·준비·시도 의미를 앞 용언에 더한다.",
  "primary": [
    15
  ],
  "auxiliary": [
    96
  ],
  "surface": [
    25,
    17
  ],
  "primary_scope": "주어진 문법 기능 기준을 개별 용례에 적용한다.",
  "auxiliary_scope": "같은 용언의 문자적 독립 행위와 해당 문맥의 보조 의미를 해석해야 기준 적용이 가능.",
  "evidence": [
    "보기에서㉠은 자립적 서술어,㉡은 반드시 다른 용언 뒤에서 의미 보조라고 구별.",
    "원PDF 밑줄①버리니②주었다③둬라④오겠다고⑤보고 직접 확인."
  ],
  "competing_codes": [
    {
      "code": 96,
      "reason": "일상적 문맥 의미 판독은 필수 보조다. 그러나 유사 어의를 고르는 문제가 아니라 주어진 자립/보조라는 문법 기능 구분에 맞는 예를 고르므로 적용 기준을 별도 기록한다."
    },
    {
      "code": 25,
      "reason": "본용언/보조용언 분류 적용으로도 같은 행동을 기술할 수 있다.15는 구체 판독 기준을 강조하는 대표이고25와 번호상 독점 경계를 확정하지 않는다."
    },
    {
      "code": 17,
      "reason": "용례를 문법 범주에 귀속하는 넓은 기술은 가능하나 어떤 문맥 기능 때문에 귀속되는지 생략하면 밑줄의 독립 행위를 판독한 근거가 소실된다. 국소 중첩 한계 보존."
    }
  ],
  "falsification_probe": "앞말 뒤에 위치한다는 것만으로 보조 용언이라면④도 잘못 분류된다. 위치 외에 자체 행위를 나타내는지를 확인해야 한다.",
  "source_scope": "독서 지문과 연결된 문법 적용 문항. 국어 독서의 일반 내용 판단과 동일한 독립 표본 유형으로 무구분 일반화하지 않는다.",
  "confidence": 0.97,
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
