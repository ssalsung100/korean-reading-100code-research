> 이 파일은 원장으로부터 자동 생성된 열람용 파생본이다. 연구의 authoritative source는 raw queue이며, 이 파일을 직접 편집하지 않는다.

# GV

## 0. 문항 정보

- **Passage group:** G042

### 제시문

```text
채권은 사업에 필요한 자금을 조달하기 위해 발행하는 유가 증권으로, 국채나 회사채 등 발행 주체에 따라 그 종류가 다양하다. 채권의 액면 금액, 액면 이자율, 만기일 등의 지급 조건은 채권 발행 시 정해지며, 채권 소유자는 매입 후에 정기적으로 이자액을 받고, 만기일에는 마지막 이자액과 액면 금액을 지급받는다. 이때 이자액은 액면 이자율을 액면 금액에 곱한 것으로 대개 연 단위로 지급된다. 채권은 만기일 전에 거래되기도 하는데, 이때 채권 가격은 현재 가치, 만기, 지급 불능 위험 등 여러 요인에 따라 결정된다.

채권 투자자는 정기적으로 받게 될 이자액과 액면 금액을 각각 현재 시점에서 평가한 값들의 합계인 채권의 현재 가치에서 채권의 매입 가격을 뺀 순수익의 크기를 따진다. 채권 보유로 미래에 받을 수 있는 금액을 현재 가치로 환산하여 평가할 때는 금리를 반영한다. 가령 금리가 연 10 %이고, 내년에 지급받게 될 금액이 110 원이라면, 110 원의 현재 가치는 100 원이다. 즉 금리는 현재 가치에 반대 방향으로 영향을 준다. 따라서 금리가 상승하면 채권의 현재 가치가 하락하게 되고 이에 따라 채권의 가격도 하락하게 되는 결

과로 이어진다. 이처럼 수시로 변동되는 시중 금리는 현재 가치의 평가 구조상 채권 가격의 변동에 영향을 주는 요인이 된다.

채권의 매입 시점부터 만기일까지의 기간인 만기도 채권의 가격에 영향을 준다. 일반적으로 다른 지급 조건이 동일하다면 만기가 긴 채권일수록 가격은 금리 변화에 더 민감하므로 가격 변동의 위험이 크다. 채권은 발행된 이후에는 만기가 점점 짧아지므로 ㉠ 만기일이 다가올수록 채권 가격은 금리 변화에 덜 민감해진다. 따라서 투자자들은 만기가 긴 채권일수록 높은 순수익을 기대하므로 액면 이자율이 더 높은 채권을 선호한다.

또 액면 금액과 이자액을 약정된 일자에 지급할 수 없는 지급 불능 위험도 채권 가격에 영향을 준다. 예를 들어 채권을 발행한 기업의 경영 환경이 악화될 경우, 그 기업은 지급 능력이 떨어질 수 있다. 이런 채권에 투자하는 사람들은 위험을 감수해야 하므로 이에 대한 보상을 요구하게 되고, 이에 따라 채권 가격은 상대적으로 낮게 형성된다.

한편 채권은 서로 대체가 가능한 금융 자산의 하나이기 때문에, 다른 자산 시장의 상황에 따라 가격에 영향을 받기도 한다. 가령 주식 시장이 호황이어서 ㉡ 주식 투자를 통한 수익이 커지면 상대적으로 채권에 대한 수요가 줄어 채권 가격이 하락할 수도 있다.
```

### 발문

```text
&lt;보기&gt;의 A는 어떤 채권의 가격과 금리 간의 관계를 나타낸 그래프이다. 윗글의 ㉠과 ㉡에 따른 A의 변화 결과를 바르게 예측한 것은?

&lt; 보 기 &gt;

㉠

㉡
```

### 선지

```json
[
  "ⓐ\n\nⓒ",
  "ⓑ\n\nⓐ",
  "ⓑ\n\nⓒ",
  "ⓒ\n\nⓐ",
  "ⓒ\n\nⓑ"
]
```

### 원문 자료 감사

```json
{
  "case_id": "GV",
  "source_file_exists": true,
  "mechanically_linked": true,
  "assets": [
    {
      "path": "data/기본기_연구/prepared_backlog/blind_sources/GV.json",
      "exists": true,
      "kind": "supplement_or_source"
    },
    {
      "path": "data/기본기_연구/prepared_backlog/blind_sources/GV_graph_figure.png",
      "exists": true,
      "kind": "image"
    }
  ],
  "image_files_exist": true,
  "image_meaning_verified": false,
  "choice_count": 5,
  "all_choices_empty": false,
  "warnings": [],
  "ready": true
}
```

