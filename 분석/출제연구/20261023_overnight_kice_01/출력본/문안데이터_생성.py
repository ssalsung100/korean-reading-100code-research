"""현재 Markdown에서 학생용/교사용을 분리해 Typst 입력을 생성한다."""
from pathlib import Path
import hashlib
import html
import json
import re

OUT=Path(__file__).resolve().parent
ROOT=OUT.parent
DEST=OUT/'typst'
SECTIONS=[
 ('01','지역 빈곤','A_지역빈곤/03_학생용_최종후보.md','A_지역빈곤/04_교사용_전선지해설.md'),
 ('02','품질 보증','B_품질보증/03_학생용_최종후보.md','B_품질보증/04_교사용_전선지해설.md'),
 ('03','공유자원','C_공유자원/03_학생용_최종후보.md','C_공유자원/04_교사용_전선지해설.md'),
 ('04','사회적 확산','D_추가연구/04_사회적확산_학생용후보.md','D_추가연구/05_사회적확산_교사용.md'),
]
MARKS='①②③④⑤'


def rich(s):
    # 문안은 실행 가능한 Typst 코드가 아니라 문자열 조각으로 넘긴다.
    s=html.unescape(s.strip())
    pattern=re.compile(r'\*\*(.+?)\*\*|`([^`]+)`|\[([^\]]+)\]\(([^)]+)\)')
    result=[];last=0
    for m in pattern.finditer(s):
        if m.start()>last:result.append({'kind':'text','text':s[last:m.start()]})
        if m.group(1) is not None:result.append({'kind':'strong','text':m.group(1)})
        elif m.group(2) is not None:result.append({'kind':'code','text':m.group(2)})
        else:result.append({'kind':'link','text':m.group(3),'url':m.group(4)})
        last=m.end()
    if last<len(s):result.append({'kind':'text','text':s[last:]})
    return result


def plain(spans):return ''.join(x['text'] for x in spans)


def parse_table(lines):
    rows=[[c.strip() for c in re.split(r'(?<!\\)\|',l.strip().strip('|'))] for l in lines]
    assert len(rows)>=2 and all(re.fullmatch(r':?-+:?',x.strip()) for x in rows[1]),rows
    header=rows[0];rows=rows[2:]
    assert all(len(row)==len(header) for row in rows),rows
    widths=[]
    for col in range(len(header)):
        words=[]
        for cell in [header[col]]+[row[col] for row in rows]:
            words.extend(plain(rich(cell)).split())
        widths.append(min(8,max(2,max(map(len,words),default=2))))
    return {'type':'table','headers':[rich(x) for x in header],
            'header_words':[plain(rich(x)).split() for x in header],'widths':widths,
            'rows':[[rich(x) for x in row] for row in rows]}


def blocks(lines,source):
    cleaned=[]
    for line in lines:
        line=re.sub(r'^\s*>\s?', '',line).rstrip()
        if re.sub(r'\*\*','',line.strip())=='<보기>':continue
        cleaned.append(line)
    out=[];i=0
    while i<len(cleaned):
        line=cleaned[i].strip()
        if not line or line=='---':i+=1;continue
        if line.startswith('```'):raise ValueError('인쇄 변환에 예상하지 않은 코드 블록')
        if line.startswith('|'):
            end=i+1
            while end<len(cleaned) and cleaned[end].strip().startswith('|'):end+=1
            out.append(parse_table(cleaned[i:end]));i=end;continue
        image=re.fullmatch(r'!\[([^\]]*)\]\(([^)]+)\)',line)
        if image:
            path=(source.parent/image.group(2)).resolve()
            assert path.is_file()
            rel=path.relative_to(ROOT.resolve()).as_posix()
            out.append({'type':'image','alt':rich(image.group(1)),'path':'/'+rel});i+=1;continue
        h=re.match(r'^(#{1,6})\s+(.+)',line)
        if h:
            out.append({'type':'heading','level':len(h.group(1)),'spans':rich(h.group(2))});i+=1;continue
        bullet=re.match(r'^[-*]\s+(.+)',line)
        if bullet:
            out.append({'type':'bullet','spans':rich(bullet.group(1))});i+=1;continue
        parts=[line];i+=1
        while i<len(cleaned) and cleaned[i].strip() and not re.match(r'^(?:\||#{1,6}\s|[-*]\s|!\[|---$)',cleaned[i].strip()):
            parts.append(cleaned[i].strip());i+=1
        out.append({'type':'paragraph','spans':rich(' '.join(parts))})
    return out


