> 이 파일은 원장으로부터 자동 생성된 열람용 파생본이다. 연구의 authoritative source는 raw queue이며, 이 파일을 직접 편집하지 않는다.

# EO

## 0. 문항 정보

- **Passage group:** G029

### 제시문

```text
문장이나 영상, 음성을 만들어 내는 인공 지능 생성 모델 중 확산 모델은 영상의 복원, 생성 및 변환에 뛰어난 성능을 보인다. 확산 모델의 기본 발상은, 원본 이미지에 노이즈를 점진적으로 추가하였다가 그 노이즈를 다시 제거해 나가면 원본 이미지를 복원할 수 있다는 것이다. 노이즈는 불필요하거나 원하지 않는 값을 의미한다. 원하는 값만 들어 있는 원본 이미지에 노이즈를 단계별로 더하면 노이즈가 포함된 확산 이미지가 되고, 여러 단계를 거치면 결국 원본 이미지가 어떤 이미지였는지 전혀 알아볼 수 없는 노이즈 이미지가 된다. 역으로, 단계별로 더해진 노이즈를 알 수 있다면 노이즈 이미지에서 원본 이미지를 복원할 수 있다. 확산 모델은 노이즈 생성기, 이미지 연산기, 노이즈 예측기로 구성되며, 순확산 과정과 역확산 과정 순으로 작동한다.

순확산 과정은 이미지에 노이즈를 추가하면서 노이즈 예측기를 학습시키는 과정이다. 첫 단계에서는, 노이즈 생성기에서 노이즈를 만든 후 이미지 연산기가 이 노이즈를 원본 이미지에 더해서 노이즈가 포함된 확산 이미지를 출력한다. 다음 단계부터는 노이즈 생성기에서 만든 노이즈를 이전 단계에서 출력된 확산 이미지에 더한다. 이러한 단계를 충분히 반복하면 최종적으로 노이즈 이미지가 출력된다. 이때 더해지는 노이즈는 크기나 분포 양상 등 그 특성이 단계별로 다르다. 따라서 노이즈 예측기는 단계별로 확산 이미지를 입력받아 이미지에 포함된 노이즈의 특성을 추출하여 수치들로 표현하고, 이 수치들을 바탕으로 노이즈를 예측한다. 노이즈 예측기 내부의 이러한 수치들을 잠재 표현이라고 한다. 노이즈 예측기는 잠재 표현을 구하고 노이즈를 예측하는 방식을 학습한다.

노이즈 예측기의 학습 방법은 기계 학습 중에서 지도 학습에 해당한다. 지도 학습은 학습 데이터에 정답이 주어져 출력과 정답의 차이가 작아지도록 모델을 학습시키는 방법이다. 노이즈 예측기를 학습시킬 때는 노이즈 생성기에서 만들어 넣어 준 노이즈가 정답에 해당하며 이 노이즈와 예측된 노이즈 사이의 차이가 작아지도록 학습시킨다.

역확산 과정은 노이즈 이미지에서 노이즈를 제거하여 원본 이미지를 복원하는 과정이다. 노이즈를 제거하려면 이미지에 단계별로 어떤 특성의 노이즈가 더해졌는지 알아야 하는데 노이즈 예측기가 이 역할을 한다. 노이즈 이미지 또는 중간 단계에서의 확산 이미지를 노이즈 예측기에 입력하면 이미지에 포함된 노이즈의 특성을 추출하여 잠재 표현을 구하고 이를 바탕으로 노이즈를 예측한다. 이미지 연산기는 입력된 확산 이미지로부터 이 노이즈를 빼서 현 단계의 노이즈를 제거한 확산 이미지를 출력한다. 확산 이미지에 이런 단계를 반복하면 결국 노이즈가 대부분 제거되어 원본 이미지에 가까운 이미지만 남게 된다.

한편, 많은 종류의 이미지를 학습시킨 후 학습된 이미지의 잠재 표현에 고유 번호를 붙이면 역확산 과정에서 이미지를 선택하여 생성할 수 있다. 또한 잠재 표현의 수치들을 조정하면 다른 특성의 노이즈가 생성되어 여러 이미지를 혼합하거나 실재하지 않는 이미지를 만들어 낼 수도 있다.
```

### 발문

```text
잠재 표현에 대한 설명으로 적절하지 않은 것은?
```

### 선지

```json
[
  "잠재 표현의 수치들을 조정하면 여러 이미지를 혼합할 수 있다.",
  "역확산 과정에서 잠재 표현이 다르면 예측되는 노이즈가 다르다.",
  "확산 모델의 학습에는 잠재 표현을 구하는 방식이 포함되어 있다.",
  "잠재 표현은 이미지에 더해진 노이즈의 크기나 분포 양상에 따라 다른 값들이 얻어진다.",
  "잠재 표현은 노이즈 예측기가 원본 이미지를 입력받아 노이즈의 특성을 추출한 결과이다."
]
```

### 원문 자료 감사

```json
{
  "case_id": "EO",
  "source_file_exists": true,
  "mechanically_linked": true,
  "assets": [],
  "image_files_exist": true,
  "image_meaning_verified": false,
  "choice_count": 5,
  "all_choices_empty": false,
  "warnings": [],
  "ready": true
}
```

## 1. 최초 blind 풀이

### 최초 blind 풀이 — `EO-blind-20260913-02`

**선택 답**

`5`

**확신도**

```text
높음
```

**필요 정보와 위치**

