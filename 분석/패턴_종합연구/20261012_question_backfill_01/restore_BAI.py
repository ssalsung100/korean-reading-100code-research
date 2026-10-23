import sys,json,copy
sys.dont_write_bytecode=True
from backfill_io import OUT,ROOT,BYCASE,entry,source,sha,write
q=BYCASE['BAI'];e=entry(q);s=copy.deepcopy(source(q))
m=json.loads((OUT/'source_overrides.json').read_text());assert q['unique_question'] not in m
pairs=[('온도는 이며 이를 절대 온도 라고 한다. 실제로 까지','온도는 -273.16℃이며 이를 절대 온도 0K라고 한다. 실제로 0K까지'),('상온(약 )에서 대략 의','상온(약 300K)에서 대략 200m/s의'),('원래의 약 까지','원래의 약 1/10000까지'),('상온에서 의 속도로','상온에서 200m/s의 속도로'),('에너지 준위 에서 그보다 더 높은 특정 에너지 준위 로','에너지 준위 E₁에서 그보다 더 높은 특정 에너지 준위 E₂로'),('에너지 값의 차이 에','에너지 값의 차이 ΔE에'),('에너지는 보다 작지만','에너지는 ΔE보다 작지만'),('낮은 준위 에 있던','낮은 준위 E₁에 있던'),('허용된 준위 에 올려','허용된 준위 E₂에 올려'),('잠시 후에 에 해당하는','잠시 후에 ΔE에 해당하는'),('전자를 에서 로 내려놓는다','전자를 E₂에서 E₁로 내려놓는다')]
for a,b in pairs:
 assert a in s['passage_text'],a
 s['passage_text']=s['passage_text'].replace(a,b)
assert '절대 온도 에' in s['choices'][3]
s['choices'][3]=s['choices'][3].replace('절대 온도 에','절대 온도 0K에')
s['backfill_source_derivation']={'original_source_path':e['source_path'],'original_sha256':sha(ROOT/e['source_path']),'evidence_paths':['data/기본기_연구/prepared_backlog/blind_sources/G368_restore_page13.png','data/기본기_연구/prepared_backlog/blind_sources/G368_restore_page14.png'],'method':'기존공식렌더를주에이전트가직접판독하여이번폴더파생본에누락수치·기호·선지④0K만복원.','changes':[{'old':a,'new':b} for a,b in pairs]+[{'field':'choices.3','new':s['choices'][3]}],'limits':'-273.16℃는공식인쇄표기를그대로보존. 평균운동속도의제곱·원자의진동수라는기존문구를외부물리지식으로교정하지않음.','original_unchanged':True}
name='BAI_source_with_restored_symbols.json';write(name,s);m[q['unique_question']]=str(OUT.relative_to(ROOT)/name);write('source_overrides.json',m)
print('BAI 파생본문·④0K 복원 저장. 원본·기존hold 불변.')
