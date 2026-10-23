import sys,subprocess,json,xml.etree.ElementTree as E
sys.dont_write_bytecode=True
from backfill_io import ROOT,OUT,sha,write
hwp='자료/MEET_언어추론/공식_정답표_원본/2007_언어추론_정답표.hwp'
page='자료/MEET_언어추론/페이지/2007/official_page_067_3x.png'
m=next(r for r in json.loads((ROOT/'자료/MEET_언어추론/공식_정답표_원본/source_manifest.json').read_text()) if r['label']=='2007')
assert sha(ROOT/hwp)==m['official_file_sha256']
r=subprocess.run(['hwp5proc','xml',str(ROOT/hwp)],capture_output=True,check=True)
x=E.fromstring(r.stdout)
tables=[]
for t in x.iter('TableControl'):
 tables.append([[''.join(c.itertext()).strip() for c in row.findall('TableCell')] for row in t.iter('TableRow')])
assert '홀수형' in str(tables[0])
answer={}
for row in tables[1][1:]:
 for i in range(0,len(row),2):answer[int(row[i])]=row[i+1]
assert len(answer)==40 and answer[34]=='②'
write('BCF_official_source_review_20261016.json',{'case':'BCF','identity':'MEET2007홀수형34번','question_page':{'path':page,'sha256':sha(ROOT/page),'direct_visual_review':'이번주에이전트가공식14쪽이미지직접확인.ㄱ행성온도/ㄴ은하개수/ㄷ항성평균수명/ㄹ은하구성원소종류,②ㄱㄷ/③ㄱㄹ일치.'},'answer_original':{'path':hwp,'sha256':sha(ROOT/hwp),'matches_source_manifest':True,'method':'이번hwp5proc xml로원HWP표셀직접추출·홀수형표식과표1의문항/정답쌍확인.렌더이미지의시각대조는아님.','heading_table':tables[0],'odd_answer_table':tables[1],'question_number':34,'answer':'②'},'initial_answer_preserved':3,'initial_confidence_preserved':0.86,'resolution_scope':'정답출처와전사대조만이번추가확인.ㄷ간접영향과ㄹ배제의일관된의미기준은미해결.최초오답·기존needs_astra_review불변.','needs_astra_review':True})
print('BCF공식문제이미지·원HWP홀수형34번②직접추출확인저장.의미유보유지.')