```json
[
  "2문단 예측기는 확산 이미지를 입력받아 노이즈 특성 수치 표현을 구함",
  "4문단 노이즈 이미지 또는 중간 확산 이미지 입력",
  "5문단 잠재 표현 조정으로 다른 특성 노이즈 및 이미지 혼합 가능"
]
```

**코드명 없는 최소 논리 구조**

```text
잠재 표현을 구하는 예측기의 입력은 노이즈가 포함된 이미지이다.⑤는 이를 원본 이미지로 바꾸었다. 원본 이미지에는 원하는 값만 들어 있으므로 주어진 절차의 노이즈 특성 추출 입력과 다르다.
```

**중간 추론**

```json
[
  "① 마지막 문단의 수치 조정과 이미지 혼합에 명시 대응",
  "② 잠재 표현을 바탕으로 노이즈를 예측하고 수치 조정 시 다른 특성 노이즈가 만들어진다는 설명에 대응",
  "③ 잠재 표현을 구하는 방식과 노이즈 예측 방식을 학습한다고 명시",
  "④ 노이즈 특성을 추출한 수치 표현이므로 특성에 따라 수치가 달라짐",
  "⑤ 이미지 종류를 원본으로 교체하여 입력 대상을 잘못 배정"
]
```

**가장 매력적인 오답**

`2`

**오답의 정확한 오류**

```text
일반 함수에서 다른 입력이 반드시 다른 출력은 아니라는 외부 논리를 기계적으로 적용하면②를 의심할 수 있다. 그러나 본문은 잠재 표현 수치 조정 시 다른 특성 노이즈가 생성된다고 명시한다. 이 문항에서는 본문의 설정 범위에서 읽는다.
```

**노출 정보**

```json
{
  "official_answer_seen": false,
  "sdss_seen": false,
  "prior_project_judgment_seen": false,
  "same_group_blind_passage_seen": true,
  "prior_training_exposure": "확인 불가"
}
```

**기타 기록 필드**

```json
{
  "passage_group": "G029"
}
```

## 2. 공식 정답 대조

### 공식 정답 대조 — `EO-answer_check-20260913-02`

**최초 선택**

`5`

**공식 정답**

`5`

**기타 기록 필드**

```json
{
  "passage_group": "G029",
  "group_blind_barrier_verified": true,
  "is_correct": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "잠재 표현을 구하는 예측기의 입력은 노이즈가 포함된 확산/노이즈 이미지이며 원하는 값만 있는 원본 이미지가 아니다.⑤의 입력 종류 교체가 오류이다.",
  "revision_after_answer": "없음",
  "sdss_seen": false
}
```

## 3. 독립 코드 판정

### 독립 코드 판정 — `EO-independent_code-20260913-02`

**주 코드**

```json
[
  {
    "code": 45,
    "name": "함수",
    "reason": "이미지 입력→노이즈 특성 추출→잠재 표현이라는 대응을 복원하고 첫 입력 항의 교체를 검출한다."
  }
]
```

**보조 코드**

```json
[
  {
    "code": 17,
    "name": "대상범주",
    "reason": "원본은 원하는 값만 있고 확산/노이즈 이미지는 노이즈를 포함한다는 입력 유형 차이가 검출 근거다. 추상적 입력 연결만 그려서는⑤의 종류 교체를 판단할 수 없다."
  }
]
```

**표면 코드**

```json
[
  {
    "code": 16,
    "name": "개념분석",
    "reason": "잠재 표현 정의가 문제의 소재이나 필요충분 정의 성분을 새로 조합하는 것이 아니라 생성 경로의 잘못된 입력을 찾는다."
  }
]
```

**경쟁 코드 및 반증**

```json
[
  {
    "code": 17,
    "verdict": "필수 보조",
    "falsification": "원본과 확산 이미지가 다르다는 것만으로 모든 입력 교체가 오류는 아니다. 예측기가 실제 어느 유형을 입력받는지 작동 연결을 알아야⑤를 배제한다."
  },
  {
    "code": 16,
    "verdict": "표면",
    "falsification": "잠재 표현은 수치들이라는 정의만 맞춰도⑤의 입력 원본 이미지 오류는 남는다. 그 수치가 어디서 추출되는지 경로 복원이 필요하다."
  },
  {
    "code": 49,
    "verdict": "주 코드 배제",
    "falsification": "수치를 조정해 다른 노이즈를 만든다는②·① 검토는 있지만 두 양의 증가·감소 상관을 판단하지 않는다."
  },
  {
    "code": 10,
    "verdict": "주 코드 배제",
    "falsification": "노이즈를 추출하려면 노이즈 포함 입력이 필요하다고 말할 수 있으나 결정 근거는 구체 입력의 명시 배정이다. 모든 입력 관계를 필요조건으로 재분류할 추가 근거가 없다."
  }
]
```

**확신도**

```text
높음
```

**경계 메모**

```text
EN은 과정별 요소 참여, EO는 특정 처리의 입력 종류 확인으로 같은#45 군 안의 수행 하위형이 다르다. #17과의 결합을 보존하며 번호 하나로 입력의 물성을 삭제하지 않는다.
```

**정규화된 주 코드 후보**

