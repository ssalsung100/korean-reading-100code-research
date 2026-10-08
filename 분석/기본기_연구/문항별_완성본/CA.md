> 이 파일은 원장으로부터 자동 생성된 열람용 파생본이다. 연구의 authoritative source는 raw queue이며, 이 파일을 직접 편집하지 않는다.

# CA

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
윗글을 바탕으로 &lt;보기&gt;를 탐구한 내용으로 가장 적절한 것은? [3점]

&lt; 보 기 &gt;

그림은 장치가 장착된 차량의 운전자에게 제공된 영상에서 전방 부분만 보여 준 것이다. 차량 전방의 바닥에 그려진 네 개의 도형이 영상에서 각각 A, B, C, D로 나타나 있고, C와 D는 직사각형이고 크기는 같다. p와 q는 각각 영상 속 임의의 한 점이다.
```

### 선지

```json
[
  "원근 효과가 제거되기 전의 영상에서 C는 윗변이 아랫변보다 긴 사다리꼴 모양이다.",
  "시점 변환 전의 영상에서 D는 C보다 더 작은 크기로 영상의 더 아래쪽에 위치한다.",
  "A와 B는 p와 q 간의 대응 관계를 이용하여 바닥에 그려진 도형을 크기가 유지되도록 한 평면에 놓은 것이다.",
  "B에 대한 A의 상대적 크기는 가상의 좌표계를 이용하여 시점을 변환하기 전의 영상에서보다 더 커진 것이다.",
  "p가 A 위의 한 점이라면 A는 p에 대응하는 실세계의 점이 시점 변환을 통해 선으로 나타난 것이다."
]
```

### 원문 자료 감사

```json
{
  "case_id": "CA",
  "source_file_exists": true,
  "mechanically_linked": true,
  "assets": [
    {
      "path": "prepared_backlog/blind_sources/CA.json",
      "exists": false,
      "kind": "supplement_or_source"
    },
    {
      "path": "prepared_backlog/blind_sources/CA_supplement_20260910.json",
      "exists": false,
      "kind": "supplement_or_source"
    },
    {
      "path": "prepared_backlog/blind_sources/CA_assets/CA_question16_figure.bmp",
      "exists": false,
      "kind": "image"
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
  "image_files_exist": false,
  "image_meaning_verified": false,
  "choice_count": 5,
  "all_choices_empty": false,
  "warnings": [
    "참조한 보충/원문 자산이 export에 없음: prepared_backlog/blind_sources/CA.json, prepared_backlog/blind_sources/CA_supplement_20260910.json, prepared_backlog/blind_sources/CA_assets/CA_question16_figure.bmp, sealed/answer_sdss.jsonl official_answer_verified, 각 blind_source 및 sealed/answer_sdss.jsonl 해당 행"
  ],
  "ready": false
}
```

## 1. 최초 blind 풀이

### 최초 blind 풀이 — `CA-blind-20260910-01`

**선택 답**

`4`

**확신도**

`0.99`

**코드명 없는 최소 논리 구조**

```text
A는 B보다 멀어 변환 전에는 더 강하게 축소된다. 원근 효과 제거 후 A/B 크기 비는 변환 전보다 커지므로 ④가 맞다.
```

**중간 추론**

```json
[
  "① C의 윗변은 더 멀므로 변환 전에는 아랫변보다 짧게 보임.",
  "② D는 C보다 가까우므로 변환 전 더 아래쪽인 것은 맞지만 더 작은 것은 아님.",
  "③ p와 q는 모두 영상 속 점. 필요한 대응은 영상의 점과 실세계의 대응점 사이의 관계.",
  "⑤ 한 점에 대응하는 실세계 점이 선 전체로 바뀌는 것이 아님. 선 A는 여러 점의 집합.",
  "A가 변환 후에도 B보다 짧다는 그림의 절대 비교와, A/B 비가 변환 전보다 증가했다는 비교는 양립."
]
```

**가장 매력적인 오답**

```json
{
  "choice": 2,
  "error": "그림에서 D가 아래쪽이라는 참인 위치 설명에 끌리기 쉬우나, 동일 실제 크기의 더 가까운 D는 변환 전 더 크게 보여야 함."
}
```

**노출 정보**

```text
이번 G014 정답·태그·기존 판정 미노출. 과거 노출 unknown, strict blind 확정 제외. 그림 누락 상태에서는 답을 저장하지 않았고 복원 그림 직접 판독 후 최초 답 저장.
```

**기타 기록 필드**

```json
{
  "passage_group": "G014",
  "source": [
    "prepared_backlog/blind_sources/CA.json",
    "prepared_backlog/blind_sources/CA_supplement_20260910.json",
    "prepared_backlog/blind_sources/CA_assets/CA_question16_figure.bmp"
  ],
  "necessary_information_and_locations": [
    "그림: 차량 전진 방향 위쪽. A는 B보다 위쪽/먼 곳, C는 D보다 위쪽/먼 곳. p는 A 위 한 점, q는 B 위 한 점.",
    "본문3~4문단: 먼 물체는 원래 영상에서 작게 보이며 시점 변환 후 격자의 상대적 크기를 실세계와 동일하게 복원."
  ],
  "quality_note": "manifest visual_placeholder=false였어도 stem이 참조하는 그림 본체는 누락되어 있었다. 복원본을 사용했음을 보존."
}
```

## 2. 공식 정답 대조

### 공식 정답 대조 — `CA-answer_check-20260910-01`

**공식 정답**

`4`

**일치 여부**

`true`

**정답 대조 reasoning**

```text
먼 A가 가까운 B보다 원근에 따른 축소가 크므로, 이를 제거하면 A/B 상대 크기가 변환 전보다 커진다.
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

### 독립 코드 판정 — `CA-independent_code-20260910-01`

**주 코드**

```json
[
  {
    "code": 84,
    "reason": "A/B라는 상대 크기를 변환 전후 비교. A와 B 각각의 절대 크기만으로는 정답④를 설명할 수 없음."
  }
]
```

**보조 코드**

```json
[
  {
    "code": 45,
    "reason": "실세계 점과 영상 점의 대응으로 원근 효과가 제거된 영상 생성."
  },
  {
    "code": 49,
    "reason": "먼 A가 가까운 B보다 변환 전 더 축소되는 거리-크기 방향."
  },
  {
    "code": 86,
    "reason": "변환 후에도 A<B일 수 있지만 A/B는 변환 전보다 증가함을 비교."
  }
]
```

**표면 코드**

```json
[
  {
    "code": 90,
    "reason": "그림에 여러 점·도형이 있지만 경우의 수를 세지 않음."
  }
]
```

**경쟁 코드 및 반증**

```json
[
  {
    "code": 85,
    "rejection": "A와 B의 길이 합이 고정된 몫의 경쟁이 아님. A/B의 변화는 두 물체에 적용된 거리별 축소 비율의 차이에서 나옴."
  },
  {
    "code": 43,
    "rejection": "C,D의 실세계 크기 동일은 주어진 도형 조건이지 실험에서 교란을 제거해 효과를 추정하는 과제 아님."
  },
  {
    "code": 40,
    "rejection": "⑤에서 점과 선 전체를 혼동하지만 정답④의 상대 크기 변화가 이 부분/전체 관계에 의존하지 않음."
  }
]
```

**확신도**

```text
높음
```

**경계 메모**

```text
BX는 같은 통화 금액의 환산과 고정 금 비율, CA는 거리별 다른 축소의 제거 후 A/B 변화. 둘 다 분수식으로 쓰이지만 분모의 역할이 다름. 합이 고정됐다는 전제를 발명하지 않는다.
```

**정규화된 주 코드 후보**

```json
[
  {
    "source_key": "primary",
    "value": [
      {
        "code": 84,
        "reason": "A/B라는 상대 크기를 변환 전후 비교. A와 B 각각의 절대 크기만으로는 정답④를 설명할 수 없음."
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
        "code": 45,
        "reason": "실세계 점과 영상 점의 대응으로 원근 효과가 제거된 영상 생성."
      },
      {
        "code": 49,
        "reason": "먼 A가 가까운 B보다 변환 전 더 축소되는 거리-크기 방향."
      },
      {
        "code": 86,
        "reason": "변환 후에도 A<B일 수 있지만 A/B는 변환 전보다 증가함을 비교."
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
        "code": 85,
        "rejection": "A와 B의 길이 합이 고정된 몫의 경쟁이 아님. A/B의 변화는 두 물체에 적용된 거리별 축소 비율의 차이에서 나옴."
      },
      {
        "code": 43,
        "rejection": "C,D의 실세계 크기 동일은 주어진 도형 조건이지 실험에서 교란을 제거해 효과를 추정하는 과제 아님."
      },
      {
        "code": 40,
        "rejection": "⑤에서 점과 선 전체를 혼동하지만 정답④의 상대 크기 변화가 이 부분/전체 관계에 의존하지 않음."
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

### SDSS 사후 대조 — `CA-sdss_compare-20260910-01`

**사이트 원래 코드**

```json
[
  "문제해결도식",
  "억제의억제는촉진"
]
```

**사이트 코드 번호**

```json
[
  59,
  52
]
```

**독립 주 코드**

```json
[
  84
]
```

**비교**

```text
#59는 원근 효과 제거라는 전체 문제/해결 맥락. #52는 상대적으로 더 작게 보이게 하던 원근 효과를 제거하면 A/B가 증가한다는 방향을 넓게 기술할 수 있다. 다만 독립된 두 억제 주체의 인과 사슬이 본문에 있는 것은 아니다.
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
  "decision": "최초 #84 유지. #52를 축소 요인의 제거라는 기능적 재서술 후보로 인정하되 생물학적 이중 억제 구조와 곧바로 동일시하지 않는다. A의 절대 확대만이 아니라 B 대비 상대 크기가 결론임을 보존.",
  "source": "각 blind_source 및 sealed/answer_sdss.jsonl 해당 행"
}
```

## 5. 후속 보강

이 case에 명시적으로 연결된 depth_backfill 또는 case-specific boundary_revision 기록이 없습니다.

### 명시적으로 연결된 집단 기록 참조

- `G014-induction-20260910-01` — 집단 귀납 기록 (집단/교차 사례 기록; 개별 case 판단으로 변환하지 않음)
- `META-G001-G014-meta_induction-20260910-01` — 교차 사례 귀납 기록 (집단/교차 사례 기록; 개별 case 판단으로 변환하지 않음)

## 6. 원장 추적

사용된 원장 record_id (queue 순서):
- `CA-blind-20260910-01` — 최초 blind 풀이 / done
- `CA-answer_check-20260910-01` — 공식 정답 대조 / done
- `CA-independent_code-20260910-01` — 독립 코드 판정 / done
- `CA-sdss_compare-20260910-01` — SDSS 사후 대조 / done
- `G014-induction-20260910-01` — 집단 귀납 기록 / done
- `META-G001-G014-meta_induction-20260910-01` — 교차 사례 귀납 기록 / done
