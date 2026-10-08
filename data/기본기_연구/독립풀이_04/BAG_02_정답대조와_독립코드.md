

<!-- luna-raw:BAG-answer_check-20261001-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G367",
  "selected_answer": 5,
  "official_answer": 5,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2016/2016_answer_2016학년도_법학적성시험_언어이해_정답표.hwp",
  "answer_access": "sealed 공식 정답 필드 대조; 정답표 원본 별도 재검증 아님",
  "code_free_logic_fixed": "숙련 공급 증가율이 수요 증가율을 앞서면 프리미엄이 축소되고 불평등이 완화된다.",
  "original_blind_preserved": true,
  "group_blind_barrier_verified": true,
  "sdss_seen": false
}
```


<!-- luna-raw:BAG-independent_code-20261001-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    49
  ],
  "auxiliary": [
    46,
    87,
    39
  ],
  "surface": [
    100
  ],
  "decisive_operation": "공급과 수요의 증가율을 비교하여 프리미엄과 불평등의 변화 방향을 적용한다.⑤가 방향을 역전한다.",
  "evidence": [
    "3문단 교육이 기술보다 빠름→공급 상대 확대→프리미엄 축소",
    "역사 연구: 교육 임금 격차가 불평등의 큰 부분 설명"
  ],
  "competing_codes": [
    {
      "code": 87,
      "rebuttal": "증가율 비교는 입력 조건이지만 미분이나 기울기 계산이 결정적이지 않다. 주로 올리는 것은 유보한다."
    },
    {
      "code": 86,
      "rebuttal": "수준의 크기 비교가 아니라 증가 속도 및 결과 방향이다. 절대 공급량 초과로 바꾸지 않는다."
    },
    {
      "code": 46,
      "rebuttal": "공급→임금 격차라는 경로는 보조로 보존하나 이 문항에서 새 중간 기제를 복원할 필요 없이 주어진 방향을 적용한다."
    },
    {
      "code": 100,
      "rebuttal": "경주 비유를 알아보는 것보다 그 비유가 가리키는 두 증가 속도의 관계를 적용하는 일이 필요하다."
    }
  ],
  "boundary_note": "49는 통계적 공변에 한정하지 않는 원표 용례 유지.46과 배타적이지 않으며 직접 방향 적용/기제 복원의 작업 우선순위로 구분.",
  "confidence": 0.93,
  "passage_group": "G367",
  "sdss_seen": false,
  "code_free_logic_preserved": true
}
```
