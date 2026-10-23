// 평가원식 Typst 범용 조판 템플릿 v0.5
// v0.4의 공식 y0 줄간격 보정을 유지하고,
// 보기 박스 제목-본문 첫 줄 간격을 공식 q23-q24 계측값에 맞게 조정한다.
// 텍스트는 Typst로 재조판하고, 실제 도식/그림만 이미지로 넣는다.

#let kice = (
  font: "HCR Batang",
  size: 11.05pt,
  tracking: 0.12pt,
  page-width: 842pt,
  page-height: 1191pt,
  margin-left: 87.9pt,
  margin-right: 83.65pt,
  margin-top: 150pt,
  margin-bottom: 88pt,
  column-width: 321.8pt,
  column-gutter: 26.85pt,
  line-leading: 10.45pt,
  question-number-width: 24.78pt,
  question-below: 17.0pt,
  question-below-choice: 18.9pt,
  choice-first-indent: 11.28pt,
  choice-continuation-indent: 21.59pt,
  choice-hanging-indent: 10.31pt,
  choice-gap: 0pt,
  choice-after: 9.0pt,
  view-width: 306.18pt,
  view-stroke: 0.36pt + black,
  view-title-gap: 45pt,
  view-inset-x: 8.5pt,
  view-inset-top: 2.4pt,
  view-inset-bottom: 8.0pt,
  view-above: 13.0pt,
  view-below: 19.5pt,
  figure-stroke: 0.36pt + black,
  figure-inset: 3pt,
  figure-above: 8pt,
  figure-below: 12pt,
)

#let base-style = [
  #set text(font: kice.font, size: kice.size, lang: "ko", tracking: kice.tracking)
  #set par(justify: false, first-line-indent: 0pt, leading: kice.line-leading, spacing: 0pt)
]

#let document(body) = [
  #set page(
    width: kice.page-width,
    height: kice.page-height,
    margin: (
      left: kice.margin-left,
      right: kice.margin-right,
      top: kice.margin-top,
      bottom: kice.margin-bottom,
    ),
  )
  #base-style
  #body
]

#let neg(body: [않은]) = underline(offset: 1.1pt, stroke: 0.45pt + black, body)

#let exam-page(left, right: []) = grid(columns: (kice.column-width, kice.column-width), gutter: kice.column-gutter)[
  #base-style
  #left
][
  #base-style
  #right
]

#let q(no, body) = block(width: 100%, below: kice.question-below)[
  #grid(columns: (kice.question-number-width, 1fr), gutter: 0pt)[
    #text(weight: "regular")[#no.]
  ][
    #block(width: 100%)[
      #body
    ]
  ]
]

#let q-choice(no, body) = block(width: 100%, below: kice.question-below-choice)[
  #grid(columns: (kice.question-number-width, 1fr), gutter: 0pt)[
    #text(weight: "regular")[#no.]
  ][
    #block(width: 100%)[
      #body
    ]
  ]
]

#let passage(body) = block(width: 100%)[
  #par(
    justify: false,
    first-line-indent: 0pt,
    leading: kice.line-leading,
    spacing: 0pt,
  )[#body]
]

#let choice(mark, body) = block(width: 100%, above: kice.choice-gap, below: kice.choice-after)[
  #pad(left: kice.choice-first-indent)[
    #block(width: 100%)[
      #par(
        justify: false,
        first-line-indent: 0pt,
        hanging-indent: kice.choice-hanging-indent,
        leading: kice.line-leading,
        spacing: 0pt,
      )[#mark#body]
    ]
  ]
]

#let choices(items) = [
  #for item in items [
    #choice(item.at(0), item.at(1))
  ]
]

#let viewbox(body, title: [\<보 기\>]) = block(width: 100%, above: kice.view-above, below: kice.view-below)[
  #pad(left: kice.choice-first-indent)[
    #box(width: kice.view-width)[
      #grid(columns: (1fr, kice.view-title-gap, 1fr), gutter: 0pt)[
        #line(length: 100%, stroke: kice.view-stroke)
      ][
        #align(center)[#text(weight: "regular")[#title]]
      ][
        #line(length: 100%, stroke: kice.view-stroke)
      ]
    ]
    #box(
      width: kice.view-width,
      stroke: (left: kice.view-stroke, right: kice.view-stroke, bottom: kice.view-stroke, top: none),
      inset: (
        left: kice.view-inset-x,
        right: kice.view-inset-x,
        top: kice.view-inset-top,
        bottom: kice.view-inset-bottom,
      ),
    )[
      #set par(justify: false, first-line-indent: 0pt, leading: kice.line-leading, spacing: 0pt)
      #body
    ]
  ]
]

// 실제 평가원 도식/그림만 삽입한다. 지문, 문제, 선지, 보기 텍스트는 이 함수로 넣지 않는다.
// 공식 crop 좌표를 보존할 때는 width/height를 PDF 계측값에 맞춰 지정한다.
#let source-figure(path, caption: none, width: 100%, height: auto, framed: false) = block(
  width: 100%,
  above: kice.figure-above,
  below: kice.figure-below,
)[
  #let content = align(center)[#image(path, width: width, height: height, fit: "contain")]
  #if framed [
    #box(width: width, stroke: kice.figure-stroke, inset: kice.figure-inset)[#content]
  ] else [
    #content
  ]
  #if caption != none [
    #v(4pt)
    #align(center)[#text(size: 9.2pt)[#caption]]
  ]
]
