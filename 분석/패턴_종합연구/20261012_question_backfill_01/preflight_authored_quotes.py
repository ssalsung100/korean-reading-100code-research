"""새 author 파일의 인용만 읽기 전용 확인.의미 감사나 저장을 대신하지 않음."""
import ast,sys
sys.dont_write_bytecode=True
import backfill_io as b
p=b.OUT/sys.argv[1]
def literal(n):
 if isinstance(n,ast.Call) and isinstance(n.func,ast.Name) and n.func.id=='B':
  return {'field':'stem','quote':ast.literal_eval(n.args[0])}
 return ast.literal_eval(n)
count=0
for n in ast.parse(p.read_text()).body:
 if not isinstance(n,ast.Expr) or not isinstance(n.value,ast.Call) or not isinstance(n.value.func,ast.Name) or n.value.func.id!='add':continue
 c=n.value;q=b.BYCASE[ast.literal_eval(c.args[0])]
 quotes=[literal(t.elts[1]) for t in c.args[2].elts]
 for sc in c.args[3].elts:quotes += [literal(x) for x in sc.args[1].elts]
 for quote in quotes:b.evidence(q,quote)
 count+=1
print(f'{p.name}: {count}문항의 작성 인용만 확인.저장·의미판정 없음.')
