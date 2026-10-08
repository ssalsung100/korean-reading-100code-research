

<!-- luna-raw:BAL-blind-20261001-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G368",
  "selected_answer": 2,
  "confidence": 0.96,
  "necessary_information_locations": [
    "3문단: 광자 운동량은 파장에 반비례, 에너지는 진동수에 비례, 진동수와 파장 반비례",
    "마지막 문단: 냉각 광원 진동수는 공명보다 작게 설정",
    "G368_visual03/05.md: 루비듐85.47·780nm, 리튬6.94·670nm"
  ],
  "minimal_logic_without_codes": "리튬의 공명 파장은 짧으므로 공명 진동수와 대응 광자 운동량은 크다. 같은 속도에서 냉각시키는 광자는 각 원자 공명보다 낮은 진동수로 조정되어도 두 종 사이 순서는 유지된다. 따라서 리튬 흡수 광자 운동량이 더 작다는②는 반대다.",
  "intermediate_reasoning": [
    "①670<780이므로 리튬 공명 진동수가 크다.",
    "② 파장이 짧은 쪽의 광자 운동량이 크므로 제시 방향 반대. 같은 속도 조건에서 도플러 보정으로 순서가 뒤집히지 않는다.",
    "③같은 v에서 p=mv이고 리튬 질량이 작아 원자 운동량은 작다.",
    "④공명 진동수가 달라 동일 속도에서도 루비듐용 진동수는 리튬 공명 조건과 맞지 않는다.",
    "⑤공명보다 낮은 진동수는 공명보다 긴 파장에 대응하므로670nm보다 길게 설정."
  ],
  "most_attractive_wrong_answer": 5,
  "exact_error": "다가오는 원자에서 감지 진동수가 커진다는 조건을 광원의 설정 진동수가 커야 한다는 결론으로 뒤집기 쉽다. 감지값을 공명에 맞추려면 광원 진동수는 낮게, 파장은 길게 한다.",
  "source_quality_limit": "본문 수치·에너지 기호가 누락되어 다른 세 문항은 hold. BAL 자체 선지와 필수 표·방향 관계는 완비. 외부 물리 지식으로 지문의 평균속도 정의 등을 교정하지 않고 문항 내부 설명 범위로 판단.",
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_project_judgment_seen": false,
    "historical_exposure": "확인 불가"
  },
  "strict_blind_eligible": "과거 노출 미확정으로 엄격 성과 확정 제외",
  "group_barrier": "BAI/BAJ/BAK 유효 blind 완료 전 G368 답/SDSS 봉인",
  "source": "data/기본기_연구/prepared_backlog/blind_sources/BAL.json 및 G368_visual01~05",
  "quota_status": "unavailable"
}
```
