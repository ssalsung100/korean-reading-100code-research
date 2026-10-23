import json
import html
from 연구도구 import BASE, ROOT, log

SELECT = {
    "PA01": [15, 16], "PA02": [37, 40], "PA03": [14, 16],
    "PA04": [47, 49], "PA05": [18, 20], "PA06": [43, 44],
    "PA07": [22, 23], "PA08": [23, 24], "PA09": [17, 19],
    "PA10": [28, 29], "PA11": [19, 20], "PA12": [18, 20],
    "PA13": [28, 29], "PA14": [25, 26], "PA15": [39, 41],
    "PA16": [15, 17], "PA17": [14, 15], "PA18": [9, 10],
}
rows = [json.loads(x) for x in (ROOT / "data/kice_questions.jsonl").read_text().splitlines()]
samples = [json.loads(x) for x in (BASE / "02_평가원지문_표본목록.jsonl").read_text().splitlines()]
for s in samples[:18]:
    sid = s["sample_id"]
    assert (BASE / f"03_지문별_심층분석/{sid}.md").exists()
    selected = [r for r in rows if r["passage_id"] == s["passage_id"] and r["question_number"] in SELECT[sid]]
    text = "\n\n".join(f"## {r['question_number']}번\n\n" + html.unescape(r["stem"]) + "\n\n" +
                       "\n\n".join(f"{i}. {html.unescape(x)}" for i, x in enumerate(r["choices"], 1))
                       for r in selected)
    (BASE / f"근거/문항/{sid}.md").write_text(text + "\n")
log("문항자료_개방", list(SELECT), "18개 지문 자체 분석 저장 후 각 2문항을 발췌. 답·해설·SDSS는 출력하지 않았다. 시각자료가 부족한 몽타주50·음악45·수분25·CT21·검색16은 완전 문항 분석에서 제외한다.")
