

<!-- luna-raw:BLD-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G462",
  "selected_answer": 2,
  "official_answer": 2,
  "match": true,
  "original_blind_preserved": true,
  "group_blind_barrier_verified": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2020/2020_answer_2020_LEET_언어이해_정답표.hwp",
  "minimal_logic_without_codes": "같은단백질에서잘라낸여러펩타이드는원서열의서로다른구간이므로모두동일서열이라는②는도출되지않는다.절단위치가규칙적이라는것과각조각의서열동일성은다르다.",
  "sdss_seen": false,
  "strict_blind_eligible": false
}
```


<!-- luna-raw:BLD-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G462",
  "minimal_logic_without_codes": "하나의원서열을규칙적으로여러구간으로자르는것은각구간의서열이같다는뜻이아니다.",
  "primary": [
    {
      "code": 40,
      "reason": "하나의단백질전체와절단된여러펩타이드부분을구분하고부분끼리의동일성을함부로부여하지않는다."
    }
  ],
  "auxiliary": [
    {
      "code": 45,
      "reason": "원서열과절단규칙에서조각서열·분자량을예측하는변환관계를④에서적용한다."
    },
    {
      "code": 4,
      "reason": "생성되는펩타이드들의서열을모두같다고하는일괄동일성주장을배제한다."
    },
    {
      "code": 2,
      "reason": "⑤는발암확정이아닌후보라는강도를유지한다."
    }
  ],
  "surface": [
    {
      "code": 92,
      "reason": "분자량계산은원리상가능하지만주어진수치계산을요구하지않는다."
    }
  ],
  "competing_codes": [
    {
      "code": 22,
      "rejection": "개념계층의상속이아니다.동일원단백질에서유래했다고서열전체가모든조각에상속되지않는다."
    },
    {
      "code": 41,
      "rejection": "부분성질을전체로옮기는구성의오류보다는공통전체유래를부분상호동일성으로잘못확장한문제다."
    },
    {
      "code": 45,
      "rejection": "정해진절단규칙의출력판독으로도같은오류를설명가능해40/45유일주우선유보.40은전체와조각을분리하는작업대표."
    }
  ],
  "counterexample": "원서열의두절단구간에상이한아미노산배열이있으면절단규칙이같아도두펩타이드서열은다르다.반복서열로우연히같은조각이나올가능성은금지하지않는다.",
  "confidence": 0.92,
  "sdss_seen": false
}
```
