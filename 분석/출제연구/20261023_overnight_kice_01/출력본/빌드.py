"""현재 원고의 검토용 PDF를 다시 만든다. 기존 연구 자료는 읽기만 한다."""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import argparse
import json
import shutil
import subprocess
import sys
import fitz

OUT = Path(__file__).resolve().parent
ROOT = OUT.parent
NAMES = ['01_지역빈곤', '02_품질보증', '03_공유자원', '04_사회적확산']


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--typst', default=shutil.which('typst'))
    parser.add_argument('--font-path', default='/mnt/c/Windows/Fonts')
    parser.add_argument('--render-dir', default='미리보기/검수본')
    parser.add_argument('--mode', choices=['both', 'student', 'teacher'], default='both')
    parser.add_argument('--section', type=int, choices=range(4))
    args = parser.parse_args()
    if not args.typst:
        parser.error('Typst 실행 파일을 --typst로 지정하십시오.')
    version = subprocess.check_output([args.typst, '--version'], text=True).strip()
    subprocess.run([sys.executable, str(OUT/'문안데이터_생성.py')], check=True)
    render = OUT/args.render_dir
    render.mkdir(parents=True, exist_ok=True)
    records = []
    for mode, prefix in [('student', '학생용'), ('teacher', '교사용')]:
        if args.mode != 'both' and args.mode != mode:
            continue
        for i, name in enumerate(NAMES):
            if args.section is not None and i != args.section:
                continue
            pdf = OUT/f'{prefix}_{name}.pdf'
            cmd = [args.typst, 'compile', '--root', str(ROOT), '--font-path', args.font_path,
                   '--input', f'mode={mode}', '--input', f'section={i}',
                   str(OUT/'typst/main.typ'), str(pdf)]
            result = subprocess.run(cmd, text=True, capture_output=True)
            if result.returncode:
                raise RuntimeError(result.stderr)
            doc = fitz.open(pdf)
            for page in doc:
                page.get_pixmap(matrix=fitz.Matrix(1.25, 1.25), alpha=False).save(render/f'{pdf.stem}_{page.number+1}.png')
            records.append({'파일':pdf.name, '페이지':len(doc), '경고':result.stderr.strip()})
            print(f'{pdf.name}: {len(doc)}쪽', flush=True)
    (OUT/'빌드기록.json').write_text(json.dumps({
        '시각':datetime.now(ZoneInfo('Asia/Seoul')).isoformat(),
        'Typst':version, '글꼴경로':args.font_path, '이번빌드범위':args.mode, '세트인덱스':args.section, 'PDF':records,
        'PNG위치':str(render.relative_to(OUT)), '원고':'현재 Markdown에서 생성, 문안 자체 수정 없음',
    }, ensure_ascii=False, indent=2)+'\n')
    validation = subprocess.run([sys.executable, str(OUT/'문안_대조.py')], text=True, capture_output=True)
    if validation.returncode:
        raise RuntimeError(validation.stdout + validation.stderr)
    report = json.loads((OUT/'문안대조_검증결과.json').read_text())
    print(json.dumps({'문안대조':report['통과'], '학생용전체순서일치':len(report['학생용']),
                      '교사용미검출':sum(len(r['검출실패']) for r in report['교사용'])},ensure_ascii=False))


if __name__ == '__main__':
    main()
