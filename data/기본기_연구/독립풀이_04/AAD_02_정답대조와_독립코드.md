

<!-- luna-raw:AAD-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G167",
  "blind_answer": 5,
  "official_answer": 5,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "정확한 학습 정보와 조합 과정 왜곡 가능의 양립을⑤가 보존.",
  "official_answer_source": "sealed answer_sdss canonical 기계 연결; 해당 배포정답표 별도 직접검증 아님",
  "group_barrier": "AAC/AAD/AAE 전체blind raw 저장 후 answer만 공개",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AAD-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    12
  ],
  "auxiliary": [
    45,
    14,
    2
  ],
  "surface": [
    46,
    22
  ],
  "evidence": "입력 정보의 정확성만으로 생성 결과의 정확성이 충분히 보장되지 않는다. 추출·조합이라는 중간 단계에 별도 왜곡 가능성이 있어 정확한 입력과 왜곡된 결과가 양립.",
  "competing_codes": [
    {
      "code": 45,
      "assessment": "입력-변환-출력의 역할 분리가 실제 보조이며12와 국소 중첩. 모든 과정을 함수 코드로 단독 환원하지 않음."
    },
    {
      "code": 14,
      "assessment": "정확한 입력/왜곡 출력의 양립이⑤ 직접 내용.12는 왜곡 방지 충분조건을 거부하는 관점으로 같은 판단을 재기술하므로 중복 계수 금지."
    },
    {
      "code": 2,
      "assessment": "⑤는 왜곡이 반드시 발생한다가 아니라 가능하다는 한계가 중요. 정확 입력이면 오류 불가능이라는 보장을 기각하는 단계와 중첩."
    },
    {
      "code": 22,
      "assessment": "입력 속성의 출력 상속 실패로 표현 가능하지만 범주 구성원에 공통 속성을 옮기는 것이 아니라 변환 단계에서 정보가 달라질 수 있다는 설명."
    }
  ],
  "counterfactual_test": "생성 과정에서도 의도·맥락 보존과 정확성을 별도로 보장하는 전제가 추가되어야 입력 정확성만의 부족을 메울 수 있다. 원문은 그 보장을 주지 않는다.",
  "confidence": 0.92,
  "passage_group": "G167",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
