# BNG blind-only source restoration appendix

- `blind_only: true`
- `passage_group: G480`
- `case_id: BNG`
- `source_role: canonical_text_restoration`
- `hold_record: BNG-hold-source-20261003-01`

## 공식 2024 홀수형 PDF 대조 결과

공식 PDF의 보기에서 확인된 기호 정의:

- `R맑음`, `R비`: 날씨가 맑을 때와 비가 올 때 개인이 투표 참여로부터 얻을 수 있는 보상
- `B`: 유권자의 지지 후보가 당선되었을 경우 얻을 수 있는 혜택
- `P`: 유권자 자신의 투표로 지지 후보가 선거에서 승리할 확률
- `S`: 투표 행위 자체가 가져올 수 있는 만족감(심리적 효용)
- `DC`, `OC`: 각각 직접비용과 기회비용

공식 수식:

\[
R_{맑음}=P\times B+S-(DC_{맑음}+OC_{맑음})
\]

\[
R_{비}=P\times B+S-(DC_{비}+OC_{비})
\]

\[
R_{맑음}-R_{비}=(DC_{비}-DC_{맑음})+(OC_{비}-OC_{맑음})
\]

공식 PDF의 보기와 ①~⑤ 전체를 crop으로 보존했다. 선지 원문은 다음과 같다.

① 기존 연구에 따르면 `DC비-DC맑음`은 양(+)의 값을 갖는다.

② 거주지 근처에 투표소가 추가로 설치된다면 `DC비`는 감소한다.

③ `R맑음-R비>0`이라면 선거일에 비가 올 때에는 투표할 가능성이 낮아진다.

④ 선거일이 공휴일로 지정되면 `OC비-OC맑음`은 음(-)의 값을 가질 수 있다.

⑤ 일반적으로 미국에서 `DC비-DC맑음`은 흑인 유권자가 백인 유권자보다 작게 느낀다.

원 crop은 보존하되 다음 10~12번 지문 일부가 우측·하단에 incidental하게 포함되어 있다. 다음 10~12번 지문의 공식답·SDSS·선지 전체는 노출되지 않았다. 이후 blind 사용에는 세로 구분선 왼쪽만 남긴 verified tight crop을 우선 참조한다.

- 원 crop: `BNG_official_view_choices_crop.png`
- 기존 tight crop: `BNG_official_view_choices_tight_crop.png`
- verified tight crop: `BNG_official_view_choices_verified_tight_crop.png`

검증 근거: `자료/LEET_언어이해/원본/2024/2024_question_odd_2024_LEET_언어이해(홀수형).pdf` 및 `자료/LEET_언어이해/페이지/2024/2024_question_odd/page_005.png`. 이 부록은 정답·SDSS 태그·판정을 포함하지 않는다.
