# ID 시각자료 순서·라벨 근거 (blind-only)

이 기록은 그림 자산의 문서상 순서와 라벨 매핑만 보존한다. 정답, 태그, 해설, 코드 판정은 기록하지 않는다.

- 정본 후보: `고3 기출/2027 고3 국어 독서_Ⅳ. 기술.hwpx`의 `Contents/section0.xml` (로컬 기출 편집본)
- 해당 문항의 보기 공정도 앵커 뒤에 `hc:img binaryItemIDRef="image31"`가 배치되어 있고, shapeComment 원본명은 `CLP0000e898004f.bmp`, 크기는 `963×343pixel`이다. 이 그림 안에 `마스크 A`와 `마스크 B` 표기가 함께 있다.
- 이어지는 선택지 표에서 문서 XML 순서는 `<hp:t>①</hp:t>` → `image32`, `<hp:t>②</hp:t>` → `image33`, `<hp:t>③</hp:t>` → `image34`, `<hp:t>④</hp:t>` → `image35`, `<hp:t>⑤</hp:t>` → `image36`이다. 각 번호는 그림 객체보다 먼저 나오는 별도 텍스트 앵커로 확인했다.
- 각 선택지 그림의 HWPX shapeComment 원본명은 순서대로 `CLP0000e8980052.bmp`, `CLP0000e8980051.bmp`, `CLP0000e8980053.bmp`, `CLP0000e8980054.bmp`, `CLP0000e8980055.bmp`이다.
- `ID_patterns.png`는 위 공정도(image31)를 상단에, 선택지 ①~⑤를 XML 앵커 순서대로 하단에 배치한 기계적 합성물이다. 선택지 번호는 문서 앵커에서 확인된 번호를 표시했다. `ID_process.png`는 image31을 별도 보존한 공정도 crop이다.

카탈로그 `자료/평가원_독서_시각자료_원본/manifest.json`은 image31을 `view_visual/fabrication_sequence_diagram`, image32~36을 각각 `choice_visual/illustrated_choice`로 기록하고 동일 문항에 연결한다. 원문 배포 직접 검증은 하지 않았으며, 로컬 KICE 편집본 경유임을 provenance에 분리 기록한다.