## 1. 최초 blind 풀이

### 최초 blind 풀이 — `GV-blind-20260915-01`

**선택 답**

`3`

**확신도**

```text
높음
```

**필요 정보와 위치**

```json
[
  "㉠만기 접근→금리 변화에 덜 민감",
  "㉡주식수익 증가→채권수요 감소→채권가격 하락 가능",
  "복원 그래프 직접 판독:가로금리,세로가격;ⓐ는A보다위,ⓒ는A보다아래,ⓑ는A를가로지르며더완만"
]
```

**코드명 없는 최소 논리 구조**

```text
㉠은 같은 금리 변화에 따른 가격 변화폭 감소이므로 기울기가 완만해진ⓑ이다.㉡은 같은 금리에서 가격이 더 낮은ⓒ다. 따라서③이다.
```

**중간 추론**

```json
[
  "ⓐ/ⓒ는 가격 수준이 달라진 모습을 나타내며 그것만으로 금리 민감도 감소를 뜻하지 않는다.",
  "ⓑ는A와 교차하므로 모든 금리에서 가격이 낮다는 의미로 읽을 수 없다.",
  "②는㉠ⓑ까지 맞지만㉡을가격상승ⓐ로역전한다.",
  "⑤는㉠을단순가격하락ⓒ로읽고㉡을기울기변화ⓑ로바꾼다."
]
```

**가장 매력적인 오답**

`5`

**오답의 정확한 오류**

```text
민감도 감소를 가격 감소로 바꾸고,수요 감소의 가격 수준 효과를 민감도 변화로 바꾼다.
```

**노출 정보**

```json
{
  "official_answer_seen": false,
  "sdss_seen": false,
  "prior_project_judgment_seen": false,
  "same_group_passage_seen": true,
  "prior_training_exposure": "확인 불가"
}
```

**기타 기록 필드**

```json
{
  "passage_group": "G042",
  "source": [
    "data/기본기_연구/prepared_backlog/blind_sources/GV.json",
    "data/기본기_연구/prepared_backlog/blind_sources/GV_graph_figure.png"
  ],
  "source_quality": "누락 그림 주 Astra 직접 판독으로 hold 해소. 원문 그림의 관계 확인이며 실제 금융시장 곡선 예측으로 일반화하지 않는다.",
  "original_hold_preserved": true
}
```

## 2. 공식 정답 대조

### 공식 정답 대조 — `GV-answer_check-20260915-01`

**공식 정답**

`3`

**일치 여부**

`true`

**기타 기록 필드**

```json
{
  "passage_group": "G042",
  "group_blind_barrier_verified": true,
  "blind_selected_answer": 3,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "민감도 감소는ⓑ의 완만함,수요 감소는ⓒ의 가격 수준 하락으로 대응한다.",
  "sdss_disclosed": false,
  "source_quality": "GV 그래프는 답 공개 전 주 Astra 직접 판독 완료. 기존hold 불변.",
  "quota_status": "unavailable"
}
```

## 3. 독립 코드 판정

### 독립 코드 판정 — `GV-independent_code-20260915-01`

**주 코드**

```json
[
  {
    "code": 87,
    "name": "기울기",
    "scope": "㉠의ⓑ 대응 및㉡과 구별",
    "reason": "민감도는 금리 변화에 대한 가격 변화의 크기이며 곡선의 가파름과 대응한다."
  }
]
```

**보조 코드**

```json
[
  {
    "code": 49,
    "name": "상관관계",
    "scope": "㉡의ⓒ 대응",
    "reason": "주식 수익↑→채권 수요↓→가격↓ 방향을 읽어 아래 곡선을 선택한다."
  },
  {
    "code": 45,
    "name": "함수",
    "scope": "곡선의 입력/출력 및 비교 조건",
    "reason": "가로 금리·세로 가격에서 같은 입력의 출력 수준과 입력 변화에 대한 출력 변화량을 분리한다."
  }
]
```

**표면 코드**

```json
[
  {
    "code": 3,
    "name": "선후",
    "reason": "만기일이 가까워진다는 시간이 나와도 직접 그래프 과제는 민감도 변화다."
  }
]
```

**경쟁 코드 및 반증**

