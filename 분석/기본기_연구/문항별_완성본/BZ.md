> 이 파일은 원장으로부터 자동 생성된 열람용 파생본이다. 연구의 authoritative source는 raw queue이며, 이 파일을 직접 편집하지 않는다.

# BZ

## 0. 문항 정보

- **Passage group:** G014

### 제시문

```text
주차하거나 좁은 길을 지날 때 운전자를 돕는 장치들이 있다. 이 중 차량 전후좌우에 장착된 카메라로 촬영한 영상을 이용하여 차량 주위 360 °의 상황을 위에서 내려다본 것 같은 영상을 만들어 차 안의 모니터를 통해 운전자에게 제공하는 장치가있다. 운전자에게 제공되는 영상이 어떻게 만들어지는지 알아보자.

먼저 차량 주위 바닥에 바둑판 모양의 격자판을 펴 놓고 카메라로 촬영한다. 이 장치에서 사용하는 광각 카메라는 큰 시야각을 갖고 있어 사각지대가 줄지만 빛이 렌즈를 ⓐ 지날 때 렌즈 고유의 곡률로 인해 영상이 중심부는 볼록하고 중심부에서 멀수록 더 휘어지는 현상, 즉 렌즈에 의한 상의 왜곡이 발생한다. 이 왜곡에 영향을 주는 카메라 자체의 특징을 내부 변수라고 하며 왜곡 계수로 나타낸다. 이를 알 수 있다면 왜곡 모델을 설정하여 왜곡을 보정할 수 있다. 한편 차량에 장착된 카메라의 기울어짐 등으로 인해 발생하는 왜곡의 원인을 외부 변수라고 한다. ㉠ 촬영된 영상과 실세계 격자판을 비교하면 영상에서 격자판이 회전한 각도나 격자판의 위치 변화를 통해 카메라의 기울어진 각도 등을 알 수 있으므로 왜곡을 보정할 수 있다.

왜곡 보정이 끝나면 영상의 점들에 대응하는 3차원 실세계의 점들을 추정하여 이로부터 원근 효과가 제거된 영상을 얻는 시점 변환이 필요하다. 카메라가 3차원 실세계를 2차원 영상으로 투영하면 크기가 동일한 물체라도 카메라로부터 멀리 있을수록 더 작게 나타나는데, 위에서 내려다보는 시점의 영상에서는 거리에 따른 물체의 크기 변화가 없어야 하기 때문이다.

㉡ 왜곡이 보정된 영상에서의 몇 개의 점과 그에 대응하는 실세계 격자판의 점들의 위치를 알고 있다면, 영상의 모든 점들과 격자판의 점들 간의 대응 관계를 가상의 좌표계를 이용하여 기술할 수 있다. 이 대응 관계를 이용해서 영상의 점들을 격자의 모양과 격자 간의 상대적인 크기가 실세계에서와 동일하게 유지되도록 한 평면에 놓으면 2차원 영상으로 나타난다. 이때 얻은 영상이 ㉢ 위에서 내려다보는 시점의 영상이 된다. 이와 같은 방법으로 구한 각 방향의 영상을 합성하면 차량 주위를 위에서 내려다본 것 같은 영상이 만들어진다.
```

### 발문

```text
㉠~㉢을 이해한 내용으로 가장 적절한 것은?
```

### 선지

```json
[
  "㉠에서 광각 카메라를 이용하여 확보한 시야각은 ㉡에서는 작아지겠군.",
  "㉡에서는 ㉠과 마찬가지로 렌즈와 격자판 사이의 거리가 멀어질수록 격자판이 작아 보이겠군.",
  "㉡에서는 ㉠에서 렌즈와 격자판 사이의 거리에 따른 렌즈의 곡률 변화로 생긴 휘어짐이 보정되었겠군.",
  "㉡과 실세계 격자판을 비교하여 격자판의 위치 변화를 보정한 ㉢은 카메라의 기울어짐에 의한 왜곡을 바로잡은 것이겠군.",
  "㉡에서 렌즈에 의한 상의 왜곡 때문에 격자판의 윗부분으로 갈수록 격자 크기가 더 작아 보이던 것이 ㉢에서 보정되었겠군."
]
```

### 원문 자료 감사

