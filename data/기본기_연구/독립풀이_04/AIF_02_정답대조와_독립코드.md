

<!-- luna-raw:AIF-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G212",
  "blind_answer": 4,
  "official_answer": 4,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "정자나무마을은노동과공동체놀이가함께있고 마지막골목은아이들이복종하며노동하는곳으로변했다.④이두공간의성격을보존한다.",
  "official_answer_source": "자료/평가원_정답표/원본/모의평가/2023_6월_국어_1교시_국어영역_정답표.pdf",
  "verification_scope": "sealed답필드대조, 공식PDF정답셀 직접검증은 아직아님",
  "barrier_verified": "G212 전체 blind3 저장 후 answer필드만 공개; SDSS 미공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AIF-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G212",
  "primary": [
    39
  ],
  "auxiliary": [
    17,
    5
  ],
  "surface": [
    23,
    42
  ],
  "judgment_reason": "공간별로 노동·놀이의 존재를 맞추어 (가)의 공존과 (나)의 노동만 남음을 대조한다. 작품별 귀속17과 (나)의 전후 변화5를 근거로 비교39를 수행한다.",
  "competing_codes": [
    {
      "code": 17,
      "verdict": "보조 후보",
      "reason": "각 공간에 속성을 맞춘다는 기술도 가능.39가 독점적이라고 단정하지 않되 두 공간의 관계 비교를 작업 대표로 채택"
    },
    {
      "code": 5,
      "verdict": "보조",
      "reason": "골목의 처음 놀이와 끝 노동의 변화가 후반 속성을 지지"
    },
    {
      "code": 23,
      "verdict": "주 기각",
      "reason": "(가) 안의 노동·놀이 공존이 있으나 정답 전체는 두 공간의 공통점 확인이 아니라 차이 비교"
    },
    {
      "code": 42,
      "verdict": "표면",
      "reason": "공간 소재이나 경계의 안팎 이동이 정답의 핵심이 아님"
    }
  ],
  "minimal_change_test": "(나) 끝에 놀이도 지속된다는 근거가 추가되면④의 노동만이 깨진다. (가)가 낯선 곳이라는③은 고향이라는 귀속 하나로 기각 가능.",
  "sdss_seen": false,
  "confidence": 0.94,
  "quota_status": "unavailable"
}
```