```json
[
  {
    "code": 86,
    "verdict": "양적 비교의 넓은 설명은 가능하나 수준과 변화율을 별도 보존하지 않으면ⓑ/ⓒ를 구별할 수 없다."
  },
  {
    "code": 43,
    "verdict": "같은 금리에서 비교해야 하지만 통제 성립의 검증이 아니라 이미 주어진 그래프 해석이다."
  },
  {
    "code": 46,
    "verdict": "수요 경로는㉡을 뒷받침한다. 그러나 같은 인과 감소라는 말로㉠민감도 감소까지 가격 하락으로 바꾸면⑤ 오류가 된다."
  }
]
```

**확신도**

```text
높음;전역 분리 미확정
```

**경계 메모**

```text
#87은 #45의 변화량/민감도 하위 작업으로 볼 수 있다. 별개 본질의 코드로 강제 분리하지 않는다.
```

**정규화된 주 코드 후보**

```json
[
  {
    "source_key": "primary",
    "value": [
      {
        "code": 87,
        "name": "기울기",
        "scope": "㉠의ⓑ 대응 및㉡과 구별",
        "reason": "민감도는 금리 변화에 대한 가격 변화의 크기이며 곡선의 가파름과 대응한다."
      }
    ]
  }
]
```

**정규화된 보조 코드**

```json
[
  {
    "source_key": "auxiliary",
    "value": [
      {
        "code": 49,
        "name": "상관관계",
        "scope": "㉡의ⓒ 대응",
        "reason": "주식 수익↑→채권 수요↓→가격↓ 방향을 읽어 아래 곡선을 선택한다."
      },
      {
        "code": 45,
        "name": "함수",
        "scope": "곡선의 입력/출력 및 비교 조건",
        "reason": "가로 금리·세로 가격에서 같은 입력의 출력 수준과 입력 변화에 대한 출력 변화량을 분리한다."
      }
    ]
  }
]
```

**정규화된 경쟁 코드 및 반증**

```json
[
  {
    "source_key": "competing_codes",
    "value": [
      {
        "code": 86,
        "verdict": "양적 비교의 넓은 설명은 가능하나 수준과 변화율을 별도 보존하지 않으면ⓑ/ⓒ를 구별할 수 없다."
      },
      {
        "code": 43,
        "verdict": "같은 금리에서 비교해야 하지만 통제 성립의 검증이 아니라 이미 주어진 그래프 해석이다."
      },
      {
        "code": 46,
        "verdict": "수요 경로는㉡을 뒷받침한다. 그러나 같은 인과 감소라는 말로㉠민감도 감소까지 가격 하락으로 바꾸면⑤ 오류가 된다."
      }
    ]
  }
]
```

**기타 기록 필드**

```json
{
  "passage_group": "G042",
  "logic_without_codes": "같은 금리 변화의 가격 변화폭이 줄어드는 것과 같은 금리에서 가격 수준이 낮아지는 것을 서로 다른 곡선 변화로 대응한다.",
  "falsification_attempt": "ⓑ는A와 교차하므로 민감도가 줄어도 모든 금리에서 가격이 더 낮아지는 것은 아니다. 실제 그림이 민감도 감소→수준 하락이라는 가설의 반례다.",
  "sdss_disclosed": false
}
```

## 4. SDSS 사후 대조

> SDSS는 독립 판정 후 공개된 제3자 후보 라벨이다. 이 기록은 독립 판정의 근거로 소급 사용하지 않는다.

### SDSS 사후 대조 — `GV-sdss_compare-20260915-01`

**사이트 원래 코드**

```json
[]
```

**독립 주 코드**

```json
[
  87
]
```

**기타 기록 필드**

```json
{
  "passage_group": "G042",
  "group_independent_barrier_verified": true,
  "candidate_id": null,
  "comparison_status": "prepared_index_unlinked",
  "meaning_comparison": "사이트 연결이 없는 준비 자료이므로 실제 무코드·불일치로 집계하지 않는다.",
  "revision_required": false,
  "unresolved": "실제 사이트 태그·적용 범위 미확인"
}
```

## 5. 후속 보강

이 case에 명시적으로 연결된 depth_backfill 또는 case-specific boundary_revision 기록이 없습니다.


## 6. 원장 추적

사용된 원장 record_id (queue 순서):
- `GV-hold-20260915-graph-01` — hold / hold
- `GV-blind-20260915-01` — 최초 blind 풀이 / done
- `GV-answer_check-20260915-01` — 공식 정답 대조 / done
- `GV-independent_code-20260915-01` — 독립 코드 판정 / done
- `GV-sdss_compare-20260915-01` — SDSS 사후 대조 / done
