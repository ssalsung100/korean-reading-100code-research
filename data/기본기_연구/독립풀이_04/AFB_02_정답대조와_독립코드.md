

<!-- luna-raw:AFB-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G193",
  "blind_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "작업증명이합의알고리즘의예인관계를뒤집은진술에O를준학생판정이잘못됨.",
  "official_answer_source": "sealed canonical answer 기계 연결; 공식배포답표직접대조아님",
  "group_barrier": "AFB/AFC/AFD/AFE 전체 blind raw 저장 후 answer 필드만 공개",
  "sdss_seen": false,
  "sdss_linkage_absence_disclosed_before_blind": true,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AFB-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G193",
  "logic_without_codes_fixed": "작업증명은 합의 알고리즘의 한 예다. 예와 상위 종류의 위치를 교환한 문장은 거짓이므로 X여야 하는데 학생은 O로 표시했다. 문장 진위와 학생 표시의 일치 여부를 별도로 비교한다.",
  "primary": [
    {
      "code": 17,
      "name": "대상범주",
      "reason": "④의 예시 대상과 상위 종류의 귀속 방향을 보존하는 것이 정답 결정 연산이다."
    }
  ],
  "auxiliary": [
    {
      "code": 23,
      "name": "교집합",
      "scope": "②·③ 오답 배제",
      "reason": "구조 분석/장점 설명과 응용 분야/경쟁 양상 설명을 함께 주장한 문장은 앞 절이 참이어도 전체 참이 아니다. 두 절을 각각 확인한다."
    }
  ],
  "surface": [
    {
      "code": 25,
      "name": "분류",
      "reason": "종류·예시의 표면 구조지만 완결된 분류표 구성은 요구되지 않는다."
    }
  ],
  "competing_codes": [
    {
      "code": 37,
      "name": "사례찾기",
      "rebuttal": "새 사례가 요건을 충족하는지 찾는 작업은 없다. 다만 예와 종류의 귀속이라는 국소 연산은17과 중첩하므로 번호만으로 배타화하지 않는다."
    },
    {
      "code": 12,
      "name": "조건문",
      "rebuttal": "하위 종류이면 상위 종류라는 포함 방향으로 재표현 가능하다. 이 문항에서17과 실질 중첩하며 유일 주를 논리적 차이로 증명하지 않는다. 주17은 실제 선지의 귀속 교환을 드러내는 대표 표기다."
    },
    {
      "code": 21,
      "name": "정의는필충",
      "rebuttal": "작업증명과 합의 알고리즘은 동치 정의로 주어지지 않았다.⑤의 노드 정의는 적절한 학생 판정 확인에 쓰일 뿐④의 역전 오류를 결정하지 않는다."
    }
  ],
  "evidence": [
    "본문1문단: 합의 알고리즘의 예로 작업증명이 있다.",
    "원 학습지④: 합의 알고리즘은 작업증명의 한 예이다 / O. 원BMP를 PNG로 형식변환하여 직접 확인."
  ],
  "boundary_note": "17/12/37의 국소 중첩을 보존한다. 예시 방향 역전과 O/X 표시 오류를 두 층위로 기록하며, O/X라는 표면만으로18 모순을 추가하지 않는다.",
  "confidence": 0.94,
  "exposure": {
    "group_all_blind_and_answer_check_saved": true,
    "actual_sdss_tags_seen": false,
    "sdss_linkage_absence_preexposed": true,
    "strict_blind_eligible": false
  },
  "quota_status": "unavailable"
}
```
