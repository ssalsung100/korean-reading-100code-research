

<!-- luna-raw:BOT-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G493",
  "selected_answer": 2,
  "confidence": 0.99,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "necessary_information": [
    {
      "location": "[A]·보기",
      "evidence": "소비 최대 정태상태가 황금률. X국은 현재 정태상태지만 자본이 황금률보다 높아 소비 장려로 저축률을 낮춘다."
    },
    {
      "location": "본문 항등식·수렴식",
      "evidence": "c=(1-s)y, i=sy, 자본변화=i-dk. 같은 생산함수에서 자본이 줄면 생산도 줄어든다."
    }
  ],
  "minimal_logic_without_codes": "저축률 하락 직후 자본·생산은 그대로여서 소비가 뛰지만, 이후 자본과생산이새정태상태로줄어드는동안 고정된 새소비비율의 소비도감소한다.②의점차증가가틀리다. 최종소비는황금률이어서원래보다높다.",
  "intermediate_reasoning": [
    "① 현재 소비가 즉각 늘고 이후에도 황금률의 더 높은 최종소비까지 내려오므로 현재 고령층·청년층 모두 이익을 얻는다.",
    "③ 황금률의 최대 정태소비는 기존 과잉자본 정태소비보다 높다.",
    "④ 감가상각률이 고정되어 자본이 감소하면 감가상각량도 낮은 수준으로 수렴한다.",
    "⑤ 저축률 하락 뒤 신규투자가 감가상각보다 작아져 자본은 낮은 황금률로 수렴한다."
  ],
  "most_attractive_wrong": {
    "choice": 1,
    "exact_error": "[A]의 황금률 미달 상태에서 저축을 늘리는 정책의 세대간 갈등을, 황금률 초과 상태에서 저축을 줄이는 반대 정책에 그대로 복사한다."
  },
  "source_restoration": {
    "crop": "data/기본기_연구/prepared_backlog/blind_sources/G493_official_A_crop.png",
    "astra_direct_seen": true,
    "range": "황금률 정의로 시작해 고령층의 정책 반대 가능성으로 끝나는 단락",
    "resolved_before_answer_disclosure": true
  },
  "scope_limit": "정책이 목표인 황금률을 달성하도록 저축률을 조정하고 다른 조건이 고정된 보기의 모형이다. 임의의 과도한 저축률 변화까지 일반화하지 않는다."
}
```