```json
[
  {
    "source_key": "primary",
    "value": [
      {
        "code": 45,
        "name": "함수",
        "reason": "이미지 입력→노이즈 특성 추출→잠재 표현이라는 대응을 복원하고 첫 입력 항의 교체를 검출한다."
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
        "code": 17,
        "name": "대상범주",
        "reason": "원본은 원하는 값만 있고 확산/노이즈 이미지는 노이즈를 포함한다는 입력 유형 차이가 검출 근거다. 추상적 입력 연결만 그려서는⑤의 종류 교체를 판단할 수 없다."
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
        "code": 17,
        "verdict": "필수 보조",
        "falsification": "원본과 확산 이미지가 다르다는 것만으로 모든 입력 교체가 오류는 아니다. 예측기가 실제 어느 유형을 입력받는지 작동 연결을 알아야⑤를 배제한다."
      },
      {
        "code": 16,
        "verdict": "표면",
        "falsification": "잠재 표현은 수치들이라는 정의만 맞춰도⑤의 입력 원본 이미지 오류는 남는다. 그 수치가 어디서 추출되는지 경로 복원이 필요하다."
      },
      {
        "code": 49,
        "verdict": "주 코드 배제",
        "falsification": "수치를 조정해 다른 노이즈를 만든다는②·① 검토는 있지만 두 양의 증가·감소 상관을 판단하지 않는다."
      },
      {
        "code": 10,
        "verdict": "주 코드 배제",
        "falsification": "노이즈를 추출하려면 노이즈 포함 입력이 필요하다고 말할 수 있으나 결정 근거는 구체 입력의 명시 배정이다. 모든 입력 관계를 필요조건으로 재분류할 추가 근거가 없다."
      }
    ]
  }
]
```

**기타 기록 필드**

```json
{
  "passage_group": "G029",
  "sdss_seen": false,
  "logic_without_codes_fixed": "노이즈 예측기는 노이즈가 포함된 이미지에서 특성을 추출하여 잠재 표현을 구한다.⑤가 원본 이미지를 그 입력으로 지정한 것은 절차에서 입력 종류를 잘못 배정한 것이다."
}
```

## 4. SDSS 사후 대조

> SDSS는 독립 판정 후 공개된 제3자 후보 라벨이다. 이 기록은 독립 판정의 근거로 소급 사용하지 않는다.

### SDSS 사후 대조 — `EO-sdss_compare-20260913-02`

**사이트 원래 코드**

```json
[
  "함수"
]
```

**의미 비교**

```text
사이트#45와 독립#45가 일치한다. 이 문항은 노이즈 특성 추출의 입력이 원본인지 확산 이미지인지 확인하며#17 입력 유형 구별이 필수 보조다.
```

**독립 판정 보존**

`true`

**기타 기록 필드**

```json
{
  "passage_group": "G029",
  "group_independent_barrier_verified": true,
  "site_original_code_numbers": [
    45
  ],
  "comparison_result": "주 코드 일치",
  "revision_after_disclosure": "주/보조/표면 최초 판정 변경 없음",
  "unresolved": "다른 잠재 표현 수치가 다른 예측값이라는 본문 설정을 일반 수학 함수의 일대일성으로 확대하지 않음."
}
```

## 5. 후속 보강

아래 기록은 시간순으로 덧붙였다. 최초 blind·정답·독립 코드 판정을 대체하지 않는다.

### 경계 수정 기록 — `DZ-EO-EP-boundary_revision-20260913-02`

**기타 기록 필드**

```json
{
  "case_ids": [
    "DZ",
    "EO",
    "EP"
  ],
  "review_kind": "SDSS 공개 이후 사례 간 반례 검토; 새 독립 최초 판정 아님",
  "official_sources_directly_read": [
    "data/기본기_연구/prepared_backlog/blind_sources/DZ.json",
    "data/기본기_연구/prepared_backlog/blind_sources/EO.json",
    "data/기본기_연구/prepared_backlog/blind_sources/EP.json"
  ],
  "existing_rule": "G025-G026 boundary_revision에서 과정 소재만으로#45를 주 코드로 올리지 않으며 DZ는 주체/술어 귀속#17로 판단했다.",
  "counterexample": "EO를 입력 관계가 있다는 이유만으로#45 우위라고 하면 DZ의 개시제→분해→불안정이라는 관계에도 같은 이유가 적용되어 기존#17과의 배타적 우선순위가 무너진다. EO⑤는 원본을 노이즈 포함 이미지로 고치는 단일 역할 귀속으로 해결되며 여러 연결 합성이 필수는 아니다.",
  "refinements": [
    {
      "boundary": "#17/#45",
      "finding": "특정 입력 칸에 어느 대상을 배정하는가를 판단하는 EO는 대상 귀속과 입력 관계 확인이라는 두 설명이 같은 국소 행동을 가리킨다. 단일 입력 관계라는 이유만으로#45의 고유 우위를 확정하지 않는다.",
      "revised_case": "EO",
      "original_primary": [
        45
      ],
      "original_auxiliary": [
        17
      ],
      "revised_primary_candidates": [
        17,
        45
      ],
      "primary_priority_status": "유보. 공동 필수 관점이며 유일 주 코드 우선순위 신뢰도를 낮춤.",
      "original_judgment_preserved": true
    },
    {
      "boundary": "국소 역할 귀속/과정 조건별 연결 선택",
      "finding": "EP는 예측기가 두 과정 모두에 있지만 출력 전달의 목적지가 달라 과정 조건과 간선을 함께 봐야 한다. 대상 이름 수정 한 번으로 오류 유형을 모두 보존할 수 없어#45 주와#12/#17 보조를 유지한다."
    }
  ],
  "falsification_attempts": [
    "EO에서 예측기의 입력 대상을 직접 대응시키는 최소 풀이를 시도하여 전체 경로 합성 없이⑤ 배제를 확인했다.",
    "DZ를 함수적 사건 관계로 다시 표현할 수 있으므로 입력/출력 어휘 유무만으로 두 코드의 본질 경계를 세우는 시도를 기각했다.",
    "EP의 예측기 출현 사실은 참인데 전달 연결이 틀리므로 단순 주체 존재/부재 판정으로 환원하는 시도를 기각했다."
  ],
  "redivision_conditions": [
    "이미 알려진 입력 유형만 교체한 문항은#17/#45 국소 중첩으로 처리 가능",
    "동일 유형 입력에서도 단계 조건에 따라 공급자·수신자가 달라져 여러 연결 선택이 필요하면#45 우선 근거가 강해짐",
    "서로 다른 코드 번호나 사이트의#45 일치만으로 유일 주 우선순위를 정하지 않음"
  ],
  "generation_principles": [
    "단일 역할 칸 교체와 조건별 전달 연결 이동을 다른 오답 하위형으로 보존한다.",
    "최종 문항 코드 외에 최소 풀이에서 실제 사용한 관계 수와 조건 수를 기록해 과잉 과정 분류를 막는다."
  ],
  "confidence": {
    "counterexample": "높음",
    "EO_unique_primary": "유보",
    "global_code_identity": "미확정"
  },
  "source_exposure_note": "기존 DZ는 완료 사례 재검토. G030의 미완료 blind/답/코드/SDSS에는 진입하지 않음."
}
```

