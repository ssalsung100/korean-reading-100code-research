

<!-- luna-raw:BEJ-answer_check-20261002-r2-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G402",
  "all_group_blind_records_before_any_group_answer_check": true,
  "selected_answer": 1,
  "official_answer": 1,
  "match": true,
  "original_blind_preserved": true,
  "fixed_logic_without_codes": "본문의 고정 암호 방식은 내용 보호와 경로 추적 방지를 함께 보장하지 않는다.",
  "sdss_disclosed": false
}
```


<!-- luna-raw:BEJ-independent_code-20261002-r2-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G402",
  "primary": [
    {
      "code": 17,
      "reason": "보호되는 대상인 내용과 이동 경로를 구분하여 효과 범위의 전이를 막는다."
    }
  ],
  "auxiliary": [
    {
      "code": 2,
      "reason": "암호화만으로 경로 노출을 방지할 수 있다는 충분한 보장 읽기를 제한한다."
    },
    {
      "code": 19,
      "reason": "내용 보호 방법의 한계를 후속 변화 방식으로 보완하는 설명 구조가 있다."
    }
  ],
  "surface": [
    {
      "code": 50,
      "reason": "정보 경로라는 소재만으로 차단 추론 주 코드가 되지는 않는다."
    }
  ],
  "competing_codes": [
    {
      "code": 46,
      "rejection": "경로가 드러나는 기제는 근거지만 판별점은 보호 대상 범위를 옮긴 진술이다. 포괄 인과만으로 오류를 좁히기 어렵다."
    },
    {
      "code": 18,
      "rejection": "모순은 오답 판정 결과를 말할 뿐 내용과 경로의 구분이라는 실제 작업을 특정하지 못한다."
    },
    {
      "code": 43,
      "rejection": "통제된 실험 비교 없이 본문의 명시적 제한을 확인한다."
    }
  ],
  "confidence": 0.93,
  "sdss_disclosed": false
}
```
