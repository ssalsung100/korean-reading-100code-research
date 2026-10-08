

<!-- luna-raw:BND-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G479",
  "selected_answer": 3,
  "official_answer": 3,
  "match": true,
  "original_blind_preserved": true,
  "group_blind_barrier_verified": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2024/2024_answer_2024언어이해정답.pdf",
  "minimal_logic_without_codes": "본문의 단일값 집합 삭제 설명을 따라 ℓ≥2인 유효 다양성 조건으로 읽으면 ㄱ은 참,ㄴ은 집합수3대2로 거짓,ㄷ은(a) k≤2·ℓ=2와(b) k=3또는4·ℓ=2가 되어 참이다.③을 선택한다.",
  "sdss_seen": false,
  "strict_blind_eligible": false,
  "source_verification": "공식PDF crop 직접 확인.별도ℓ≥2표기는없음.",
  "interpretive_assumption_preserved": "ℓ≥2는 별도 수식으로 직접 표기된 것이 아니라 단일값 집합을 삭제한다는 본문의 적용 설명에 근거해 채택한 해석이다.원문에 명시된 부등식으로 소급하지 않는다.",
  "countermodel_if_ell1_allowed": "k_a=2,ℓ_a=1이면(a)6개 유지;k_b=3,ℓ_b=2이면(b)4개 유지.이때ㄷ의전반조건은만족하지만ℓ값은다르다.따라서하한해석을달리하면ㄷ판정이달라진다.",
  "confidence_after_check": 0.89,
  "scope_limit": "공식③은 채택한 문맥 해석과 일치하지만 ℓ의 하한이 별도 수식으로 명시됐다는 근거로 사용하지 않는다."
}
```


<!-- luna-raw:BND-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G479",
  "minimal_logic_without_codes": "동질집합 수, 각 집합의 레코드 수, 서로 다른 민감값 수를 따로 센 뒤k·ℓ의 문턱을 적용한다.채택한ℓ≥2 해석에서ㄱㄷ만 참이다.",
  "primary": [
    {
      "code": 31,
      "reason": "집합의 수3/2, 집합별 원소 수2/4, 서로 다른 민감값 수2라는 서로 다른 계수 대상을 구분한다."
    }
  ],
  "auxiliary": [
    {
      "code": 25,
      "reason": "우편번호·연령·마스킹된 성별을 묶음 기준으로 삼고 구매수준을 그룹 키로 쓰지 않는다."
    },
    {
      "code": 12,
      "reason": "집합 크기≥k 및 민감값수≥ℓ라는 결합 통과조건에서 매개변수 범위를 역으로 제한한다."
    },
    {
      "code": 92,
      "reason": "잔존율6/6과4/6을 비교하여 주어진50% 이상100% 미만 조건을 판정한다."
    },
    {
      "code": 10,
      "reason": "ㄷ에서같은ℓ가되려면문맥상비자명한다양성하한을유지해야함을명시한다."
    }
  ],
  "surface": [
    {
      "code": 43,
      "reason": "처리방식(a)/(b)의 차이는 명시돼 있으며 결과를 비교할 때 다른 입력 표는 동일하다.새 실험 통제 설계를 한 것은 아니다."
    }
  ],
  "competing_codes": [
    {
      "code": 84,
      "rejection": "분모6의 비율 비교는 보조 계산이지만 먼저 그룹을 구성하고 서로 다른 개수의 종류를 나누어야 한다."
    },
    {
      "code": 90,
      "rejection": "가능한k·ℓ사례를열거해검증할수있으나정답은경우의수를계산하는것보다각조건이요구하는관계판정이다."
    },
    {
      "code": 4,
      "rejection": "최소ℓ개의값을모두같은ℓ값이라는등호로바꾸려면허용영역과상한2를함께써야한다.양화표현만으로해결되지않는다."
    }
  ],
  "interpretive_assumption": "k와ℓ는개수를표시하는정수매개변수로읽고,단일민감값집합을삭제한다는적용설명에서ℓ≥2를채택한다.별도부등식표기는원문에없다.",
  "remaining_uncertainty": "ℓ=1을허용하면(k_a,ℓ_a)=(2,1),(k_b,ℓ_b)=(3,2)가ㄷ의반례다.공식정답일치만으로이하한문제나반례를삭제하지않는다.",
  "confidence": 0.89,
  "sdss_seen": false
}
```
