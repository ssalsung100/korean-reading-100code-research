

<!-- luna-raw:BAF-answer_check-20261001-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G367",
  "selected_answer": 3,
  "official_answer": 3,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2016/2016_answer_2016학년도_법학적성시험_언어이해_정답표.hwp",
  "answer_access": "sealed 공식 정답 필드 대조; 정답표 원본 별도 재검증 아님",
  "code_free_logic_fixed": "초기와 후기 모두 숙련 수요가 증가한다. 숙련 내용의 차이를 숙련 유무의 차이로 치환할 수 없다.",
  "original_blind_preserved": true,
  "group_blind_barrier_verified": true,
  "sdss_seen": false
}
```


<!-- luna-raw:BAF-independent_code-20261001-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    17
  ],
  "auxiliary": [
    3,
    16,
    39
  ],
  "surface": [
    5,
    46
  ],
  "decisive_operation": "초기 계산·독해도 숙련의 한 내용임을 유지하여 시기별 속성을 귀속한다. 숙련 내용의 변화에서 초기 미숙련 선호를 도출한③을 배제한다.",
  "evidence": [
    "2문단 초기/후기 숙련 내용 구분",
    "3문단 숙련 수요 증가 방향은 세기 내내 유지"
  ],
  "competing_codes": [
    {
      "code": 5,
      "rebuttal": "수요 방향은 지속되고 숙련 내용은 변화한다. 단일 지속/변화 이분만으로는 어느 속성이 변하는지 분리하지 못한다."
    },
    {
      "code": 3,
      "rebuttal": "초기와 후기의 시점 보존은 보조이나 결정적 오류는 초기 능력을 미숙련으로 분류한 범주 전환이다."
    },
    {
      "code": 46,
      "rebuttal": "교육과 성장 인과는①의 근거지만 오답③ 결정은 숙련 수요의 대상·내용 확인이다."
    }
  ],
  "boundary_note": "17/16/39는 이 사례에서 요건·속성 귀속이 겹친다. 번호별 배타적 연산으로 중복 계수하지 않는다.",
  "confidence": 0.89,
  "passage_group": "G367",
  "sdss_seen": false,
  "code_free_logic_preserved": true
}
```
