

<!-- luna-raw:BQS-answer_check-20261005-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G510",
  "selected_answer": 1,
  "official_answer": 1,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/표/2017/2017_answer/table_001.md (공식 HWP 추출 홀수형 11~13)",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "헌정 수단의 대표 다수결 제한 및 공적 토론 촉발 가능성을 투표로의 대체와 구별한다.",
  "strict_blind_eligible": false,
  "sdss_seen": false,
  "source_verification_limit": "공식 HWP에서 추출된 표 확인. 이번에 HWP 원본 직접 렌더링 재검증은 하지 않음.",
  "incidental_answer_exposure": "정답표 행 출력으로 2017 홀수·짝수 1~3,21~23,31~33 정답이 함께 노출됨. 이후 해당 문항은 엄격 blind 실적에서 제외. 원문·SDSS는 미열람."
}
```


<!-- luna-raw:BQS-independent_code-20261005-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G510",
  "sdss_seen": false,
  "primary": [
    {
      "code": 44,
      "reason": "헌정주의 수단이 의회 다수결을 제한하거나 토론을 촉발하는 작용을 추적하고 토론을 투표로 대체한다는 기능 오귀속을 배제한다."
    }
  ],
  "auxiliary": [
    {
      "code": 39,
      "reason": "선출 투표와 공적 토론이라는 두 참여 방식을 같은 것으로 섞지 않는다."
    },
    {
      "code": 12,
      "reason": "사법 심사가 토론을 촉진한다면 재평가할 수 있다는 조건부 연결을 보존한다."
    },
    {
      "code": 75,
      "cluster": "C074_075",
      "reason": "사법 심사 비판과 글쓴이의 조건부 재평가를 구별한다."
    }
  ],
  "surface": [
    {
      "code": 93,
      "reason": "토론이 등장하나 발화자·수신자의 전달 실패 분석을 요구하지 않는다."
    }
  ],
  "competing_codes": [
    {
      "code": 13,
      "rejection": "사법 심사와 공화주의가 언제나 양립 불가능하다고 할 수 없다. 마지막 문단이 조건부 조화를 제안한다."
    },
    {
      "code": 82,
      "rejection": "비판 뒤 재평가가 있다는 형식만으로 정반합 종합을 요구하는 연산이 되지 않는다."
    },
    {
      "code": 63,
      "rejection": "사법 심사 평가 변화는 지문 구조이나 정답① 배제는 주어진 수단의 기능을 잘못 바꾼 데서 직접 가능하다."
    }
  ],
  "confidence": 0.91,
  "scope_limit": "44는 결정 구간의 기능 대응을 대표한다. 39의 참여 방식 구분 및12의 조건부 평가가 다른 선지 검증에 필요하며 단일코드로 환원하지 않는다."
}
```
