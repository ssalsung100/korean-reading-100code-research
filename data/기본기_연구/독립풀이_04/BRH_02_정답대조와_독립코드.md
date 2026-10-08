

<!-- luna-raw:BRH-answer_check-20261005-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G516",
  "selected_answer": 1,
  "official_answer": 1,
  "match": true,
  "official_answer_source": "자료/MEET_언어추론/공식_정답표_원본/2006_언어추론_정답표_검증용.pdf 1쪽 홀수형30, 셀 crop 직접 확인",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "효과를 내는 관계적 잠재력은 실제 접촉이 없어도 대상에 남는다.그 자체로 좋은 본유적 경험이나 현재 느낌 보고와 구별한다.",
  "strict_blind_eligible": false,
  "sdss_seen": false,
  "incidental_answer_exposure": "PDF 머리말100자 출력에2006 MEET 홀수/짝수1·2·11·12·21·22·31·32의 답이 함께 노출됨.후속 해당사례는노출확인 처리하고strictblind제외.문제원문·SDSS미열람."
}
```


<!-- luna-raw:BRH-independent_code-20261005-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G516",
  "sdss_seen": false,
  "primary": [
    {
      "code": 16,
      "reason": "대상의 잠재력이라는 개념의 관계성·비현재적 존속이라는 두 특징을 빵의 영양가에 대응한다."
    }
  ],
  "auxiliary": [
    {
      "code": 37,
      "reason": "보기 사례가 만족하는 개념 요건을 역으로 찾는다."
    },
    {
      "code": 2,
      "reason": "실제 작용의 발생과 작용할 가능성을 구별한다."
    }
  ],
  "surface": [
    {
      "code": 75,
      "reason": "주관주의·객관주의·상대주의 논쟁은 배경이며① 결정은 잠재력 정의로 가능하다."
    }
  ],
  "competing_codes": [
    {
      "code": 69,
      "rejection": "미적가치와 영양가의 구조 유사성은 있으나 알려진 속성으로 미지 속성을 추정하지 않는다.주어진 정의와 사례의 대응이 중심이다."
    },
    {
      "code": 95,
      "rejection": "현재 누군가가 먹고 있어야 영양가가 존재한다는 전제는 보기에서 부정된다."
    },
    {
      "code": 42,
      "rejection": "대상 안에 남는다고 해서 인간과의 관계와 무관한 절대 내부 속성은 아니다."
    },
    {
      "code": 63,
      "rejection": "영양가 사례로 상대주의의 이론적 강도를 평가하는 문항이 아니다."
    }
  ],
  "confidence": 0.96,
  "scope_limit": "16/37은 개념내포 확인과 사례대응의 층위로 중첩.보기가 미적가치 이론을 과학적으로 입증한다는 해석은 금지."
}
```
