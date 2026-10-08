> 이 파일은 원장으로부터 자동 생성된 열람용 파생본이다. 연구의 authoritative source는 raw queue이며, 이 파일을 직접 편집하지 않는다.

# GN

## 0. 문항 정보

- **Passage group:** G040

### 제시문

```text
가위, 바위, 보! 무엇을 내느냐에 따라 서로의 승패는 확연히 갈리지만 이 게임의 묘미는 영원한 승자도, 영원한 패자도 없다는 데 있다. 이렇게 서로 끝없이 물고 물리는 가위바위보의 관계가 생물 다양성을 설명하기 위한 모델이 될 수 있다는 연구가 있어 눈길을 끈다.

한 연구팀은 동물의 장내에 서식하는 대장균 중 서로 다른 세 집단 간의 증식 경쟁에서 가위바위보의 관계를 관찰했다. ‘집단 C’는 콜리신이라는 독소를 생산하고, ‘집단 S’는 다른 집단에 비해 빠른 속도로 증식하지만 콜리신에 의해 증식이 억제된다. ‘집단 R’은 ‘집단 C’보다 빠르고 ‘집단 S’보다 느린 증식 속도를 가진 반면 콜리신에 저항성을 지닌다. 세 집단 중 두 집단씩을 각각 섞어 배양하면 증식 속도의 차이로 인해 집단 간 증식 경쟁에 따른 승패가 확실하다. 반면 세 집단을 서로 인접시켜 배양하면, 각 두 집단 간의 경계에서는 일방적으로 영역을 침범하는 현상이 나타나지만, 결과적으로 가위바위보의 관계처럼 서로 물고 물리는 삼자 간의 공존 관계가 관찰된다.

[A]

다른 연구팀은 생쥐들의 장내에 세 대장균 집단을 투여한 후 각 집단 간의 증식 경쟁을 살폈다. 그 결과 한 시점에는 생쥐 개체별로 어느 한 집단이 우세했지만, 시간이 지나면서 우세한 집단이 일정한 순서로 계속 바뀌는 것을 발견했다. 이는 서로 격리된 여러 공간에서 세 집단이 동시에 우세 집단으로 존재할 수 있음을 의미하기도 한다.

위 사례는 생태계에서 절대 강자가 없을 수도 있음을 보여 주는 좋은 본보기로 거론된다. 생물 간 경쟁을 설명하는 방식 중 승패가 명확한 양자 간의 관계에 비해, 삼자의 병존 가능성을 보여 주는 가위바위보의 관계는 생물 다양성의 설명에 보다 적합한 모델이 될 수 있다.
```

### 발문

```text
[A]의 내용을 &lt;보기&gt;와 같이 그렸을 때, ㉠～㉢과 ⓐ, ⓑ에 들어갈 내용이 바르게 짝지어진 것은? [3점]

&lt; 보 기 &gt;

✽ 그리는 방법 : 두 집단 간의 관계를 ‘강자’ → ‘약자’로 표시하고, 화살표에 강자의 강점을 표기

화살표의 방향 설정

강점

집단
```

### 선지

```json
[
  "모두 시계 방향\n\n㉠ : 콜리신 생산\n\nⓑ :집단 R",
  "모두 시계 방향\n\n㉠ : 증식 속도\n\nⓐ :집단 C",
  "모두 시계 방향\n\n㉡ : 저항성 및 증식 속도\n\nⓐ :집단 R",
  "모두 반시계 방향\n\n㉡ : 콜리신 생산\n\nⓑ :집단 C",
  "모두 반시계 방향\n\n㉢ : 증식 속도\n\nⓐ :집단 C"
]
```

### 원문 자료 감사

