#import "project_roles.typ": student-document, teacher-document
#let mode = sys.inputs.at("mode", default: "student")
#let index = int(sys.inputs.at("section", default: "0"))
#let data = json(if mode == "student" { "student_data.json" } else { "teacher_data.json" })
#let s = data.at(index)
#set document(title: s.title, author: "독서 연습")
#if mode == "student" { student-document(s) } else { teacher-document(s) }
