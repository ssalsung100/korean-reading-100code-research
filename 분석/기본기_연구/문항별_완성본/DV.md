> 이 파일은 원장으로부터 자동 생성된 열람용 파생본이다. 연구의 authoritative source는 raw queue이며, 이 파일을 직접 편집하지 않는다.

# DV

## 0. 문항 정보

- **Passage group:** G025

### 제시문

```text
데이터를 처리할 때 데이터의 정확성은 매우 중요하다. 그런데 데이터에 결측치와 이상치가 포함되면 데이터의 특징을 제대로 ⓐ 나타내기 어렵다.

결측치는 데이터 값이 ⓑ 빠져 있는 것이다. 결측치를 처리하는 방법 중 하나인 대체는 다른 값으로 결측치를 채우는 것인데, 대체하는 값으로는 평균, 중앙값, 최빈값을 많이 사용한다. 중앙값은 데이터를 크기순으로 정렬했을 때 중앙에 위치한 값이다. 크기가 같은 값이 복수일 경우에도 순위를 매겨 중앙값을 찾고, 데이터의 개수가 짝수이면 중앙에 있는 두 값의 평균이 중앙값이다. 또 최빈값은 데이터에 가장 많이 나타나는 값을 이른다. 일반적으로 데이터 값이 연속적인 수치이면 평균으로, 석차처럼 순위가 있는 값에는 중앙값으로, 직업과 같이 문자인 경우에는 최빈값으로 결측치를 대체한다.

이상치는 데이터의 다른 값에 비해 유달리 크거나 작은 값으로, 데이터를 수집할 때 측정 오류 등에 의해 주로 ⓒ 생긴다. 그러나 정상적인 데이터라도 데이터의 특징을 왜곡하는 데이터 값이 있을 수 있다. 예를 들어, 데이터가 어떤 프로 선수들의 연봉이고 그중 한 명의 연봉이 유달리 많다면, 이상치가 포함된 데이터에 해당한다. 이런 데이터의 특징을 하나의 수치로 나타내려는 경우 ㉠ 대푯값으로 평균보다 중앙값을 주로 사용한다.

평면상에 있는 점들의 위치를 나타내는 데이터에서도 이상치를 발견할 수 있다. 대부분의 점들이 가상의 직선 주위에 모여 있다면 이 직선은 데이터의 특징을 잘 나타낸다고 할 수 있다. 이 직선을 직선 L이라고 하자. 그런데 직선 L로부터 멀리 떨어진 위치에도 몇 개의 점이 있다. 이 점들이 이상치이다.

㉡ 이상치를 포함하는 데이터에서 직선 L을 찾는다고 하자. 이때 사용할 수 있는 기법의 하나인 A 기법은 두 점을 무작위로 골라 정상치 집합으로 가정하고, 이 두 점을 ⓓ 지나는 후보 직선을 그어 나머지 점들과 후보 직선 사이의 거리를 구한다. 이 거리가 허용 범위 이내인 점들을 정상치 집합에 추가한다. 정상치 집합의 점의 개수가 미리 정해 둔 기준, 즉 문턱값보다 많으면 후보 직선을 최종 후보군에 넣는다. 반대로 점의 개수가 문턱값보다 적으면 후보 직선을 버린다. 만약 처음에 고른 점이 이상치이면, 대부분의 점들은 해당 후보 직선과의 거리가 너무 ⓔ 멀어 이 직선은 최종 후보군에서 제외되는 것이다. 이 과정을 반복하여 최종 후보군을 구하고, 최종 후보군에 포함된 직선 중에서 정상치 집합의 데이터 개수가 최대인 직선을 직선 L로 선택한다. 이 기법은 이상치가 있어도 직선 L을 찾을 가능성이 높다.
```

### 발문

```text
윗글을 이해한 내용으로 적절하지 않은 것은?
```

### 선지

