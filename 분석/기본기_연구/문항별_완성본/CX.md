> 이 파일은 원장으로부터 자동 생성된 열람용 파생본이다. 연구의 authoritative source는 raw queue이며, 이 파일을 직접 편집하지 않는다.

# CX

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
문맥상 ⓐ의 의미와 가장 가까운 것은?
```

### 선지

```json
[
  "공부를 하다 보니 시간은 자정이 넘었다.",
  "그들은 큰 산을 넘어서 마을에 도착했다.",
  "철새들이 국경선을 넘어서 훨훨 날아갔다.",
  "선수들은 가까스로 어려운 고비를 넘었다.",
  "갑자기 냄비에서 물이 넘어서 좀 당황했다.\n\n## 2024학년도"
]
```

### 원문 자료 감사

```json
{
  "case_id": "CX",
  "source_file_exists": true,
  "mechanically_linked": true,
  "assets": [
    {
      "path": "data/기본기_연구/prepared_backlog/blind_sources/CX.json",
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

### 최초 blind 풀이 — `CX-blind-20260911-01`

**선택 답**

`1`

**확신도**

`0.99`

**필요 정보와 위치**

```json
[
  {
    "location": "첫 문단 ⓐ",
    "information": "수백 개가 넘는 항목: 일정 기준 수량을 초과함."
  },
  {
    "location": "선택지 ①",
    "information": "시간이 자정을 넘었다: 일정한 시간 기준을 지남."
  }
]
```

**코드명 없는 최소 논리 구조**

```text
수량 기준 초과와 시간 기준 초과가 대응하므로 ①이다. 다른 선택지는 장애물·경계의 이동, 난관 극복, 용기의 용량 초과로 흘러나옴이다.
```

**중간 추론**

```json
[
  "② 산을 통과함, ③ 공간적 경계를 건넘, ④ 어려움을 극복함, ⑤ 액체가 흘러나옴을 뜻한다."
]
```

**노출 정보**

```json
{
  "official_answer_seen": false,
  "sdss_seen": false,
  "prior_exposure": "같은 group 원문만 읽음; 세션 이전 노출 미확인",
  "identity_noise": "⑤ 끝에 다음 단락 제목 ## 2024학년도가 붙어 있음. 해당 제목은 의미 판정에서 제외."
}
```

**기타 기록 필드**

```json
{
  "passage_group": "G019",
  "source": "data/기본기_연구/prepared_backlog/blind_sources/CX.json",
  "most_attractive_wrong": {
    "choice": 5,
    "exact_error": "양이 많다는 공통 요소는 있으나 본문은 기준 수량을 초과함, ⑤는 용기 밖으로 흘러나오는 물리 현상이므로 같은 문맥 의미가 아니다."
  },
  "barrier": "CU·CV·CX 저장. CW 그림 복원·blind 완료 전 답·태그 금지"
}
```

## 2. 공식 정답 대조

### 공식 정답 대조 — `CX-answer_check-20260912-01`

**최초 선택**

`1`

**공식 정답**

`1`

**기타 기록 필드**

```json
{
  "passage_group": "G019",
  "matches": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "수량 기준 초과와 시간 기준 경과는 같은 문맥 뜻으로 대응하며 물의 용기 밖 유출과 구별한다.",
  "group_blind_barrier": "CU·CV·CX 기존 blind와 CW 신규 blind raw 전부 저장 후 답만 공개",
  "answer_source": "prepared_backlog/sealed/answer_sdss.jsonl; data/kice_questions.jsonl (official_answer_verified)",
  "sdss_disclosed": false,
  "exposure_note": "원 blind 노출 기록 불변. CW는 provisional source 사전 노출로 엄격 신규 blind 성과 제외."
}
```

## 3. 독립 코드 판정

### 독립 코드 판정 — `CX-independent_code-20260912-01`

**주 코드**

```json
[]
```

**보조 코드**

```json
[]
```

**표면 코드**

```json
[
  {
    "code": 86,
    "name": "양적비교",
    "reason": "수백 개 초과라는 뜻의 설명에는 수량이 등장"
  },
  {
    "code": 42,
    "name": "내부/외부",
    "scope": "③ 국경 통과·⑤ 용기 밖 유출"
  }
]
```

**경쟁 코드 및 반증**

```json
[
  {
    "code": 86,
    "verdict": "주 코드 기각",
    "reason": "값의 크기를 계산하거나 두 양을 비교하여 답을 내지 않는다. 시간과 수량의 문맥 뜻 대응이 중심이다."
  },
  {
    "code": 3,
    "verdict": "기각",
    "reason": "①에 자정이라는 시간 기준이 있지만 사건의 선후를 따지는 판단은 없다."
  },
  {
    "code": 42,
    "verdict": "정답 주로 기각",
    "reason": "공간 경계 이동이나 용기 밖 유출을 배제하는 설명에는 쓸 수 있어도①의 비공간적 기준 초과를 내부/외부로 강제 번역할 필요가 없다."
  }
]
```

**확신도**

```text
어휘 판단 높음, 특정 100코드 미배당
```

**정규화된 주 코드 후보**

```json
[
  {
    "source_key": "primary",
    "value": []
  }
]
```

**정규화된 보조 코드**

```json
[
  {
    "source_key": "auxiliary",
    "value": []
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
        "verdict": "주 코드 기각",
        "reason": "값의 크기를 계산하거나 두 양을 비교하여 답을 내지 않는다. 시간과 수량의 문맥 뜻 대응이 중심이다."
      },
      {
        "code": 3,
        "verdict": "기각",
        "reason": "①에 자정이라는 시간 기준이 있지만 사건의 선후를 따지는 판단은 없다."
      },
      {
        "code": 42,
        "verdict": "정답 주로 기각",
        "reason": "공간 경계 이동이나 용기 밖 유출을 배제하는 설명에는 쓸 수 있어도①의 비공간적 기준 초과를 내부/외부로 강제 번역할 필요가 없다."
      }
    ]
  }
]
```

**기타 기록 필드**

```json
{
  "passage_group": "G019",
  "logic_without_codes": "넘다의 기준값 초과라는 문맥 뜻을 시간 기준을 지남과 대응시키고 공간 이동·난관 극복·유출과 구별한다.",
  "uncoded_primary_operation": "다의어의 문맥 의미 비교",
  "sdss_disclosed": false
}
```

## 4. SDSS 사후 대조

> SDSS는 독립 판정 후 공개된 제3자 후보 라벨이다. 이 기록은 독립 판정의 근거로 소급 사용하지 않는다.

### SDSS 사후 대조 — `CX-sdss_compare-20260912-01`

**비교**

```text
넘다의 대상이 수량·시간·산·국경·고비·물이므로 대상에 따른 문맥 의미 분류에 #17을 연결할 수 있다. 다만 수량과 시간이 다른 대상이어도 같은 뜻이라는 답이므로 대상 종류만 나누는 것으로 충분하지 않다.
```

**독립 판정 보존**

`true`

**기타 기록 필드**

```json
{
  "passage_group": "G019",
  "site_original_code_numbers": [
    17
  ],
  "source": "prepared_backlog/sealed/answer_sdss.jsonl",
  "disclosure_barrier": "G019 모든 independent_code raw 후 공개",
  "limitation": "독립 주 미배당 유지. 사이트 적용이 목적어 범주인지 어휘 의미 범주인지 미확인.",
  "site_is_third_party_candidate_index": true,
  "unresolved": [
    "#17의 정확한 사이트 적용 위치"
  ]
}
```

## 5. 후속 보강

이 case에 명시적으로 연결된 depth_backfill 또는 case-specific boundary_revision 기록이 없습니다.

### 명시적으로 연결된 집단 기록 참조

- `META-G018-G020-meta_induction-20260912-01` — 교차 사례 귀납 기록 (집단/교차 사례 기록; 개별 case 판단으로 변환하지 않음)

## 6. 원장 추적

사용된 원장 record_id (queue 순서):
- `CX-blind-20260911-01` — 최초 blind 풀이 / done
- `CX-answer_check-20260912-01` — 공식 정답 대조 / done
- `CX-independent_code-20260912-01` — 독립 코드 판정 / done
- `CX-sdss_compare-20260912-01` — SDSS 사후 대조 / done
- `META-G018-G020-meta_induction-20260912-01` — 교차 사례 귀납 기록 / done
