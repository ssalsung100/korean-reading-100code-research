> 이 파일은 원장으로부터 자동 생성된 열람용 파생본이다. 연구의 authoritative source는 raw queue이며, 이 파일을 직접 편집하지 않는다.

# CU

## 0. 문항 정보

- **Passage group:** G019

### 제시문

```text
인터넷 검색 엔진은 검색어를 포함하는 웹 페이지를 찾아 화면에 보여 준다. 웹 페이지가 화면에 나타나는 순서를 정하기 위해 검색 엔진은 수백 개가 ⓐ 넘는 항목을 고려한 다양한 방식을 사용한다. 대표적인 항목으로 중요도와 적합도가 있다.

검색 엔진은 빠른 시간 내에 검색 결과를 보여 주기 위해 웹 페이지들의 데이터를 수집하여 인덱스를 미리 작성해 놓는다. 인덱스란 단어를 알파벳순으로 정리한 목록으로, 여기에는 각 단어가 등장하는 웹 페이지와 단어의 빈도수 등이 저장된다. 이때 각 웹 페이지의 중요도가 함께 기록된다.

㉠ 중요도는 웹 페이지의 중요성을 값으로 나타낸 것으로 링크 분석 기법으로 측정할 수 있다. 기본적인 링크 분석 기법에서 웹 페이지 A의 값은 A를 링크한 각 웹 페이지들로부터 받는 값의 합이다. 이렇게 받은 A의 값은 A가 링크한 다른 웹 페이지들에 균등하게 나눠진다. 즉 A의 값이 4이고 A가 두 개의 링크를 통해 다른 웹 페이지로 연결된다면, A의 값은 유지되면서 두 웹 페이지에는 각각 2가 보내진다.

하지만 두 웹 페이지가 실제로 받는 값은 2에 댐핑 인자를 곱한 값이다. 댐핑 인자는 사용자들이 웹 페이지를 읽다가 링크를 통해 다른 웹 페이지로 이동하지 않는 비율을 반영한 값으로 1 미만의 값을 가진다. 댐핑 인자는 모든 링크에 동일하게 적용된다. 가령 그 비율이 20 %이면 댐핑 인자는 0.8이고 두 웹 페이지는 A로부터 각각 1.6을 받는다. 웹 페이지로 연결된 링크를 통해 받는 값을 모두 반영했을 때의 값이 각 웹 페이지의 중요도이다. 웹 페이지들을 연결하는 링크들은 변할 수 있기 때문에 검색 엔진은 주기적으로 웹 페이지의 중요도를 갱신한다.

사용자가 검색어를 입력하면 검색 엔진은 인덱스에서 검색어에 적합한 웹 페이지를 찾는다. ㉡ 적합도는 단어의 빈도, 단어가 포함된 웹 페이지의 수, 웹 페이지의 글자 수를 반영한 식을 통해 값이 정해진다. 해당 검색어가 많이 나올수록, 그 검색어를 포함하는 다른 웹 페이지의 수가 적을수록, 현재 웹 페이지의 글자 수가 전체 웹 페이지의 평균 글자 수에 비해 적을수록 적합도가 높아진다. 검색 엔진은 중요도와 적합도, 기타 항목들을 적절한 비율로 합산하여 화면에 나열되는 웹 페이지의 순서를 결정한다.
```

### 발문

```text
윗글을 통해 알 수 있는 내용으로 가장 적절한 것은?
```

### 선지

```json
[
  "인덱스는 사용자가 검색어를 입력한 직후에 작성된다.",
  "사용자가 링크를 따라 다른 웹 페이지로 이동하는 비율이 높을수록 댐핑 인자가 커진다.",
  "링크 분석 기법은 웹 페이지 사이의 링크를 분석하여 웹 페이지의 적합도를 값으로 나타낸다.",
  "웹 페이지의 중요도는 다른 웹 페이지에서 받는 값과 다른 웹 페이지에 나눠 주는 값의 합이다.",
  "사용자가 검색어를 입력하면 검색 엔진은 검색한 결과를 인덱스에 정렬된 순서대로 화면에 나타낸다."
]
```

### 원문 자료 감사