```json
{
  "case_id": "BZ",
  "source_file_exists": true,
  "mechanically_linked": true,
  "assets": [
    {
      "path": "prepared_backlog/blind_sources/BZ.json",
      "exists": false,
      "kind": "supplement_or_source"
    },
    {
      "path": "sealed/answer_sdss.jsonl official_answer_verified",
      "exists": false,
      "kind": "supplement_or_source"
    },
    {
      "path": "각 blind_source 및 sealed/answer_sdss.jsonl 해당 행",
      "exists": false,
      "kind": "supplement_or_source"
    }
  ],
  "image_files_exist": true,
  "image_meaning_verified": false,
  "choice_count": 5,
  "all_choices_empty": false,
  "warnings": [
    "참조한 보충/원문 자산이 export에 없음: prepared_backlog/blind_sources/BZ.json, sealed/answer_sdss.jsonl official_answer_verified, 각 blind_source 및 sealed/answer_sdss.jsonl 해당 행"
  ],
  "ready": false
}
```

## 1. 최초 blind 풀이

### 최초 blind 풀이 — `BZ-blind-20260910-01`

**선택 답**

`2`

**확신도**

`0.99`

**코드명 없는 최소 논리 구조**

```text
㉡은 렌즈·설치 왜곡을 보정했지만 아직 원근 효과를 제거하는 시점 변환 전이다. 그러므로 ㉠처럼 멀수록 작게 보인다는 ②가 맞다.
```

**중간 추론**

```json
[
  "① 왜곡 보정으로 카메라 시야각 자체가 작아진다는 근거 없음.",
  "③ 렌즈 곡률은 고유 특징이지 격자판 거리 때문에 변한다고 한 것이 아님.",
  "④ 카메라 기울기 보정은 ㉠→㉡ 단계인데 ㉡→㉢에 옮김.",
  "⑤ ㉡의 원근에 의한 크기 차이를 렌즈 왜곡 때문이라고 잘못 귀속."
]
```

**가장 매력적인 오답**

```json
{
  "choice": 5,
  "error": "㉢에서 멀리 있는 격자도 상대적 크기가 복원된다는 결과는 맞지만 ㉡에 남은 원인을 렌즈 왜곡이라고 한 점이 틀림."
}
```

**노출 정보**

```text
이번 세션 G014 답·태그·기존 판정 미노출. 과거 노출 unknown, strict blind 확정 제외.
```

**기타 기록 필드**

```json
{
  "passage_group": "G014",
  "source": "prepared_backlog/blind_sources/BZ.json",
  "necessary_information_and_locations": [
    "2문단 ㉠ 렌즈 자체 왜곡과 카메라 기울기 왜곡 보정",
    "3문단 왜곡 보정 후에도 원근 효과 제거 위한 시점 변환 필요",
    "4문단 ㉡ 왜곡 보정된 영상→좌표 대응→㉢ 내려다보는 영상"
  ]
}
```

## 2. 공식 정답 대조

### 공식 정답 대조 — `BZ-answer_check-20260910-01`

**공식 정답**

`2`

**일치 여부**

`true`

**정답 대조 reasoning**

```text
왜곡 보정 완료는 원근 효과 제거 완료가 아니다. ㉡은 시점 변환 전이라 멀수록 작아 보임.
```

**기타 기록 필드**

```json
{
  "passage_group": "G014",
  "barrier": "BY·BZ·CA·CB 전체 blind done raw 저장 후 정답만 공개",
  "first_record_preserved": true,
  "source": "sealed/answer_sdss.jsonl official_answer_verified",
  "sdss_exposure": "미공개"
}
```

## 3. 독립 코드 판정

### 독립 코드 판정 — `BZ-independent_code-20260910-01`

**주 코드**

```json
[
  {
    "code": 45,
    "reason": "왜곡 보정의 출력㉡과 시점 변환의 출력㉢에 남는/제거되는 영상 특성을 단계별로 대응."
  }
]
```

**보조 코드**

```json
[
  {
    "code": 5,
    "reason": "㉠→㉡에서 원근 효과는 유지되며 ㉢에서 제거됨."
  },
  {
    "code": 3,
    "reason": "시점 변환이 왜곡 보정 이후라는 순서를 유지."
  },
  {
    "code": 46,
    "reason": "③⑤에서 렌즈 곡률과 거리 변화의 원인 귀속 오류를 구별."
  }
]
```

**표면 코드**

```json
[
  {
    "code": 86,
    "reason": "멀수록 작다는 크기 어휘가 있으나 정량적 대소 계산보다 남은 효과 식별이 핵심."
  }
]
```

**경쟁 코드 및 반증**