```json
{
  "case_id": "GN",
  "source_file_exists": true,
  "mechanically_linked": true,
  "assets": [
    {
      "path": "data/기본기_연구/prepared_backlog/blind_sources/GN.json",
      "exists": true,
      "kind": "supplement_or_source"
    },
    {
      "path": "data/기본기_연구/prepared_backlog/blind_sources/GN_graph_figure.png",
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

### 최초 blind 풀이 — `GN-blind-20260915-01`

**선택 답**

`1`

**확신도**

```text
높음
```

**필요 정보와 위치**

```json
[
  "2문단 C의 콜리신 생산/S의 콜리신 취약/R의 저항성과 중간 증식",
  "복원 그림 직접 판독:상단S,좌하ⓐ,우하ⓑ;왼간선㉠,아랫간선㉡,오른간선㉢;강자→약자 및 강점 표기"
]
```

**코드명 없는 최소 논리 구조**

```text
C→S는 콜리신 생산, S→R은 빠른 증식, R→C는 저항성과 빠른 증식이다. 모두 시계 방향이면 상단S→우하R→좌하C→상단S이므로ⓑR이며㉠콜리신 생산이다. 따라서①이다.
```

**중간 추론**

```json
[
  "시계 방향 배치에서㉡은 R→C로 저항성 및 증식 속도,㉢은 S→R로 증식 속도다.",
  "②는 시계 방향ⓐC까지 맞지만㉠의 강점이 증식 속도가 아니다.",
  "③은㉡ 강점은 맞지만 시계 방향ⓐ는R이 아니라C다.",
  "반시계 방향이면S→좌하R→우하C→S이고㉡은R→C이므로④의 콜리신 생산이 틀리다.",
  "⑤반시계에서는ⓐR이며㉢은C→S의 콜리신 생산이므로 둘 다 틀리다."
]
```

**가장 매력적인 오답**

`3`

**오답의 정확한 오류**

```text
㉡의 강점만 맞춰 선택하면 같은 순환 방향에서 정해지는ⓐ 집단을 놓친다. 두 표기를 동시에 만족해야 한다.
```

**노출 정보**

```json
{
  "official_answer_seen": false,
  "sdss_seen": false,
  "prior_project_judgment_seen": false,
  "same_group_passage_seen": true,
  "prior_training_exposure": "확인 불가",
  "source_identity": "그림 복원 보고는 공식 문제 PDF12쪽;시험 식별 정보는 주 Astra에 아직 미공개"
}
```

**기타 기록 필드**

```json
{
  "passage_group": "G040",
  "source": [
    "data/기본기_연구/prepared_backlog/blind_sources/GN.json",
    "data/기본기_연구/prepared_backlog/blind_sources/GN_graph_figure.png"
  ],
  "source_quality": "GN 그래프 누락은 복원 그림의 주 Astra 직접 판독으로 해소. [A]의 정확 범위는 별도 확인 대기이며 해당 생태 관계는 지문2문단에 명시되어 답에 영향 없음.원문 전체 정본 대조 성과로 확대하지 않는다.",
  "original_hold_preserved": true
}
```

## 2. 공식 정답 대조

### 공식 정답 대조 — `GN-answer_check-20260915-01`

**공식 정답**

`1`

**일치 여부**

`true`

**기타 기록 필드**

```json
{
  "passage_group": "G040",
  "group_blind_barrier_verified": true,
  "blind_selected_answer": 1,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "C→S→R→C의 상대 우세를 그림 위치에 대응한다. 시계 방향이면ⓐC·ⓑR이고㉠콜리신 생산이다.",
  "sdss_disclosed": false,
  "qualification": "GN 그림 직접 판독 완료, [A] 정확 범위 확인 대기. GO②의 조건부 해석을 무조건 다양성 보장으로 강화하지 않음.",
  "quota_status": "unavailable"
}
```

## 3. 독립 코드 판정

### 독립 코드 판정 — `GN-independent_code-20260915-01`

**주 코드**

```json
[
  {
    "code": 39,
    "name": "비교대상",
    "scope": "세 비교 쌍의 우세 관계와 선택지 동시 대응",
    "reason": "C/S, S/R, R/C의 서로 다른 비교 상대와 강점을 보존해야 한다. 독소 생산 또는 빠른 증식이라는 한 속성을 절대 우세로 바꾸면 순환을 놓친다."
  }
]
```

**보조 코드**

```json
[
  {
    "code": 46,
    "name": "인과관계",
    "scope": "각 간선의 강점 복원",
    "reason": "C가 S를 억제하는 원인과 R이 C를 이기는 저항성·증식 속도 조합을 구별한다."
  },
  {
    "code": 17,
    "name": "대상범주",
    "scope": "그림ⓐⓑ 및㉠~㉢ 귀속",
    "reason": "상대 우세 내용을 그림의 지정 위치에 일관되게 옮긴다. #39와 대상 대응 부분이 겹치므로 독립 행동으로 중복 계수하지 않는다."
  }
]
```

**표면 코드**

```json
[
  {
    "code": 9,
    "name": "위계",
    "reason": "강자/약자라는 표현은 있으나 모든 쌍에 통용되는 단일 서열이 아니다."
  }
]
```

**경쟁 코드 및 반증**

```json
[
  {
    "code": 45,
    "verdict": "비교 상대를 입력,승자를 출력으로 재기술 가능하여 국소 중첩한다. 다만 입력 변화의 출력 합성보다는 이미 제시한 쌍별 관계를 위치에 옮기는 과제가 직접적이다. #39와 유일 주 경계는 확정하지 않는다."
  },
  {
    "code": 49,
    "verdict": "증식 속도만의 증감 방향으로는 C가 S에 우세함을 설명하지 못한다. 콜리신 취약/저항성이 비교 쌍마다 다르다."
  },
  {
    "code": 90,
    "verdict": "가능한 배치를 열거할 수 있어도 조합 총수를 산출할 필요는 없다. 상단 S와 회전 방향으로 두 빈칸이 직접 결정된다."
  },
  {
    "code": 43,
    "verdict": "실험 비교 소재지만 다른 변수 통제 여부를 따져 인과 효과를 식별하는 판단은 요구하지 않는다."
  }
]
```

**확신도**

```text
관계·오류 위치 높음;유일 주 번호 우선순위 유보
```

**경계 메모**

```text
#39/#17/#45는 대상·관계·대응 표현의 국소 중첩이다. 비교 쌍 보존을 작업 대표로 택하되 번호 전체 분리 근거로 사용하지 않는다.
```

**정규화된 주 코드 후보**

```json
[
  {
    "source_key": "primary",
    "value": [
      {
        "code": 39,
        "name": "비교대상",
        "scope": "세 비교 쌍의 우세 관계와 선택지 동시 대응",
        "reason": "C/S, S/R, R/C의 서로 다른 비교 상대와 강점을 보존해야 한다. 독소 생산 또는 빠른 증식이라는 한 속성을 절대 우세로 바꾸면 순환을 놓친다."
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
        "code": 46,
        "name": "인과관계",
        "scope": "각 간선의 강점 복원",
        "reason": "C가 S를 억제하는 원인과 R이 C를 이기는 저항성·증식 속도 조합을 구별한다."
      },
      {
        "code": 17,
        "name": "대상범주",
        "scope": "그림ⓐⓑ 및㉠~㉢ 귀속",
        "reason": "상대 우세 내용을 그림의 지정 위치에 일관되게 옮긴다. #39와 대상 대응 부분이 겹치므로 독립 행동으로 중복 계수하지 않는다."
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
        "code": 45,
        "verdict": "비교 상대를 입력,승자를 출력으로 재기술 가능하여 국소 중첩한다. 다만 입력 변화의 출력 합성보다는 이미 제시한 쌍별 관계를 위치에 옮기는 과제가 직접적이다. #39와 유일 주 경계는 확정하지 않는다."
      },
      {
        "code": 49,
        "verdict": "증식 속도만의 증감 방향으로는 C가 S에 우세함을 설명하지 못한다. 콜리신 취약/저항성이 비교 쌍마다 다르다."
      },
      {
        "code": 90,
        "verdict": "가능한 배치를 열거할 수 있어도 조합 총수를 산출할 필요는 없다. 상단 S와 회전 방향으로 두 빈칸이 직접 결정된다."
      },
      {
        "code": 43,
        "verdict": "실험 비교 소재지만 다른 변수 통제 여부를 따져 인과 효과를 식별하는 판단은 요구하지 않는다."
      }
    ]
  }
]
```

**기타 기록 필드**

```json
{
  "passage_group": "G040",
  "logic_without_codes": "비교 쌍마다 승자와 승리 이유를 정하고, 방향이 있는 삼각형에 집단과 강점의 위치를 일관되게 배치한다.",
  "falsification_attempt": "증식 속도 S>R>C만으로 선형 서열을 만들면 C→S 간선이 반례다. 반대로 콜리신만으로 C를 절대 강자로 삼으면 R→C가 반례다. 두 실제 원문 관계가 단일 속성 비교의 충분성을 기각한다.",
  "sdss_disclosed": false
}
```

## 4. SDSS 사후 대조

> SDSS는 독립 판정 후 공개된 제3자 후보 라벨이다. 이 기록은 독립 판정의 근거로 소급 사용하지 않는다.

### SDSS 사후 대조 — `GN-sdss_compare-20260915-01`

**사이트 원래 코드**

```json
[]
```

**독립 주 코드**

```json
[
  39
]
```

**기타 기록 필드**

```json
{
  "passage_group": "G040",
  "group_independent_barrier_verified": true,
  "candidate_id": null,
  "comparison_status": "prepared_index_unlinked",
  "meaning_comparison": "준비 색인에 연결이 없으므로 실제 사이트 무코드 판정이나 독립 판정과의 불일치로 처리하지 않는다.",
  "revision_required": false,
  "unresolved": "사이트 실제 수록·태그·적용 범위 미확인",
  "source_quality_update": "GN [A]는 보조원이 공식 문제 PDF에서 둘째 문단 전체라고 복원했다. 주 Astra는 supplement를 확인했으며 원 PDF 괄호 직접 판독 성과와 구별한다."
}
```

## 5. 후속 보강

이 case에 명시적으로 연결된 depth_backfill 또는 case-specific boundary_revision 기록이 없습니다.

### 명시적으로 연결된 집단 기록 참조

- `META-G039-G041-meta_induction-20260915-01` — 교차 사례 귀납 기록 (집단/교차 사례 기록; 개별 case 판단으로 변환하지 않음)

## 6. 원장 추적

사용된 원장 record_id (queue 순서):
- `GN-hold-20260915-missing-figure-01` — hold / hold
- `GN-blind-20260915-01` — 최초 blind 풀이 / done
- `GN-answer_check-20260915-01` — 공식 정답 대조 / done
- `GN-independent_code-20260915-01` — 독립 코드 판정 / done
- `GN-sdss_compare-20260915-01` — SDSS 사후 대조 / done
- `META-G039-G041-meta_induction-20260915-01` — 교차 사례 귀납 기록 / done