```json
{
  "case_id": "CU",
  "source_file_exists": true,
  "mechanically_linked": true,
  "assets": [
    {
      "path": "data/기본기_연구/prepared_backlog/blind_sources/CU.json",
      "exists": true,
      "kind": "supplement_or_source"
    },
    {
      "path": "prepared_backlog/sealed/answer_sdss.jsonl",
      "exists": false,
      "kind": "supplement_or_source"
    }
  ],
  "image_files_exist": true,
  "image_meaning_verified": false,
  "choice_count": 5,
  "all_choices_empty": false,
  "warnings": [
    "참조한 보충/원문 자산이 export에 없음: prepared_backlog/sealed/answer_sdss.jsonl"
  ],
  "ready": false
}
```

## 1. 최초 blind 풀이

### 최초 blind 풀이 — `CU-blind-20260911-01`

**선택 답**

`2`

**확신도**

`0.99`

**필요 정보와 위치**

```json
[
  {
    "location": "4문단",
    "information": "이동하지 않는 비율 20%이면 댐핑 인자 0.8이며 1 미만."
  },
  {
    "location": "2·3·5문단",
    "information": "인덱스는 미리 작성, 중요도는 받은 값의 합, 순위는 중요도·적합도 등 합산으로 결정."
  }
]
```

**코드명 없는 최소 논리 구조**

```text
이동하지 않는 비율의 여집합인 이동 비율이 댐핑 인자에 반영된다. 따라서 이동 비율이 높을수록 인자가 커지는 ②가 적절하다.
```

**중간 추론**

```json
[
  "①은 인덱스 준비 시점을 검색 입력 뒤로 옮긴다.",
  "③은 중요도와 적합도를 교환한다.",
  "④는 나눠 주는 값을 중요도에 다시 더하여 중복 계산한다.",
  "⑤는 단어 인덱스 정렬과 결과 페이지 순위를 혼동한다."
]
```

**노출 정보**

```json
{
  "official_answer_seen": false,
  "sdss_seen": false,
  "prior_exposure": "이번 세션 신규 지문. 이전 노출 미확인"
}
```

**기타 기록 필드**

```json
{
  "passage_group": "G019",
  "source": "data/기본기_연구/prepared_backlog/blind_sources/CU.json",
  "most_attractive_wrong": {
    "choice": 4,
    "exact_error": "보낸 뒤에도 자기 값이 유지된다는 설명을 보낸 값까지 더해 증가한다는 뜻으로 읽으면 오류다. 중요도는 받은 값의 합이다."
  },
  "barrier": "G019 전체 blind 전 답·태그 금지"
}
```

## 2. 공식 정답 대조

### 공식 정답 대조 — `CU-answer_check-20260912-01`

**최초 선택**

`2`

**공식 정답**

`2`

**기타 기록 필드**

```json
{
  "passage_group": "G019",
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "이동하지 않는 비율의 보수인 이동 비율이 증가하면 댐핑 인자가 증가한다.",
  "group_blind_barrier": "CU·CV·CX 기존 blind와 CW 신규 blind raw 전부 저장 후 답만 공개",
  "answer_source": "prepared_backlog/sealed/answer_sdss.jsonl; data/kice_questions.jsonl (official_answer_verified)",
  "sdss_disclosed": false,
  "exposure_note": "원 blind 노출 기록 불변. CW는 provisional source 사전 노출로 엄격 신규 blind 성과 제외."
}
```

## 3. 독립 코드 판정

### 독립 코드 판정 — `CU-independent_code-20260912-01`

**주 코드**

```json
[
  {
    "code": 49,
    "name": "상관관계",
    "reason": "정답②의 증가 방향을 재진술한다. 사이트 별칭의 넓은 증감 방향 범위로 적용."
  }
]
```

**보조 코드**

```json
[
  {
    "code": 85,
    "name": "비율은경쟁적",
    "reason": "비이동 비율과 이동 비율은 합1인 보완 비율"
  },
  {
    "code": 45,
    "name": "함수",
    "reason": "비이동 비율r에서 댐핑1-r로 대응"
  }
]
```

**표면 코드**

```json
[
  {
    "code": 3,
    "name": "선후",
    "scope": "오답① 인덱스 작성 시점"
  },
  {
    "code": 25,
    "name": "분류",
    "scope": "중요도/적합도 지표 구별"
  }
]
```

**경쟁 코드 및 반증**