def parse_student(source,no,label):
    s=source.read_text()
    title=re.match(r'^# (.+)',s).group(1)
    before,after=s.split('\n---\n',1)
    passage=blocks(before.splitlines()[1:],source)
    assert all(b['type']=='paragraph' for b in passage)
    pieces=re.split(r'(?m)^## ([123])\.\s*(.+)\n',after)
    assert len(pieces)==10
    qs=[]
    for k in [1,4,7]:
        qno,prompt,content=pieces[k:k+3];lines=content.splitlines()
        starts=[i for i,l in enumerate(lines) if re.match(r'^[①②③④⑤]\s',l)]
        if starts:
            assert len(starts)==5
            pre=lines[:starts[0]];options=[]
            for n,start in enumerate(starts):
                end=starts[n+1] if n<4 else len(lines)
                joined=' '.join(x.strip() for x in lines[start:end] if x.strip())
                m=re.match(r'^([①②③④⑤])\s+(.*)$',joined)
                assert m.group(1)==MARKS[n]
                options.append({'mark':m.group(1),'spans':rich(m.group(2))})
            option_table=None
        else:
            first=next(i for i,l in enumerate(lines) if re.match(r'^\|\s*①\s*\|',l))
            table_start=first-2
            assert lines[table_start].strip().startswith('|')
            pre=lines[:table_start]
            table_lines=[x for x in lines[table_start:] if x.strip()]
            option_table=parse_table(table_lines)
            assert [plain(row[0]) for row in option_table['rows']]==list(MARKS)
            options=[]
        prelude=blocks(pre,source)
        qs.append({'no':int(qno),'prompt':rich(prompt),'view_title':'<보기>' if '<보기>' in '\n'.join(pre) else '',
                   'prelude':prelude,'options':options,'option_table':option_table})
    assert [q['no'] for q in qs]==[1,2,3]
    assert not re.search(r'정답\s*[:은]|교사용|설계 의도',s)
    return {'id':no,'label':label,'title':title,'passage':passage,'questions':qs,'source':str(source.relative_to(ROOT))}


def atom_texts(bs):
    result=[]
    for b in bs:
        if b['type']=='table':
            result += [plain(c) for c in b['headers']]
            result += [plain(c) for row in b['rows'] for c in row]
        elif b['type']=='image':result.append(plain(b['alt']))
        else:result.append(plain(b['spans']))
    return [x for x in result if x]


def main():
    students=[];teachers=[];manifest=[]
    keys=json.loads((ROOT/'checkpoint.json').read_text())['현재학생용정답']
    key_names=['지역빈곤','품질보증','공유자원','추가_사회적확산']
    for index,(no,label,sfile,tfile) in enumerate(SECTIONS):
        sp,tp=ROOT/sfile,ROOT/tfile
        student=parse_student(sp,no,label);students.append(student)
        tb=blocks(tp.read_text().splitlines(),tp)
        assert tb[0]['type']=='heading' and tb[0]['level']==1
        teachers.append({'id':no,'label':label,'title':student['title'],'teacher_title':tb[0]['spans'],
                         'blocks':tb[1:],'answers':keys[key_names[index]],'source':tfile})
        atoms=atom_texts(student['passage'])
        for q in student['questions']:
            atoms.append(plain(q['prompt']));atoms+=atom_texts(q['prelude'])
            atoms += [plain(o['spans']) for o in q['options']]
            if q['option_table']:atoms+=atom_texts([q['option_table']])
        manifest.append({'id':no,'title':student['title'],'student_source':sfile,'teacher_source':tfile,
                         'student_sha256':hashlib.sha256(sp.read_bytes()).hexdigest(),
                         'teacher_sha256':hashlib.sha256(tp.read_bytes()).hexdigest(),
                         'student_atoms':atoms,'teacher_atoms':atom_texts(tb),
                         'question_count':3,'choice_count':15})
    DEST.mkdir(exist_ok=True)
    for name,data in [('student_data.json',students),('teacher_data.json',teachers),('문안_검증기준.json',manifest)]:
        (DEST/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'학생입력':'4세트·12문항·60선지, 정답 필드 없음','교사입력':'별도 JSON','원본':'현재 Markdown 그대로 읽음'},ensure_ascii=False))


if __name__=='__main__':main()
