"""검수한 개별 PDF 합본과 학생용만의 명시적 파일 목록 ZIP을 만든다."""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import json
import re
import zipfile
import fitz

OUT = Path(__file__).resolve().parent
ROOT = OUT.parent
SECTIONS = [
    ('01_지역빈곤', '지역의 빈곤과 전체의 빈곤', 'A_지역빈곤/03_학생용_최종후보.md'),
    ('02_품질보증', '품질을 알리는 보증', 'B_품질보증/03_학생용_최종후보.md'),
    ('03_공유자원', '공유자원과 권리의 묶음', 'C_공유자원/03_학생용_최종후보.md'),
    ('04_사회적확산', '관계의 연결과 행동의 확산', 'D_추가연구/04_사회적확산_학생용후보.md'),
]


def main():
    validation = json.loads((OUT/'문안대조_검증결과.json').read_text())
    assert validation['통과'], '문안 검증 통과 후 묶을 것'
    records = []
    for prefix in ['학생용', '교사용']:
        combined = fitz.open()
        toc = []
        original_text = ''
        for suffix, title, _ in SECTIONS:
            doc = fitz.open(OUT/f'{prefix}_{suffix}.pdf')
            toc.append([1, f'{suffix[:2]}. {title}', len(combined)+1])
            combined.insert_pdf(doc)
            original_text += ''.join(p.get_text() for p in doc)
        combined.set_toc(toc)
        combined.set_metadata({'title':f'독서 연습 4세트 — {prefix}',
                               'author':'', 'subject':'현재 후보 문안의 검토용 출력본',
                               'creator':'Typst / PyMuPDF'})
        target = OUT/f'{prefix}_4세트_합본.pdf'
        combined.save(target, garbage=4, deflate=True)
        check = fitz.open(target)
        assert ''.join(p.get_text() for p in check) == original_text
        assert check.get_toc() == toc
        records.append({'파일':target.name,'페이지':len(check),'책갈피':toc,'개별파일대비문자순서동일':True})
    whitelist = [(OUT/'학생용_4세트_합본.pdf', '학생용_4세트_합본.pdf')]
    for suffix, _, source in SECTIONS:
        whitelist.append((OUT/f'학생용_{suffix}.pdf', f'개별PDF/학생용_{suffix}.pdf'))
        whitelist.append((ROOT/source, f'수정가능원고/학생용_{suffix}.md'))
    for file, arc in whitelist:
        assert '교사용' not in arc and '정답' not in arc
        text = file.read_text() if file.suffix == '.md' else ''.join(p.get_text() for p in fitz.open(file))
        assert not re.search(r'정답|교사용|설계\s*의도|연구\s*기록', text), file
    archive = OUT/'학생용_4세트_문제와원고.zip'
    with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED) as z:
        for file, arc in whitelist:
            z.write(file, arc)
    with zipfile.ZipFile(archive) as z:
        assert z.namelist() == [arc for _, arc in whitelist]
        assert z.testzip() is None
    report = {'시각':datetime.now(ZoneInfo('Asia/Seoul')).isoformat(),
              '합본':records,'학생용ZIP':archive.name,'ZIP명시포함목록':[arc for _,arc in whitelist],
              '범위':'학생용 PDF5개·현재 학생용 원고4개만. 정답·해설·raw·연구 기록·기출 원문은 포함하지 않음.',
              '통과':True}
    (OUT/'묶음_검증결과.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False,indent=2))


if __name__ == '__main__':
    main()
