> 이 파일은 원장으로부터 자동 생성된 열람용 파생본이다. 연구의 authoritative source는 raw queue이며, 이 파일을 직접 편집하지 않는다.

# CV

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
㉠, ㉡을 고려하여 검색 결과에서 웹 페이지의 순위를 높이기 위한 방안으로 가장 적절한 것은?
```

### 선지

```json
[
  "화제가 되고 있는 검색어들을 웹 페이지에 최대한 많이 나열하여 ㉠을 높인다.",
  "사람들이 많이 접속하는 유명 검색 사이트로 연결하는 링크를 웹 페이지에 많이 포함시켜 ㉠을 높인다.",
  "알파벳순으로 앞 순서에 있는 단어들을 웹 페이지 첫 부분에 많이 포함시켜 ㉡을 높인다.",
  "다른 많은 웹 페이지들이 링크하도록 웹 페이지에서 여러 주제를 다루고 전체 글자 수를 많게 하여 ㉡을 높인다.",
  "다른 웹 페이지에서 흔히 다루지 않는 주제를 간략하게 설명하되 주제와 관련된 단어를 자주 사용하여 ㉡을 높인다."
]
```

### 원문 자료 감사

```json
{
  "case_id": "CV",
  "source_file_exists": true,
  "mechanically_linked": true,
  "assets": [
    {
      "path": "data/기본기_연구/prepared_backlog/blind_sources/CV.json",
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

### 최초 blind 풀이 — `CV-blind-20260911-01`

**선택 답**

`5`

**확신도**

`0.99`

**필요 정보와 위치**

```json
[
  {
    "location": "5문단",
    "information": "검색어 빈도 증가, 검색어 포함 다른 페이지 수 감소, 현재 글자 수 감소가 적합도를 높인다."
  },
  {
    "location": "3문단",
    "information": "중요도는 외부 페이지로부터 들어오는 값으로 정해진다."
  }
]
```

**코드명 없는 최소 논리 구조**

```text
⑤는 희소한 주제·짧은 글·주제 단어 반복으로 적합도를 높이는 세 조건을 같은 방향으로 충족한다.
```

**중간 추론**

```json
[
  "① 검색어 나열은 중요도를 직접 높이는 링크 조건이 아니다.",
  "② 유명 사이트로 내가 링크하는 것과 유명 사이트가 나를 링크하는 것을 바꿨다.",
  "③ 알파벳 순서·앞부분 위치는 적합도 상승 조건이 아니다.",
  "④ 글자 수 증가는 적합도를 낮추는 방향이고 들어오는 링크는 중요도 요소다."
]
```

**노출 정보**

```json
{
  "official_answer_seen": false,
  "sdss_seen": false,
  "prior_exposure": "같은 group 원문만 읽음; 세션 이전 노출 미확인"
}
```

**기타 기록 필드**

```json
{
  "passage_group": "G019",
  "source": "data/기본기_연구/prepared_backlog/blind_sources/CV.json",
  "most_attractive_wrong": {
    "choice": 2,
    "exact_error": "유명 페이지와 연결된다는 공통 표현에 이끌려 링크 방향을 지우면 중요도 유입과 유출을 바꿔 읽게 된다."
  },
  "barrier": "G019 전체 blind 전 답·태그 금지"
}
```

## 2. 공식 정답 대조

### 공식 정답 대조 — `CV-answer_check-20260912-01`

**최초 선택**

`5`

**공식 정답**

`5`

**기타 기록 필드**

```json
{
  "passage_group": "G019",
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "적합도는 검색어 빈도 증가·그 단어를 포함하는 다른 페이지수 감소·자기 글자수 감소와 같은 방향으로 높아진다. 링크 유입과 유출을 구별한다.",
  "group_blind_barrier": "CU·CV·CX 기존 blind와 CW 신규 blind raw 전부 저장 후 답만 공개",
  "answer_source": "prepared_backlog/sealed/answer_sdss.jsonl; data/kice_questions.jsonl (official_answer_verified)",
  "sdss_disclosed": false,
  "exposure_note": "원 blind 노출 기록 불변. CW는 provisional source 사전 노출로 엄격 신규 blind 성과 제외."
}
```

## 3. 독립 코드 판정

### 독립 코드 판정 — `CV-independent_code-20260912-01`

**주 코드**

```json
[
  {
    "code": 45,
    "name": "함수",
    "reason": "검색어 빈도·다른 페이지 수·자기 글자 수의 입력들이 적합도에 어떻게 대응하는지 적용"
  }
]
```

**보조 코드**

```json
[
  {
    "code": 49,
    "name": "상관관계",
    "reason": "세 입력 각각의 증감 방향 적용"
  },
  {
    "code": 44,
    "name": "수단/목적",
    "reason": "적합도를 높이려는 조절 방안 선택"
  }
]
```

**표면 코드**

```json
[
  {
    "code": 42,
    "name": "내부/외부",
    "scope": "오답② 내 페이지에서 외부 페이지로의 링크",
    "reason": "공간 구분보다 유입/유출 방향 자체가 중요"
  }
]
```

**경쟁 코드 및 반증**

```json
[
  {
    "code": 84,
    "verdict": "보류",
    "reason": "본문은 구체 적합도 식을 제시하지 않고 단조 방향만 준다. 빈도를 분자, 길이를 분모에 놓은 정확한 식을 새로 만들어서는 안 된다."
  },
  {
    "code": 46,
    "verdict": "주 코드 기각",
    "reason": "지표 산정 규칙에 대한 전략 적용이며 경험적 인과 경로 확인이 필수는 아니다."
  },
  {
    "code": 42,
    "verdict": "② 국소 설명",
    "reason": "내부/외부가 같아도 링크의 향하는 방향을 바꾸면② 판단이 바뀌며, 정답⑤의 세 입력 조절은 경계 분류를 요구하지 않는다."
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
        "code": 45,
        "name": "함수",
        "reason": "검색어 빈도·다른 페이지 수·자기 글자 수의 입력들이 적합도에 어떻게 대응하는지 적용"
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
        "reason": "세 입력 각각의 증감 방향 적용"
      },
      {
        "code": 44,
        "name": "수단/목적",
        "reason": "적합도를 높이려는 조절 방안 선택"
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
        "code": 84,
        "verdict": "보류",
        "reason": "본문은 구체 적합도 식을 제시하지 않고 단조 방향만 준다. 빈도를 분자, 길이를 분모에 놓은 정확한 식을 새로 만들어서는 안 된다."
      },
      {
        "code": 46,
        "verdict": "주 코드 기각",
        "reason": "지표 산정 규칙에 대한 전략 적용이며 경험적 인과 경로 확인이 필수는 아니다."
      },
      {
        "code": 42,
        "verdict": "② 국소 설명",
        "reason": "내부/외부가 같아도 링크의 향하는 방향을 바꾸면② 판단이 바뀌며, 정답⑤의 세 입력 조절은 경계 분류를 요구하지 않는다."
      }
    ]
  }
]
```

**기타 기록 필드**

```json
{
  "passage_group": "G019",
  "logic_without_codes": "적합도의 세 입력을 모두 높이는 방향으로 조절하는 방안을 확인하고 다른 지표의 조건이나 링크 방향을 바꾼 선지를 배제한다.",
  "sdss_disclosed": false
}
```

## 4. SDSS 사후 대조

> SDSS는 독립 판정 후 공개된 제3자 후보 라벨이다. 이 기록은 독립 판정의 근거로 소급 사용하지 않는다.

### SDSS 사후 대조 — `CV-sdss_compare-20260912-01`

**비교**

```text
사이트 #45가 독립 주 코드와 일치한다. 다변수 입력의 단조 방향을 적용하는 사례이다.
```

**독립 판정 보존**

`true`

**기타 기록 필드**

```json
{
  "passage_group": "G019",
  "site_original_code_numbers": [
    45
  ],
  "source": "prepared_backlog/sealed/answer_sdss.jsonl",
  "disclosure_barrier": "G019 모든 independent_code raw 후 공개",
  "limitation": "본문에 정확한 적합도 수식은 없어 분수식·정확한 함수 형태를 임의 복원하지 않는다.",
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
- `CV-blind-20260911-01` — 최초 blind 풀이 / done
- `CV-answer_check-20260912-01` — 공식 정답 대조 / done
- `CV-independent_code-20260912-01` — 독립 코드 판정 / done
- `CV-sdss_compare-20260912-01` — SDSS 사후 대조 / done
- `META-G018-G020-meta_induction-20260912-01` — 교차 사례 귀납 기록 / done