```json
[
  {
    "code": 46,
    "verdict": "주 코드 기각",
    "reason": "사용자 행동이 현실에서 다른 변수를 발생시키는 경로보다 정의된 댐핑값의 대응·방향을 읽는다."
  },
  {
    "code": 92,
    "verdict": "보조 이하",
    "reason": "1-r은 설명용으로 쓸 수 있지만 구체적 수치 계산 없이 방향 판단이 가능하다."
  },
  {
    "code": 3,
    "verdict": "①의 오답 범위",
    "reason": "검색 전 인덱스 작성은①을 배제하지만②의 정답 관계를 담당하지 않는다."
  }
]
```

**확신도**

```text
높음
```

**정규화된 주 코드 후보**

```json
[
  {
    "source_key": "primary",
    "value": [
      {
        "code": 49,
        "name": "상관관계",
        "reason": "정답②의 증가 방향을 재진술한다. 사이트 별칭의 넓은 증감 방향 범위로 적용."
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
        "code": 85,
        "name": "비율은경쟁적",
        "reason": "비이동 비율과 이동 비율은 합1인 보완 비율"
      },
      {
        "code": 45,
        "name": "함수",
        "reason": "비이동 비율r에서 댐핑1-r로 대응"
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
        "code": 46,
        "verdict": "주 코드 기각",
        "reason": "사용자 행동이 현실에서 다른 변수를 발생시키는 경로보다 정의된 댐핑값의 대응·방향을 읽는다."
      },
      {
        "code": 92,
        "verdict": "보조 이하",
        "reason": "1-r은 설명용으로 쓸 수 있지만 구체적 수치 계산 없이 방향 판단이 가능하다."
      },
      {
        "code": 3,
        "verdict": "①의 오답 범위",
        "reason": "검색 전 인덱스 작성은①을 배제하지만②의 정답 관계를 담당하지 않는다."
      }
    ]
  }
]
```

**기타 기록 필드**

```json
{
  "passage_group": "G019",
  "logic_without_codes": "비이동 비율과 이동 비율이 합쳐1이라는 관계에서 이동 비율의 증가에 따른 댐핑 인자의 증가를 확인한다.",
  "sdss_disclosed": false
}
```

## 4. SDSS 사후 대조

> SDSS는 독립 판정 후 공개된 제3자 후보 라벨이다. 이 기록은 독립 판정의 근거로 소급 사용하지 않는다.

### SDSS 사후 대조 — `CU-sdss_compare-20260912-01`

**비교**

```text
전체 사용자 중 비이동 사용자를 제외하면 이동 사용자라는 차집합 표상으로 정답②의 보수 관계를 설명할 수 있다. 독립 #85 보완 비율과 #45 1-r가 같은 계산을 서로 다른 표상으로 기술한다. 독립 #49 주는 그 결과의 증가 방향이다.
```

**독립 판정 보존**

`true`

**기타 기록 필드**

```json
{
  "passage_group": "G019",
  "site_original_code_numbers": [
    89
  ],
  "source": "prepared_backlog/sealed/answer_sdss.jsonl",
  "disclosure_barrier": "G019 모든 independent_code raw 후 공개",
  "limitation": "집합 차 연산·고정합 비율·증감 적용을 층위별로 보존하며 #89/#85 전체를 통합하지 않는다.",
  "site_is_third_party_candidate_index": true,
  "unresolved": []
}
```

## 5. 후속 보강

이 case에 명시적으로 연결된 depth_backfill 또는 case-specific boundary_revision 기록이 없습니다.

### 명시적으로 연결된 집단 기록 참조

- `META-G018-G020-meta_induction-20260912-01` — 교차 사례 귀납 기록 (집단/교차 사례 기록; 개별 case 판단으로 변환하지 않음)

## 6. 원장 추적

사용된 원장 record_id (queue 순서):
- `CU-blind-20260911-01` — 최초 blind 풀이 / done
- `CU-answer_check-20260912-01` — 공식 정답 대조 / done
- `CU-independent_code-20260912-01` — 독립 코드 판정 / done
- `CU-sdss_compare-20260912-01` — SDSS 사후 대조 / done
- `META-G018-G020-meta_induction-20260912-01` — 교차 사례 귀납 기록 / done
