import sys,json,copy,itertools
sys.dont_write_bytecode=True
from backfill_io import OUT,ROOT,BYCASE,entry,source,write,sha
q=BYCASE['BFX'];e=entry(q);s=copy.deepcopy(source(q));m=json.loads((OUT/'source_overrides.json').read_text());assert q['unique_question'] not in m
structures=['(((A,B),C),D)','(((A,C),B),D)','(((A,D),B),C)','(((A,D),C),B)','(((B,C),A),D)']
s['choices']=['[계통도 직접 전사] '+t+'; 괄호는 먼저 결합한 분류군을 표시한다.' for t in structures]
s['backfill_source_derivation']={'original_source_path':e['source_path'],'original_sha256':sha(ROOT/e['source_path']),'official_page':'자료/LEET_언어이해/HWP_홀수형_페이지_렌더링/2010/page_005.png','official_crop':'분석/패턴_종합연구/20261012_question_backfill_01/BFX_official_choices_crop.png','method':'주 에이전트가2010홀수형12번의표·번호·다섯도식과G415_visual05~09를각각직접대조. 각번호의최초결합·후속결합·잎배치를텍스트전사. 가지길이의수치를새로부여하지않음.','mapping':{str(i+1):{'visual':f'data/기본기_연구/prepared_backlog/blind_sources/G415_visual{5+i:02}.jpg','structure':t} for i,t in enumerate(structures)},'resolves':'기존BFX의원선지번호대응유보만이번사후보완에서해소. 최초blind의번호불확실성기록은보존.','original_unchanged':True}
n='BFX_source_with_verified_choices.json';write(n,s);m[q['unique_question']]=str(OUT.relative_to(ROOT)/n);write('source_overrides.json',m)
sets={'A':{3,6},'B':{1,2,3,5,6,7},'C':{3,4,8},'D':set()}
d={a+b:len(sets[a]^sets[b])/8 for a,b in itertools.combinations(sets,2)}
write('BFX_source_and_distance_review.json',{'source_derivation':s['backfill_source_derivation'],'positive_character_sets':{k:sorted(v) for k,v in sets.items()},'pairwise_distances':d,'after_first_merge':{'AD-C':(d['AC']+d['CD'])/2,'AD-B':(d['AB']+d['BD'])/2,'B-C':d['BC']},'chosen_topology':structures[3],'official_choice_number_verified':4,'verification_scope':'공식문제지선지번호확인과표기반검산. 정답표의새독립시각대조아님.'})
print('BFX 다섯 선지 번호 대응 확인·거리 검산 저장')
