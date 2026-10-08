

<!-- luna-raw:AAF-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G168",
  "blind_answer": 2,
  "official_answer": 2,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "(가)는 시대 과제에 응답한 모델의 등장, (나)는 임대차 과제 해결 제도를 서술하므로②. 출현 순서와 완전 대체를 동일시하지 않는다.",
  "official_answer_source": "sealed canonical answer 기계 연결. 이번 stage에서 공식 배포 답표 직접 대조한 것은 아님.",
  "strict_blind_eligible": false,
  "stage_qualification": "과거 원문·전체답표 노출 후 재구성 결과의 대조이며 strict blind 정답률에서 제외.",
  "group_barrier": "AAG 실제 범위 복원 후 여섯 사례 전체 코드 없는 재구성 raw 저장 확인을 거쳐 answer 필드만 공개.",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AAF-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G168",
  "logic_without_codes_fixed": "(가)는 시대 과제에 대응하여 법 모델들이 등장한 과정을, (나)는 임차인 보호 등의 과제를 해결하는 제도를 설명한다. (가)의 한계→보완 전개를 (나)의 저자에 의한 새 방안 제안으로 옮기지 않는다.",
  "primary": [
    {
      "code": 64,
      "name": "논의영역",
      "reason": "각 글이 무엇을 어떤 서술 행위로 다루는지 대응한다. 문제 해결 제도를 설명함과 필자가 새 제도를 제안함은 다르다."
    }
  ],
  "auxiliary": [
    {
      "code": 59,
      "name": "문제해결도식",
      "reason": "자유 보장/실질 불평등/과도 개입의 과제와 대응 모델, 임차인 보호 과제와 제도를 요약하여②의 내용 대응을 뒷받침한다."
    },
    {
      "code": 3,
      "name": "선후",
      "scope": "(가) 출현 과정",
      "reason": "모델들의 출현 순서는 있지만 이전 모델의 완전 대체까지 말하지 않는다."
    }
  ],
  "surface": [
    {
      "code": 75,
      "name": "경쟁입장",
      "reason": "복수 법 모델이 소재이나 이 문항은 개별 사안에 대한 각 모델의 견해를 예측하는 것이 아니다."
    }
  ],
  "competing_codes": [
    {
      "code": 17,
      "name": "대상범주",
      "rebuttal": "글별 서술 내용의 귀속이라는 점에서64와 국소 중첩하며 독립 필수 연산으로 중복 계수하지 않는다.64는 글의 주제·서술 행위를 드러내는 대표 표기이고 유일 주는 유보."
    },
    {
      "code": 59,
      "name": "문제해결도식",
      "rebuttal": "문제/방안 내용은②의 중요한 근거지만⑤의 함정은 방안의 내용 자체보다 기존 제도 소개를 저자의 새 제안으로 바꾸는 서술 행위의 교환이다. 보조를 유지하며 경계는 국소적."
    },
    {
      "code": 5,
      "name": "지속/변화",
      "rebuttal": "여러 모델의 출현이 언급되지만 변화가 곧 완전 대체임을 판정하는 문항은 아니다. 현재 공존한다는 문장을 남겨 시간 배열의 과잉 해석을 방지한다."
    }
  ],
  "evidence": [
    "(가) 자유주의 한계 보완으로 복지 모델, 그 부작용 보완으로 절차 모델 등장; 마지막 문단은 세 모델 공존 명시.",
    "(나)는 법/계약 우선과 보호 제도·분쟁 절차를 설명하며 필자의 새 제안은 없다."
  ],
  "confidence": 0.94,
  "strict_blind_eligible": false,
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
