

<!-- luna-raw:BMV-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G477",
  "selected_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "group_blind_barrier_verified": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2021/2021_answer_2021_LEET_언어이해_정답표_배포용.hwp",
  "minimal_logic_without_codes": "④는 해당작용의 중간 생성물이 동화작용의 재료로 쓰인다는 설명에 맞는다.",
  "sdss_seen": false,
  "strict_blind_eligible": false
}
```


<!-- luna-raw:BMV-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G477",
  "minimal_logic_without_codes": "해당작용의 중간 산물이 동화작용의 입력 재료가 되는 역할을④에 대응한다.",
  "primary": [
    {
      "code": 45,
      "reason": "한 대사 과정의 산출물이 다른 과정의 재료가 되는 입력·출력 관계를 보존한다."
    }
  ],
  "auxiliary": [
    {
      "code": 17,
      "reason": "NAD+와 NADH의 소비·생성·재생 역할을 바꾸지 않는다."
    },
    {
      "code": 46,
      "reason": "⑤의 유전자 변이와 대사 변화 사이 원인·결과 방향을 본문에 맞춰 구분한다."
    },
    {
      "code": 16,
      "reason": "거대 분자 분해의 이화작용과 합성의 동화작용을 구분한다."
    }
  ],
  "surface": [
    {
      "code": 49,
      "reason": "젖산·포도당 양의 관계는 있지만④의 직접 판독은 물질의 역할 대응이다."
    }
  ],
  "competing_codes": [
    {
      "code": 40,
      "rejection": "여러 반응이 한 대사 체계의 부분이라는 사실만으로 어느 산물이 어느 과정의 입력인지 결정할 수 없다."
    },
    {
      "code": 5,
      "rejection": "세포의 악성화 변화가 배경에 있어도④는 두 과정 사이의 물질 이동 역할을 묻는다."
    },
    {
      "code": 55,
      "rejection": "⑤에는 역전된 인과가 있지만 정답④의 수용은 인과 오류 검사가 아닌 입력·출력 대응이다."
    }
  ],
  "confidence": 0.94,
  "sdss_seen": false
}
```
