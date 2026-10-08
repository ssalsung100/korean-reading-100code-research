

<!-- luna-raw:BQR-answer_check-20261005-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G510",
  "selected_answer": 3,
  "official_answer": 3,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/표/2017/2017_answer/table_001.md (공식 HWP 추출 홀수형 11~13)",
  "group_blind_barrier_verified": true,
  "original_blind_preserved": true,
  "minimal_logic_without_codes": "국가의 확대에 따른 파벌 다양화와 한 파벌의 영향 확대를 구별한다. 후자는 분할의 이익을 훼손한다.",
  "strict_blind_eligible": false,
  "sdss_seen": false,
  "source_verification_limit": "공식 HWP에서 추출된 표 확인. 이번에 HWP 원본 직접 렌더링 재검증은 하지 않음.",
  "incidental_answer_exposure": "정답표 행 출력으로 2017 홀수·짝수 1~3,21~23,31~33 정답이 함께 노출됨. 이후 해당 문항은 엄격 blind 실적에서 제외. 원문·SDSS는 미열람."
}
```


<!-- luna-raw:BQR-independent_code-20261005-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G510",
  "sdss_seen": false,
  "primary": [
    {
      "code": 17,
      "reason": "커지는 대상을 공화국 전체와 특정 파벌로 구별해야 ③과④의 반대 효과가 설명된다."
    }
  ],
  "auxiliary": [
    {
      "code": 46,
      "reason": "한 파벌 영향 확산은 억제할 내부 위협이지 위협 감소 수단이 아니다."
    },
    {
      "code": 75,
      "cluster": "C074_075",
      "reason": "연방주의자의 분할·결집 효과 해석을 그 주체에 귀속한다."
    }
  ],
  "surface": [
    {
      "code": 86,
      "reason": "작은/큰 규모라는 양적 표상이 있지만 수량 계산·서열 계산은 필요 없다."
    }
  ],
  "competing_codes": [
    {
      "code": 41,
      "rejection": "부분 파벌과 전체 국가가 등장해도 모든 부분의 속성을 전체에 합성한 오류는 아니다."
    },
    {
      "code": 49,
      "rejection": "증감 방향도 필요하지만 무엇의 규모인지를 바꾸면 인과 방향이 달라진다는 대상 구분이 선행한다."
    },
    {
      "code": 63,
      "rejection": "새 증거가 연방주의를 약화하는지를 평가하는 문제가 아니라 그 입장에 맞는 진술을 식별한다."
    },
    {
      "code": 40,
      "rejection": "부분·전체 소속을 명시하면 17과 국소 중첩한다. 별개 필수 연산으로 강제 분리하지 않고 대상 변화에 초점을 둔다."
    }
  ],
  "confidence": 0.93,
  "scope_limit": "17/40 주 우선순위는 국소 작업 대표이며 전역적인 배타 경계가 아니다.⑤의 본성 일반화는 직접 명시보다 추론이 많다는 blind 제한을 보존한다."
}
```
