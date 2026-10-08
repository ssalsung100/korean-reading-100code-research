

<!-- luna-raw:AIE-answer_check-20260921-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G212",
  "blind_answer": 2,
  "official_answer": 2,
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "(나)는그와아이들의관계가사건을거쳐복종으로바뀌며상징적으로주제를드러낸다.②이 적절.",
  "official_answer_source": "자료/평가원_정답표/원본/모의평가/2023_6월_국어_1교시_국어영역_정답표.pdf",
  "verification_scope": "sealed답필드대조, 공식PDF정답셀 직접검증은 아직아님",
  "barrier_verified": "G212 전체 blind3 저장 후 answer필드만 공개; SDSS 미공개",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AIE-independent_code-20260921-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G212",
  "primary": [
    100
  ],
  "auxiliary": [
    3,
    39,
    17
  ],
  "surface": [
    97
  ],
  "judgment_reason": "(나)의 유리 담장·관용·추방·부하화 사건이 상징적 권력관계를 보여 준다는②를 수용한다. 정답의 상징적 서사 해석과 다른 선지의 형식 특징 귀속을 분리한다.",
  "competing_codes": [
    {
      "code": 3,
      "verdict": "보조",
      "reason": "사건의 전개가 필요하지만 시간순 나열만으로 상징적 주제 암시를 설명하지 못함"
    },
    {
      "code": 17,
      "verdict": "특정 오답 보조",
      "reason": "④의 반복변주 특징을 두 작품 모두에 귀속한 오류를 검사"
    },
    {
      "code": 39,
      "verdict": "보조",
      "reason": "두 작품의 특징 대조는 오답 배제에 쓰이나② 직접 수용은 (나) 내부 근거로 가능"
    },
    {
      "code": 97,
      "verdict": "특정 오답 표면",
      "reason": "⑤ 청자에게 건네는 어조를 작품 간 잘못 맞춤.②은 서술자 직접충고가 아니라 사건의 상징"
    }
  ],
  "minimal_change_test": "사건들이 권력의 유인·배제·복종이라는 뜻을 나타내지 않는 일상적 유리수선 이야기라면②의 상징성 근거가 약해진다. 본문 결말의 부하화가 그 차이를 만든다.",
  "sdss_seen": false,
  "confidence": 0.93,
  "quota_status": "unavailable"
}
```
