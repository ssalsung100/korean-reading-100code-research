import sys,json,copy
sys.dont_write_bytecode=True
from backfill_io import OUT,ROOT,BYCASE,source,entry,write,sha
base=json.loads((OUT/'BAI_source_with_restored_symbols.json').read_text());original=json.loads((ROOT/base['backfill_source_derivation']['original_source_path']).read_text())
m=json.loads((OUT/'source_overrides.json').read_text())
view='소리굽쇠는 고유한 공명 진동수를 가져서, 공명 진동수와 일치하는 소리를 가해 주면 공명하고, 공명 진동수에서 약간 벗어난 진동수의 소리를 가해 주면 공명하지 않는다. 그림과 같이 마주 향한 고정된 두 스피커에서 진동수 498Hz의 음파를 발생시키고, 공명 진동수가 500Hz인 소리굽쇠를 두 스피커 사이의 중앙에서 오른쪽으로 v의 속도로 움직였더니 소리굽쇠가 공명했다. 그 후에 다음과 같이 조작하면서 소리굽쇠의 공명 여부를 관찰했다. 단, 소리굽쇠는 두 스피커 사이에서만 움직인다.\nㄱ. 소리굽쇠를 중앙에서 왼쪽으로 v의 속도로 움직였다.\nㄴ. 소리굽쇠를 중앙에서 오른쪽으로 2v의 속도로 움직였다.\nㄷ. 왼쪽 스피커를 끄고 소리굽쇠를 중앙에서 왼쪽으로 v의 속도로 움직였다.'
for c in ['BAK','BAL']:
 q=BYCASE[c];assert q['unique_question'] not in m
 e=entry(q);s=copy.deepcopy(source(q));assert s['passage_text']==original['passage_text']
 s['passage_text']=base['passage_text']
 if c=='BAK':s['stem']=s['stem'].replace('[시각 자료 1]','<보기>\n'+view)
 s['backfill_source_derivation']={'original_source_path':e['source_path'],'original_sha256':sha(ROOT/e['source_path']),'restored_passage_from':'분석/패턴_종합연구/20261012_question_backfill_01/BAI_source_with_restored_symbols.json','evidence_paths':base['backfill_source_derivation']['evidence_paths'],'additional_repair':'BAK보기전체와기준v·ㄱv·ㄴ2v·ㄷv를공식렌더직접판독하여stem에복원' if c=='BAK' else 'BAL본문수치·기호만공통복원. 표는원래보충MD및공식렌더확인.','original_unchanged':True}
 name=c+'_source_with_restored_symbols.json';write(name,s);m[q['unique_question']]=str(OUT.relative_to(ROOT)/name)
write('source_overrides.json',m);print('BAK/BAL 공통본문·BAK보기 별도파생본 저장')
