

<!-- luna-raw:BH-sdss_compare-20260910-01 -->
## Astra raw handoff — sdss_compare

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G009",
  "barrier": "BE~BH independent_code 모두 raw 저장 확인",
  "site_original_codes": [
    "필요조건",
    "허위적인과"
  ],
  "site_code_numbers": [
    10,
    55
  ],
  "independent_primary": [
    5
  ],
  "comparison": "#10은 삼각형 크기 축소에 실제 물체 축소가 필요하다는 조건 후보, #55는 원근에 따른 겉보기 축소를 실제 축소 원인으로 오인한 관계 후보. 다만 정답④에 명시 인과 논증은 없어 사이트 #55의 정확한 적용 의미는 보류. 주 #5 유지.",
  "source": "sealed/answer_sdss.jsonl BH",
  "unresolved": true
}
```


<!-- luna-raw:BH-boundary_revision-20260910-01 -->
## Astra raw handoff — boundary_revision

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "scope": "기존 sdss_compare의 미해결 #55 의미 연결만 추가 검토. 완료된 blind/answer/독립판정은 재작성하지 않음.",
  "sources": [
    "prepared_backlog/blind_sources/BH.json",
    "prepared_backlog/blind_sources/BH_supplement_20260910_scene_plan.bmp; PNG 변환본을 Astra 직접 판독"
  ],
  "direct_observation": "장면3은 풍선이 더 이상 커지지 않고 모양을 유지한 채 관찰자로부터 멀어지는 상황이다. 선지④는 모델링 삼각형이 작아진다고 한다. 본문은 이동 때 정점 간격이 유지된다고 명시한다.",
  "refinement": "물체-관찰자 거리 변화에 따른 화면상 축소와 모델링의 정점 간격 변화는 다른 단계의 값이다. 선지④의 명시적 오류는 유지되는 모델링 크기를 변한다고 한 것이다. 거리 변화→모델링 축소라는 인과 명제는 선지에 직접 쓰이지 않았고, 독자가 보충할 수 있는 오독 경로다.",
  "original_primary_preserved": [
    5
  ],
  "site_original_codes_preserved": [
    "필요조건",
    "허위적인과"
  ],
  "site55_working_interpretation": "#55가 잘못된 변화 원인 연결까지 포괄한다면 적용 가능. 그러나 현재 태그만으로 사이트 저자의 실제 연결을 확정할 수 없어 unresolved 유지.",
  "site10_limit": "원 raw의 실제 물체 축소 필요라는 설명은 이 장면의 모양 유지·모델링 규칙 안에서만 읽는다. 모든 물체 변형에서 각 삼각형 축소의 필요충분조건을 확정한 뜻이 아니다.",
  "boundary_rule": "명시된 관계, 정답이 부정하는 관계, 매력적 오독을 설명하려고 연구자가 복원한 관계를 별도 기록한다. 세 번째만 존재할 때 사이트 태그와 주 코드의 일치를 확정하지 않는다.",
  "comparison_case": "BW 역시 선지 자체의 명시적 허위 인과 논증보다 다른 관계를 연결하는 유혹이 있다는 공통점. BH는 모델링/렌더링 단계, BW는 조건부 전망의 분기가 구별 대상.",
  "needs_astra_review": "사이트 원 해설 또는 적용 선지가 직접 확인될 때 #55 의미 연결 재검토. 현재 자료로 저자 의도까지 해결하지 않음."
}
```
