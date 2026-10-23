// Korean workbook base v1
// Purpose: keep KICE-like text rhythm stable while allowing workbook rails.
// Do not edit local spacing in content files. Extend through these roles.

#import "kice_eval_like_template_v5.typ": *

#let wb = (
  ink: rgb("24384f"),
  teal: rgb("1f6f78"),
  wine: rgb("7a3434"),
  moss: rgb("526f4a"),
  gray: rgb("6f7378"),
  pale: rgb("f5f6f7"),
  paper: white,

  study-margin-x: 76pt,
  study-margin-y: 72pt,
  study-rail-width: 92pt,
  study-rail-gutter: 8pt,

  title-size: 13pt,
  meta-size: 8.2pt,
  rail-title-size: 8pt,
  rail-body-size: 7.8pt,

  source-head-above: 6pt,
  source-head-below: 6pt,
  plain-line-below: 4.8pt,
  question-line-above: 8pt,
  question-line-below: 5pt,
  choice-line-above: 3pt,
  choice-line-below: 5pt,
)

#let exam-text-style = [
  #set text(font: kice.font, size: 9.2pt, lang: "ko", tracking: 0.04pt)
  #set par(justify: false, first-line-indent: 0pt, leading: 9.0pt, spacing: 0pt)
]

#let workbook-document(body) = [
  #set page(
    width: kice.page-width,
    height: kice.page-height,
    margin: (
      left: wb.study-margin-x,
      right: wb.study-margin-x,
      top: wb.study-margin-y,
      bottom: wb.study-margin-y,
    ),
  )
  #set text(font: kice.font, lang: "ko", fill: black)
  #set par(justify: false, first-line-indent: 0pt, spacing: 0pt)
  #body
]

#let book-cover(title, subtitle, note: none) = [
  #set page(width: kice.page-width, height: kice.page-height, margin: 72pt)
  #v(112pt)
  #text(size: 28pt, weight: "bold", fill: wb.ink)[#title]
  #v(10pt)
  #text(size: 12pt, fill: wb.gray)[#subtitle]
  #v(52pt)
  #box(width: 100%, height: 1.2pt, fill: wb.ink)
  #if note != none [
    #v(18pt)
    #text(size: 9pt, fill: wb.gray)[#note]
  ]
]

#let chapter-map(rows) = [
  #text(size: 18pt, weight: "bold", fill: wb.ink)[전체 구성]
  #v(14pt)
  #for row in rows [
    #grid(columns: (58pt, 1fr, 52pt), gutter: 8pt)[
      #text(size: 8.5pt, fill: wb.teal, weight: "bold")[#row.at(0)]
    ][
      #text(size: 9.4pt)[#row.at(1)]
    ][
      #align(right)[#text(size: 8.5pt, fill: wb.gray)[#row.at(2)]]
    ]
    #v(5pt)
  ]
]

#let unit-head(no, section, title, qs) = block(width: 100%, below: 6pt)[
  #box(width: 100%, height: 1pt, fill: wb.teal)
  #v(4pt)
  #text(size: wb.title-size, fill: wb.ink, weight: "bold")[#no  #title]
  #h(6pt)
  #text(size: wb.meta-size, fill: wb.gray)[#section · 문항 #qs]
]

#let workbook-rail(title: [분석 레일], body: [핵심어 / 근거문장 / 오답 유형 / 다시 볼 선지]) = box(
  width: 100%,
  stroke: 0.36pt + wb.teal,
  inset: 5pt,
)[
  #text(size: wb.rail-title-size, fill: wb.teal, weight: "bold")[#title]
  #v(3pt)
  #text(size: wb.rail-body-size)[#body]
]

#let material-slot(label, body: none) = box(width: 100%, fill: wb.pale, inset: 5pt)[
  #text(size: 8pt, fill: wb.gray)[#label]
  #if body != none [
    #v(3pt)
    #text(size: 8pt, fill: black)[#body]
  ]
]

#let source-head(body) = block(width: 100%, above: wb.source-head-above, below: wb.source-head-below)[
  #text(size: 9pt, fill: wb.teal, weight: "bold")[#body]
]

#let source-line(body) = block(width: 100%, above: 0pt, below: wb.plain-line-below)[
  #body
]

#let question-line(body) = block(width: 100%, above: wb.question-line-above, below: wb.question-line-below)[
  #body
]

#let choice-line(body) = block(width: 100%, above: wb.choice-line-above, below: wb.choice-line-below)[
  #pad(left: kice.choice-first-indent)[
    #par(hanging-indent: kice.choice-hanging-indent, leading: kice.line-leading, spacing: 0pt)[#body]
  ]
]

#let workbook-exam-text(body) = [
  #exam-text-style
  #body
]

#let workbook-card(no, section, title, qs, body, rail: workbook-rail()) = block(width: 100%, above: 8pt, below: 12pt)[
  #grid(columns: (1fr, wb.study-rail-width), gutter: wb.study-rail-gutter)[
    #unit-head(no, section, title, qs)
    #body
  ][
    #rail
  ]
]

#let strict-exam-spread(left, right: []) = document[
  #exam-page(left, right: right)
]

#let strict-source(range, body) = [
  #source-head(range)
  #passage(body)
]

#let strict-question(no, prompt, options, view: none, figure: none) = [
  #q-choice(no)[#prompt]
  #if view != none [
    #viewbox(view)
  ]
  #if figure != none [
    #figure
  ]
  #choices(options)
]
