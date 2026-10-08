> 이 파일은 원장으로부터 자동 생성된 열람용 파생본이다. 연구의 authoritative source는 raw queue이며, 이 파일을 직접 편집하지 않는다.

# CB

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
문맥상 ⓐ의 의미와 가장 가까운 것은?
```

### 선지

```json
[
  "그때 동생이 탄 버스는 교차로를 지나고 있었다.",
  "그것은 슬픈 감정을 지나서 아픔으로 남아 있다.",
  "어느새 정오가 훌쩍 지나 식사할 시간이 되었다.",
  "물의 온도가 어는점을 지나 계속 내려가고 있다.",
  "가장 힘든 고비를 지나고 나니 마음이 가뿐하다."
]
```

### 원문 자료 감사

```json
{
  "case_id": "CB",
  "source_file_exists": true,
  "mechanically_linked": true,
  "assets": [
    {
      "path": "prepared_backlog/blind_sources/CB.json",
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
    "참조한 보충/원문 자산이 export에 없음: prepared_backlog/blind_sources/CB.json, sealed/answer_sdss.jsonl official_answer_verified, 각 blind_source 및 sealed/answer_sdss.jsonl 해당 행"
  ],
  "ready": false
}
```

## 1. 최초 blind 풀이

### 최초 blind 풀이 — `CB-blind-20260910-01`

**선택 답**

`1`

**확신도**

`0.99`

**코드명 없는 최소 논리 구조**

```text
빛이 렌즈를 지나는 것과 버스가 교차로를 지나는 것은 모두 공간상의 통과를 뜻한다.
```

**중간 추론**

```json
[
  "② 감정의 상태가 다른 상태로 넘어감.",
  "③ 일정 시간대가 흘러감.",
  "④ 온도가 기준점을 넘어서 내려감.",
  "⑤ 어려운 과정·시기를 겪고 넘어감."
]
```

**가장 매력적인 오답**

```json
{
  "choice": 4,
  "error": "기준점을 통과한다는 추상적 닮음은 있으나 공간상의 장소를 이동하는 본문 용례와 다름."
}
```

**노출 정보**

```text
G014 공식답·SDSS·기존 판정 미노출. 과거 노출 unknown, strict blind 확정 제외.
```

**기타 기록 필드**

```json
{
  "passage_group": "G014",
  "source": "prepared_backlog/blind_sources/CB.json",
  "necessary_information_and_locations": [
    "본문2문단 빛이 렌즈를 지날 때",
    "선지① 버스가 교차로를 지나고 있음"
  ]
}
```

## 2. 공식 정답 대조

### 공식 정답 대조 — `CB-answer_check-20260910-01`

**공식 정답**

`1`

**일치 여부**

`true`

**정답 대조 reasoning**

```text
렌즈/교차로를 지나다는 공간의 통과라는 문맥 의미가 같다.
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

### 독립 코드 판정 — `CB-independent_code-20260910-01`

**주 코드**

```json
[
  {
    "code": 96,
    "reason": "지나다의 공간 통과 용례를 렌즈/교차로에서 대응하는 문맥 의미 선택."
  }
]
```

**보조 코드**

```json
[
  {
    "code": 17,
    "reason": "장소·시간·기준점·시련·감정 상태라는 목적어 영역 차이로 용례 구분."
  }
]
```

**표면 코드**

```json
[
  {
    "code": 3,
    "reason": "③의 시간 경과는 오답 용례 소재, 본문 의미는 시간 순서 추론이 아님."
  }
]
```

**경쟁 코드 및 반증**

```json
[
  {
    "code": 99,
    "rejection": "대용 표현의 참조 대상이나 생략 논항을 복원하지 않음."
  },
  {
    "code": 100,
    "rejection": "일부 선지가 추상적 확장 용례인 점은 도움되지만 정답은 물리적 공간 통과의 직접 대응이며 별도의 비유 사상을 요구하지 않음."
  },
  {
    "code": 46,
    "rejection": "빛이 렌즈를 통과해 왜곡이 생기는 배경과 동사의 문맥 의미 선택은 구별."
  }
]
```

**확신도**

```text
중간
```

**경계 메모**

```text
#96은 문맥 의미 문항의 잔여 후보로 표시. #17과 함께 목적어의 의미 영역을 살피지만 범주명만 맞으면 모든 어휘 용례가 같다고 일반화하지 않음.
```

**정규화된 주 코드 후보**

```json
[
  {
    "source_key": "primary",
    "value": [
      {
        "code": 96,
        "reason": "지나다의 공간 통과 용례를 렌즈/교차로에서 대응하는 문맥 의미 선택."
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
        "reason": "장소·시간·기준점·시련·감정 상태라는 목적어 영역 차이로 용례 구분."
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
        "code": 99,
        "rejection": "대용 표현의 참조 대상이나 생략 논항을 복원하지 않음."
      },
      {
        "code": 100,
        "rejection": "일부 선지가 추상적 확장 용례인 점은 도움되지만 정답은 물리적 공간 통과의 직접 대응이며 별도의 비유 사상을 요구하지 않음."
      },
      {
        "code": 46,
        "rejection": "빛이 렌즈를 통과해 왜곡이 생기는 배경과 동사의 문맥 의미 선택은 구별."
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

### SDSS 사후 대조 — `CB-sdss_compare-20260910-01`

**사이트 원래 코드**

```json
[
  "대상범주"
]
```

**사이트 코드 번호**

```json
[
  17
]
```

**독립 주 코드**

```json
[
  96
]
```

**비교**

```text
독립 보조 #17과 일치. 장소를 통과하는 용례와 시간·수치 기준·감정·시련을 지나는 용례를 구별하는 데 목적어 영역이 유용하다.
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
  "decision": "#96과 #17은 이 사례에서 문맥 의미 선택의 상위 기술과 판별 단서로 연결됨. 원 번호 및 최초 주/보조 보존.",
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
- `CB-blind-20260910-01` — 최초 blind 풀이 / done
- `CB-answer_check-20260910-01` — 공식 정답 대조 / done
- `CB-independent_code-20260910-01` — 독립 코드 판정 / done
- `CB-sdss_compare-20260910-01` — SDSS 사후 대조 / done
- `G014-induction-20260910-01` — 집단 귀납 기록 / done
- `META-G001-G014-meta_induction-20260910-01` — 교차 사례 귀납 기록 / done
