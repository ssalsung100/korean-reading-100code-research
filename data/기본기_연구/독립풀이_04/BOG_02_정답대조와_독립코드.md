

<!-- luna-raw:BOG-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G489",
  "selected_answer": 4,
  "official_answer": 4,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2025/2025_answer_2025언어이해정답.pdf",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "①②③⑤는 단백질 위치·헴 기능·연구자·분석 대상의 명시적 교환이라 배제된다.④는 붉은 소변이 다른 질환의 특징이라는 구별을 적용한 선택이나 조지3세에게 그 증상이 실제로 없었다고 본문이 직접 말하지는 않아 소거에 의존한다.",
  "strict_blind_eligible": false,
  "sdss_seen": false,
  "confidence_after_check": 0.7,
  "remaining_uncertainty": "④의 실제 붉은 소변 부재는 본문에서 직접 확정되지 않는다. 미언급을 부재로 바꾸는 추론 위험과 단일 질환·증상 특이성 가정을 공식답 전부터 보존한다. BOH 표는 읽었으나 그 표를 BOG 원문에 있던 근거로 소급하지 않았다.",
  "source_restoration_before_disclosure": false
}
```


<!-- luna-raw:BOG-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G489",
  "minimal_logic_without_codes": "①②③⑤는 위치·기능·연구자·목표 유전자의 명시 정보를 바꿔 배제한다. 남은④의 증상 부재는 질환별 서술 범위를 구분한 문맥 추론이나 엄밀히 충분한 원문 근거는 미확정이다.",
  "primary": [
    {
      "code": 17,
      "reason": "실제 수행한 소거 경로는 단백질 위치·기능, 연구자와 연구 결과, 헴 대사와 비소 대사의 귀속을 유지하는 것이다.④ 자체를 충분히 입증하는 유일 주로 확정한 것은 아니다."
    }
  ],
  "auxiliary": [
    {
      "code": 71,
      "reason": "명시적 불일치 네 선지를 제거해④를 선택한 경로를 기록한다."
    },
    {
      "code": 25,
      "reason": "선천성 조혈기성과 혼합 포르피린증의 증상 서술 범위를 나눈다."
    },
    {
      "code": 2,
      "reason": "조지3세의 포르피린증은 가설이며 증거 불충분이라는 진단 확신의 강도를 유지한다."
    }
  ],
  "surface": [
    {
      "code": 46,
      "reason": "질환-증상 경로는 있으나 특정 인물의 다른 증상 부재까지 자동 결정하지 않는다."
    }
  ],
  "competing_codes": [
    {
      "code": 13,
      "rejection": "질환 종류가 다르다는 것만으로 동시 발병이나 같은 증상의 공유가 논리적으로 금지되지 않는다."
    },
    {
      "code": 12,
      "rejection": "선천성 조혈기성→붉은 소변이라는 본문 관계에서 다른 질환→붉은 소변 없음이라는 이의 추론을 자동 허용하지 않는다."
    },
    {
      "code": 34,
      "rejection": "혼합 환자는 누구도 붉은 소변을 보지 않는다는 전칭 부정을 원문에서 확보하지 못했다."
    },
    {
      "code": 36,
      "rejection": "반례의 부재가 증상 부재의 증명은 아니며 가설 경쟁에서 자료 미언급을 검증된 반례로 만들지 않는다."
    }
  ],
  "confidence": 0.7,
  "sdss_seen": false,
  "unresolved": "공식④는 보존하지만 증상 목록 완전성 또는 상호 배타적인 단일 원인 경로 등의 추가 전제 없이는 붉은 소변 부재의 연역 증명은 미완료다. 사례 연구 기본 단계는 완료하되 이 경계는 향후 depth 대상이다."
}
```