```json
[
  {
    "code": 49,
    "rejection": "거리-크기 반대 방향을 알기만 해서는 왜 ㉡에 여전히 그 관계가 남는지 설명 못함. 단계의 산출 특성 복원이 선행되어야 함."
  },
  {
    "code": 55,
    "rejection": "오답③⑤의 원인 오귀속은 후보로 인정하나 참인 ② 결정의 주 연산은 단계별 특성 유지다. 명시 인과 오류가 필요한 선지에 한해 보조 적용 가능."
  },
  {
    "code": 19,
    "rejection": "후속 단계가 앞 단계의 미제거 효과를 처리하지만 새 해결책을 제안/평가하는 과제는 아님."
  }
]
```

**확신도**

```text
높음(단계 대응), 중간(주 번호의 유일성)
```

**경계 메모**

```text
왜곡이라는 일상적 포괄어에 원근 효과를 합쳐 모든 왜곡이 제거됐다고 읽지 않는다. 본문이 별도 단계로 정의한 효과를 유지한다.
```

**정규화된 주 코드 후보**

```json
[
  {
    "source_key": "primary",
    "value": [
      {
        "code": 45,
        "reason": "왜곡 보정의 출력㉡과 시점 변환의 출력㉢에 남는/제거되는 영상 특성을 단계별로 대응."
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
        "code": 5,
        "reason": "㉠→㉡에서 원근 효과는 유지되며 ㉢에서 제거됨."
      },
      {
        "code": 3,
        "reason": "시점 변환이 왜곡 보정 이후라는 순서를 유지."
      },
      {
        "code": 46,
        "reason": "③⑤에서 렌즈 곡률과 거리 변화의 원인 귀속 오류를 구별."
      }
    ]
  }
]
```

**정규화된 경쟁 코드 및 반증**

```json
[
  {
    "source_key": "competitors",
    "value": [
      {
        "code": 49,
        "rejection": "거리-크기 반대 방향을 알기만 해서는 왜 ㉡에 여전히 그 관계가 남는지 설명 못함. 단계의 산출 특성 복원이 선행되어야 함."
      },
      {
        "code": 55,
        "rejection": "오답③⑤의 원인 오귀속은 후보로 인정하나 참인 ② 결정의 주 연산은 단계별 특성 유지다. 명시 인과 오류가 필요한 선지에 한해 보조 적용 가능."
      },
      {
        "code": 19,
        "rejection": "후속 단계가 앞 단계의 미제거 효과를 처리하지만 새 해결책을 제안/평가하는 과제는 아님."
      }
    ]
  }
]
```

**기타 기록 필드**

```json
{
  "passage_group": "G014",
  "barrier": "group 전체 answer_check 완료; SDSS 미공개"
}
```

## 4. SDSS 사후 대조

> SDSS는 독립 판정 후 공개된 제3자 후보 라벨이다. 이 기록은 독립 판정의 근거로 소급 사용하지 않는다.

### SDSS 사후 대조 — `BZ-sdss_compare-20260910-01`

**사이트 원래 코드**

```json
[
  "함수",
  "허위적인과"
]
```

**사이트 코드 번호**

```json
[
  45,
  55
]
```

**독립 주 코드**

```json
[
  45
]
```

**비교**

```text
주 #45 일치. 공개 전 #55 경쟁 검토에서 이미 오답③⑤의 원인 오귀속을 인정했다. ③은 거리 변화가 렌즈 곡률을 바꾼다고 하고, ⑤는 원근에 의한 크기 차이를 렌즈 왜곡 때문이라고 명시한다.
```

**SDSS의 역할**

```text
제3자 후보 색인
```

**기타 기록 필드**

```json
{
  "passage_group": "G014",
  "barrier": "BY~CB 전체 independent_code raw 저장 확인 후 공개",
  "decision": "#55는 특정 오답 설명, #45는 정답②의 단계별 산출 특성 설명으로 구분. 최초 판정 변경 없음.",
  "source": "각 blind_source 및 sealed/answer_sdss.jsonl 해당 행"
}
```

## 5. 후속 보강

아래 기록은 시간순으로 덧붙였다. 최초 blind·정답·독립 코드 판정을 대체하지 않는다.

### 후속 보강 — `AB-BZ-CT-GC-depth_backfill-20260915-semantic-audit-01`

**기타 기록 필드**

