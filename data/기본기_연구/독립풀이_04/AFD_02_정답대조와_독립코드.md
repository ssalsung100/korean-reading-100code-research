

<!-- luna-raw:AFD-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G193",
  "blind_answer": 2,
  "official_answer": 2,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "다른노드에원래내용이중복저장된것이복원을돕는다. 한체인여러블록의이중포함과구분.",
  "official_answer_source": "sealed canonical answer 기계 연결; 공식배포답표직접대조아님",
  "group_barrier": "AFB/AFC/AFD/AFE 전체 blind raw 저장 후 answer 필드만 공개",
  "sdss_seen": false,
  "sdss_linkage_absence_disclosed_before_blind": true,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AFD-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G193",
  "logic_without_codes_fixed": "일부 삭제 후에도 여러 노드에 중복 저장된 원래 내용을 이용할 수 있다. 승인된 원래 내용 복원에는 재승인도 필요하지 않으므로 복원이 용이하다는 결과를 설명한다. 여러 노드의 동일 체인 복제와 한 체인 안 여러 블록의 내용 중복을 구별한다.",
  "primary": [
    {
      "code": 56,
      "name": "설명",
      "reason": "②의 여러 노드 중복 저장을 ㉠의 복원 용이성을 설명하는 근거로 연결한다. 발문의 이유라는 말만이 아니라 실제로 무엇이 남아 복원을 가능하게 하는지를 복원한다."
    }
  ],
  "auxiliary": [
    {
      "code": 17,
      "name": "대상범주",
      "scope": "⑤ 배제",
      "reason": "반복된 내용의 저장 위치는 여러 노드이지 동일 체인의 서로 다른 블록이 아니다. 중복의 대상 단위와 장소를 보존한다."
    },
    {
      "code": 24,
      "name": "원칙/예외",
      "scope": "④ 배제",
      "reason": "새 블록 연결 승인과 이미 승인된 원래 내용의 복원을 구별해 재승인 불필요라는 명시 범위를 적용한다."
    }
  ],
  "surface": [
    {
      "code": 40,
      "name": "부분관계",
      "reason": "노드·체인·블록의 구성 정보는⑤ 위치 구별에 관여하지만 부분 성질의 전체 전이는 없다."
    }
  ],
  "competing_codes": [
    {
      "code": 46,
      "name": "인과관계",
      "rebuttal": "중복 저장→원래 내용 확보→복원 용이의 설명 경로를 그대로 기술할 수 있어56과 국소 중첩한다. 별개의 필수 추론으로 이중 계수하지 않고 대표56의 유일성은 유보한다."
    },
    {
      "code": 44,
      "name": "수단/목적",
      "rebuttal": "중복 저장을 복원 목적의 수단으로 표현할 수 있으나 원문은 행위자의 목표·선택을 논증하지 않는다. 목적 어휘를 덧붙이지 않아도 설명은 성립한다."
    },
    {
      "code": 40,
      "name": "부분관계",
      "rebuttal": "⑤는 단위/소속 구별이라는 점에서17과 중첩 가능하다. 그러나 정답②의 설명을 확정하려면 구성도만이 아니라 삭제 후 다른 노드에 원내용이 남는다는 연결이 필요하다."
    }
  ],
  "evidence": [
    "1문단: 연결된 블록 집합을 여러 컴퓨터에 중복 저장.",
    "3문단: 일부 삭제 후 승인된 원래 데이터 복원에는 승인 과정 불필요.",
    "⑤: 같은 체인의 서로 다른 블록에 이중 포함이라는 오답."
  ],
  "boundary_note": "56/46의 국소 중첩과17/40의 단위 귀속 중첩을 보존. 재승인 불필요만으로 복원할 내용의 확보까지 설명되지는 않으므로1문단의 저장 위치 정보를 결합한다.",
  "confidence": 0.93,
  "exposure": {
    "actual_sdss_tags_seen": false,
    "sdss_linkage_absence_preexposed": true,
    "strict_blind_eligible": false
  },
  "scope_limit": "인용 지문의 설명 관계만 분석하며 원문 밖 복구·공격 절차를 생성하지 않는다.",
  "quota_status": "unavailable"
}
```
