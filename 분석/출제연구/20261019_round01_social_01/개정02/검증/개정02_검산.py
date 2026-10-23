"""개정02의 수치·반례·자료 보존·배포 구성을 확인한다.

자연어 선지의 의미와 모든 해석을 자동 증명하는 스크립트가 아니다.
원문·원장에는 쓰지 않고 개정02 안의 검증 결과와 독립 풀이 ZIP만 만든다.
"""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
from zipfile import ZipFile, ZIP_DEFLATED
import json
import re

OUT = Path(__file__).resolve().parents[1]
ROOT = OUT.parents[3]
VERIFY = OUT / "검증"


def digest(p):
    return sha256(p.read_bytes()).hexdigest()


def metrics(incomes, z=100):
    gaps = [max(F(z) - F(y), F(0)) for y in incomes]
    g = [x / z for x in gaps]
    n = len(incomes)
    q = sum(x > 0 for x in gaps)
    return dict(H=F(q, n), G=sum(g) / n, S=sum(x*x for x in g) / n,
                T=sum(gaps), q=q, I=sum(g)/q if q else None)


def serial(value):
    if isinstance(value, F):
        return {"유리수": str(value), "소수값": float(value)}
    if isinstance(value, dict):
        return {k: serial(v) for k, v in value.items()}
    if isinstance(value, list):
        return [serial(v) for v in value]
    return value


def question_parts(text):
    pat = r"(?ms)^## ([123])\. ([^\n]+)\n(.*?)(?=^## [123]\. |\Z)"
    result = {}
    for m in re.finditer(pat, text):
        choices = re.findall(r"(?m)^([①②③④⑤]) (.+)$", m[3])
        assert [c[0] for c in choices] == list("①②③④⑤")
        result[int(m[1])] = dict(stem=m[2], block=m[0],
                                choices=dict(choices),
                                view=m[3].split("\n① ", 1)[0])
    assert set(result) == {1, 2, 3}
    return result


# 1. 풀이의 결정적 수치와 반례
states = {
    "지급 전": [20, 80, 100, 160],
    "갑": [20, 100, 100, 160],
    "을": [40, 80, 100, 160],
    "병": [25, 85, 105, 165],
    "을 뒤 B→A 10": [50, 70, 100, 160],
    "갑 뒤 B→A 10": [30, 90, 100, 160],
    "을 뒤 각 40": [80, 120, 100, 160],
    "을 뒤 A60 B20": [100, 100, 100, 160],
}
expected = {
    "지급 전": (F(1,2), F(1,4), F(17,100), 100),
    "갑": (F(1,4), F(1,5), F(4,25), 80),
    "을": (F(1,2), F(1,5), F(1,10), 80),
    "병": (F(1,2), F(9,40), F(117,800), 90),
    "을 뒤 B→A 10": (F(1,2), F(1,5), F(17,200), 80),
    "갑 뒤 B→A 10": (F(1,2), F(1,5), F(1,8), 80),
    "을 뒤 각 40": (F(1,4), F(1,20), F(1,100), 20),
    "을 뒤 A60 B20": (F(0), F(0), F(0), 0),
}
computed = {name: metrics(vals) for name, vals in states.items()}
for name, values in computed.items():
    assert tuple(values[k] for k in ("H", "G", "S", "T")) == expected[name]
    assert values["T"] == 4 * 100 * values["G"]

# 1번①: 두 지급이 각기 G에 기여하는 양은 같고 S의 기여는 다름.
baseline = metrics([20,80,100,160])
pay_low = metrics([30,80,100,160])
pay_high = metrics([20,90,100,160])
assert baseline["G"] - pay_low["G"] == baseline["G"] - pay_high["G"] == F(1,40)
assert baseline["S"] - pay_low["S"] == F(3,80)
assert baseline["S"] - pay_high["S"] == F(3,400)

# 1번②: 같은 H에서 G가 낮아졌어도 S가 높아지는 반례.
c1 = metrics([40,40,100,160])
c2 = metrics([10,80,100,160])
assert c1["H"] == c2["H"]
assert c2["G"] < c1["G"] and c2["S"] > c1["S"]

# 1번④: 조건이 실제 가능한지 검사. 일반 증명은 교사용 문서의 합/분모 논증.
avg_before = metrics([20,100,100,160])
avg_after = metrics([80,90,100,160])
assert avg_after["q"] > avg_before["q"]
assert avg_after["G"] < avg_before["G"]
assert avg_after["I"] < avg_before["I"]

# 2번: 같은 보고값과 평균, 서로 다른 문턱 아래 인원·최저 소득·S.
witnesses = [[60,60,120,160], [30,90,120,160]]
w = [metrics(x) for x in witnesses]
for x in w:
    assert x["q"] == 2 and x["H"] == F(1,2) and x["G"] == F(1,5)
    assert x["I"] == F(2,5) and x["T"] == 80
