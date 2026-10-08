

<!-- luna-raw:BOG-blind-20261003-01 -->
## Astra raw handoff — blind

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G489",
  "selected_answer": 4,
  "confidence": 0.7,
  "exposure": {
    "official_answer_seen": false,
    "sdss_seen": false,
    "prior_judgment_seen": false,
    "past_exposure": "unknown",
    "strict_blind_eligible": false
  },
  "necessary_information": [
    {
      "location": "각 단백질 위치·조지3세 연구 문단",
      "evidence": "미오글로빈은 근육, 적혈구 산소운반은 헤모글로빈이다. 비소 발견은 콕스이며 탐색 목표는 헴 합성 관련 유전자였다."
    },
    {
      "location": "질환별 증세 문단",
      "evidence": "붉은 소변은 선천성 조혈기성 포르피린증의 코프로포르피리노젠I 배출과 연결되고 조지3세는 혼합 포르피린증 또는 양극성장애 가설로 서술된다."
    }
  ],
  "minimal_logic_without_codes": "①②③⑤는 단백질 위치·헴 기능·연구자·분석 대상의 명시적 교환이라 배제된다.④는 붉은 소변이 다른 질환의 특징이라는 구별을 적용한 선택이나 조지3세에게 그 증상이 실제로 없었다고 본문이 직접 말하지는 않아 소거에 의존한다.",
  "intermediate_reasoning": [
    "① 근육 단백질을 적혈구 내부로 옮겼다.",
    "② 시토크롬에도 헴은 산소 결합 능력을 부여한다.",
    "③ 매캘파인·헌터의 문헌 연구와 콕스의 비소 발견을 혼동했다.",
    "⑤ 비소 대사 유전자 결함이 아니라 헴 합성과 연관된 유전자 결함을 찾으려 했다.",
    "④ 혼합 질환에 선천성 조혈기성의 특이 증상을 옮기지 않는 문항 의도로 읽어 선택한다. 다른 질환이 반드시 상호 배타이며 조지3세의 증상이 완전 열거되었다는 근거까지 확보한 것은 아니다."
  ],
  "most_attractive_wrong": {
    "choice": 3,
    "exact_error": "같은 환자의 포르피린증 가설을 다룬 연구들이라는 이유로 문헌조사와 후속 모발 비소 분석의 결과를 같은 연구자에게 귀속한다."
  },
  "remaining_uncertainty": "④의 실제 붉은 소변 부재는 본문에서 직접 확정되지 않는다. 미언급을 부재로 바꾸는 추론 위험과 단일 질환·증상 특이성 가정을 공식답 전부터 보존한다. BOH 표는 읽었으나 그 표를 BOG 원문에 있던 근거로 소급하지 않았다."
}
```