### 경계 수정 기록 — `DZ-EO-EP-EJ-boundary_revision-20260915-semantic-audit-01`

**기타 기록 필드**

```json
{
  "case_ids": [
    "DZ",
    "EO",
    "EP",
    "EJ"
  ],
  "original_blind_preserved": true,
  "review_kind": "완료 사례 사후 감사. 원문 직접 재독 후 강한 경쟁 표현 비교. 기존 판정 및 과거 revision 모두 불변",
  "source_record_ids": [
    "DZ-independent_code-20260913-01",
    "EO-independent_code-20260913-02",
    "EP-independent_code-20260913-02",
    "DZ-EO-EP-boundary_revision-20260913-02",
    "EJ-independent_code-20260913-02",
    "EJ-depth_backfill-20260913-03"
  ],
  "evidence_additions": [
    {
      "case": "DZ",
      "passage_group": "G026",
      "source": "data/기본기_연구/prepared_backlog/blind_sources/DZ.json",
      "task": "알 수 있는 내용 중 부적절 선지 선택",
      "target": "④의 주체·분해 결과·안정 상태를 포함한 전체 문장",
      "evidence_location": "3문단 에틸렌 결합 구성, 4문단 '열을 흡수한 과산화물 개시제는 ... 불안정한 ... 분자로 분해된다' 및 뒤 연쇄 반응; choices[3]",
      "relation_without_codes": "열 흡수 개시제→분해→불안정 원자 포함 분자; 그 원자가 에틸렌과 결합→다른 탄소에 홀전자→다음 반응. 사슬 끝끼리 결합하면 안정화·종료.",
      "changed_part": "개시제의 분해를 에틸렌에 붙이고, 중간 단계 불안정화를 분해에 의한 안정화로 바꿈",
      "decisive_operation": "주체·단계·결과가 함께 적힌 사건표와④를 비교. 주체 한 칸만 고쳐도 전체 문장이 맞아지는 것은 아님",
      "evidence_type": "합성 함의",
      "evidence_qualification": "개시제 분해 후 불안정은 직접 명시. 에틸렌이라는 단어가 있거나 일부 결합이 끊어진다는 사실만으로 '분해되면서 안정'을 허용하지 않음",
      "existing_code_layers": "주#17 사건 귀속, 보조#3 단계·#5 상태 변화, 표면#45 과정. 원기록 유지",
      "strongest_competitor": "단계별 함수형 표: 입력=열 흡수 개시제/에틸렌, 처리=분해/결합, 출력=불안정 원자/새 사슬 끝. #45로 이 표를 쓰면#17 사건 귀속과 같은 오류를 검출한다. #46의 인과 경로도 정확한 주체·상태를 포함하면 반박 가능하다.",
      "competitor_relation": "입출력/사건표는 같은 국소 수행의 다른 표현. 전체 중합의 모든 연결을 합성하는 추가 수행은 정답에 필수 아님",
      "priority": "#17 대표 유지; 함수식으로 표현 가능하다는 이유만으로#45 주로 변경하거나#45 설명을 배제하지 않음"
    },
    {
      "case": "EO",
      "passage_group": "G029",
      "source": "data/기본기_연구/prepared_backlog/blind_sources/EO.json",
      "task": "잠재 표현 설명 중 부적절 선지 선택",
      "target": "⑤ 입력 대상 절",
      "evidence_location": "1문단 원본=원하는 값만, 2문단 예측기는 단계별 확산 이미지 입력→노이즈 특성의 수치화; 4문단 역확산 입력; choices[4]",
      "relation_without_codes": "노이즈 포함 이미지→예측기→노이즈 특성 수치(잠재 표현)",
      "changed_part": "예측기의 입력을 노이즈 포함 이미지에서 원본 이미지로 교체",
      "decisive_operation": "입력 역할 한 칸을 원문과 대응",
      "evidence_type": "직접 함의",
      "existing_code_layers": "최초 주#45/보조#17/표면#16, 후속#17·#45 우선순위 유보를 보존",
      "strongest_competitor": "#17 표에 대상=예측기, 역할=입력, 값=노이즈 포함 이미지를 적으면 충분. #16도 '잠재 표현=예측기가 노이즈 포함 이미지에서 추출한 특성의 수치'라는 생성 출처 포함 정의로 구성하면 같은 판단. '수치이다'만 적은 약한 정의를 반증 대상으로 삼지 않음",
      "competitor_relation": "같은 국소 수행의 다른 표현. 정의에 출처를 포함하는 표현이#16 원저자 범위인지 여부는 미결",
      "priority": "#17/#45 유일 우선순위 유보 유지. #16의 약한 정의만 기각한 과거 논증은 강한 대안 배제 근거로 불충분; 새 주 번호 확정 없음"
    },
    {
      "case": "EP",
      "passage_group": "G029",
      "source": "data/기본기_연구/prepared_backlog/blind_sources/EP.json",
      "task": "보기의 단계 이해 중 부적절 선지 선택",
      "target": "③ 순확산 조건 아래 예측 노이즈→이미지 연산기 연결",
      "evidence_location": "2문단 생성기가 만든 노이즈를 연산기가 더함, 3문단 예측값은 정답 노이즈와 학습 비교, 4문단 예측 노이즈를 연산기가 뺌; choices[2], choices[4]",
      "relation_without_codes": "순확산: 연산기 노이즈 입력=생성값, 학습 비교=예측값 대 생성값. 역확산: 연산기 제거 입력=예측값",
      "changed_part": "순확산 조건에 역확산의 공급 연결을 이식",
      "decisive_operation": "과정 조건을 선택한 뒤 그 과정의 공급자·값·수신자 대응을 확인",
      "evidence_type": "합성 함의",
      "evidence_qualification": "원문이 설명하는 장치 연결과 용도 안에서③을 기각. '문장에 안 나왔다'만으로 현실의 모든 부가 연결이 불가능하다고 주장하지 않음",
      "existing_code_layers": "최초 주#45=전달 연결, 보조#12=과정 조건·#17=공급값 귀속, 표면#92=더하기/빼기. 기존 판정 보존",
      "strongest_competitor": "완전한 조건부 귀속표: (순확산, 연산기 노이즈 입력, 생성기 생성값), (순확산, 학습 비교, 예측값/생성값), (역확산, 연산기 제거 입력, 예측기 예측값). ③의 삼항/사항 튜플을 첫 행과 대조하면 전체 경로 합성 없이 같은 오류를 찾는다. 조건문도 순확산이면 공급자는 생성기라는 구체 결과까지 포함하면 충분하다.",
      "competitor_relation": "과정 조건을 포함한 귀속표와 경로표는 같은 국소 수행의 다른 표현. 과정 없는 대상표에 비해 조건 선택은 별개의 추가 수행이지만, 그것이#45에만 속한다는 근거는 없음",
      "priority": "사후 current_primary_candidates=[12,17,45], 유일 우선순위 유보. 원 최초#45를 소급 수정하지 않음",
      "counterexample_to_prior_boundary": "20260913 revision의 'EP는 대상 이름 수정 한 번으로 모두 보존 불가'는 맞아도 강한 귀속표로 환원 불가를 뜻하지 않는다. 표에 과정 열을 추가하면 정보 손실 없이 판단 가능. EP에서 여러 간선 합성이 반드시 필요하다는 강화된 주장에 반례"
    },
    {
      "case": "EJ",
      "passage_group": "G028",
      "source": "data/기본기_연구/prepared_backlog/blind_sources/EJ.json",
      "task": "㉠ 박은식/㉡ 천두슈 이해 중 가장 적절한 선지 선택",
      "target": "정답② 두 절과 매력적 오답③의 박은식 절·④의 천두슈 절",
      "evidence_location": "(가)4문단 서양 준거/민족 주체성 대조 및 박은식 과학 연구 시급·유학 혁신; (나)3문단 철학의 과학 방법 요구·전쟁은 이용의 죄악; choices[1:4]",
      "relation_without_codes": "박은식: 과학 수용과 자국 철학 재구성 지지. 천두슈: 철학의 과학 방법 이용 지지, 과학 오용 책임 인정. 선지 끝 태도 술어가 두 절에 각각 걸림",
      "changed_part": "③ 시급성 인정에 부인을, ④ 오용 책임 인정에 비판을 붙임",
      "decisive_operation": "인물별 명제를 태도 방향까지 포함해 적고 각 선지의 두 절을 검증",
      "evidence_type": "합성 함의",
      "evidence_qualification": "③·④ 기각은 직접 명시된 견해/태도와 충돌. ② 박은식의 서양 주체 준거 반대는 자국 철학·주체 재구성 문맥에서 추론되며 같은 표현이 직접 인용된 것은 아님",
      "existing_code_layers": "최초 주#80/보조#75, 이후#75·#80 유일 우선순위 유보. 표면#39=두 대상, #33=② 천두슈 절의 국소 부정 방향",
      "strongest_competitor": "견해표의 셀을 '박은식은 과학 연구가 시급하다고 본다', '천두슈는 전쟁 책임을 과학 오용에 돌린다'처럼 완전 명제로 쓰면 별도 태도표 없이③·④가 기각된다. 주체-명제-태도 표와 진위 결과 동일",
      "competitor_relation": "#75/#80 같은 국소 수행의 다른 표현. #39 공통점 산출은 이 문항 필수가 아님. #33 단독으로 두 절의 실질 견해를 결정하는 설명은 배제",
      "priority": "기존 사후 유보 유지. 단순 지지/반대를 확인했다는 이유로 고유 인식 연산을 입증하지 않음"
    }
  ],
  "revised_rule": "O1 귀속에는 입력·사건·조건 인덱스를 포함할 수 있다. O4는 조건 선택/단일 연결 대조/복수 연결 합성을 분리한다. O6는 태도에 주의를 주는 O1의 특수 적용 후보이며 별개 능력으로 확정하지 않는다.",
  "decisions": {
    "유지": "조건과 태도 정보가 빠진 표로는 판단을 보존하지 못함",
    "수정": "EP의 경로표 우위를 조건부 귀속표와의 국소 동치/유일 우선순위 유보로 제한",
    "유보": "O1/O4/O6 독립성과#16/#17/#45/#75/#80 전역 포함 관계",
    "반례": "EP 완전 조건부 귀속표; DZ는 주어만 고쳐도 결과 오류가 남아 모든 문항의 단일 칸 수정 가설을 반박",
    "다음_falsification_target": "미열람 지문에서 두 연결을 실제로 합성해야만 드러나는 결과 또는 믿음/앎의 강도 차이가 필요한 사례를 선정하되 이번에는 열람하지 않음"
  },
  "minimal_variants": [
    {
      "case": "DZ",
      "one_change": "④ 첫 주체 '불안정한 원자를 가진 에틸렌'을 '과산화물 개시제'로만 교체",
      "predicted_change": "안정해진다는 결과 오류가 남아 문장 전체는 여전히 부적절. 완전 정문화가 아닌 단일 수정의 불충분성을 검사",
      "synthetic_not_corpus": true
    },
    {
      "case": "EO",
      "one_change": "⑤의 원본 이미지를 확산 이미지로 교체",
      "predicted_change": "입력 귀속 오류 해소",
      "synthetic_not_corpus": true
    },
    {
      "case": "EP",
      "one_change": "③의 순확산을 역확산으로 교체",
      "predicted_change": "확산 이미지 입력에서 예측 노이즈가 제거 연산기에 들어가는 연결이 적절해짐. 문항 전체 단일 정답 보장은 별도",
      "synthetic_not_corpus": true
    },
    {
      "case": "EJ",
      "one_change": "③ 박은식 절의 태도만 부인에서 인정으로 교체; 천두슈 절 부인은 유지",
      "predicted_change": "③ 박은식 절 오류가 해소. 원문 공통 종결 '부인'을 통째로 바꾸면 두 절을 바꾸므로 단일 변형이 아님. 의미상 한 절만 명시적으로 다시 쓰는 검토용 변형",
      "synthetic_not_corpus": true
    }
  ],
  "student_action": "누가/어느 과정에서/무엇을 입력·생성·인정하는지 필요한 열만 만든다. 대상 이름이 같아도 조건·태도가 다르면 별도로 비교하고, 이미 표에 담긴 확인을 두 번의 독립 수행으로 세지 않는다.",
  "generation_principle": "입력 대상, 과정 조건, 태도 하나를 이동한 선지를 설계한다. 여러 오류가 겹친 DZ형은 한 칸 수정으로 정답화된다고 가정하지 않는다.",
  "sampling": {
    "cases": 4,
    "distinct_passage_groups": 3,
    "EO_EP_same_passage": true,
    "new_corpus_cases": 0
  },
  "confidence": "국소 대안 구성 높음; 원저자 코드 정의와 전역 우선순위 미결"
}
```

