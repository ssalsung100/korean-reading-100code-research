

<!-- luna-raw:ANP-answer_check-20260927-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G258",
  "selected_answer": 2,
  "official_answer": 2,
  "match": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2010/2010_answer_2010_법학적성시험_언어이해_정답표.hwp",
  "fixed_logic_without_codes": "초기 자유주의 대표제의 목적은 합리화와수의 위험 제한. 민주주의 실현으로 바꾼② 오류.",
  "original_blind_preserved": true,
  "barrier": "group전체blind저장 확인",
  "sdss_disclosed": false
}
```


<!-- luna-raw:ANP-independent_code-20260927-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "primary": [
    {
      "code": 44,
      "reason": "대표선출 수단의 실제 목적은 수 제한·합리화이며 민주적 참여 실현으로 바뀜"
    }
  ],
  "auxiliary": [
    {
      "code": 75,
      "reason": "시기별 주체의 견해 귀속"
    },
    {
      "code": 3,
      "reason": "초기 자유주의와 후대 자유민주주의를 분리"
    }
  ],
  "surface": [
    {
      "code": 79,
      "reason": "정치 권리 규범 소재"
    }
  ],
  "competitors": [
    {
      "code": 17,
      "refutation": "목적의 주체 귀속으로도 기술 가능하나 단순대상 교체보다 같은 수단이 지향하는 목적이 반대인 것이 직접 근거"
    },
    {
      "code": 19,
      "refutation": "후대 중간집단 복원은 보완이지만 정답은 초기 대표제 목적"
    },
    {
      "code": 26,
      "refutation": "자유주의와민주주의 대립은 배경이나 모든 속성 배타화하면 후대 조정 설명과 충돌"
    }
  ],
  "counterfactual_probe": "②의 민주주의 실현을 수의 위험 제거로 바꾸면 참. 대표제가 있다는 제도명만으로 민주적 목적을 자동 귀속하지 않는다.",
  "boundary_status": "44/75/17 목적 내용·주체 귀속 중첩",
  "confidence": 0.95,
  "passage_group": "G258",
  "sdss_disclosed": false
}
```
