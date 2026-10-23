import sys,ast
sys.dont_write_bytecode=True
from backfill_io import OUT,ROOT,add,scene as S
from resume_support_20261015_04 import guard,finish
P=lambda p,r:{'pattern_id':p,'case_specific_fit':r}
v=str(OUT.relative_to(ROOT)/'BEQ_BET_BEU_prior_review.json')
guard(['BEU'])
a=ast.parse((OUT/'author_016k.py').read_text())
selected=[n for n in a.body if isinstance(n,ast.Expr) and isinstance(n.value,ast.Call) and isinstance(n.value.func,ast.Name) and n.value.func.id=='add' and ast.literal_eval(n.value.args[0])=='BEU']
assert len(selected)==1
exec(compile(ast.Module(body=selected,type_ignores=[]),'author_016k.py:BEU복구','exec'))
finish('author_016k.py',['BEQ','BET','BEU'],['631~633 저장. 원문줄바꿈인용오류로BEQ/BET만먼저저장됨을확인한뒤BEU만복구. 기존2문항재실행없음.'])
