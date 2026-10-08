

<!-- luna-raw:BPK-answer_check-20261004-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G499",
  "selected_answer": 4,
  "official_answer": 4,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2026/2026_answer_2026_LEET_언어이해_정답표.pdf",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "④의두조건은한경계와값을비교하는조건이지그림에서별도로구분한양끝경계의숫자구간표기를요구하지않는다. 본문의조건식구문구분에따라④를배제한다.",
  "strict_blind_eligible": false,
  "sdss_seen": false,
  "source_restoration_before_disclosure": true
}
```


<!-- luna-raw:BPK-independent_code-20261004-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G499",
  "minimal_logic_without_codes": "④의 출력120 초과/이하와 경력3년 초과는 한 경계에 대한 크기 비교이며, 원문에서 별도로 분류한 양끝 경계의 숫자구간 표기와 다르다.",
  "primary": [
    {
      "code": 16,
      "reason": "본문이 정의한 조건식 구문 종류를 구별해④를 판정한다."
    }
  ],
  "auxiliary": [
    {
      "code": 86,
      "reason": "초과/이하 및 경곗값 포함 여부를 그대로 유지한다."
    },
    {
      "code": 12,
      "reason": "유형과 경력 조건을 결합하여 위험도를 결정한다."
    },
    {
      "code": 13,
      "reason": "유일 정책 아래서는 스크랩카의 별도 규칙과 짧은 경력 규칙이 동시에 적중하지 않게 분리해야 한다."
    },
    {
      "code": 45,
      "reason": "첫 노드의 자동차 유형 출력이 다음 노드 입력이 되는 구조를 확인한다."
    }
  ],
  "surface": [
    {
      "code": 90,
      "reason": "스포츠카 경력 규칙 두 행을 구분하지만 전체 조합 수를 계산하는 문제는 아니다."
    }
  ],
  "competing_codes": [
    {
      "code": 29,
      "rejection": "부등식 해집합도 수학적으로 구간에 속할 수 있다.④는 집합의 수학적 동치가 아니라 원문의 구문 분류 맥락으로 판단한다."
    },
    {
      "code": 92,
      "rejection": "정확 위험도나 금액의 산술 계산보다 조건식 표현과 중복 관리가 필요하다."
    },
    {
      "code": 8,
      "rejection": "유일 정책의 중복을 임의의 우선순위로 해결하면 지정된 정책을 바꾸는 것이 된다."
    }
  ],
  "confidence": 0.94,
  "sdss_seen": false,
  "scope_limit": "단일 경계 조건을 다른 동치 구간 구문으로 나타낼 가능성을 전면 부정하지 않는다. 문항의 조건 서술과 그림의 구문 구분을 기준으로 삼았다."
}
```
