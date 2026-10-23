#import "kice_eval_like_template_v5.typ" as exam
#import "korean_workbook_base_v1.typ" as wb

#let k = exam.kice
#let roles = (
  source-indent: 10.3pt,
  source-inset: 8.5pt,
  question-above: 12pt,
  table-leading: 4.2pt,
  table-inset: 4pt,
  heading-above: 13pt,
  heading-below: 7pt,
)

#let rich(spans) = {
  if spans.len() == 0 { return [] }
  for s in spans {
    if s.kind == "strong" {
      strong(s.text)
    } else if s.kind == "code" {
      text(s.text)
    } else if s.kind == "link" and (s.url.starts-with("https://") or s.url.starts-with("http://")) {
      link(s.url, s.text)
    } else {
      text(s.text)
    }
  }
}

#let page-head(s, teacher: false) = block(width: 100%)[
  #set text(font: k.font, lang: "ko", tracking: k.tracking)
  #grid(columns: (70pt, 1fr, 70pt), align: horizon)[
    #text(size: 13pt, weight: "bold")[세트 #s.id]
  ][
    #align(center)[#text(size: 19pt, weight: "bold")[#s.title]]
  ][
    #align(right)[#text(size: 10pt)[#if teacher [교사용] else [독서 연습]]]
  ]
  #block(above: 8pt)[#line(length: 100%, stroke: 0.6pt + black)]
]

#let page-foot(s) = context align(center)[
  #text(font: k.font, size: 10pt)[#s.id · #counter(page).display("1")]
]

#let table-heading(words) = {
  let out = []
  for (i, word) in words.enumerate() {
    out += box(strong(word))
    if i < words.len()-1 { out += text(" ") }
  }
  out
}

#let data-table(t, teacher: false) = block(width: 100%, above: 7pt, below: 7pt)[
  #set par(first-line-indent: 0pt, leading: roles.table-leading, spacing: 0pt)
  #let n = t.headers.len()
  #table(
    columns: t.widths.map(w => w * 1fr),
    inset: roles.table-inset,
    stroke: k.view-stroke,
    align: if teacher { left + horizon } else { center + horizon },
    fill: (x, y) => if y == 0 { rgb("f2f2f2") } else { none },
    table.header(..if teacher { t.headers.map(h => strong(rich(h))) } else { t.header_words.map(words => table-heading(words)) }),
    ..t.rows.map(row => row.map(c => rich(c))).flatten(),
  )
]

#let render-blocks(bs, teacher: false) = {
  for b in bs {
    if b.type == "paragraph" {
      block(width: 100%, above: 0pt, below: k.line-leading, breakable: not teacher)[
        #par(first-line-indent: if teacher { 0pt } else { (amount: roles.source-indent, all: true) }, leading: k.line-leading, spacing: 0pt)[#rich(b.spans)]
      ]
    } else if b.type == "bullet" {
      block(width: 100%, below: k.line-leading)[
        #grid(columns: (12pt, 1fr), gutter: 0pt)[•][#rich(b.spans)]
      ]
    } else if b.type == "heading" {
      block(width: 100%, above: roles.heading-above, below: roles.heading-below, sticky: true)[
        #text(size: if b.level == 2 { 13pt } else { 11.5pt }, weight: "bold")[#rich(b.spans)]
      ]
    } else if b.type == "table" {
      data-table(b, teacher: teacher)
    } else if b.type == "image" {
      block(width: 100%, above: k.figure-above, below: k.line-leading, breakable: false)[
        #align(center)[#image(b.path, width: 100%, fit: "contain")]
        #block(above: 6pt)[#align(center)[#text(size: 9.2pt)[#rich(b.alt)]]]
      ]
    }
  }
}

#let source-head(body) = block(width: 100%, below: 9pt, sticky: true)[
  #text(weight: "bold")[#body]
]

#let source-line(paragraphs) = block(
  width: 100%, stroke: k.view-stroke, inset: roles.source-inset,
  above: 0pt, below: 13pt, breakable: true,
)[
  #set par(first-line-indent: (amount: roles.source-indent, all: true), leading: k.line-leading, spacing: k.line-leading)
  #for (i, p) in paragraphs.enumerate() {
    rich(p.spans)
    if i < paragraphs.len()-1 { parbreak() }
  }
]

#let question-line(no, prompt) = block(width: 100%, above: roles.question-above, sticky: true)[
  #exam.q-choice(no, rich(prompt))
]

#let choice-line(mark, body) = block(breakable: false)[#exam.choice(mark, body)]

#let viewbox(bs, title: "") = block(breakable: false)[
  #if title != "" {
    exam.viewbox(render-blocks(bs))
  } else {
    block(width: 100%, above: k.view-above, below: k.view-below)[
      #pad(left: k.choice-first-indent)[
        #box(width: k.view-width, stroke: k.view-stroke, inset: (x: k.view-inset-x, y: k.view-inset-bottom))[
          #render-blocks(bs)
        ]
      ]
    ]
  }
]

#let choice-table(t) = block(breakable: false, below: k.choice-after)[
  #pad(left: k.choice-first-indent)[
    #set par(leading: roles.table-leading, spacing: 0pt, first-line-indent: 0pt)
    #table(
      columns: (24.78pt, 1fr, 1fr), align: center + horizon,
      stroke: none, inset: (x: 4pt, y: 5pt),
      table.header(..t.headers.map(h => underline(rich(h)))),
      ..t.rows.map(row => row.map(c => rich(c))).flatten(),
    )
  ]
]

#let render-question(q) = block(breakable: false)[
  #question-line(q.no, q.prompt)
  #if q.prelude.len() > 0 { viewbox(q.prelude, title: q.view_title) }
  #if q.option_table != none {
    choice-table(q.option_table)
  } else {
    for o in q.options { choice-line(o.mark, rich(o.spans)) }
  }
]

#let student-document(s) = exam.document[
  #set text(font: k.font, size: k.size, lang: "ko", tracking: k.tracking)
  #set par(justify: false, leading: k.line-leading, spacing: k.line-leading)
  #set page(columns: 2, header: page-head(s), footer: page-foot(s))
  #set columns(gutter: k.column-gutter)
  #source-head(text("[1~3] 다음 글을 읽고 물음에 답하시오."))
  #source-line(s.passage)
  #for q in s.questions { render-question(q) }
]

#let teacher-document(s) = wb.workbook-document[
  #set text(font: k.font, size: k.size, lang: "ko", tracking: k.tracking)
  #set par(justify: false, leading: k.line-leading, spacing: k.line-leading)
  #set page(header: page-head(s, teacher: true), footer: page-foot(s))
  #wb.workbook-card(
    s.id, "교사용", rich(s.teacher_title), "1~3", render-blocks(s.blocks.slice(0, 1), teacher: true),
    rail: wb.workbook-rail(title: [정답], body: [
      #set par(leading: 4.2pt, spacing: 4.2pt)
      #for (i, a) in s.answers.enumerate() [#(i+1). #a #linebreak()]
      #linebreak()
      학생 난도·선택률은 미확인
    ]),
  )
  #render-blocks(s.blocks.slice(1), teacher: true)
]
