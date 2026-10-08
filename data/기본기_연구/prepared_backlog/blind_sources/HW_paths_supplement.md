# HW 그림 순서 근거 (blind source supplement)

이 기록은 그림의 위·아래 순서를 확인하기 위한 원문 구조 근거만 남긴다. 정답, 태그, 해설, 코드 판정은 기록하지 않는다.

- 확인한 정본: `고3 기출/2027 고3 국어 독서_Ⅳ. 기술.hwpx`의 `Contents/section0.xml`
- 해당 문항의 순차 XML 구조에서 조건 문장 뒤에 `<hp:t>(가)</hp:t>`가 먼저 나오고, 바로 이어진 그림 객체의 `<hc:img binaryItemIDRef="image11">`가 나온다.
- 그 그림 객체의 shapeComment는 `CLP0000e898003c.bmp`, 크기 `605×362pixel`로 기록되어 있다.
- 이어서 `<hp:t>(나)</hp:t>`가 나오고, 바로 이어진 그림 객체의 `<hc:img binaryItemIDRef="image12">`가 나온다.
- 두 번째 그림 객체의 shapeComment는 `CLP0000e898003d.bmp`, 크기 `600×363pixel`로 기록되어 있다.
- 따라서 `HW_paths.png`의 위쪽은 HWPX 문서에서 (가) 앵커 다음에 배치된 `image11`, 아래쪽은 (나) 앵커 다음에 배치된 `image12`이다. 이는 파일 번호를 임의로 해석한 것이 아니라 HWPX 문서 내 앵커와 그림 객체의 순차 배치를 따른 것이다.

카탈로그 `자료/평가원_독서_시각자료_원본/manifest.json`도 두 자산을 동일 문항에 명시적으로 연결한다: `image11`·`image12` 각각 `KICE-2013-6월_모평-Q44-46-S044~046-Q45`, `role: view_visual`, `provenance_status: extracted_from_local_kice_compilation_hwpx`.
