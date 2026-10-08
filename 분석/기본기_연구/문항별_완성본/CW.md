> 이 파일은 원장으로부터 자동 생성된 열람용 파생본이다. 연구의 authoritative source는 raw queue이며, 이 파일을 직접 편집하지 않는다.

# CW

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
&lt;보기&gt;는 웹 페이지들의 관계를 도식화한 것이다. 윗글을 바탕으로 &lt;보기&gt;를 이해한 내용으로 적절한 것은? [3점]

&lt; 보 기 &gt;

a

b

c

e

d

원은 웹 페이지이고, 화살표는 웹 페이지에서 링크를 통해 화살표 방향의 다른 웹 페이지로 연결됨을 뜻한다. 댐핑 인자는 0.5이고, d와 e의 중요도는 16으로 고정된 값이다.

(단, 링크와 댐핑 인자 외에 웹 페이지의 중요도에 영향을 주는 다른 요소는 고려하지 않음.)
```

### 선지

```json
[
  "a의 중요도는 16이다.",
  "a가 b와 d로부터 각각 받는 값은 같다.",
  "b에서 a로의 링크가 끊어지면 b와 c의 중요도는 같다.",
  "e에서 a로의 링크가 추가되면 b의 중요도는 6이다.",
  "e에서 c로의 링크가 추가되면 c의 중요도는 5이다."
]
```

### 원문 자료 감사

```json
{
  "case_id": "CW",
  "source_file_exists": true,
  "mechanically_linked": true,
  "assets": [
    {
      "path": "data/기본기_연구/prepared_backlog/blind_sources/CW.json",
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

### 최초 blind 풀이 — `CW-blind-20260912-01`

**선택 답**

`5`

**확신도**

```text
높음
```

**필요 정보와 위치**

```json
[
  "공통 지문3~4문단 수신 합·송신 링크수 균등 분배·댐핑 인자",
  "보기 d=e=16 고정, 댐핑0.5",
  "공식 application render: b→a, b→c, d→a, e→b; a·c는 외부로 보내고 d·e는 외부에서 받음"
]
```

**코드명 없는 최소 논리 구조**

```text
송신 페이지의 값을 나가는 링크 수로 나누고0.5를 곱해 각 수신값을 구한다. 링크 추가 시 새 유입뿐 아니라 기존 송신 경로의 분배와 후속 수신값도 다시 계산한다.
```

**중간 추론**

```json
[
  "기본 b=16×0.5=8, a=16×0.5+(8/2)×0.5=10, c=(8/2)×0.5=2. ①16 아님, ②a가 d와 b에서 받는 값은8과2로 다름.",
  "③b→a를 끊으면 b는8로 그대로, b의 송신 링크가 c 하나여서 c=8×0.5=4. 서로 같지 않음.",
  "④e→a 추가 시 e의 송신 링크는a,b 두 개, b=(16/2)×0.5=4이므로6 아님.",
  "⑤e→c 추가 시 e→b=4이므로 b=4, b→c=(4/2)×0.5=1, e→c=(16/2)×0.5=4. c=1+4=5."
]
```

**가장 매력적인 오답**

```json
{
  "choice": 3,
  "exact_error": "b에서a로 보내지 않으니 c가 b의 값 전부를 받는다고 오독하면 같아 보인다. 링크수 분배 뒤에도0.5를 곱하므로 c는b의 절반이다."
}
```

**노출 정보**

```json
{
  "official_answer_seen": false,
  "sdss_seen": false,
  "prior_project_judgment_seen": "같은 CW의 미완료 hold 일부 추론만 노출, 공식답·코드 없음",
  "past_learning_exposure": "확인 불가",
  "same_passage_prior_exposure": true,
  "unverified_vector_geometry_seen": true,
  "valid_original_graph_seen": true,
  "strict_blind_qualification": "원문/미완료 hold와 provisional geometry의 사전 노출이 있어 엄격 신규 blind 성과에서 제외. 정답·SDSS 사전 노출은 없음."
}
```

**기타 기록 필드**

```json
{
  "passage_group": "G019",
  "additional_trap": "⑤를 검증할 때 기존 b=8을 고정하면 c=2+4=6으로 오산한다. e의 분배 변화가 b와 다시 c로 전파됨을 반영해야 한다.",
  "source": "data/기본기_연구/prepared_backlog/blind_sources/CW.json",
  "visual_source": "data/기본기_연구/prepared_backlog/blind_sources/CW_graph_original_render.png",
  "source_quality_resolution": "한컴 원본 렌더를 직접 시각 판독함. 외부로 나가거나 들어오는 화살표 자체는 원본에 실제 존재한다. 앞 hold의 외부 선분 관찰만으로 원본이 잘못되었다고 결론내리지 않는다. v2의 방향·연결·화살촉은 원본과 달라 채택하지 않음. 최초 hold 기록은 보존."
}
```

## 2. 공식 정답 대조

### 공식 정답 대조 — `CW-answer_check-20260912-01`

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
  "logic_without_codes_fixed": "e→c 추가 시 e의 두 송신 링크로 각각4가 전달되어 b=4, b→c=1과 e→c=4를 합쳐 c=5. 원본 그림 검증 후 계산.",
  "group_blind_barrier": "CU·CV·CX 기존 blind와 CW 신규 blind raw 전부 저장 후 답만 공개",
  "answer_source": "prepared_backlog/sealed/answer_sdss.jsonl; data/kice_questions.jsonl (official_answer_verified)",
  "sdss_disclosed": false,
  "exposure_note": "원 blind 노출 기록 불변. CW는 provisional source 사전 노출로 엄격 신규 blind 성과 제외."
}
```

## 3. 독립 코드 판정

### 독립 코드 판정 — `CW-independent_code-20260912-01`

**주 코드**

```json
[
  {
    "code": 45,
    "name": "함수",
    "reason": "그래프 연결과 링크수를 입력으로 각 노드 산출값의 연쇄 대응을 복원한다."
  }
]
```

**보조 코드**

```json
[
  {
    "code": 84,
    "name": "분수식",
    "reason": "송신값은 링크수로 나누어 균등 분배된다."
  },
  {
    "code": 92,
    "name": "수식",
    "reason": "⑤는 b=4, c=4/2×0.5+16/2×0.5=5라는 계산이 필요"
  },
  {
    "code": 85,
    "name": "비율은경쟁적",
    "reason": "e의 고정 총 송신8을 두 링크가 나누어 기존 e→b 몫이8에서4로 줄어든다."
  }
]
```

**표면 코드**

```json
[
  {
    "code": 50,
    "name": "길이막히면뒤로못간다",
    "scope": "③ 링크 단절",
    "reason": "단절 이후 남은 링크로의 재분배까지 필요"
  }
]
```

**경쟁 코드 및 반증**

```json
[
  {
    "code": 49,
    "verdict": "보조 가능, 주로 부족",
    "reason": "새 링크가 생기면 c가 늘어난다는 방향만으로⑤의 정확한5 또는③의 비동일성을 결정할 수 없다."
  },
  {
    "code": 50,
    "verdict": "③ 일부에만 적용",
    "reason": "끊긴 길로 값이 안 간다는 사실 외에 남은 링크수 변화와 댐핑을 계산해야 한다. 단절 자체를 모두의 주 연산으로 삼지 않는다."
  },
  {
    "code": 46,
    "verdict": "표상 중첩 가능, 주 보류",
    "reason": "중요도 값의 계산 갱신은 실제 물질 전달의 경험적 인과라기보다 정의된 알고리즘의 의존 경로다."
  }
]
```

**확신도**

```text
높음
```

**경계 메모**

```text
합 고정 #85는 e의 총 송신8 범위에서만 성립한다. 전체 그래프 중요도 합이 항상 고정이라고 확대하지 않는다.
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
        "reason": "그래프 연결과 링크수를 입력으로 각 노드 산출값의 연쇄 대응을 복원한다."
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
        "code": 84,
        "name": "분수식",
        "reason": "송신값은 링크수로 나누어 균등 분배된다."
      },
      {
        "code": 92,
        "name": "수식",
        "reason": "⑤는 b=4, c=4/2×0.5+16/2×0.5=5라는 계산이 필요"
      },
      {
        "code": 85,
        "name": "비율은경쟁적",
        "reason": "e의 고정 총 송신8을 두 링크가 나누어 기존 e→b 몫이8에서4로 줄어든다."
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
        "code": 49,
        "verdict": "보조 가능, 주로 부족",
        "reason": "새 링크가 생기면 c가 늘어난다는 방향만으로⑤의 정확한5 또는③의 비동일성을 결정할 수 없다."
      },
      {
        "code": 50,
        "verdict": "③ 일부에만 적용",
        "reason": "끊긴 길로 값이 안 간다는 사실 외에 남은 링크수 변화와 댐핑을 계산해야 한다. 단절 자체를 모두의 주 연산으로 삼지 않는다."
      },
      {
        "code": 46,
        "verdict": "표상 중첩 가능, 주 보류",
        "reason": "중요도 값의 계산 갱신은 실제 물질 전달의 경험적 인과라기보다 정의된 알고리즘의 의존 경로다."
      }
    ]
  }
]
```

**기타 기록 필드**

```json
{
  "passage_group": "G019",
  "logic_without_codes": "각 송신값=송신 노드값×0.5/송신 링크수, 수신 노드값=유입합. 링크 추가로 e의 분모가 바뀌면 b의 값과 b에서 c로 가는 값도 순서대로 다시 계산한다.",
  "ablation_test": [
    "⑤에서 e→c=4만 더하고 기존c=2를 유지하면6으로 오답. b를 재계산하는 단계가 필수.",
    "③에서 분배만 적용하고 댐핑을 지우면 b=c로 오판. 두 연산은 별도 보존."
  ],
  "source_quality": "공식 HWP application render 직접 시각 판독 완료. strict 신규 blind 제외 및 이전 hold 보존.",
  "sdss_disclosed": false
}
```

## 4. SDSS 사후 대조

> SDSS는 독립 판정 후 공개된 제3자 후보 라벨이다. 이 기록은 독립 판정의 근거로 소급 사용하지 않는다.

### SDSS 사후 대조 — `CW-sdss_compare-20260912-01`

**비교**

```text
사이트 #45가 독립 주 코드와 일치한다. CV와 같은 표지이지만 그래프 연결 변경에 따른 분모와 중간값 갱신이 필수인 수치 합성 대응이다.
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
  "limitation": "CV의 방향 조절과 CW의 연쇄 재계산을 같은 풀이 행동으로 합치지 않는다. 원형 코드와 하위 수행을 함께 보존.",
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
- `CW-hold-20260911-diagram-missing-01` — hold / hold
- `CW-hold-20260911-vector-fidelity-02` — hold / hold
- `CW-hold-20260912-vector-fidelity-03` — hold / needs_astra_review
- `CW-blind-20260912-01` — 최초 blind 풀이 / done
- `CW-answer_check-20260912-01` — 공식 정답 대조 / done
- `CW-independent_code-20260912-01` — 독립 코드 판정 / done
- `CW-sdss_compare-20260912-01` — SDSS 사후 대조 / done
- `META-G018-G020-meta_induction-20260912-01` — 교차 사례 귀납 기록 / done
