

<!-- luna-raw:BAJ-blind-20261001-restored-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "necessary_information_locations": [
    "인쇄면13 오른쪽: 접근시 감지 진동수 증가, 고유 공명 진동수만 흡수",
    "인쇄면13 그림과 말미: E1→E2 흡수, E2→E1 방출, 방출 에너지ΔE",
    "인쇄면14 Q30① 공명 진동수 광원을 다가오는 원자에 조사"
  ],
  "minimal_logic_without_codes": "접근 원자에게 광원의 공명 진동수 자체를 쏘면 감지값은 공명보다 커진다. 그러면 선택적 흡수 조건이 맞지 않아 E1에서E2로 올릴 수 없다. 따라서①이 틀리다.",
  "intermediate_reasoning": [
    "①광원f=f0,접근→감지f>f0이므로 흡수·준위상승 불가.",
    "②공명 진동수 광자 자체의 에너지는ΔE.",
    "③흡수 과정을 거쳐 방출하는 광자의 에너지는 고정 준위 차ΔE. 흡수 광원의 에너지도 항상ΔE라는 뜻으로 넓히지 않는다.",
    "④정지 원자에서는 도플러 변화 없이ΔE 광자를 흡수.",
    "⑤E2→E1은 낮은 준위로 돌아오는 방출."
  ],
  "most_attractive_wrong_answer": 3,
  "exact_error": "문장의 방출 광자를 흡수 광자까지 포괄하는 동일 에너지 주장으로 읽으면③을 오인한다. 냉각에서 흡수 광원 에너지는ΔE보다 작고 방출은ΔE이며,③의 서술 대상은 흡수 후 방출하는 광자다.",
  "passage_group": "G368",
  "selected_answer": 1,
  "confidence": 0.98,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가",
    "official_question_full_pages_directly_seen": true
  },
  "strict_blind_eligible": "과거 노출 미확정으로 엄격 성과 확정 제외",
  "source": [
    "data/기본기_연구/prepared_backlog/blind_sources/G368_restore_page13.png",
    "data/기본기_연구/prepared_backlog/blind_sources/G368_restore_page14.png"
  ],
  "provenance": "공식2016 LEET 홀수형 HWP 등록 렌더 인쇄면13~14 직접 확인. page13 상단 이전완료 BAH도 보이나 신규 미풀이 외부문항 없음.",
  "original_hold_preserved": true,
  "source_repair": "누락 기호·BAK v/2v 확인 완료. 첫crop 불완전 기록은 보존.",
  "quota_status": "unavailable"
}
```
