

<!-- luna-raw:AX-sdss_compare-20260910-01 -->
## Astra raw handoff — sdss_compare

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G007",
  "barrier": "AT~AY independent_code 모두 raw 저장 확인",
  "site_original_codes": [
    "질적차이"
  ],
  "site_code_numbers": [
    7
  ],
  "independent_primary": [
    62
  ],
  "comparison": "#7의 정확 적용 위치 불명. 은/약·비단의 지속성 차이 또는 효용 평가 범주 구별은 후보이나 태그만으로 확정 못함. 정답④ 비판 연결의 타당성 판정 #62를 유지하며 의미 연결 보류.",
  "source": "sealed/answer_sdss.jsonl AX",
  "unresolved": true
}
```


<!-- luna-raw:AX-boundary_revision-20260910-01 -->
## Astra raw handoff — boundary_revision

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "scope": "기존 [A] 범위 보류에 대한 정본 구조 근거 추가. 완료된 blind/answer/독립판정은 보존.",
  "source": "고3 기출/2027 고3 국어 독서_Ⅰ. 인문, 독서.hwpx :: Contents/section0.xml",
  "source_sha256": "42be085121b4e158e4d29430cc0a8ff1605dc144e2255e9df2bbf08552f47d44",
  "mechanical_evidence": "Luna가 추출한 XML을 Astra가 직접 확인. [A]는 표 id=1530744151의 병합 셀 텍스트이고, 표는 박제가 문단과 같은 외부 hp:p의 첫 run 안에 위치. vertRelTo=PARA, vertAlign=TOP, vertOffset=96, height=27567. 이덕무 문단은 다음 별도 hp:p.",
  "scope_resolution": "최소한 [A] 표지의 앵커는 박제가 문단이다. blind text에서 이덕무 문단 앞에 놓인 독립 행 [A]를 뒤 문단의 시작 표시로 해석하면 안 된다. 단, 부유 표의 정확한 괄호 하단 위치는 페이지 렌더링 또는 평가원 원본 대조를 하지 않았으므로 전체 시각적 범위까지 구조만으로 확정했다고 쓰지 않는다.",
  "semantic_effect": "박제가의 실용적 입장과 북학론 당위성을 [A]의 내용으로 사용하는 ①②의 근거가 이 앵커와 부합한다. 정답④의 은 효용 평가 및 기존 주 #62 판단은 이덕무 문단을 [A]로 읽어 얻은 것이 아니므로 현재 근거로 변경할 이유 없음.",
  "original_primary_preserved": [
    62
  ],
  "site_original_codes_preserved": [
    "질적차이"
  ],
  "unresolved": [
    "[A]의 시각적 괄호 하단 정확 위치는 미확인.",
    "사이트 #7의 정확한 적용 위치는 앵커 복원으로 해결되지 않음. 은/약·비단의 지속성 차이 후보만 보존."
  ],
  "source_quality_rule": "부유 괄호 표지가 평문에서 문단 사이로 이동한 경우, 평문 순서를 범위의 증거로 삼지 말고 앵커와 시각 경계를 구별해 기록한다."
}
```
