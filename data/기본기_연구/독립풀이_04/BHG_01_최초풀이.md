

<!-- luna-raw:BHG-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G428",
  "selected_answer": 5,
  "confidence": 0.95,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "source": [
    "data/기본기_연구/prepared_backlog/blind_sources/BHG.json",
    "data/기본기_연구/prepared_backlog/blind_sources/G428_visual01.tif",
    "data/기본기_연구/prepared_backlog/blind_sources/G428_visual02.md"
  ],
  "necessary_information": [
    {
      "location": "본문2~3문단",
      "evidence": "근접은 거리 최소, 방향은 원점 기준 부호와 원점 거리. 후기는 일체감/관용경계 반영."
    },
    {
      "location": "보기ㄱ~ㅂ 및 그림",
      "evidence": "후보0,4,7,9; 중위3,7,5; 원점5; 양 후보 모두 자기 위치±2 밖이면 기권; 전체 분포 좌우 대칭이며 정당 일체자 규모 동일."
    }
  ],
  "minimal_logic_without_codes": "예선에서 이론별 후보를 먼저 정하고 그 후보에 한해 본선 투표 범위를 정한다. 방향 이론 후보0/9의 후기 본선에서는 관용경계로 투표 가능 집단이 왼쪽[0,2],오른쪽[7,10]가 되어 오른쪽 후보가 더 많은 표를 얻는다.따라서⑤가 부적절하다.",
  "intermediate_reasoning": [
    "①초기 근접에서 B1=7은 B당 중위7과 일치하여9보다 우세. A당은4가0보다 중위3에 가까워 A2가 진출.",
    "②본선4/7의 동거리 위치5.5. 전체 중위5보다 오른쪽에서 갈리므로 A2가 더 많은 표를 얻는다.",
    "③초기 방향에서는 A1=0,B2=9가 각 진영 효용 극대화. 본선은 원점5를 기준으로 좌우 동수,중립은 기권하여 승자 없음.",
    "④후기 근접에서도 양당 중위에 더 가까운 A2/B1이 일체자 지지를 확보한다. 동수 일체자 지지의 균형에 중도층의4 선호가 더해져 A2 우세. 추가 관용 기권 규칙을 적용해도 좌우 대칭 구간 비교에서4 우세는 유지된다.",
    "⑤후기 방향은 보기의 양 후보가 동시에±2를 초과할 때만 기권한다는 규칙을 적용한다. 예선에서는 원점 왼쪽은0,오른쪽은9를 더 선호. 본선은(2,7)에서 둘 다 관용 밖.0쪽[0,2]와9쪽[7,10]를 비교하면 대칭인[0,3] 중[0,2]보다[7,10]가 넓어 B2 우세. 후보별 허용 여부를 별도 탈락 요건으로 바꾸지 않는다."
  ],
  "most_attractive_wrong": {
    "choice": 3,
    "exact_error": "초기 방향에 후기의 관용경계 기권을 소급하면 비대칭 득표를 예상하게 된다. 초기에는 원점 양측의 대칭 분포로 표가 갈려 동률이다."
  },
  "source_limitations": [
    "연속 곡선은 정확한 득표 수를 제공하지 않는다. 좌우 대칭과 추가 양의 면적만으로 순위를 비교한다."
  ],
  "confidence_note": "후기 근접의 일체감 가중치는 수식화되지 않았다.④는 동일 규모 일체자와 각 당 중위에 가까운 후보 및 전체 중위 관계에 근거한 정성 판정이며 임의 가중치를 만들어 계산하지 않았다."
}
```
