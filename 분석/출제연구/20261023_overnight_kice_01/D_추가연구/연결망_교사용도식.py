"""현재 학생용 3번 표에서 연결을 읽어 교사용 정적 도식을 만든다."""
from pathlib import Path
import os
os.environ.setdefault('MPLCONFIGDIR','/tmp/overnight_kice_mpl')
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
from matplotlib.font_manager import FontProperties

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'도식'
OUT.mkdir(exist_ok=True)
source=(ROOT/'04_사회적확산_학생용후보.md').read_text().split('## 3.',1)[1]
graphs={'I':{},'II':{}}
for line in source.splitlines():
    if not line.startswith('|'):
        continue
    cells=[x.strip() for x in line.strip('|').split('|')]
    if len(cells)==3 and cells[0] in list('ABCDEF'):
        for name,column in [('I',1),('II',2)]:
            graphs[name][cells[0]]={x.strip() for x in cells[column].split(',')}


def adoption_times(g):
    active=set('AB');times={v:(0 if v in active else None) for v in g}
    for t in range(1,len(g)+1):
        new={v for v in g if v not in active and len(g[v]&active)>=2}
        if not new:
            return times
        for v in new:times[v]=t
        active|=new
    return times


known=json.loads((ROOT/'사회적확산_검증결과.json').read_text())['모형']
times={}
for name,g in graphs.items():
    assert set(g)==set('ABCDEF')
    assert all(len(g[v])==3 and all(v in g[w] for w in g[v]) for v in g)
    times[name]=adoption_times(g)
    assert times[name]==known[name]['최초채택']

regular=FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc')
bold=FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc')
plt.rcParams['svg.fonttype']='path'
fig,ax=plt.subplots(figsize=(14,7),dpi=160)
fig.patch.set_facecolor('white')
ax.set_xlim(0,1130);ax.set_ylim(565,0);ax.set_aspect('equal');ax.axis('off')
ax.text(565,28,'사회적 확산 3번 · 정답 진술을 직접 확인하는 도식',ha='center',va='center',fontproperties=bold,fontsize=19,color='#172b4d')
positions={
 'I':{'A':(85,180),'B':(85,340),'D':(260,130),'E':(260,260),'F':(260,390),'C':(435,260)},
 'II':{'A':(650,150),'B':(650,370),'D':(785,260),'C':(1040,150),'E':(1040,370),'F':(900,260)},
}
colors={0:'#345e9e',1:'#e9a23b',2:'#2a7f62',None:'#e7e9ed'}
for name,left,width in [('I',20,500),('II',570,540)]:
    ax.add_patch(Rectangle((left,90),width,350,facecolor='#fbfcfe',edgecolor='#cdd5df',linewidth=1))
    ax.text(left+width/2,72,f'모형 {name}',ha='center',fontproperties=bold,fontsize=17,color='#172b4d')
    g=graphs[name];pos=positions[name]
    edges={(min(a,b),max(a,b)) for a in g for b in g[a]}
    assert len(edges)==9
    for a,b in sorted(edges):
        x1,y1=pos[a];x2,y2=pos[b]
        ax.plot([x1,x2],[y1,y2],color='#7d8998',linewidth=1.5,zorder=1)
    for v,(x,y) in pos.items():
        stage=times[name][v];fg='white' if stage in [0,2] else '#18212f'
        ax.add_patch(Circle((x,y),27,facecolor=colors[stage],edgecolor='white',linewidth=2,zorder=2))
        ax.text(x,y-6,v,ha='center',va='center',fontproperties=bold,fontsize=17,color=fg,zorder=3)
        ax.text(x,y+12,str(stage) if stage is not None else '—',ha='center',va='center',fontproperties=regular,fontsize=11,color=fg,zorder=3)
ax.text(270,464,'0단계 A·B → 1단계 D·E·F → 2단계 C',ha='center',fontproperties=regular,fontsize=12,color='#172b4d')
ax.text(840,464,'0단계 A·B → 1단계 D → 이후 변화 없음',ha='center',fontproperties=regular,fontsize=12,color='#172b4d')
ax.text(840,487,'1단계 이후 C·E·F의 채택 이웃은 각각 1명',ha='center',fontproperties=regular,fontsize=11,color='#525e6c')
for stage,label,x in [(0,'초기 채택',100),(1,'1단계 채택',330),(2,'2단계 채택',560),(None,'미채택',800)]:
    ax.add_patch(Circle((x,520),8,facecolor=colors[stage],edgecolor='#7d8998',linewidth=.5))
    ax.text(x+16,520,label,va='center',fontproperties=regular,fontsize=11,color='#172b4d')
ax.text(565,552,'교사용 · 연결은 양방향이며 원 안의 숫자는 최초 채택 단계이다. 연결망은 창작 모형이다.',ha='center',fontproperties=regular,fontsize=10,color='#525e6c')
fig.tight_layout(pad=.3)
for ext in ['svg','png']:
    fig.savefig(OUT/f'두연결망_최초채택단계.{ext}',facecolor='white',bbox_inches='tight')
plt.close(fig)
print(json.dumps({'도식':'현재 학생용 표와 검증 결과 일치','파일':['도식/두연결망_최초채택단계.svg','도식/두연결망_최초채택단계.png']},ensure_ascii=False))
