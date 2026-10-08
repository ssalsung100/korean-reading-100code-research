

<!-- luna-raw:BLV-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G468",
  "selected_answer": 3,
  "official_answer": 3,
  "match": true,
  "original_blind_preserved": true,
  "group_blind_barrier_verified": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2020/2020_answer_2020_LEET_언어이해_정답표.hwp",
  "minimal_logic_without_codes": "가장자리7번째를패턴시작으로두면7~11은넓고12~16은좁으며17~22는다시넓다.20번째가좁다는③이틀리다.",
  "sdss_seen": false,
  "strict_blind_eligible": false,
  "source_restoration_before_disclosure": true,
  "source_scope_verified": "公式crop직접확인:[A]예시한문단,[B]마지막한문단.잘못된초기부록범위는정정됨."
}
```


<!-- luna-raw:BLV-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G468",
  "minimal_logic_without_codes": "7번째부터넓음5·좁음5·넓음6의구간을대입하면20번째는마지막넓은구간에해당한다.",
  "primary": [
    {
      "code": 92,
      "reason": "시작인덱스와구간길이를결합해7~11,12~16,17~22의범위를계산한다."
    }
  ],
  "auxiliary": [
    {
      "code": 3,
      "reason": "층의순서와연도를대응하고벌목·생육시작시점을구분한다."
    },
    {
      "code": 45,
      "reason": "나이테위치에서연대와폭패턴으로의대응을적용한다."
    },
    {
      "code": 31,
      "reason": "나이테개수와패턴구간내위치를혼동하지않는다."
    }
  ],
  "surface": [
    {
      "code": 49,
      "reason": "폭은강수량과관련되지만이문항은강수량원인을새로추론하지않는다."
    }
  ],
  "competing_codes": [
    {
      "code": 84,
      "rejection": "비율이나분모변화를계산하는것이아니라정수구간과연도차를계산한다."
    },
    {
      "code": 86,
      "rejection": "폭의대소라기보다어느인덱스가어느범주인지확인하는과제다."
    },
    {
      "code": 99,
      "rejection": "[A]범위복원은자료전제이며복원후정답을결정하는행동은인덱스계산이다."
    }
  ],
  "source_limit": "공식문구의근사연대와층위차감관례를보존.표지범위는공식이미지에서예시문단하나로확인.",
  "confidence": 0.95,
  "sdss_seen": false
}
```