```json
{
  "case_ids": [
    "AB",
    "BZ",
    "CT",
    "GC"
  ],
  "original_blind_preserved": true,
  "review_kind": "완료 사례 사후 감사; 법률 지문의 내부 독해이며 현행법 일반에 대한 주장 아님",
  "source_record_ids": [
    "AB-independent_code-20260909-01",
    "BZ-independent_code-20260910-01",
    "CT-hold-20260911-source-check-01",
    "CT-blind-20260911-01",
    "CT-independent_code-20260911-01",
    "GC-independent_code-20260914-02",
    "GC-depth_backfill-20260914-02"
  ],
  "evidence_additions": [
    {
      "case": "AB",
      "passage_group": "G001",
      "source": "data/기본기_연구/prepared_backlog/blind_sources/AB.json",
      "task": "보기 대법원 입장 추론 중 부적절 선지 선택",
      "target": "④ 인과 관계 존재 입증 책임의 주체",
      "evidence_location": "5문단 '입증 책임은 여전히 피해자인 원고', '원칙을 바꾸지는 않는다', '정도를 낮추어'; 보기 세 연결 중 폐수 도달만 증명하면 충분; choices[3:5]",
      "changed_element": "인과 인정에 요구되는 증명 정도/항목",
      "retained_element": "인과 관계 존재의 입증 책임자는 원고",
      "retention_warrant": "원문이 책임 주체 유지와 인정 후 피고의 방해 증거 제출을 각각 명시",
      "wrong_extension": "피고의 사후 방해 증거 제출을 인과 존재 입증 책임 자체가 회사로 이전된 것으로 확대",
      "decisive_operation": "증명 명제·주체·단계를 나누어④와⑤를 대조",
      "evidence_type": "직접 함의",
      "existing_code_layers": "주#24=원칙/예외 범위, 보조#5=변경/유지·#3=⑤ 시점·#16=입증 책임 뜻, 표면#46=인과 소재",
      "strongest_competitor": "#17식 (원고, 인과 존재, 완화된 인정 전), (피고, 성립 방해 증거, 인정 후) 귀속표도 같은 답을 낸다. #12로 공해 소송일 때도 원고 책임이라는 구체 조건 결과를 쓰면 가능",
      "competitor_relation": "같은 국소 수행의 다른 표현; 수치 조건 적용과 책임 명제 구분을 지운 설명은 불충분",
      "priority": "최초#24 유지, 유일한 인지 경로라고 주장하지 않음"
    },
    {
      "case": "BZ",
      "passage_group": "G014",
      "source": "data/기본기_연구/prepared_backlog/blind_sources/BZ.json",
      "task": "㉠~㉢ 이해 중 가장 적절한 선지 선택",
      "target": "정답② ㉠과㉡에 남은 원근 효과; 오답⑤ 원인 귀속",
      "evidence_location": "2문단 렌즈/기울기 왜곡 보정; 3문단 '왜곡 보정이 끝나면 ... 원근 효과가 제거된 ... 시점 변환이 필요'; 4문단㉡→㉢; choices[1], choices[4]",
      "changed_element": "㉠→㉡에서 렌즈/설치 왜곡, ㉡→㉢에서 원근 효과",
      "retained_element": "㉡까지 거리 증가에 따른 격자의 작아 보임",
      "retention_warrant": "보정 뒤에도 별도로 원근 효과를 제거해야 한다는 단계 규정. 침묵을 근거로 임의 보존하지 않음",
      "wrong_extension": "앞 보정의 제거 범위를 원근 효과까지 확장하거나, 뒤 시점 변환의 목적을 렌즈/기울기 보정으로 바꿈",
      "decisive_operation": "단계별 제거 대상/잔존 효과 표에서② 확인",
      "evidence_type": "합성 함의",
      "existing_code_layers": "실제 raw 주#45, 보조#5/#3/#46, 표면#86. 검토 보고서 O2 표의#24·#5·#22·#12만으로 이 사례 번호를 대체하면 안 됨",
      "strongest_competitor": "#5로㉠㉡㉢의 원근 효과 유/유/무 상태표를 만들면 정답 결정. #45의 단계 입출력표와 동일 정보를 보존",
      "competitor_relation": "같은 국소 수행의 다른 표현",
      "priority": "최초#45 유지, #5 대비 유일 우선순위 유보",
      "counterexample": "O2를 모두 법칙의 예외 적용이라고 부르면 BZ가 맞지 않는다. 정상적인 순차 공정의 처리 범위 구분이다. 또한① 시야각 감소는 직접 반대 진술보다 지지 부족으로 구별"
    },
    {
      "case": "CT",
      "passage_group": "G018",
      "source": "data/기본기_연구/prepared_backlog/blind_sources/CT.json",
      "supplements": [
        "data/기본기_연구/prepared_backlog/blind_sources/CT_source_supplement.json",
        "data/기본기_연구/prepared_backlog/blind_sources/CT_equation_supplement.json"
      ],
      "provenance": [
        "data/기본기_연구/prepared_backlog/sealed/CT_source_provenance.json",
        "data/기본기_연구/prepared_backlog/sealed/CT_equation_provenance.json"
      ],
      "task": "보기 계산 결과 중 부적절 선지 선택",
      "target": "④ 노력 상승인 경우 반환 지분 1/3",
      "evidence_location": "2·3문단 유류분/부족액; 5문단 마지막 '시가 상승의 원인이 무엇이든 상속 개시 당시'; 보기 A300→700 B100; equation_supplement equations[0:3]",
      "source_fidelity": "CT.json과 최초 source_supplement는 선지 분수 누락. 후속 equation_supplement의 XML script가 본문1/2, ②3/7, ④1/3을 보완한다. 이 세 값과 기존 연결 provenance를 읽었음. 공식 원 배포 PDF/원 페이지 그림을 이번에 직접 검증했다는 뜻은 아님",
      "changed_element": "노력 상승이면 부족액 산정에 넣는 A 가치700→300",
      "retained_element": "지분 분모700; B에서 이미 받은100; 유류분 비율1/2",
      "retention_warrant": "분모는 원인 무관 상속 개시 시가라는 명시 문장, B100은 보기의 두 경우 공통 조건",
      "wrong_extension": "부족액 평가 기준의 취득 시가 예외를 지분 분모로 전이",
      "decisive_operation": "노력 있음: (300+100)/2−100=100, 100/700=1/7≠1/3. 노력 없음: (700+100)/2−100=300, 300/700=3/7. ⑤는 실제 남긴 B에서100으로 동일",
      "evidence_type": "합성 함의",
      "existing_code_layers": "주#84=분모/지분 관계·#24=예외 범위, 보조#92=계산·#3=시점·#16=⑤ 개념 구별, 표면#85",
      "strongest_competitor": "#45 조건부 함수 D(e)=((e?300:700)+100)/2−100, R(e)=D(e)/700도 정확히 같은 답을 낸다. #24 범위 표시만 하고 수량 관계를 생략하면 선지1/3을 판별할 수 없음",
      "competitor_relation": "완전 함수식은 같은 수행의 다른 표현; 범위 선택에 더해 산술 합성은 별개의 추가 수행",
      "priority": "원 두 주 코드 유지; O2만으로 풀이 완료한다고 축약하지 않음"
    },
    {
      "case": "GC",
      "passage_group": "G037",
      "source": "data/기본기_연구/prepared_backlog/blind_sources/GC.json",
      "task": "연대 보증인 이해 중 가장 적절한 선지 선택",
      "target": "⑤ 주채무 이행 후 보증 의무; ②는 별도 해석 주장",
      "evidence_location": "(나)1문단 주채무 소멸→보증 채무 소멸; 3문단 '이러한 권리를 포기'하는 연대 특약; 4문단 해석 방법에 따른 결론 차이; choices[4], choices[1]",
      "changed_element": "직접 청구에 대한 거절권 포기",
      "retained_element": "보증의 주채무 소멸 시 보증 채무 소멸 규칙",
      "retention_warrant": "연대 특약은 보증 계약에 포함되는 특정 권리 포기로 규정; 보증 전체에 대한 소멸 규칙이 앞에 명시됨",
      "wrong_extension": "거절권 소멸을 주채무 이행 이후까지 독립적인 지급 의무가 존속한다는 것으로 확대",
      "decisive_operation": "주채무자 이행→채권 실현/주채무 소멸→보증 채무 소멸",
      "evidence_type": "합성 함의",
      "existing_code_layers": "주#12 조건 적용, 보조#24 예외 범위·#17④ 당사자 귀속, 표면#3② 시점 접점",
      "strongest_competitor": "#22로 연대 보증⊂보증과 모든 보증의 주채무 종속 규칙을 적용해도⑤가 나온다. #10로 보증 채무 존속의 필요조건을 주채무 존속으로 놓고 대우 적용도 가능",
      "competitor_relation": "#12/#22/#10 완전 규칙을 포함하면 같은 국소 수행의 다른 표현; 법적 종속을 물리 인과로 치환하는 설명은 배제",
      "priority": "최초#12와 과거#12/#22 유보 유지",
      "unresolved": "②는 미해결. 직접 청구 가능과 '주채무자가 이행하지 않는 경우'가 논리적으로 양립 불가능하다고 입증되지 않음. 입법 취지를 문리 근거로 옮기면 안 된다는 지적만으로②의 반대까지 증명하지 않는다.⑤ 근거 확보와 모든 선지의 엄밀 배제 완료를 구분"
    }
  ],
  "boundary_or_generation_impact": "O2를 '명시된 처리/특례의 범위를 한정하고 별도로 근거 있는 관계를 유지'로 수정. AB는 직접 유지 명시, BZ는 단계 구분, CT는 예외 비적용 명시+계산, GC는 보증 하위유형과 일반 규칙 적용으로 근거 종류가 다름.",
  "candidate_rule": {
    "decision": "수정",
    "retained": "변경과 유지의 근거를 각각 찾음",
    "counterexample": "BZ는 예외가 아니며 CT는 보존만으로 수치 판단 불가",
    "held": "예외이면 언급 없는 모든 속성을 자동 보존한다는 규칙은 채택하지 않음; GC② 유보",
    "next_falsification_target": "후속 미열람 지문에서 예외가 두 속성을 함께 바꾸거나 앞 처리의 간접 효과로 뒤 상태도 변하는 명시 사례. 이번에는 열지 않음"
  },
  "minimal_variants": [
    {
      "case": "AB",
      "one_change": "④의 '회사 쪽'을 '어민들 쪽'으로 교체",
      "predicted_change": "책임 주체 오귀속 해소",
      "synthetic_not_corpus": true
    },
    {
      "case": "BZ",
      "one_change": "② 첫 ㉡을㉢으로 교체",
      "predicted_change": "원근 효과 제거 후에도 멀수록 작다는 진술이 되어 부적절",
      "synthetic_not_corpus": true
    },
    {
      "case": "CT",
      "one_change": "④ 분수1/3을1/7로 교체",
      "predicted_change": "④ 계산 오류 해소. 모든 선택지가 적절해질 수 있으므로 완성 문항으로 세지 않음",
      "synthetic_not_corpus": true
    },
    {
      "case": "GC",
      "one_change": "⑤의 '더 이상 ... 의무가 없다'를 '여전히 ... 의무가 있다'로 교체",
      "predicted_change": "주채무 소멸 규칙과 충돌",
      "synthetic_not_corpus": true
    }
  ],
  "student_action": "무엇이 달라졌는지와 무엇이 남는지 각각 근거 문장을 붙인다. 계산식의 같은 숫자라도 어느 단계 값인지 표시하고, 명시된 일반 규칙·상위 유형·공정 순서가 없으면 침묵만으로 유지라고 단정하지 않는다.",
  "generation_principle": "앞 단계/특례의 결과를 인접 단계에 옮기는 오답을 만들되, 보존 근거를 지문에 실제로 제공한다. CT형은 계산 단계를 생략하지 않는다.",
  "sampling": {
    "cases": 4,
    "distinct_passage_groups": 4,
    "new_corpus_cases": 0,
    "cross_record_dependency": "GC와 앞 DV/GA 검토의 GA는 같은G037"
  },
  "confidence": "핵심 선지 높음; CT 원 배포본 직접 검증 및 GC② 상세 배제는 유보"
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

- `G014-induction-20260910-01` — 집단 귀납 기록 (집단/교차 사례 기록; 개별 case 판단으로 변환하지 않음)
- `META-G001-G014-meta_induction-20260910-01` — 교차 사례 귀납 기록 (집단/교차 사례 기록; 개별 case 판단으로 변환하지 않음)

## 6. 원장 추적

사용된 원장 record_id (queue 순서):
- `BZ-blind-20260910-01` — 최초 blind 풀이 / done
- `BZ-answer_check-20260910-01` — 공식 정답 대조 / done
- `BZ-independent_code-20260910-01` — 독립 코드 판정 / done
- `BZ-sdss_compare-20260910-01` — SDSS 사후 대조 / done
- `G014-induction-20260910-01` — 집단 귀납 기록 / done
- `META-G001-G014-meta_induction-20260910-01` — 교차 사례 귀납 기록 / done
- `AB-BZ-CT-GC-depth_backfill-20260915-semantic-audit-01` — 후속 보강 / done
- `ANCHORS-O1-O8-boundary_revision-20260915-semantic-audit-01` — 경계 수정 기록 / done
