

<!-- luna-raw:ACN-answer_check-20260920-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G179",
  "blind_answer": 3,
  "official_answer": 3,
  "match": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "문맥의 가려 판단하는 분별을 깨달음으로 옮기는교체가부적절. 최초근접의미불확실성은보존.",
  "official_answer_source": "sealed canonical 정답 기계연결; 해당배포원표직접검증아님",
  "group_barrier": "ACK/ACL/ACM/ACN 전체blind저장후answer만공개",
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```


<!-- luna-raw:ACN-independent_code-20260920-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G179",
  "primary": [
    96
  ],
  "auxiliary": [],
  "surface": [
    80
  ],
  "logic_without_codes_fixed": "고정 관념을 분별한다는 것은 이를 가려 판단하는 행위다. 깨닫는다는 교체는 알아차림에 가까워 이 문맥의 판단 행위를 충분히 보존하지 못한다.",
  "evidence": [
    "ⓒ 앞에는 공중이 고정 관념의 틀로 세상을 본다는 진술, 뒤에는 이를 분별할 수 있는 이가 드물다는 진술이 있다.",
    "괴리/동떨어짐, 기피/멀리함, 적합/알맞음, 달성/이루어짐은 해당 문장 역할을 유지한다."
  ],
  "primary_scope": "문맥 속 동사의 의미와 행위 방식을 보존하는 치환 검사",
  "competitors_rejected": [
    {
      "code": 80,
      "reason": "인식이 소재이지만 인식 주체와 대상의 관계를 교환한 선지는 아니다. 같은 주체·대상을 두고 분별/깨달음의 의미 적합성을 비교한다."
    },
    {
      "code": 16,
      "reason": "학술 개념의 정의 요건을 분해하여 사례에 적용하는 문제가 아니다."
    },
    {
      "code": 98,
      "reason": "소유·귀속 등 A의B 관계를 복원해야 하는 교체가 아니다."
    }
  ],
  "counterfactual_test": "대상과 주체를 그대로 두고 깨달을을 가려 판단할로 교체하면 문맥의 핵심 행위를 보존한다.",
  "boundary_note": "공식답③과 일치해도 두 동사의 모든 문맥에서 상호 치환이 불가능하다고 일반화하지 않는다. 최초 blind의 근접 의미 불확실성을 유지한다.",
  "confidence": 0.87,
  "sdss_seen": false,
  "quota_status": "unavailable"
}
```
