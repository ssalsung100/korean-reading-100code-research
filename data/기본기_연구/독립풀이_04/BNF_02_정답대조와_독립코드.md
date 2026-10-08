

<!-- luna-raw:BNF-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G480",
  "selected_answer": 2,
  "official_answer": 2,
  "match": true,
  "original_blind_preserved": true,
  "group_blind_barrier_verified": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2024/2024_answer_2024언어이해정답.pdf",
  "minimal_logic_without_codes": "ㄱ은 다른 조건을 고정한 재선 후보 정보 축적,ㄴ은 넓은 지역에서 한 도시의 대표성 한계로 가능하다.시간당 임금과 투표율의 음의 관계는 기회비용 설명과 부합하므로 그 필요가 줄어든다는ㄷ은 맞지 않는다.②이다.",
  "sdss_seen": false,
  "strict_blind_eligible": false
}
```


<!-- luna-raw:BNF-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G480",
  "minimal_logic_without_codes": "정보 비용과 포기 소득의 변화가 투표 참여에 연결되는 방향을 판단하고, 넓은 지역을 한 도시 자료로 대표하는 측정 한계를 구분한다.",
  "primary": [
    {
      "code": 46,
      "reason": "ㄱ의 정보 비용 감소와ㄷ의 임금·포기 소득·참여 감소를 비용 기제로 연결한다."
    }
  ],
  "auxiliary": [
    {
      "code": 43,
      "reason": "ㄱ은 다른 조건을 고정한 비교라는 명시 조건을 유지한다."
    },
    {
      "code": 45,
      "reason": "ㄴ은 도시 강수량이라는 입력 대리지표가 주 전체 날씨를 얼마나 표현하는지의 측정 대응이다."
    },
    {
      "code": 63,
      "reason": "ㄷ의 음의 관계는 기회비용 설명을 배제할 근거가 아니라 그 검토와 부합하는 자료다.인과 확정으로 확대하지 않는다."
    },
    {
      "code": 2,
      "reason": "ㄱㄴ의 가능성 진술을 모든 재선·모든 큰 주에 대한 필연으로 바꾸지 않는다."
    }
  ],
  "surface": [
    {
      "code": 49,
      "reason": "관측된 음의 상관이 있지만 그 사실 자체와 설명 기제의 필요성 평가는 별도 단계다."
    }
  ],
  "competing_codes": [
    {
      "code": 41,
      "rejection": "한 도시의 날씨를 주의 대리지표로 쓰는 것은 대표성 검토 문제다.모든 부분의 속성을 전체에 옮기는 전형적 결합 오류와 자동 동일시하지 않는다."
    },
    {
      "code": 55,
      "rejection": "임금-참여 상관만으로 인과가 확정되지는 않지만 그렇다고 기회비용 설명과의 부합 자체를 허위 인과라고 배제할 수는 없다."
    },
    {
      "code": 86,
      "rejection": "주 면적이나 임금의 정량 차이를 계산하는 문제가 아니라 측정 범위와 비용 경로를 판독한다."
    }
  ],
  "confidence": 0.93,
  "sdss_seen": false
}
```
