

<!-- luna-raw:ANI-blind-20260927-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "selected_answer": 4,
  "confidence": 0.97,
  "required_information": [
    {
      "location": "2문단 ㉠",
      "evidence": "참여 기회 확대가 실질적 참여 확대를 보장하지 않음"
    }
  ],
  "minimal_logic_without_codes": "기회를 넓힌 조치와 실제 참여 행동의 양이 늘지 않은 결과가 동시에 있어야 한다. 공휴일 지정은 시간적 기회 확대이고 투표율 불변은 행동 불증가다.",
  "intermediate_reasoning": [
    "①노조 허용은 기회지만 노사 갈등은 참여 행동의 양이 아님",
    "②피선거권은 기회지만 당선자의 재력 구성은 참여 행동의 확대 여부와 다름",
    "③지역 투표 성향은 참여 규모가 아님",
    "④참여 기회 확대/행동량 불증가를 함께 충족",
    "⑤관심은 행동이 아니므로 실제 참여 증가 여부를 알 수 없음"
  ],
  "attractive_wrong_answer": 2,
  "exact_error": "결과적으로 당선된 대표자의 구성과 출마·투표 등 실제 참여 범위를 동일시한다. 저소득 출마가 늘어도 재력가 당선이 대부분일 수 있어②는 실질 참여 불증가를 보장하지 않음.",
  "passage_group": "G255",
  "exposure": {
    "current_session": "blind-only source; 답·태그 미열람",
    "historical": "manifest unknown; 저장소 참조0"
  }
}
```
