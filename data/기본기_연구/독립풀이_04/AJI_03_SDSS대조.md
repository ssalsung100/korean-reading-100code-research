

<!-- luna-raw:AJI-sdss_compare-20260921-01 -->
## Astra raw handoff — sdss_compare

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G220",
  "candidate_id": "CAND-496aef23a5631e5c",
  "site_original_codes": [],
  "site_marked_answer": null,
  "comparison_status": "unavailable_no_site_tags",
  "meaning_comparison": "실제태그없어의미대조불가,독립판정유지",
  "barrier_verified": "G220전체독립4후첫공개",
  "provenance": "2026수능27~30;AJH공식범위직접확인,공식답PDF연결필드대조",
  "quota_status": "unavailable"
}
```


<!-- luna-raw:AJI-boundary_revision-20260922-01 -->
## Astra raw handoff — boundary_revision

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G220",
  "original_independent_record": "AJI-independent_code-20260921-01",
  "original_blind_preserved": true,
  "review_type": "SDSS 공개 이후 미확정 경계의 원문 재검토; 신규 blind 성과 아님",
  "source": "data/기본기_연구/prepared_backlog/blind_sources/AJI_official_stem.json",
  "previous": {
    "primary": [],
    "primary_candidates": [
      3,
      93,
      45
    ],
    "working_representative": 3,
    "auxiliary": [
      17
    ]
  },
  "revised": {
    "primary": [
      93
    ],
    "auxiliary": [
      3,
      17
    ],
    "surface": [
      45,
      63
    ],
    "scope": "AJI의 정답 결정 및 선지별 기여에 한정. 3/93/45 전역 분리 확정 아님"
  },
  "evidence": [
    {
      "location": "방문 전 소문을 회상하는 후반 문단",
      "text": "소문을 듣고 찾아온 온 씨와 만나 언쟁을 벌이게 되었던",
      "supports": "온 씨가 ⓑ의 수신자이며 그 정보와 관련하여 허명두를 방문함"
    },
    {
      "location": "대화에서 온 씨 발화 및 허명두 응답",
      "text": "당신이 무슨 짓을 꾸미고 있는지 다들 알고 있소",
      "supports": "방문에서 소문과 관련된 상대의 입장·행동을 확인하는 대화가 이루어짐. 모든 소문 내용의 객관적 진실을 입증했다는 뜻은 아님"
    },
    {
      "location": "언쟁 직후 서술",
      "text": "온 씨가 만나는 사람에게마다 ⓐ 이야기를 퍼뜨렸기 때문",
      "supports": "수신자였던 온 씨가 후속 이야기의 발신자가 됨"
    },
    {
      "location": "⑤",
      "text": "ⓐ에는 ⓐ를 처음 퍼뜨린 인물이 ⓑ와 관련하여 찾아가 만난 인물에게 확인한 내용이 반영되어 있다",
      "supports": "정답은 시간 순서뿐 아니라 확인한 내용의 전달 경로와 반영을 요구함"
    }
  ],
  "logic_without_codes": "온 씨는 먼저 소문을 듣고 허명두를 방문하여 관련 대화를 나눈 다음, 그 만남에서 확인한 내용이 담긴 이야기를 다른 사람들에게 퍼뜨린다. 서술 제시 순서와 실제 사건 순서는 다르다.",
  "competing_codes": [
    {
      "code": 3,
      "verdict": "보조로 재배치",
      "reason": "ⓑ→방문→ⓐ의 순서는 ②를 배제하고 ⑤의 전제가 된다. 그러나 시간만 바르게 두어도 ⓐ가 확인 내용과 무관하면 ⑤는 성립하지 않아 정답의 전 관계를 포괄하지 못한다."
    },
    {
      "code": 45,
      "verdict": "독립 주 후보에서 제외, 과정 표현의 표면 층위로 보존",
      "reason": "입력→확인→출력으로 표현할 수는 있으나 입력별 변환 규칙이나 산출값을 계산·추적하는 별도 요구는 없다. 이 사례에서는 동일 정보 전달 경로를 일반 과정도로 재기술한 것에 그친다."
    },
    {
      "code": 17,
      "verdict": "보조 유지",
      "reason": "수신자·방문 대상·발신자의 귀속 보존이 필요하다. 다만 귀속만으로 확인 내용이 ⓐ에 반영되는 연결을 모두 설명하지는 못한다."
    },
    {
      "code": 63,
      "verdict": "주 기각",
      "reason": "④의 소문 거짓 판명은 근거 없는 설명이다. 정답은 새 증거가 소문의 신뢰도를 얼마나 높이는지 평가하지 않는다."
    }
  ],
  "falsification_attempts": [
    {
      "change": "사건 순서는 유지하고 ⓐ를 방문 내용과 무관한 이야기로 교체",
      "result": "⑤가 거짓이 된다. 선후만으로는 정답 충분 설명 불가."
    },
    {
      "change": "ⓑ와 방문 및 ⓐ의 내용 연결을 유지하고 서술 순서만 실제 사건 순서로 재배치",
      "result": "⑤의 참은 유지된다. 회상 배열 복원은 보조 부담이다."
    },
    {
      "change": "ⓐ를 퍼뜨린 자를 방문하지 않은 다른 사람으로 교체하되 시간 순서는 유지",
      "result": "⑤의 동일 행위자 경로가 끊긴다. 시간과 정보 전달자의 역할은 독립 점검해야 한다."
    }
  ],
  "revised_boundary": "정보·소문이 등장한다는 이유만으로 93을 부여하지 않는다. 정답이 수신→확인→발신 주체와 내용의 연계를 실제로 요구할 때 93의 기여를 인정한다. 45는 모든 과정이 입력·출력으로 표현 가능하다는 이유만으로 독립 코드로 중복 계수하지 않는다.",
  "generation_principles": [
    "서술 순서를 바꾸는 변형과 정보 전달자·내용 연결을 바꾸는 변형을 따로 만들고 어느 변화가 정답을 바꾸는지 기록한다.",
    "확인한 내용의 전달과 소문 전체의 사실 입증을 구별한다."
  ],
  "redivision_condition": "다른 사례에서 발신자·수신자가 고정되어도 처리 규칙이나 입력별 산출 변경만으로 정답이 달라지면 45의 독립 기여를 다시 비교한다.",
  "confidence": 0.93,
  "quota_status": "unavailable"
}
```