```json
[
  "데이터가 수치로 구성되지 않아도 최빈값을 구할 수 있다.",
  "데이터의 특징이 언제나 하나의 수치로 나타나는 것은 아니다.",
  "데이터가 정상적으로 수집되었다면 이상치가 존재하지 않는다.",
  "데이터에 동일한 수치가 여러 개 있어도 중앙값으로 결측치를 대체할 수 있다.",
  "데이터를 수집하는 과정에서 측정 오류가 발생한 값이라도 이상치가 아닐 수 있다."
]
```

### 원문 자료 감사

```json
{
  "case_id": "DV",
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

### 최초 blind 풀이 — `DV-blind-20260913-01`

**선택 답**

`3`

**확신도**

```text
높음
```

**필요 정보와 위치**

```json
[
  "3문단: 정상적인 데이터라도 특징을 왜곡하는 값 존재, 선수 연봉 예",
  "2문단: 문자 최빈값 및 동률 포함 중앙값",
  "4~5문단: 점 위치 데이터의 특징을 직선으로 나타냄"
]
```

**코드명 없는 최소 논리 구조**

```text
정상 수집된 데이터에도 유달리 큰 값이 있을 수 있다. 그러므로 정상 수집이면 이상치가 없다는 전칭 명제는 반례에 의해 거짓이다.
```

**중간 추론**

```json
[
  "① 직업과 같은 문자도 최빈값 사용 가능",
  "② 직선으로 특징을 나타내는 사례가 있으므로 하나의 수치만으로 표현되는 것은 아님",
  "③ 정상 수집과 이상치 존재는 양립",
  "④ 중복 값에도 순위를 매겨 중앙값 계산 가능",
  "⑤ 측정 오류는 이상치의 주된 원인이지 모든 오류값이 반드시 유달리 크거나 작다는 충분조건이 아님"
]
```

**가장 매력적인 오답**

`5`

**오답의 정확한 오류**

```text
주로 측정 오류 등에 의해 생긴다는 설명을 뒤집어 측정 오류이면 반드시 이상치라고 읽는 오류. 오류값도 다른 값들과 유사할 수 있다.
```

**노출 정보**

```json
{
  "official_answer_seen": false,
  "sdss_seen": false,
  "prior_project_judgment_seen": false,
  "prior_training_exposure": "확인 불가; 이번 세션의 해당 원문 첫 열람"
}
```

**기타 기록 필드**

```json
{
  "passage_group": "G025"
}
```

## 2. 공식 정답 대조

### 공식 정답 대조 — `DV-answer_check-20260913-01`

**최초 선택**

`3`

**공식 정답**

`3`

**기타 기록 필드**

```json
{
  "passage_group": "G025",
  "group_blind_barrier_verified": true,
  "is_correct": true,
  "original_blind_preserved": true,
  "logic_without_codes_fixed": "정상 수집과 이상치 존재는 양립한다. 정상 수집이면 이상치가 없다는 선택지③은 원문의 명시 반례와 충돌한다.",
  "revision_after_answer": "없음",
  "sdss_seen": false
}
```

## 3. 독립 코드 판정

### 독립 코드 판정 — `DV-independent_code-20260913-01`

**주 코드**

```json
[
  {
    "code": 36,
    "name": "반증사례",
    "reason": "선택지③의 정상 수집→이상치 부재를 정상 수집∧이상치 존재라는 본문 반례로 깨는 것이 최소 결정 연산이다."
  }
]
```

**보조 코드**

```json
[
  {
    "code": 14,
    "name": "양립가능",
    "reason": "반례가 보존하는 관계는 정상 수집과 이상치 존재의 공존이다."
  },
  {
    "code": 2,
    "name": "양상",
    "reason": "⑤에서 주된 원인을 예외 없는 발생 조건으로 강화하지 않는다."
  }
]
```

**표면 코드**

```json
[
  {
    "code": 12,
    "name": "조건문",
    "reason": "③의 문장 형식. 여기서는 조건에 따라 결과를 도출하기보다 조건문을 반례로 부정한다."
  }
]
```

**경쟁 코드 및 반증**

```json
[
  {
    "code": 16,
    "reason": "이상치 정의만으로 정상 수집과의 공존이 바로 보장되지는 않는다. 원문 정상 연봉 사례가 결정 증거다."
  },
  {
    "code": 46,
    "reason": "측정 오류의 인과 설명은 배경이다. 원인 추적 없이 정상 수집 반례만으로 정답 확정 가능."
  },
  {
    "code": 4,
    "reason": "전칭 강도 판독은 표현 층위에서 결합하나 실제 기각 증거는 한 반례의 존재다."
  }
]
```

**확신도**

```text
높음
```

**경계 메모**

```text
#36과#14는 여기서 증거 사용 방식과 확보된 양립 관계의 층위 차이. 이 한 사례로 동치/통합 선언하지 않음.
```

**정규화된 주 코드 후보**

```json
[
  {
    "source_key": "primary",
    "value": [
      {
        "code": 36,
        "name": "반증사례",
        "reason": "선택지③의 정상 수집→이상치 부재를 정상 수집∧이상치 존재라는 본문 반례로 깨는 것이 최소 결정 연산이다."
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
        "code": 14,
        "name": "양립가능",
        "reason": "반례가 보존하는 관계는 정상 수집과 이상치 존재의 공존이다."
      },
      {
        "code": 2,
        "name": "양상",
        "reason": "⑤에서 주된 원인을 예외 없는 발생 조건으로 강화하지 않는다."
      }
    ]
  }
]
```

**정규화된 경쟁 코드 및 반증**

```json
[
  {
    "source_key": "competing_codes_refuted",
    "value": [
      {
        "code": 16,
        "reason": "이상치 정의만으로 정상 수집과의 공존이 바로 보장되지는 않는다. 원문 정상 연봉 사례가 결정 증거다."
      },
      {
        "code": 46,
        "reason": "측정 오류의 인과 설명은 배경이다. 원인 추적 없이 정상 수집 반례만으로 정답 확정 가능."
      },
      {
        "code": 4,
        "reason": "전칭 강도 판독은 표현 층위에서 결합하나 실제 기각 증거는 한 반례의 존재다."
      }
    ]
  }
]
```

**기타 기록 필드**

```json
{
  "passage_group": "G025",
  "sdss_seen": false,
  "logic_without_codes": "정상 수집된 선수 연봉 중 극단 연봉이 존재한다는 예로 정상 수집이면 이상치가 없다는 일반 명제를 거부한다."
}
```

## 4. SDSS 사후 대조

> SDSS는 독립 판정 후 공개된 제3자 후보 라벨이다. 이 기록은 독립 판정의 근거로 소급 사용하지 않는다.

### SDSS 사후 대조 — `DV-sdss_compare-20260913-01`

**사이트 원래 코드**

```json
[
  "분기점"
]
```

**사이트 코드 번호**

```json
[
  57
]
```

**독립 주 코드**

```json
[
  36
]
```

**비교**

```text
불일치
```

**의미 비교**

```text
사이트#57은 데이터 유형별 대체 방식 분기나 알고리즘 문턱 분기를 포착했을 가능성은 있으나 적용 위치는 확인되지 않았다. 선택지③을 결정하는 직접 연산은 정상 수집된 이상치 반례. 번호에 맞추어 최초 판정을 수정하지 않음.
```

**독립 판정 보존**

`true`

**SDSS의 역할**

```text
제3자 후보 색인; 정답지 아님
```

**기타 기록 필드**

```json
{
  "passage_group": "G025",
  "all_group_independent_code_records_before_any_group_sdss_disclosure": true
}
```

## 5. 후속 보강

아래 기록은 시간순으로 덧붙였다. 최초 blind·정답·독립 코드 판정을 대체하지 않는다.

### 후속 보강 — `DV-GA-depth_backfill-20260915-semantic-audit-01`

**기타 기록 필드**

```json
{
  "case_ids": [
    "DV",
    "GA"
  ],
  "review_kind": "완료 사례의 사후 semantic audit; 새 blind 판정 아님",
  "original_blind_preserved": true,
  "source_record_ids": [
    "DV-blind-20260913-01",
    "DV-independent_code-20260913-01",
    "GA-blind-20260914-02",
    "GA-independent_code-20260914-02"
  ],
  "evidence_additions": [
    {
      "case": "DV",
      "passage_group": "G025",
      "source": "data/기본기_연구/prepared_backlog/blind_sources/DV.json",
      "task": "윗글 이해, 적절하지 않은 선지 선택",
      "target": "③ 전체 조건문",
      "evidence_location": "passage_text 3문단: 정상적인 데이터라도 특징을 왜곡하는 값이 있을 수 있다; 선수 연봉 예. choices[2]",
      "relation_without_codes": "P=정상 수집, Q=이상치 없음. 선지는 P→Q, 본문은 P와 이상치 존재의 양립 가능성을 직접 예시한다.",
      "changed_part": "정상 수집을 이상치 부재의 충분조건으로 강화",
      "decisive_operation": "정상 연봉 데이터에 극단 연봉이 포함되는 허용 사례를 대입해 P→Q를 기각",
      "evidence_type": "명시 반례",
      "evidence_qualification": "실제 관측 통계가 아니라 본문이 명시한 가능한 반례 상황. 모든 정상 데이터에 이상치가 있다는 뜻은 아님.",
      "existing_code_layers": "최초 주#36=반례 사용 수행/증거, 보조#14=양립 관계, 보조#2=⑤의 강도 판독, 표면#12=③ 조건문 형식. 기존 번호 보존.",
      "strongest_competitor": "#12로 ③을 조건식으로 쓰고 P∧¬Q를 대입하거나 #14로 정상 수집/이상치 존재의 양립을 확인해도 동일 결론이다.",
      "competitor_relation": "상위/하위 층위: #12 관계 형식과 #36 증거 사용. 반례 대입을 포함한 두 표현은 같은 국소 수행의 다른 표현.",
      "unique_primary": "기존#36 대표는 유지하되 모든 층을 대표하는 유일 코드라고 확정하지 않음",
      "unresolved": "⑤의 가능성은 실제 측정 오류 비이상치 사례가 명시된 것과 다름. 이 문항 정답③의 반례 근거를⑤까지 전이하지 않음."
    },
    {
      "case": "GA",
      "passage_group": "G037",
      "source": "data/기본기_연구/prepared_backlog/blind_sources/GA.json",
      "task": "(가)로 알 수 있는 내용 중 적절하지 않은 선지 선택",
      "target": "④ 후반 절: 값어치가 일치해야 계약이 체결된다",
      "evidence_location": "(가)3문단: 계약 체결 당시부터 있던 하자 때문에 대금만큼의 값어치를 하지 못하는 상태였다면 매도인이 책임; choices[3]",
      "relation_without_codes": "P=계약 체결, Q=교환 대상의 값어치 일치. 하자 있는 매매에 책임/파기 가능성을 부여하는 서술은 체결된 계약과 당시 값어치 미달의 양립을 허용한다.",
      "changed_part": "거래 대상 값어치에 대한 담보 책임을 계약 체결 이전의 필수요건으로 옮김",
      "decisive_operation": "체결된 하자 매매의 허용 상황을 복원하고 P∧¬Q를 선지 P→Q에 대입",
      "evidence_type": "합성 함의",
      "evidence_qualification": "반례 사용은 맞지만 DV처럼 별도의 구체 예가 직접 제시된 것은 아니다. 조건문만으로 실제 사례의 존재를 논리적으로 도출하지 않는다. 본문이 허용하는 계약 상황을 해석하여 반례를 구성한 것.",
      "existing_code_layers": "최초 주#10=선지가 추가한 필요조건 관계, 보조#36=기각 증거/수행, 표면#3=시점 표현, #8=③ 배당 순위. 기존 번호 보존.",
      "strongest_competitor": "#12의 체결→값어치 일치 표기와 #36의 하자 매매 대입은 #10 판독과 같은 결론을 낸다. 유상 계약 정의만 읽고 모든 약속이면 무조건 유효 체결이라고 단정하는 약한 대안은 채택하지 않는다.",
      "competitor_relation": "#10/#12 같은 국소 관계의 다른 표현; #10/#36 관계와 증거 사용의 층위 차이",
      "unique_primary": "관계 층의#10와 수행 층의#36 중 하나를 전체 유일 주 코드로 확정하지 않음",
      "unresolved": "원저자의#10/#36 전역 분류 정의 미확보; 법률 현실의 유효성 요건 전반을 이 독해 판단으로 일반화하지 않음"
    }
  ],
  "boundary_or_generation_impact": "두 사례의 반증 골격은 같지만 증거 직접성은 다르다. O3를 조건 형식·명제 강도·증거 상태의 별도 축으로 수정. 원 판정의 주 코드 차이를 풀이 행동 불일치로 세지 않는다.",
  "candidate_rule": {
    "decision": "수정",
    "retained": "P→Q를 허용된 P∧¬Q로 기각",
    "counterexample": "GA는 반례 상황 복원에 문맥 연결이 필요하므로 두 사례 모두 직접 명시 반례라는 일괄 표기는 부정확",
    "held": "반례 사용과 필요조건 판독의 코드 통합",
    "next_falsification_target": "완료 anchor 밖 새 자료는 열지 않음. 향후 P→Q만 있고 역조건이나 P∧¬Q의 근거가 없는 지문에서 지지 부족과 모순을 구분"
  },
  "minimal_variants": [
    {
      "case": "DV",
      "one_change": "③의 '존재하지 않는다'를 '존재할 수 있다'로 교체",
      "predicted_change": "③은 본문이 직접 지지하는 적절한 진술로 바뀜. 문항 전체 유일답은 재검증 필요",
      "synthetic_not_corpus": true
    },
    {
      "case": "GA",
      "one_change": "④의 '일치해야 계약이 체결된다'를 '일치하지 않아도 계약이 체결될 수 있다'로 교체",
      "predicted_change": "필수요건 추가 오류가 해소됨",
      "synthetic_not_corpus": true
    }
  ],
  "student_action": "'해야'가 무엇의 조건인지 먼저 표시한 뒤, 본문에서 그 일이 성립하면서 조건은 없는 상황이 허용되는지 찾는다. 반례가 없다는 사실만으로 역조건을 참이나 거짓으로 확정하지 않는다.",
  "generation_principle": "책임/효과 규정의 내용을 성립 요건으로 옮기거나, 주된 발생 경향을 예외 없는 조건으로 강화한다. 기각용 반례 또는 지지 부족 여부를 출제 전에 구분한다.",
  "sampling": {
    "cases": 2,
    "distinct_passage_groups": 2,
    "new_corpus_cases": 0
  },
  "confidence": "국소 판단 높음; GA 증거 분류는 본문 문맥의 허용 상황 해석에 한정; 전역 코드 우선순위 유보"
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

- `G025-induction-20260913-01` — 집단 귀납 기록 (집단/교차 사례 기록; 개별 case 판단으로 변환하지 않음)
- `META-G025-G027-meta_induction-20260913-01` — 교차 사례 귀납 기록 (집단/교차 사례 기록; 개별 case 판단으로 변환하지 않음)

## 6. 원장 추적

사용된 원장 record_id (queue 순서):
- `DV-blind-20260913-01` — 최초 blind 풀이 / done
- `DV-answer_check-20260913-01` — 공식 정답 대조 / done
- `DV-independent_code-20260913-01` — 독립 코드 판정 / done
- `DV-sdss_compare-20260913-01` — SDSS 사후 대조 / done
- `G025-induction-20260913-01` — 집단 귀납 기록 / done
- `META-G025-G027-meta_induction-20260913-01` — 교차 사례 귀납 기록 / done
- `DV-GA-depth_backfill-20260915-semantic-audit-01` — 후속 보강 / done
- `ANCHORS-O1-O8-boundary_revision-20260915-semantic-audit-01` — 경계 수정 기록 / done