assert [sum(y < 50 for y in x) for x in witnesses] == [0,1]
assert [min(x) for x in witnesses] == [60,30]
assert [x["S"] for x in w] == [F(2,25), F(1,8)]
# 고정된 합에서 제곱합 최솟값: S >= (0.8^2 / 2) / 4 = 0.08.
s_lower_bound = F(4,5)**2 / 2 / 4
assert s_lower_bound == F(2,25) > F(1,25)

# 3번⑤의 가장 짧은 충분 근거.
assert states["을"][0] + 40 == 80 < 100

# 2. 지문·발문·보기·유지 선지, 실제 변경 개수
original_path = OUT.parent / "개정01/03_학생용_개정본.md"
student_path = OUT / "04_학생용_개정02_최종.md"
old = original_path.read_text()
new = student_path.read_text()
assert old.split("\n## 1.",1)[0] == new.split("\n## 1.",1)[0]
o, n = question_parts(old), question_parts(new)
assert all(o[q]["stem"] == n[q]["stem"] for q in o)
assert all(o[q]["view"] == n[q]["view"] for q in o)
assert o[2]["block"] == n[2]["block"]
changed = [(q, c) for q in o for c in o[q]["choices"]
           if o[q]["choices"][c] != n[q]["choices"][c]]
assert changed == [(1,"①"),(1,"③"),(1,"⑤"),(3,"②"),(3,"③"),(3,"④"),(3,"⑤")]
assert len(changed) == 7
lengths = []
for q in o:
    for c in o[q]["choices"]:
        lengths.append({"문항":q, "선지":c,
                        "개정01_글자수_공백포함":len(o[q]["choices"][c]),
                        "개정02_글자수_공백포함":len(n[q]["choices"][c]),
                        "변경":(q,c) in changed})

# 3. 사전에 저장한 지정 6개 파일의 보존 상태. 저장소 전수 감사가 아님.
saved = json.loads((VERIFY / "기존자료_보존해시.json").read_text())
preserved = {}
for path, expected_hash in saved.items():
    observed = digest(ROOT / path)
    assert observed == expected_hash, path
    preserved[path] = observed

# 4. 정답을 가린 전달 묶음: 허용한 두 파일만 넣음.
packet_files = ["00_먼저읽기.md", "01_학생용.md"]
assert (OUT/"독립풀이용/01_학생용.md").read_bytes() == student_path.read_bytes()
zip_path = OUT / "독립풀이용_개정02.zip"
with ZipFile(zip_path, "w", ZIP_DEFLATED) as z:
    for filename in packet_files:
        z.write(OUT/"독립풀이용"/filename, filename)
with ZipFile(zip_path) as z:
    assert z.namelist() == packet_files
    assert z.testzip() is None
    assert z.read("01_학생용.md") == student_path.read_bytes()

# 보고서 링크를 검사하기 위해 결과 파일을 먼저 만듦.
report_path = VERIFY / "검산결과.json"
report_path.write_text("{}\n")
broken = []
for md in OUT.rglob("*.md"):
    for url in re.findall(r"\]\(([^\n)]+)\)",md.read_text()):
        url = url.strip().strip("<>")
        if re.match(r"[a-zA-Z]+://",url) or url.startswith("#"):
            continue
        url = url.split("#",1)[0]
        if url and not (md.parent/url).exists():
            broken.append([str(md.relative_to(OUT)),url])
assert not broken, broken

report = {
    "상태":"PASS — 아래의 수치·구조·지정 파일 보존 범위에 한함",
    "제한":"자연어 의미·문체 자연스러움·실제 학생 오답 유인은 자동 검증하지 않음. 독립 외부 검토 미실시.",
    "자체_의미판정_기록":{"1":[False,False,False,True,False],
                         "2":[False,True,False,False,False],
                         "3":[True,True,True,True,False]},
    "의미판정_근거":"05_교사용_정답과15선지해설.md의 전 선지 논증. 코드가 자연어를 읽고 자동 판정한 결과가 아님.",
    "정답":["④","②","⑤"],
    "3번_상태별_검산":computed,
    "1번①_각지급의_G감소":[baseline["G"]-pay_low["G"],baseline["G"]-pay_high["G"]],
    "1번①_각지급의_S감소":[baseline["S"]-pay_low["S"],baseline["S"]-pay_high["S"]],
    "1번②_반례":[c1,c2],
    "1번④_실현가능_예":[avg_before,avg_after],
    "2번_동일보고값_증거":{"소득배열":witnesses,"지표":w,"S의_최솟값":s_lower_bound},
    "원문보존":{"지문":True,"세발문":True,"두보기":True,"2번전체":True,
              "동일선지수":8,"변경선지수":7},
    "선지길이_국소진단_평가원통계아님":lengths,
    "지정6개원본_보존해시":preserved,
    "독립풀이_ZIP_포함파일":packet_files,
    "독립풀이_학생용_바이트일치":True,
    "깨진_로컬링크":broken,
}
report_path.write_text(json.dumps(serial(report), ensure_ascii=False,indent=2)+"\n")
print(json.dumps({"상태":"PASS","정답":["④","②","⑤"],
                  "변경선지":changed,"보존확인_지정파일수":len(saved),
                  "독립풀이ZIP":packet_files,"깨진링크":broken},ensure_ascii=False))