### 경계 수정 기록 — `ANCHORS-O1-O8-boundary_revision-20260915-semantic-audit-01`

**기타 기록 필드**

```json
{
  "case_ids": [
    "DV",
    "GA",
    "DZ",
    "EO",
    "EP",
    "EJ",
    "AB",
    "BZ",
    "CT",
    "GC",
    "FH",
    "FN",
    "FT",
    "GJ",
    "ET",
    "FF",
    "FL",
    "FX",
    "EF",
    "FD",
    "EI"
  ],
  "original_blind_preserved": true,
  "review_kind": "지정 완료 anchor 사후 검토의 수행군 후보 종합.새 코드 체계/신규 blind 실험 아님",
  "source_record_ids": [
    "DV-GA-depth_backfill-20260915-semantic-audit-01",
    "DZ-EO-EP-EJ-boundary_revision-20260915-semantic-audit-01",
    "AB-BZ-CT-GC-depth_backfill-20260915-semantic-audit-01",
    "FH-FN-FT-GJ-ET-depth_backfill-20260915-semantic-audit-01",
    "FF-FL-depth_backfill-20260915-semantic-audit-01",
    "FX-EF-depth_backfill-20260915-semantic-audit-01",
    "FD-EI-depth_backfill-20260915-semantic-audit-01"
  ],
  "judgment_units": [
    "발문 과제/선택 방향",
    "원문·선지 관계",
    "실제 결정 수행",
    "선지 변경 위치",
    "증거 종류와 직접성",
    "기존 코드의 층·범위 및 유일 우선순위"
  ],
  "candidate_rules": [
    {
      "candidate": "O1 귀속 고정",
      "decision": "수정",
      "retained": "주체/역할/대상 대응을 명시",
      "revision": "과정·시점·태도를 인덱스로 포함한 강한 귀속표를 인정",
      "counterexample": "DZ 주체만 교체해도 상태 결과 오류가 남는다. O1이 언제나 한 단어 교체면 충분하다는 가설 기각",
      "held": "#17/#45 통합 및 O1의 독립성",
      "student_action": "누가 어느 단계에서 무엇을 하는지 필요한 열을 붙임",
      "generation_principle": "한 대상·역할을 이동하되 겹친 오류가 있으면 각각 표시",
      "next_falsification_target": "대상표의 모든 정보가 맞아도 두 단계 합성이 빠져 결론이 달라지는 새 지문",
      "minimal_variant_reference": "EO 입력 변경 및 아래 DZ 보완 probe"
    },
    {
      "candidate": "O2 변경 범위와 불변 요소",
      "decision": "수정",
      "retained": "변경·유지에 각각 원문 근거를 요구",
      "revision": "AB/CT 법적 특례, BZ 공정 단계, GC 하위 유형 일반 규칙을 별개 하위형으로 기록",
      "counterexample": "BZ는 원칙의 예외가 아니다.CT는 보존 외에 수량 합성이 필요",
      "held": "침묵이면 모든 속성 유지라는 규칙은 채택하지 않음;GC②",
      "student_action": "어느 값/권리/효과만 바뀌는지와 유지 근거를 표시",
      "generation_principle": "예외나 처리 범위를 인접 항목에 확장하는 오답",
      "next_falsification_target": "두 속성이 함께 바뀌거나 간접 효과로 보존이 깨지는 새 지문",
      "minimal_variant_reference": "AB 주체, BZ 단계, CT 분수, GC 의무 반전"
    },
    {
      "candidate": "O3 조건·강도·증거 방향",
      "decision": "수정",
      "retained": "P→Q와P∧¬Q의 충돌",
      "revision": "관계 형식/강도/증거를 별도 축으로 구분.DV는 명시된 가능한 반례,GA는 문맥에서 허용 상황 복원",
      "counterexample": "GA의 조건적 하자 책임 서술만으로 실제 계약 사례 존재를 논리적 도출했다고 말할 수 없음;근거 부재만으로 역조건 거짓 확정 불가",
      "held": "#10/#12/#36 전역 통합;가능/필연의 모든 하위 경계는 이번 표본으로 미검증",
      "student_action": "조건 방향을 적고 허용 반례인지 지지 부재인지 구분",
      "generation_principle": "효과를 성립 요건으로 전환하거나 경향을 무예외로 강화",
      "next_falsification_target": "역조건은 미도출되지만 명시 반례도 없는 새 지문",
      "minimal_variant_reference": "DV 존재 가능/GA 불일치 체결 가능으로 변경"
    },
    {
      "candidate": "O4 경로 합성과 조건별 연결",
      "decision": "수정",
      "retained": "과정 조건과 공급 연결 보존",
      "revision": "조건 선택,단일 연결 대조,복수 관계 합성,수량 계산을 별도로 적음.EP는 완전 조건부 귀속표로도 해결",
      "counterexample": "EP에 여러 간선의 합성이 필수라는 가설 실패.CT는 부족액 산출 후 지분 계산의 합성이 실제 필요",
      "held": "O1과O4 독립성;EP의#12/#17/#45 유일 우선순위",
      "student_action": "한 연결 확인으로 끝나는지 중간 산출값을 다음 관계에 넣어야 하는지 확인",
      "generation_principle": "과정 조건 이동과 중간값/분모 변경을 구분해 설계",
      "next_falsification_target": "단일 행 조회로는 풀리지 않고 두 연결 합성이 필요한 새 지문",
      "minimal_variant_reference": "EP 순확산→역확산, CT1/3→1/7"
    },
    {
      "candidate": "O5 기준·목적 적용",
      "decision": "유지 및 수정",
      "retained": "평가 출처와 독서 목적을 고정",
      "revision": "문장 자체 진위와 지정 기준에서의 적합성을 분리하되 외부 진실 확인을 의무 단계로 추가하지 않음.이유 문항의 근거 관계는 별도 기록",
      "counterexample": "FX③ 원 저술자 견해와 다르다는 이유로 배제하면 실패.EF3문단 전체를 기능 정보로 배제하면 위치 정보를 놓침.FL은 목적 판독만으로 이유가 결정되지 않음",
      "held": "#15/#44/#64/#75 전역 분리",
      "student_action": "지금 누가 무엇을 위해 평가하는지와 실제 표시 범위 확인",
      "generation_principle": "사실은 유지하고 기준/목적을 교체",
      "next_falsification_target": "두 목적 모두에 맞는 정보,명분 목적과 진위 교정이 병행되는 새 지문",
      "minimal_variant_reference": "FX③ 관점 변경, EF 외형→호흡 목적, FF 이유→위험"
    },
    {
      "candidate": "O6 발화·태도 귀속",
      "decision": "수정·독립성 유보",
      "retained": "긍정/부정 태도까지 명제에 결합",
      "revision": "EJ에서 태도 포함 견해표와 삼항표의 국소 동치 인정.O1 특수 적용 후보",
      "counterexample": "태도가 빠진 견해표 실패만으로#75 부족/ #80 독자성을 입증할 수 없음",
      "held": "O1/O6 독립성과#75/#80 전역 포함 관계",
      "student_action": "부인/반대/인정이 어느 절에 걸리는지 표시",
      "generation_principle": "내용은 두고 태도 한 절만 반전",
      "next_falsification_target": "찬반은 같지만 믿음/앎/추측 강도가 다른 미열람 사례",
      "minimal_variant_reference": "EJ③ 박은식 절 부인→인정;천두슈 절은 유지"
    },
    {
      "candidate": "O7 비교 결과 단위",
      "decision": "유지",
      "retained": "질문·답 내용·동의 명제를 구분",
      "revision": "교집합/비교표는 원소가 무엇인지 명시하면 같은 국소 풀이일 수 있음",
      "counterexample": "FD는 두 답 내용이 달라도 공통 질문 성립.EI는 방법 수용 공통성에서 인생관 적용 공통성까지 나오지 않음",
      "held": "#39/#64/#23/#75 배타 경계 및 양립 가능성 하위형의 외부 검증",
      "student_action": "무엇이 둘 다 있어야 하는지 표의 제목으로 씀",
      "generation_principle": "같은 질문 다른 답/대립 견해 속 좁은 공동 동의를 구분",
      "next_falsification_target": "양립은 가능하나 양쪽 동의는 없는 명제",
      "minimal_variant_reference": "FD 답 내용 같음 조건 추가, EI 수용 대상을 인생관 적용으로 변경"
    },
    {
      "candidate": "O8 문맥 의미 성분",
      "decision": "유지 및 수정",
      "retained": "명사만이 아닌 역할·행위·상태·평가·결과 비교",
      "revision": "최근접 용례와 치환 의미 보존의 강도 분리.모든 성분 점검을 항상 수행하도록 강요하지 않음",
      "counterexample": "FH·ET 같은 명사 오치환,FN 다른 대상 가까운 뜻,FT 비물리 후보 내 정착/의지 강화 차이",
      "held": "#96 원저자 정의,사전 구획,O8이#17/#16과 독립이라는 주장",
      "student_action": "쉬운 분류 후 남는 차이를 문장 성분과 술어 뜻으로 확인",
      "generation_principle": "명사 동일/상이와 의미 보존/비보존을 교차해 설계",
      "next_falsification_target": "역할·결과가 같아도 관용 결합/문체로 치환 실패하는 새 용례",
      "minimal_variant_reference": "FH 향상 성분,ET 은폐,GJ 향기,FT 좌우명 변형"
    }
  ],
  "probe_quality_correction": {
    "case": "DZ",
    "prior_probe": "02 record의 원④ 주체만 개시제로 고치는 변형은 뒤 '과산화물을 개시제로 쓰면'과 자기 사용 문구를 만들어 깨끗한 단일 요인 검사가 되기 어렵다.기존 기록을 삭제하지 않고 제한을 추가",
    "replacement_probe": "검토용 기준문장 '과산화물 개시제는 열을 흡수하면 불안정한 원자를 가진 분자로 분해된다'에서 주체만 '에틸렌'으로 교체",
    "prediction": "기준문장은 본문 직접 지지,변형문장은 본문이 배정한 분해 주체와 맞지 않아 지지 실패.모든 나머지 조건/상태 성분은 유지",
    "synthetic_not_corpus": true
  },
  "sampling": {
    "cases": 21,
    "distinct_passage_groups": 15,
    "groups": [
      "G001",
      "G014",
      "G018",
      "G025",
      "G026",
      "G027",
      "G028",
      "G029",
      "G030",
      "G033",
      "G034",
      "G035",
      "G036",
      "G037",
      "G038"
    ],
    "new_corpus_cases": 0,
    "strict_blind_performance_claimed": false,
    "independent_replication_claimed": false,
    "deduplication": "G029 EO/EP, G037 GA/GC, G028 EI/EJ, G033 FD/FF/FH, G034 FL/FN은 지문 단위 중복을 제외하여 계산"
  },
  "unresolved": [
    "GC② 문리 해석의 엄밀 배제",
    "CT 보충 XML script/EF 로컬 HWPX 렌더와 공식 원 배포본 직접 검증 차이",
    "어휘 사전 뜻 구획",
    "원저자 코드의 전체 정의·적용 위치",
    "EP·EO·EJ 등 유일 주 코드 우선순위",
    "선정 anchor는 외부 미열람 검증군이 아님"
  ],
  "sdss_note": "기존 태그 판정은 불변. FD/FF/FH/FL/FN/FT/FX/GJ 8사례의 빈 태그는 의미 비교 성공/실패로 합산하지 않음",
  "artifact": "분석/기본기_연구/review_20260915/수행연산_후보_v1.md",
  "confidence": "국소 선지·대안 풀이 근거는 각 record에 명시.분량/자기점수로 품질을 주장하지 않음.8개 군의 완전성·배타성은 검증되지 않음",
  "stop_condition": "이 사후 감사 완료 뒤 새 corpus 연구 시작 없이 종료.현재 미완료G043/G044 및미열람G045/G046 상태에 진입하지 않음",
  "quota_status": "unavailable"
}
```

### 명시적으로 연결된 집단 기록 참조

- `G029-induction-20260913-02` — 집단 귀납 기록 (집단/교차 사례 기록; 개별 case 판단으로 변환하지 않음)
- `META-G028-G030-meta_induction-20260913-02` — 교차 사례 귀납 기록 (집단/교차 사례 기록; 개별 case 판단으로 변환하지 않음)

## 6. 원장 추적

사용된 원장 record_id (queue 순서):
- `EO-blind-20260913-02` — 최초 blind 풀이 / done
- `EO-answer_check-20260913-02` — 공식 정답 대조 / done
- `EO-independent_code-20260913-02` — 독립 코드 판정 / done
- `EO-sdss_compare-20260913-02` — SDSS 사후 대조 / done
- `G029-induction-20260913-02` — 집단 귀납 기록 / done
- `DZ-EO-EP-boundary_revision-20260913-02` — 경계 수정 기록 / done
- `META-G028-G030-meta_induction-20260913-02` — 교차 사례 귀납 기록 / done
- `DZ-EO-EP-EJ-boundary_revision-20260915-semantic-audit-01` — 경계 수정 기록 / done
- `ANCHORS-O1-O8-boundary_revision-20260915-semantic-audit-01` — 경계 수정 기록 / done
