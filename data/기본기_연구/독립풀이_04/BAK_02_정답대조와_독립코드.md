

<!-- luna-raw:BAK-answer_check-20261001-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G368",
  "selected_answer": 1,
  "official_answer": 1,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2016/2016_answer_2016학년도_법학적성시험_언어이해_정답표.hwp",
  "answer_access": "sealed 공식 정답 필드 대조; 정답표 원본 별도 재검증 아님",
  "code_free_logic_fixed": "v에서 접근+2Hz,2v에서+4Hz,접근 음원off이면 이격 음원만 남아 공명 조건이 성립하지 않는다.",
  "original_blind_preserved": true,
  "group_blind_barrier_verified": true,
  "sdss_seen": false,
  "source_repair_provenance": "공식 HWP question-only 등록 렌더13~14 직접 확인. 선행 hold와 불완전crop 기록 보존."
}
```


<!-- luna-raw:BAK-independent_code-20261001-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    45
  ],
  "auxiliary": [
    12,
    91,
    92
  ],
  "surface": [
    69,
    100
  ],
  "decisive_operation": "각 켜진 음원과 소리굽쇠의 접근·이격 방향 및 속력을 감지 진동수로 변환하고 출력500Hz 여부를 검사한다.",
  "evidence": [
    "기준v에서+2Hz",
    "ㄱ500/496,ㄴ502/494,ㄷ왼쪽off·오른쪽496"
  ],
  "competing_codes": [
    {
      "code": 91,
      "rebuttal": "v→2v에서 차이2→4를 얻는 부분 연산이다.음원off와 방향을 반영하지 않으면ㄷ을 해결하지 못한다."
    },
    {
      "code": 12,
      "rebuttal": "500Hz 일치라는 공명 조건은 필수 보조다.세 경우의 차이를 실제 산출하는 핵심은 방향·속도·음원 상태에 따른 변환이다."
    },
    {
      "code": 69,
      "rebuttal": "빛과 소리의 공통 법칙 적용은 있지만 유사성에서 미지 성질을 새로 추정하는 유비 논증이 아니다."
    },
    {
      "code": 87,
      "rebuttal": "차이가 속도에 비례하지만 그래프 기울기나 변화율 계산을 요구하지 않는다."
    }
  ],
  "boundary_note": "소리 크기·거리 자체를 더하지 않는다. 같은 속력이라도 음원 상태와 방향이 다르면 다른 출력이다.",
  "confidence": 0.96,
  "passage_group": "G368",
  "sdss_seen": false,
  "code_free_logic_preserved": true,
  "source_repair_provenance_preserved": true
}
```
