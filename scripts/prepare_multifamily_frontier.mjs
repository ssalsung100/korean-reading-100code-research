#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';

// Mechanical preparation only. All proposed records and blind assets are
// validated in memory before any READY rows or files are written.
const root = process.cwd();
const readJsonl = (file) => fs.readFileSync(file, 'utf8').split(/\r?\n/).filter(Boolean).map(JSON.parse);
const sha256Bytes = (value) => crypto.createHash('sha256').update(value).digest('hex');
const sha256File = (file) => sha256Bytes(fs.readFileSync(file));
const writeJson = (file, value) => fs.writeFileSync(file, JSON.stringify(value, null, 2) + '\n', 'utf8');
const appendJsonl = (file, rows) => fs.appendFileSync(file, rows.map((x) => JSON.stringify(x)).join('\n') + (rows.length ? '\n' : ''), 'utf8');

const base = path.join(root, 'data/기본기_연구/prepared_backlog');
const blindDir = path.join(base, 'blind_sources');
const packetDir = path.join(base, 'packets');
const sealedDir = path.join(base, 'sealed');
const manifestPath = path.join(base, 'manifest.jsonl');
const mappingPath = path.join(sealedDir, 'provenance_mapping.jsonl');
const answerPath = path.join(sealedDir, 'answer_sdss.jsonl');
const completionCrosswalkPath = path.join(root, 'data/기본기_연구/target_completion_crosswalk_v1.jsonl');
const researchCrosswalkPath = path.join(root, 'data/기본기_연구/research_case_target_crosswalk_v1.jsonl');
const reportDate = new Intl.DateTimeFormat('en-CA', {
  timeZone: 'Asia/Seoul', year: 'numeric', month: '2-digit', day: '2-digit',
}).format(new Date()).replaceAll('-', '');
const dryRun = process.argv.includes('--dry-run');

const candidates = readJsonl(path.join(root, 'data/기본기_연구/code_study_candidates_v2.jsonl'));
const manifest = readJsonl(manifestPath);
const mapping = readJsonl(mappingPath);
const answers = readJsonl(answerPath);
const targetCrosswalkRows = fs.existsSync(completionCrosswalkPath) ? readJsonl(completionCrosswalkPath) : [];
const researchCrosswalkRows = fs.existsSync(researchCrosswalkPath) ? readJsonl(researchCrosswalkPath) : [];
const targetCrosswalkById = new Map(targetCrosswalkRows.map((x) => [x.candidate_id, x]));
const researchCrosswalkByCase = new Map(researchCrosswalkRows.map((x) => [x.case_id, x]));
const consumedCaseIds = new Set(manifest.filter((x) => x.status === 'consumed_sdss').map((x) => x.case_id));
const targetCrosswalkValid = targetCrosswalkRows.length === candidates.length
  && targetCrosswalkById.size === candidates.length
  && candidates.every((x) => targetCrosswalkById.has(x.candidate_id))
  && researchCrosswalkRows.length === consumedCaseIds.size
  && researchCrosswalkByCase.size === consumedCaseIds.size
  && [...consumedCaseIds].every((id) => researchCrosswalkByCase.has(id))
  && targetCrosswalkRows.every((x) => ['COMPLETED_TARGET', 'HOLD', 'NOT_COMPLETED_READY_LOCAL_SOURCE',
    'NOT_COMPLETED_NEEDS_RESTORE', 'NOT_COMPLETED_SOURCE_MISSING', 'AMBIGUOUS_COMPLETION'].includes(x.status))
  && targetCrosswalkRows.filter((x) => x.status === 'COMPLETED_TARGET').every((x) => {
    const linkedCase = researchCrosswalkByCase.get(x.matched_case_id);
    return Boolean(linkedCase && linkedCase.status === 'TARGET_MATCHED' && linkedCase.candidate_id === x.candidate_id);
  });
const meetRows = readJsonl(path.join(root, 'data/meet_questions.jsonl'));
const meetQuestions = new Map(meetRows.map((x) => [x.question_id, x]));
const kiceRows = readJsonl(path.join(root, 'data/kice_questions.jsonl'));
const kiceQuestions = new Map(kiceRows.map((x) => [x.question_id, x]));
const meetVisualIndex = JSON.parse(fs.readFileSync(path.join(root, '자료/MEET_언어추론/검증/MEET_시각자료_문항별_분류_v1.json'), 'utf8'));
const meetVisuals = new Map((meetVisualIndex.records ?? []).map((x) => [x.visual_id, x]));
const leetVisualMapPath = path.join(root, '자료/LEET_언어이해/검증/HWP_홀수형_시각자료_문항매핑_v1.json');
const leetVisualIndex = fs.existsSync(leetVisualMapPath) ? JSON.parse(fs.readFileSync(leetVisualMapPath, 'utf8')) : { papers: [] };
const leetVisualMapHash = fs.existsSync(leetVisualMapPath) ? sha256File(leetVisualMapPath) : null;

const alphaValue = (id) => [...id].reduce((n, c) => n * 26 + c.charCodeAt(0) - 64, 0);
const alpha = (value) => {
  let n = value, out = '';
  while (n > 0) { n -= 1; out = String.fromCharCode(65 + (n % 26)) + out; n = Math.floor(n / 26); }
  return out;
};
const caseValues = manifest.map((x) => x.case_id).filter((x) => /^[A-Z]+$/.test(x)).map(alphaValue);
const nextCaseValue = Math.max(0, ...caseValues) + 1;
const maxManifestGroup = Math.max(0, ...manifest.map((x) => Number(String(x.passage_group ?? '').replace(/^G/, ''))).filter(Number.isFinite));
const firstNewGroupNumber = maxManifestGroup + 1;
const reportPath = path.join(base, `LUNA_FRONTIER_PREFLIGHT_${reportDate}_G${String(firstNewGroupNumber).padStart(3, '0')}.md`);
const releaseRules = [
  'all_group_blind_records_before_any_group_answer_check',
  'all_group_independent_code_records_before_any_group_sdss_disclosure',
];

const normExam = (family, raw) => {
  let s = String(raw ?? '').normalize('NFKC').replace(/[\s_]/g, '').replaceAll('국어', '');
  if (family === 'KICE') {
    s = s.replace('6평', '6월모평').replace('9평', '9월모평').replace(/([AB])형$/u, '$1');
    s = s.replace('예시', '예시문항');
  }
  return s;
};
const sourceKey = (family, year, exam, questionNumber) => `${family}|${year}|${normExam(family, exam)}|${questionNumber}`;
const candidateKey = (x) => sourceKey(x.source?.exam_family, x.source?.year, x.source?.exam_type, x.source?.question_number);

// Previously prepared/consumed questions, including older independent-study
// sources that predate the candidate index, are treated as used source IDs.
const usedQuestionIds = new Set();
const usedCandidateIds = new Set();
const usedSourceKeys = new Set();
const usedPassageIds = new Set();
const holdCaseIds = new Set(manifest.filter((x) => x.status === 'prepared').map((x) => x.case_id));
for (const row of [...mapping, ...answers]) {
  const p = row.provenance ?? {};
  if (p.question_id) usedQuestionIds.add(p.question_id);
  if (p.candidate_id || row.candidate_id) usedCandidateIds.add(p.candidate_id ?? row.candidate_id);
  if (holdCaseIds.has(row.case_id)) {
    if (p.question_id) usedQuestionIds.add(p.question_id);
    if (p.candidate_id || row.candidate_id) usedCandidateIds.add(p.candidate_id ?? row.candidate_id);
  }
  if (p.exam_family && p.academic_year && p.exam_label && p.question_number) {
    usedSourceKeys.add(sourceKey(p.exam_family, p.academic_year, p.exam_label, p.question_number));
  }
  if (p.passage_id) usedPassageIds.add(p.passage_id);
}
for (const row of manifest) {
  if (row.passage_group) usedPassageIds.add(row.passage_group);
  if (row.status === 'consumed_sdss' && row.passage_group) usedPassageIds.add(row.passage_group);
}
const qidPattern = /(?:KICE|LEET|MEET|DEET)-[\p{L}\p{N}_~.-]+-Q\d+/gu;
const historicalFiles = (() => {
  const dir = path.join(root, '분석/기본기_연구');
  if (!fs.existsSync(dir)) return [];
  const out = [];
  const walk = (d) => {
    for (const item of fs.readdirSync(d, { withFileTypes: true })) {
      const f = path.join(d, item.name);
      if (item.isDirectory()) walk(f);
      else if (/\.(?:md|json|jsonl|txt)$/i.test(item.name)) out.push(f);
    }
  };
  walk(dir);
  return out;
})();
const historicalQuestionIds = new Set();
const historicalCandidateIds = new Set();
for (const file of historicalFiles) {
  const text = fs.readFileSync(file, 'utf8');
  for (const id of text.match(qidPattern) ?? []) historicalQuestionIds.add(id);
  for (const id of text.match(/CAND-[a-f0-9]{16}/gi) ?? []) historicalCandidateIds.add(id);
}
for (const id of historicalQuestionIds) usedQuestionIds.add(id);
for (const id of historicalCandidateIds) usedCandidateIds.add(id);

// Old raw research sometimes stores candidate/question references under
// structured fields rather than the new sealed mapping. Inspect identifiers
// only; this branch never reads or interprets research payloads.
const oldQueuePath = path.join(root, 'data/기본기_연구/astra_handoff_queue.jsonl');
const oldQueueRows = fs.existsSync(oldQueuePath) ? readJsonl(oldQueuePath) : [];
const candidateIdSet = new Set(candidates.map((x) => x.candidate_id));
const collectStudyRefs = (node) => {
  if (Array.isArray(node)) { for (const x of node) collectStudyRefs(x); return; }
  if (!node || typeof node !== 'object') return;
  for (const [key, value] of Object.entries(node)) {
    if (typeof value === 'string') {
      if (key.toLowerCase().includes('candidate_id') && candidateIdSet.has(value)) usedCandidateIds.add(value);
      if ((key.toLowerCase().includes('question_id') || key.toLowerCase() === 'source_id') && /^(?:KICE|LEET|MEET|DEET)-/.test(value)) usedQuestionIds.add(value);
    }
    collectStudyRefs(value);
  }
};
for (const row of oldQueueRows) collectStudyRefs(row);

// Match an older source ID to candidate source coordinates where its legacy
// ID spelling differs. Then reject its whole passage group.
const qidLookup = new Map(candidates.filter((x) => x.canonical_connection?.question_id).map((x) => [x.canonical_connection.question_id, x]));
for (const qid of usedQuestionIds) {
  const hit = qidLookup.get(qid);
  if (hit) usedSourceKeys.add(candidateKey(hit));
}
const isUsedSource = (row) => usedCandidateIds.has(row.candidate_id)
  || usedQuestionIds.has(row.canonical_connection?.question_id)
  || usedSourceKeys.has(candidateKey(row));
const projectMetaStatePath = path.join(root, 'data/기본기_연구/meta_state.json');
const projectMetaState = fs.existsSync(projectMetaStatePath) ? JSON.parse(fs.readFileSync(projectMetaStatePath, 'utf8')) : null;
const heldCandidateIds = new Set();
const heldQuestionIds = new Set();
const heldSourceKeys = new Set();
for (const row of [...mapping, ...answers].filter((x) => holdCaseIds.has(x.case_id))) {
  const p = row.provenance ?? {};
  const candidateId = p.candidate_id ?? row.candidate_id;
  if (candidateId) heldCandidateIds.add(candidateId);
  if (p.question_id) heldQuestionIds.add(p.question_id);
  if (p.exam_family && p.academic_year && p.exam_label && p.question_number) {
    heldSourceKeys.add(sourceKey(p.exam_family, p.academic_year, p.exam_label, p.question_number));
  }
}
const crosswalkHoldCandidateIds = targetCrosswalkValid
  ? new Set(targetCrosswalkRows.filter((x) => x.status === 'HOLD').map((x) => x.candidate_id))
  : new Set(candidates.filter((x) => heldCandidateIds.has(x.candidate_id)
    || heldQuestionIds.has(x.canonical_connection?.question_id)
    || heldSourceKeys.has(candidateKey(x))).map((x) => x.candidate_id));
const crosswalkAmbiguousCandidateIds = targetCrosswalkValid
  ? new Set(targetCrosswalkRows.filter((x) => x.status === 'AMBIGUOUS_COMPLETION').map((x) => x.candidate_id))
  : new Set();
const crosswalkCompletedCandidateIds = targetCrosswalkValid
  ? new Set(targetCrosswalkRows.filter((x) => x.status === 'COMPLETED_TARGET').map((x) => x.candidate_id))
  : new Set(candidates.filter((x) => isUsedSource(x)
    && !crosswalkHoldCandidateIds.has(x.candidate_id)).map((x) => x.candidate_id));
const crosswalkBlockedRows = targetCrosswalkRows.filter((x) => ['COMPLETED_TARGET', 'HOLD', 'AMBIGUOUS_COMPLETION'].includes(x.status));
const usedCandidateIdsForChecks = targetCrosswalkValid
  ? new Set(crosswalkBlockedRows.map((x) => x.candidate_id)) : usedCandidateIds;
const usedQuestionIdsForChecks = targetCrosswalkValid
  ? new Set(crosswalkBlockedRows.map((x) => x.target_question_id).filter(Boolean)) : usedQuestionIds;
const completionCrosswalkGap = targetCrosswalkValid ? 0 : candidates.length;

const candidateIdCounts = new Map();
const questionIdCounts = new Map();
for (const c of candidates) {
  candidateIdCounts.set(c.candidate_id, (candidateIdCounts.get(c.candidate_id) ?? 0) + 1);
  const qid = c.canonical_connection?.question_id;
  if (qid) questionIdCounts.set(qid, (questionIdCounts.get(qid) ?? 0) + 1);
}

const grouped = new Map();
for (const c of candidates) {
  const pid = c.canonical_connection?.passage_id;
  if (!pid) continue;
  if (!grouped.has(pid)) grouped.set(pid, []);
  grouped.get(pid).push(c);
}
const familyRank = { LEET: 0, MEET: 1, DEET: 1, KICE: 2 };
const groupFirstQuestion = (rows) => Math.min(...rows.map((x) => Number(x.source?.question_number) || 0));
const groupSort = (a, b) => (a[1][0].source.year - b[1][0].source.year)
  || (groupFirstQuestion(a[1]) - groupFirstQuestion(b[1]))
  || a[0].localeCompare(b[0], 'en');
for (const [pid, rows] of grouped) rows.sort((a, b) => a.source.question_number - b.source.question_number);

const unresolvedById = new Map();
const addUnresolved = (row) => {
  const key = `${row.status}|${row.family}|${row.passage_group}|${row.reason}`;
  if (!unresolvedById.has(key)) unresolvedById.set(key, row);
};
const reportUnresolved = (g, status, reason) => addUnresolved({
  family: g.family, passage_group: g.id, question_count: g.rows.length, status, reason,
});
const sourceMissingLeet2008 = candidates.filter((x) => x.source?.exam_family === 'LEET'
  && x.source?.year === 2008 && x.source?.exam_type === '리트예비'
  && x.source.question_number >= 4 && x.source.question_number <= 8);
if (sourceMissingLeet2008.length) addUnresolved({
  family: 'LEET', passage_group: 'LEET-2008예비-Q04-08', question_count: sourceMissingLeet2008.length,
  status: 'SOURCE_MISSING', reason: '2008 예비 Q4~8 canonical source is not in the local repository',
});
for (const row of candidates) {
  const c = row.canonical_connection ?? {};
  if (row.source?.exam_family !== 'KICE' || c.status !== 'kice_question_not_in_local_reading_scope' || isUsedSource(row)) continue;
  const pid = c.passage_id ?? `KICE-${row.source.year}-${row.source.exam_type}-Q${row.source.question_number}`;
  addUnresolved({ family: 'KICE', passage_group: pid, question_count: 1, status: 'SOURCE_MISSING', reason: 'KICE question is outside the local canonical reading-source scope' });
}
for (const row of candidates) {
  const c = row.canonical_connection ?? {};
  if (row.source?.exam_family !== 'KICE' || c.status !== 'exact_canonical_kice_question_visual_choice_review_required' || isUsedSource(row)) continue;
  addUnresolved({ family: 'KICE', passage_group: c.passage_id ?? `KICE-${row.source.year}-Q${row.source.question_number}`, question_count: 1, status: 'NEEDS_RESTORE', reason: 'KICE visual choice material requires source restoration' });
}

function parseLeetMarkdown(sourcePath, requestedNumbers, passageId) {
  const abs = path.join(root, sourcePath);
  if (!fs.existsSync(abs)) return { error: 'canonical markdown missing' };
  const raw = fs.readFileSync(abs, 'utf8');
  const answerAt = raw.search(/^##\s*(?:정답|해설)\s*$/m);
  const usable = answerAt >= 0 ? raw.slice(0, answerAt) : raw;
  const heads = [...usable.matchAll(/^##\s+(\d+)\.\s*([^\n]*)$/gm)];
  if (!heads.length) {
    const ranges = [...usable.matchAll(/^\[(\d+)\s*[~～〜-]\s*(\d+)\]\s*다음\s*글을\s*읽고\s*물음에\s*답하시오\.\s*$/gm)];
    const groupRange = String(passageId ?? '').match(/-Q0*(\d+)-0*(\d+)$/);
    const requestedStart = groupRange ? Number(groupRange[1]) : Math.min(...requestedNumbers);
    const requestedEnd = groupRange ? Number(groupRange[2]) : Math.max(...requestedNumbers);
    const rangeIndex = ranges.findIndex((x) => Number(x[1]) === requestedStart && Number(x[2]) === requestedEnd);
    if (rangeIndex < 0) return { error: 'legacy passage range heading missing' };
    const h = ranges[rangeIndex], blockStart = h.index + h[0].length;
    const blockEnd = rangeIndex + 1 < ranges.length ? ranges[rangeIndex + 1].index : usable.length;
    const block = usable.slice(blockStart, blockEnd);
    const tokenMatches = [...block.matchAll(/([①②③④⑤])\s*/gu)];
    const labels = ['①', '②', '③', '④', '⑤'];
    const cycles = [];
    let cursor = 0;
    while (cursor + 4 < tokenMatches.length) {
      if (tokenMatches.slice(cursor, cursor + 5).map((x) => x[1]).join('') === labels.join('')) {
        cycles.push(tokenMatches.slice(cursor, cursor + 5)); cursor += 5;
      } else cursor += 1;
    }
    const rangeCount = Number(h[2]) - Number(h[1]) + 1;
    if (cycles.length !== rangeCount) return { error: `legacy choice cycles ${cycles.length}; expected ${rangeCount}` };
    const explicitHeads = [...block.matchAll(/^\s*(\d+)\.\s*/gm)]
      .filter((m) => Number(m[1]) >= Number(h[1]) && Number(m[1]) <= Number(h[2]));
    const explicitHeadSequenceMatches = explicitHeads.length === rangeCount
      && explicitHeads.every((m, i) => Number(m[1]) === Number(h[1]) + i)
      && explicitHeads.every((m, i) => m.index < cycles[i][0].index)
      && explicitHeads.every((m, i) => i === 0 || m.index > cycles[i - 1][4].index);
    if (explicitHeadSequenceMatches) {
      const questions = new Map();
      for (let ci = 0; ci < rangeCount; ci += 1) {
        const marks = cycles[ci], head = explicitHeads[ci];
        const stem = block.slice(head.index + head[0].length, marks[0].index).trim();
        const nextHeadStart = ci + 1 < rangeCount ? explicitHeads[ci + 1].index : block.length;
        const choices = marks.map((m, mi) => {
          const a = m.index + m[0].length;
          const b = mi < 4 ? marks[mi + 1].index : nextHeadStart;
          return block.slice(a, b).trim();
        });
        if (!stem || choices.some((x) => !x)) return { error: `legacy numbered question ${Number(h[1]) + ci} incomplete` };
        questions.set(Number(h[1]) + ci, { stem, choices });
      }
      const firstHead = explicitHeads[0].index;
      const passageText = block.slice(0, firstHead).trim();
      if (!passageText) return { error: 'legacy passage text missing before numbered questions' };
      return { passageText, questions: new Map(requestedNumbers.map((n) => [n, questions.get(n)])), rawSha256: sha256Bytes(Buffer.from(raw, 'utf8')), raw };
    }
    const passages = new Map();
    const firstMarks = cycles.map((x) => x[0]);
    const firstPrefixEnd = firstMarks[0].index;
    const firstPrefix = block.slice(0, firstPrefixEnd);
    const firstBlank = firstPrefix.lastIndexOf('\n\n');
    if (firstBlank < 0) return { error: 'legacy first question stem boundary missing' };
    const passageText = firstPrefix.slice(0, firstBlank).trim();
    const firstStem = firstPrefix.slice(firstBlank + 2).trim();
    if (!passageText || !firstStem) return { error: 'legacy passage/stem empty' };
    for (let ci = 0; ci < cycles.length; ci += 1) {
      const marks = cycles[ci];
      let stem = firstStem;
      if (ci > 0) {
        const prev = cycles[ci - 1][4];
        const between = block.slice(prev.index + prev[0].length, marks[0].index);
        const split = between.lastIndexOf('\n\n');
        if (split < 0) return { error: `legacy question ${Number(h[1]) + ci} stem boundary missing` };
        stem = between.slice(split + 2).trim();
      }
      let choice5End = block.length;
      if (ci + 1 < cycles.length) {
        const fifth = marks[4];
        const between = block.slice(fifth.index + fifth[0].length, cycles[ci + 1][0].index);
        const split = between.lastIndexOf('\n\n');
        if (split < 0) return { error: `legacy question ${Number(h[1]) + ci} choice boundary missing` };
        choice5End = fifth.index + fifth[0].length + split;
      }
      const choices = marks.map((m, mi) => {
        const a = m.index + m[0].length;
        const b = mi < 4 ? marks[mi + 1].index : choice5End;
        return block.slice(a, b).trim();
      });
      const qn = Number(h[1]) + ci;
      if (!stem || choices.length !== 5 || choices.some((x) => !x)) return { error: `legacy question ${qn} incomplete` };
      passages.set(qn, { stem, choices });
    }
    return {
      passageText,
      questions: new Map(requestedNumbers.map((n) => [n, passages.get(n)])),
      rawSha256: sha256Bytes(Buffer.from(raw, 'utf8')),
      raw,
      legacyPassageId: passageId,
    };
  }
  const rangeHead = usable.match(/^##\s+\[\d+\s*[~〜-]\s*\d+\][^\n]*\n?/m);
  const passageStart = rangeHead ? rangeHead.index + rangeHead[0].length : 0;
  const passageText = usable.slice(passageStart, heads[0].index).trim();
  const questions = new Map();
  for (let i = 0; i < heads.length; i += 1) {
    const n = Number(heads[i][1]), start = heads[i].index;
    const end = i + 1 < heads.length ? heads[i + 1].index : usable.length;
    const section = usable.slice(start, end).trim();
    const body = section.replace(/^##\s+\d+\.\s*[^\n]*\n?/, '').trim();
    const marks = [...body.matchAll(/(?:^|\n)\s*([①②③④⑤])\s+/g)];
    if (marks.length !== 5) { questions.set(n, { error: `choice markers ${marks.length}` }); continue; }
    const stemTail = body.slice(0, marks[0].index).trim();
    const stem = [heads[i][2].trim(), stemTail].filter(Boolean).join('\n\n');
    const choices = marks.map((m, j) => {
      const a = m.index + m[0].length;
      const b = j + 1 < marks.length ? marks[j + 1].index : body.length;
      return body.slice(a, b).trim();
    });
    questions.set(n, { stem, choices, heading: heads[i][2].trim() });
  }
  for (const n of requestedNumbers) if (!questions.has(n)) return { error: `question ${n} absent from canonical markdown` };
  return { passageText, questions, rawSha256: sha256Bytes(Buffer.from(raw, 'utf8')), raw };
}

const extractRectangularMarkdownTables = (text) => {
  const lines = text.split(/\r?\n/), tables = [];
  let i = 0;
  while (i < lines.length) {
    if (!/^\s*\|.*\|\s*$/.test(lines[i])) { i += 1; continue; }
    const start = i;
    while (i < lines.length && /^\s*\|.*\|\s*$/.test(lines[i])) i += 1;
    const block = lines.slice(start, i);
    const rows = block.map((line) => line.trim().replace(/^\|/, '').replace(/\|$/, '').split('|').map((x) => x.trim()));
    const width = rows[0]?.length ?? 0;
    if (width >= 2 && rows.length >= 2 && rows.every((r) => r.length === width)) {
      tables.push({ startLine: start + 1, endLine: i, text: block.join('\n') });
    }
  }
  return tables;
};

function normalizeTextAsset(file) {
  let text = fs.readFileSync(file, 'utf8').replace(/\r\n/g, '\n');
  const tables = extractRectangularMarkdownTables(text);
  if (tables.length) return tables.map((t) => t.text).join('\n\n') + '\n';
  // Some official structured view boxes are prose-like. Retain the exact
  // source body after removing the catalog title; identifiers stay sealed.
  text = text.replace(/^#\s*table\s+\d+\s*\n+/i, '').trim();
  if (!text || /(?:CAND-[a-f0-9]+|(?:LEET|MEET|KICE)-\d{4}-)/i.test(text)) return null;
  return `${text}\n`;
}

function parseLeetGroup(rows) {
  const first = rows[0], conn = first.canonical_connection, sourcePath = conn.source_path;
  if (!sourcePath || !fs.existsSync(path.join(root, sourcePath))) return { error: 'canonical LEET source missing', status: 'SOURCE_MISSING' };
  if (!['exact_canonical_leet_odd', 'exact_verified_leet_transcript'].includes(conn.status)) return { error: `LEET source status ${conn.status}`, status: 'SOURCE_MISSING' };
  const parsed = parseLeetMarkdown(sourcePath, rows.map((x) => x.source.question_number), conn.passage_id);
  if (parsed.error) return { error: parsed.error, status: 'NEEDS_RESTORE' };
  const caseRows = [];
  for (let i = 0; i < rows.length; i += 1) {
    const row = rows[i], qn = row.source.question_number, q = parsed.questions.get(qn);
    if (!q || !q.stem.trim() || q.choices.some((x) => !x.trim())) return { error: `LEET question ${qn} stem/choice incomplete`, status: 'NEEDS_RESTORE' };
    caseRows.push({ row, sourcePath, passageText: parsed.passageText, stem: q.stem, choices: q.choices, sourceHash: parsed.rawSha256 });
  }
  return { family: 'LEET', passageId: conn.passage_id, sourcePath, sourceHash: parsed.rawSha256, caseRows };
}

function parseMeetGroup(rows) {
  const first = rows[0], passageId = first.canonical_connection.passage_id;
  const firstQuestion = meetQuestions.get(first.canonical_connection.question_id);
  if (!firstQuestion) return { error: 'canonical MEET question record missing', status: 'SOURCE_MISSING' };
  const sourcePath = firstQuestion.source?.canonical_markdown;
  if (!sourcePath || !fs.existsSync(path.join(root, sourcePath))) return { error: 'canonical MEET transcript missing', status: 'SOURCE_MISSING' };
  if (firstQuestion.source?.verification_status !== 'official_page_visual_transcription_verified') return { error: 'MEET canonical transcript not official-page verified', status: 'NEEDS_RESTORE' };
  const raw = fs.readFileSync(path.join(root, sourcePath), 'utf8');
  const heading = raw.match(/^##\s+\[\d+\s*[~〜-]\s*\d+\][^\n]*\n?/m);
  const qHeads = [...raw.matchAll(/^##\s+(\d+)\.\s*([^\n]*)$/gm)];
  if (!heading || !qHeads.length) return { error: 'MEET group passage/question headings missing', status: 'NEEDS_RESTORE' };
  const answerAt = raw.search(/^##\s*(?:정답|해설|대조 메모)\b/m);
  const usable = answerAt >= 0 ? raw.slice(0, answerAt) : raw;
  const heads = [...usable.matchAll(/^##\s+(\d+)\.\s*([^\n]*)$/gm)];
  const passageText = usable.slice(heading.index + heading[0].length, heads[0].index).trim();
  const qmd = new Map();
  for (let i = 0; i < heads.length; i += 1) {
    const n = Number(heads[i][1]), end = i + 1 < heads.length ? heads[i + 1].index : usable.length;
    const section = usable.slice(heads[i].index, end);
    const questionBody = section.replace(/^##\s+\d+\.\s*[^\n]*\n?/, '').trim();
    const marks = [...questionBody.matchAll(/(?:^|\n)\s*([①②③④⑤])\s+/g)];
    qmd.set(n, marks.length === 5 ? { stem: [heads[i][2].trim(), questionBody.slice(0, marks[0].index).trim()].filter(Boolean).join('\n\n') } : { error: `markdown choice markers ${marks.length}` });
  }
  const caseRows = [];
  for (let i = 0; i < rows.length; i += 1) {
    const row = rows[i], qid = row.canonical_connection.question_id;
    const q = meetQuestions.get(qid), num = Number(row.source.question_number);
    if (!q || q.group_id !== passageId || q.source?.canonical_markdown !== sourcePath) return { error: `MEET passage-question linkage failed for ${qid}`, status: 'NEEDS_RESTORE' };
    if (q.source?.canonical_markdown_sha256 && q.source.canonical_markdown_sha256 !== sha256File(path.join(root, sourcePath))) return { error: `MEET markdown hash mismatch for ${qid}`, status: 'NEEDS_RESTORE' };
    if (!Array.isArray(q.choices) || q.choices.length !== 5) return { error: `MEET choice count not five for ${qid}`, status: 'NEEDS_RESTORE' };
    const choices = q.choices.map((c, idx) => {
      const text = typeof c === 'string' ? c : c?.text;
      const label = typeof c === 'object' ? c.label : ['①', '②', '③', '④', '⑤'][idx];
      return `${label ?? ['①', '②', '③', '④', '⑤'][idx]} ${String(text ?? '').trim()}`.trim();
    });
    let stem = String(q.stem ?? qmd.get(num)?.stem ?? '').trim();
    const prompt = String(q.prompt_markdown ?? '').trim();
    if (prompt && !stem.includes(prompt)) stem = `${stem}\n\n${prompt}`.trim();
    if (!stem || choices.some((x) => !x)) return { error: `MEET stem/choice missing for ${qid}`, status: 'NEEDS_RESTORE' };
    caseRows.push({ row, sourcePath, passageText, stem, choices, sourceHash: q.source.canonical_markdown_sha256 ?? sha256File(path.join(root, sourcePath)), officialPages: q.source.official_pages ?? [] });
  }
  return { family: 'MEET', passageId, sourcePath, sourceHash: sha256File(path.join(root, sourcePath)), caseRows };
}

function parseKiceGroup(rows) {
  const first = rows[0], passageId = first.canonical_connection.passage_id;
  const q0 = kiceQuestions.get(first.canonical_connection.question_id);
  if (!q0) return { error: 'canonical KICE question record missing', status: 'SOURCE_MISSING' };
  if (!['exact_canonical_kice_question'].includes(first.canonical_connection.status)) return { error: `KICE source status ${first.canonical_connection.status}`, status: 'NEEDS_RESTORE' };
  const passageText = q0.passage_text ?? q0.passage ?? q0.passage_markdown;
  if (typeof passageText !== 'string' || !passageText.trim()) return { error: 'KICE passage text missing', status: 'NEEDS_RESTORE' };
  const caseRows = [];
  for (const row of rows) {
    const q = kiceQuestions.get(row.canonical_connection.question_id);
    if (!q || q.passage_id !== passageId || !Array.isArray(q.choices) || q.choices.length !== 5) return { error: `KICE linkage/choice incomplete for ${row.canonical_connection.question_id}`, status: 'NEEDS_RESTORE' };
    const stem = String(q.stem ?? q.prompt ?? '').trim();
    const choices = q.choices.map((c, i) => `${c.label ?? ['①', '②', '③', '④', '⑤'][i]} ${String(c.text ?? c).trim()}`.trim());
    if (!stem || choices.some((x) => !x)) return { error: `KICE stem/choice missing for ${row.canonical_connection.question_id}`, status: 'NEEDS_RESTORE' };
    caseRows.push({ row, sourcePath: 'data/kice_questions.jsonl', passageText, stem, choices, sourceHash: sha256File(path.join(root, 'data/kice_questions.jsonl')) });
  }
  return { family: 'KICE', passageId, sourcePath: 'data/kice_questions.jsonl', sourceHash: sha256File(path.join(root, 'data/kice_questions.jsonl')), caseRows };
}

const families = ['LEET', 'MEET', 'DEET', 'KICE'];
const groupEntries = [...grouped.entries()].map(([id, rows]) => ({ id, rows, family: rows[0].source.exam_family }));
const groupById = new Map(groupEntries.map((x) => [x.id, x]));
const usedGroupsFromMapping = new Set();
for (const m of mapping) if (m.provenance?.passage_id) usedGroupsFromMapping.add(m.provenance.passage_id);
const groupsByFamily = new Map();
for (const family of families) groupsByFamily.set(family, groupEntries.filter((g) => g.family === family).sort((a, b) => groupSort([a.id, a.rows], [b.id, b.rows])));

const completedCandidateIds = new Set(usedCandidateIds);
const completedQuestionIds = new Set(usedQuestionIds);
const planGroups = [];
const restoredVisualGroups = new Set();
const visualErrors = [];
const selectionCounts = { LEET: 0, MEET: 0, DEET: 0, KICE: 0 };
const questionsAlreadyUsed = (g) => g.rows.some((x) => isUsedSource(x));
const sourceForGroup = (g) => {
  if (g.family === 'LEET') return parseLeetGroup(g.rows);
  if (g.family === 'MEET' || g.family === 'DEET') return parseMeetGroup(g.rows);
  if (g.family === 'KICE') return parseKiceGroup(g.rows);
  return { error: 'unsupported source family', status: 'SOURCE_MISSING' };
};

const targetGroups = 30;
const targetQuestions = 90;
const candidatePlan = [];
let groupNumberCursor = firstNewGroupNumber;
const stagingVisualWrites = new Map();
const plannedMappings = [], plannedAnswers = [], plannedManifest = [];
const usedVisualCache = new Map();

const linkedLeetAssetsForRow = (row, contextText, forceVisual) => {
  const existing = row.canonical_connection.visual_material?.linked_assets ?? [];
  const source = row.source ?? {};
  const label = `${source.year}${/예비/u.test(String(source.exam_type ?? '')) ? '예비' : ''}`;
  const paper = (leetVisualIndex.papers ?? []).find((x) => x.year === source.year && x.label === label);
  if (existing.length) {
    const enriched = existing.map((asset) => {
      if (!paper) return asset;
      const mapped = (paper.assets ?? []).find((x) => x.file === asset.authoritative_file
        && x.kind === asset.asset_kind && x.mapping_confidence === asset.mapping_confidence
        && Array.isArray(x.question_group) && Number(source.question_number) >= Number(x.question_group[0])
        && Number(source.question_number) <= Number(x.question_group[1]));
      if (!mapped) return asset.mapping_source ? { ...asset, mapping_linkage_unverified: true } : asset;
      return {
        ...asset,
        mapping_source: leetVisualMapPath.replace(root + path.sep, '').replaceAll('\\', '/'),
        mapping_source_sha256: leetVisualMapHash,
        official_hwp_source: paper.source_file,
        official_hwp_source_sha256: paper.source_sha256,
        question_group: mapped.question_group,
        mapping_basis: mapped.mapping_basis,
        asset_sha256: mapped.sha256,
      };
    });
    return enriched;
  }
  if (!forceVisual && !/(?:<보기>|<그림>|<표>|\[(?:그림|표)\])/u.test(contextText)) return [];
  const passageRange = String(row.canonical_connection?.passage_id ?? '').match(/-Q0*(\d+)-0*(\d+)$/u);
  if (!paper || !passageRange || !leetVisualMapHash) return [];
  const start = Number(passageRange[1]), end = Number(passageRange[2]);
  return (paper.assets ?? []).filter((asset) => {
    const range = asset.question_group;
    if (asset.mapping_confidence !== 'high' || !Array.isArray(range) || range.length !== 2) return false;
    return Number(range[0]) >= start && Number(range[1]) <= end;
  }).map((asset) => ({
    authoritative_file: asset.file,
    mapping_confidence: asset.mapping_confidence,
    asset_kind: asset.kind,
    mapping_source: leetVisualMapPath.replace(root + path.sep, '').replaceAll('\\', '/'),
    mapping_source_sha256: leetVisualMapHash,
    official_hwp_source: paper.source_file,
    official_hwp_source_sha256: paper.source_sha256,
    question_group: asset.question_group,
    mapping_basis: asset.mapping_basis ?? 'high_confidence_source_question_group',
    asset_sha256: asset.sha256,
  }));
};

const linkedMeetAssetsForRow = (row) => {
  const existing = row.canonical_connection.visual_material?.linked_assets ?? [];
  if (existing.length) return existing;
  const questionRecord = meetQuestions.get(row.canonical_connection.question_id);
  const markdown = questionRecord?.source?.canonical_markdown;
  if (!questionRecord || !markdown || questionRecord.group_id !== row.canonical_connection.passage_id) return [];
  return (meetVisualIndex.records ?? [])
    .filter((record) => record.group_id === questionRecord.group_id
      && record.linked_question_ids?.includes(questionRecord.question_id)
      && record.canonical_markdown === markdown
      && ['canonical_markdown_structure_linked', 'visually_classified_and_linked_to_canonical_group'].includes(record.verification_status))
    .map((record) => ({ visual_id: record.visual_id, source_file: record.original_file ?? record.canonical_markdown }));
};

const copyVisualsForCase = (groupNum, caseId, row, family, contextText = '', forceVisual = false) => {
  const visual = row.canonical_connection.visual_material ?? {};
  const refs = [];
  const prov = [];
  const linked = family === 'LEET'
    ? linkedLeetAssetsForRow(row, contextText, forceVisual)
    : family === 'MEET' || family === 'DEET'
      ? linkedMeetAssetsForRow(row)
      : (visual.linked_assets ?? []);
  for (const asset of linked) {
    let sourceFile, sourceBytes, ext, meta = {};
    if (family === 'MEET' || family === 'DEET') {
      const record = meetVisuals.get(asset.visual_id);
      const questionRecord = meetQuestions.get(row.canonical_connection.question_id);
      if (!record || record.group_id !== row.canonical_connection.passage_id
          || !record.linked_question_ids?.includes(row.canonical_connection.question_id)
          || record.canonical_markdown !== questionRecord?.source?.canonical_markdown
          || ![record.original_file, record.canonical_markdown].includes(asset.source_file)
          || !['canonical_markdown_structure_linked', 'visually_classified_and_linked_to_canonical_group'].includes(record.verification_status)) {
        return { error: `MEET visual catalog linkage failed for ${row.canonical_connection.question_id}` };
      }
      if (record.original_file) {
        sourceFile = record.original_file;
        const abs = path.join(root, sourceFile);
        if (!fs.existsSync(abs) || sha256File(abs) !== record.sha256) return { error: `MEET visual image hash mismatch ${record.visual_id}` };
        sourceBytes = fs.readFileSync(abs); ext = path.extname(abs).slice(1).toLowerCase();
        meta = { visual_id: record.visual_id, source_file: sourceFile, source_sha256: record.sha256, source_file_sha256: record.sha256, canonical_markdown: record.canonical_markdown, official_display_pages: record.display_pages ?? [], verification_status: record.verification_status };
      } else {
        sourceFile = record.canonical_markdown;
        const abs = path.join(root, sourceFile);
        if (!fs.existsSync(abs) || sha256File(abs) !== record.markdown_sha256) return { error: `MEET visual markdown hash mismatch ${record.visual_id}` };
        const lines = fs.readFileSync(abs, 'utf8').replace(/\r\n/g, '\n').split('\n');
        const block = lines.slice(record.markdown_line - 1, record.markdown_line_end).join('\n');
        const blockHashes = [block, `${block}\n`, block.trim()].map((v) => sha256Bytes(Buffer.from(v, 'utf8')));
        if (!block || !blockHashes.includes(record.content_sha256)) return { error: `MEET visual markdown block hash mismatch ${record.visual_id}` };
        sourceBytes = Buffer.from(`${block}\n`, 'utf8'); ext = 'md';
        meta = { visual_id: record.visual_id, source_file: sourceFile, source_sha256: record.content_sha256, source_file_sha256: record.markdown_sha256, canonical_markdown_sha256: record.markdown_sha256, line_start: record.markdown_line, line_end: record.markdown_line_end, verification_status: record.verification_status };
      }
    } else if (family === 'LEET') {
      sourceFile = asset.authoritative_file;
      if (!sourceFile || asset.mapping_confidence !== 'high') return { error: `LEET visual mapping not high-confidence for ${row.canonical_connection.question_id}` };
      const abs = path.join(root, sourceFile);
      if (!fs.existsSync(abs)) return { error: `LEET linked visual missing: ${sourceFile}` };
      let mappingSourcePath = null;
      if (asset.asset_sha256 && sha256File(abs) !== asset.asset_sha256) return { error: `LEET mapped visual hash mismatch: ${sourceFile}` };
      if (asset.official_hwp_source) {
        const hwp = path.join(root, asset.official_hwp_source);
        if (!fs.existsSync(hwp) || !asset.official_hwp_source_sha256 || sha256File(hwp) !== asset.official_hwp_source_sha256) {
          return { error: `LEET HWP visual provenance mismatch: ${asset.official_hwp_source}` };
        }
      }
      if (asset.mapping_linkage_unverified) return { error: `LEET visual linkage has no matching high-confidence HWP map: ${sourceFile}` };
      if (asset.mapping_source) {
        const mappingRel = asset.mapping_source.includes('/')
          ? asset.mapping_source : `자료/LEET_언어이해/검증/${asset.mapping_source}`;
        const mapFile = path.join(root, mappingRel);
        if (!fs.existsSync(mapFile) || !asset.mapping_source_sha256 || sha256File(mapFile) !== asset.mapping_source_sha256) {
          return { error: `LEET visual mapping hash mismatch: ${mappingRel}` };
        }
        mappingSourcePath = mappingRel;
      }
      ext = path.extname(abs).slice(1).toLowerCase();
      if (['png', 'jpg', 'jpeg', 'bmp', 'tif', 'tiff'].includes(ext)) sourceBytes = fs.readFileSync(abs);
      else if (ext === 'md') {
        const normalized = normalizeTextAsset(abs);
        if (!normalized) return { error: `LEET visual table could not be safely normalized: ${sourceFile}` };
        sourceBytes = Buffer.from(normalized, 'utf8'); ext = 'md';
      } else return { error: `LEET visual type unsupported: ${sourceFile}` };
      meta = {
        asset_kind: asset.asset_kind, source_file: sourceFile, source_sha256: sha256Bytes(sourceBytes),
        source_file_sha256: sha256File(abs), mapping_confidence: asset.mapping_confidence,
        ...(mappingSourcePath ? { mapping_source: mappingSourcePath, mapping_source_sha256: asset.mapping_source_sha256,
          official_hwp_source: asset.official_hwp_source, official_hwp_source_sha256: asset.official_hwp_source_sha256,
          question_group: asset.question_group, mapping_basis: asset.mapping_basis } : {}),
      };
    } else return { error: `No verified visual source adapter for ${family}` };

    const sourceHash = sha256Bytes(sourceBytes);
    const cacheKey = `${groupNum}|${sourceHash}`;
    let rel;
    if (usedVisualCache.has(cacheKey)) rel = usedVisualCache.get(cacheKey);
    else {
      const prefix = `data/기본기_연구/prepared_backlog/blind_sources/G${String(groupNum).padStart(3, '0')}_visual`;
      const idx = [...stagingVisualWrites.keys()].filter((x) => x.startsWith(prefix)).length + 1;
      rel = `${prefix}${String(idx).padStart(2, '0')}.${ext}`;
      stagingVisualWrites.set(rel, sourceBytes);
      usedVisualCache.set(cacheKey, rel);
    }
    refs.push({ file: rel.replaceAll('\\', '/'), media_type: ext === 'md' ? 'text/markdown' : `image/${ext === 'jpg' ? 'jpeg' : ext}` });
    prov.push({ ...meta, blind_asset: rel.replaceAll('\\', '/'), blind_asset_sha256: sourceHash });
  }
  return { refs, provenance: prov };
};

const normalizeSourceImageLinks = (text, refs) => {
  const imagePattern = /!\[([^\]]*)\]\(([^)]+)\)|<img\b[^>]*\bsrc=["']([^"']+)["'][^>]*>/gi;
  const imageMatches = [...text.matchAll(imagePattern)];
  if (imageMatches.length > refs.length) return null;
  let next = 0;
  let out = text.replace(imagePattern, () => `[시각 자료 ${++next}]`);
  const markerPattern = /<(?:그림|표)>|\[(?:그림|표)\]/gu;
  const markers = [...out.matchAll(markerPattern)];
  if (markers.length && refs.length === 0) return null;
  out = out.replace(markerPattern, () => `[시각 자료 ${Math.min(++next, refs.length)}]`);
  return out;
};

function prepareOneGroup(g, groupNum, caseStart) {
  const parsed = sourceForGroup(g);
  if (parsed.error) { reportUnresolved(g, parsed.status ?? 'NEEDS_RESTORE', parsed.error); return null; }
  const cases = [];
  for (let i = 0; i < parsed.caseRows.length; i += 1) {
    const item = parsed.caseRows[i], id = alpha(caseStart + i), row = item.row;
    const visualStatus = row.canonical_connection.visual_material?.status ?? 'unknown';
    const contextText = `${item.passageText}\n${item.stem}\n${item.choices.join('\n')}`;
    const visualMarkerRequired = /<(?:그림|표|보기)>|\[(?:그림|표|보기)\]/u.test(contextText);
    const visualStatusRequired = visualStatus === 'unknown' || visualStatus === 'review_required';
    const v = copyVisualsForCase(groupNum, id, row, g.family, contextText, visualStatusRequired);
    if (v.error) { reportUnresolved(g, 'NEEDS_RESTORE', v.error); return null; }
    if ((visualMarkerRequired || visualStatusRequired) && !v.refs.length) {
      reportUnresolved(g, 'NEEDS_RESTORE', `visual material has no exact linked local asset for ${row.canonical_connection.question_id}`); return null;
    }
    const passage = normalizeSourceImageLinks(item.passageText, v.refs);
    const stem = normalizeSourceImageLinks(item.stem, v.refs);
    const choices = item.choices.map((x) => normalizeSourceImageLinks(x, v.refs));
    if (passage === null || stem === null || choices.some((x) => x === null)) {
      reportUnresolved(g, 'NEEDS_RESTORE', `unmapped source image link in ${row.canonical_connection.question_id}`); return null;
    }
    if (!stem.trim() || !passage.trim() || choices.length !== 5 || choices.some((x) => !x.trim())) {
      reportUnresolved(g, 'NEEDS_RESTORE', `stem, passage, or five-choice completeness failed for ${row.canonical_connection.question_id}`); return null;
    }
    const blind = {
      blind_only: true,
      passage_group: `G${String(groupNum).padStart(3, '0')}`,
      case_id: id,
      provenance: { source_role: 'anonymous_blind_source' },
      passage_text: passage,
      stem,
      choices,
    };
    if (v.refs.length) blind.visual_supplements = [...new Map(v.refs.map((r) => [r.file, r])).values()];
    cases.push({ id, row, blind, source: item, visualProvenance: v.provenance });
  }
  return { ...parsed, cases, groupNumber: groupNum };
}

const stagedBlind = new Map();
const stagedPackets = new Map();
const readyGroups = [];
let caseCursor = nextCaseValue;
let groupCursor = firstNewGroupNumber;
const restoredSpecialMeetIds = new Set([
  'MEET-2005-Q09-11', 'MEET-2005-Q19-20', 'MEET-2005-Q21-23',
  'MEET-2005-Q30-32', 'MEET-2005-Q39-41', 'MEET-2005-Q42-43', 'MEET-2005예비-Q12-14',
]);
const groupUsed = (g) => g.rows.some((x) => isUsedSource(x))
  || usedPassageIds.has(g.id)
  || (g.family === 'MEET' && manifest.some((m) => m.passage_group === 'G024' && m.status === 'prepared') && g.id === 'G024');
const totalQuestions = () => readyGroups.reduce((n, x) => n + x.cases.length, 0);

const addCandidateGroup = (g) => {
  if (groupUsed(g)) return false;
  if (g.rows.some((x) => candidateIdCounts.get(x.candidate_id) !== 1 || questionIdCounts.get(x.canonical_connection.question_id) !== 1)) {
    reportUnresolved(g, 'NEEDS_RESTORE', 'candidate_id or question_id is not unique in the candidate index'); return false;
  }
  if (g.rows.some((x) => !x.canonical_connection?.question_id || !x.source?.question_number)) {
    reportUnresolved(g, 'SOURCE_MISSING', 'candidate/question linkage metadata missing'); return false;
  }
  if (g.id === 'LEET-2008-prelim-Q04-08' || g.rows.some((x) => x.canonical_connection?.status === 'leet_preliminary_year_not_in_canonical_scope')) {
    reportUnresolved(g, 'SOURCE_MISSING', 'LEET 2008 preliminary Q4-8 has no local canonical source'); return false;
  }
  const visualFilesBefore = new Set(stagingVisualWrites.keys());
  const visualCacheBefore = new Map(usedVisualCache);
  const tentativeIds = g.rows.map((_, i) => alpha(caseCursor + i));
  const proposed = prepareOneGroup(g, groupCursor, caseCursor);
  if (!proposed) {
    for (const file of stagingVisualWrites.keys()) if (!visualFilesBefore.has(file)) stagingVisualWrites.delete(file);
    usedVisualCache.clear();
    for (const [key, value] of visualCacheBefore) usedVisualCache.set(key, value);
    return false;
  }
  readyGroups.push(proposed);
  groupCursor += 1;
  caseCursor += proposed.cases.length;
  selectionCounts[g.family] += 1;
  if (restoredSpecialMeetIds.has(g.id)) restoredVisualGroups.add(g.id);
  return true;
};

// Reconcile every candidate against the immutable consumed-source index before
// selecting any READY batch. A source family has no priority by itself: groups
// rank by the weakest question-level source verification in that passage.
const candidateStatus = new Map();
for (const row of candidates) {
  if (crosswalkHoldCandidateIds.has(row.candidate_id)) candidateStatus.set(row.candidate_id, 'HOLD');
  else if (crosswalkAmbiguousCandidateIds.has(row.candidate_id)) candidateStatus.set(row.candidate_id, 'AMBIGUOUS_COMPLETION');
  else if (crosswalkCompletedCandidateIds.has(row.candidate_id)
      || (!targetCrosswalkValid && isUsedSource(row))) candidateStatus.set(row.candidate_id, 'COMPLETED');
}
const sourceEligibleGroups = [];
const markGroupStatus = (rows, status) => {
  for (const row of rows) if (!candidateStatus.has(row.candidate_id)) candidateStatus.set(row.candidate_id, status);
};
for (const g of groupEntries) {
  const pendingRows = g.rows.filter((row) => !candidateStatus.has(row.candidate_id));
  if (!pendingRows.length) continue;
  if (groupUsed(g)) {
    markGroupStatus(pendingRows, 'NEEDS_RESTORE');
    reportUnresolved(g, 'NEEDS_RESTORE', 'passage source overlaps a completed/exposed source group; strict blind reuse is not established');
    continue;
  }
  const declaredMissing = pendingRows.filter((row) => [
    'kice_question_not_in_local_reading_scope', 'leet_source_not_in_local_corpus',
    'leet_preliminary_year_not_in_canonical_scope',
  ].includes(row.canonical_connection?.status));
  if (declaredMissing.length) {
    for (const row of declaredMissing) candidateStatus.set(row.candidate_id, 'SOURCE_MISSING');
    const otherRows = pendingRows.filter((row) => !declaredMissing.includes(row));
    if (otherRows.length) {
      markGroupStatus(otherRows, 'NEEDS_RESTORE');
      reportUnresolved(g, 'NEEDS_RESTORE', 'passage group has mixed local and missing canonical source coordinates');
    } else reportUnresolved(g, 'SOURCE_MISSING', 'canonical reading source is absent from the local repository');
    continue;
  }
  const beforeFiles = new Set(stagingVisualWrites.keys());
  const beforeCache = new Map(usedVisualCache);
  const preview = prepareOneGroup(g, firstNewGroupNumber, nextCaseValue);
  for (const file of stagingVisualWrites.keys()) if (!beforeFiles.has(file)) stagingVisualWrites.delete(file);
  usedVisualCache.clear();
  for (const [key, value] of beforeCache) usedVisualCache.set(key, value);
  if (!preview) {
    const unresolved = [...unresolvedById.values()].filter((x) => x.passage_group === g.id).at(-1);
    const status = unresolved?.status === 'SOURCE_MISSING' ? 'SOURCE_MISSING' : 'NEEDS_RESTORE';
    markGroupStatus(pendingRows, status);
    continue;
  }
  const weakestSourceVerification = Math.min(...pendingRows.map((row) => {
    const status = row.canonical_connection?.status;
    if (status === 'exact_verified_leet_transcript' || status === 'exact_canonical_meet_jsonl'
        || status === 'exact_canonical_kice_question') return 4;
    if (status === 'exact_canonical_leet_odd') return 3;
    return 1;
  }));
  for (const row of pendingRows) candidateStatus.set(row.candidate_id, 'READY_LOCAL_SOURCE');
  sourceEligibleGroups.push({ group: g, score: weakestSourceVerification });
}
for (const row of candidates) {
  if (candidateStatus.has(row.candidate_id)) continue;
  const status = row.canonical_connection?.status;
  candidateStatus.set(row.candidate_id,
    ['kice_question_not_in_local_reading_scope', 'leet_source_not_in_local_corpus', 'leet_preliminary_year_not_in_canonical_scope'].includes(status)
      ? 'SOURCE_MISSING' : 'NEEDS_RESTORE');
}
sourceEligibleGroups.sort((a, b) => (b.score - a.score)
  || groupSort([a.group.id, a.group.rows], [b.group.id, b.group.rows]));
for (const entry of sourceEligibleGroups) {
  if (readyGroups.length >= targetGroups || totalQuestions() >= targetQuestions) break;
  if (totalQuestions() + entry.group.rows.length > 100 && readyGroups.length >= 25) continue;
  const accepted = addCandidateGroup(entry.group);
  if (!accepted) {
    const issue = [...unresolvedById.values()].filter((x) => x.passage_group === entry.group.id).at(-1);
    const status = issue?.status === 'SOURCE_MISSING' ? 'SOURCE_MISSING' : 'NEEDS_RESTORE';
    for (const row of entry.group.rows) {
      if (candidateStatus.get(row.candidate_id) === 'READY_LOCAL_SOURCE') candidateStatus.set(row.candidate_id, status);
    }
  }
}

// Build blind, packet, sealed, and manifest rows in memory.
const stagedManifest = [], stagedMappings = [], stagedAnswers = [];
for (const group of readyGroups) {
  const ids = group.cases.map((x) => x.id);
  const groupId = `G${String(group.groupNumber).padStart(3, '0')}`;
  for (const entry of group.cases) {
    const blindRel = `data/기본기_연구/prepared_backlog/blind_sources/${entry.id}.json`;
    entry.blind.passage_group = groupId;
    stagedBlind.set(blindRel, Buffer.from(`${JSON.stringify(entry.blind, null, 2)}\n`, 'utf8'));
    const c = entry.row.canonical_connection, s = entry.row.source;
    stagedManifest.push({
      case_id: entry.id,
      status: 'prepared',
      passage_group: groupId,
      group_case_ids: ids,
      group_release_rules: releaseRules,
      blind_source: blindRel,
      exclusion_checks: {
        exposure_status: 'unknown',
        semantic_review: 'not_reviewed',
        source_quality: {
          visual_placeholder: false,
          canonical_link: 'exact',
          choice_parse: 'complete',
          text_markers_preserved: true,
          source_verification: group.family === 'LEET' ? 'exact_canonical_leet_transcript' : group.family === 'MEET' ? 'official_page_visual_transcription_verified' : 'exact_canonical_kice_question',
        },
      },
    });
    stagedMappings.push({
      case_id: entry.id,
      passage_group: groupId,
      group_case_ids: ids,
      provenance: {
        candidate_id: entry.row.candidate_id,
        exam_family: s.exam_family,
        academic_year: s.year,
        exam_label: s.exam_type,
        question_number: s.question_number,
        question_id: c.question_id,
        passage_id: c.passage_id,
        source_path: group.sourcePath,
        canonical_source_path: c.source_path ?? group.sourcePath,
        source_sha256: entry.source.sourceHash,
        source_type: group.family === 'LEET' ? 'verified_canonical_leet_markdown' : group.family === 'MEET' ? 'official_page_visual_transcription_verified_markdown' : 'exact_canonical_kice_question',
        official_pages: entry.source.officialPages ?? [],
        linked_visual_assets: entry.visualProvenance,
        source_role: 'sealed_provenance_mapping',
      },
      source_status: group.family === 'MEET' ? 'exact_canonical_meet_jsonl' : group.family === 'LEET' ? 'exact_canonical_leet_odd' : 'exact_canonical_kice_question',
    });
    stagedAnswers.push({
      case_id: entry.id,
      candidate_id: entry.row.candidate_id,
      official_answer: c.official_answer,
      official_answer_source: c.official_answer_source,
      site_original_codes: entry.row.site_candidate?.site_original_codes ?? [],
      site_marked_answer: entry.row.site_candidate?.site_marked_answer ?? null,
      source_role: 'sealed_for_after_blind',
      passage_group: c.passage_id,
      release_rule: releaseRules[0],
    });
  }
  const packet = {
    blind_packet: true,
    passage_group: groupId,
    group_case_ids: ids,
    group_release_rules: releaseRules,
    source_files: ids.map((id) => `data/기본기_연구/prepared_backlog/blind_sources/${id}.json`),
  };
  stagedPackets.set(`data/기본기_연구/prepared_backlog/packets/${ids[0]}.json`, Buffer.from(`${JSON.stringify(packet, null, 2)}\n`, 'utf8'));
  const packetMd = [
    `# ${ids[0]} blind packet`, '', `- passage_group: ${groupId}`, `- group_case_ids: ${ids.join(', ')}`,
    `- blind_sources: ${ids.map((id) => `data/기본기_연구/prepared_backlog/blind_sources/${id}.json`).join('; ')}`,
    `- group_rules: ${releaseRules.join('; ')}`, '',
    'Astra는 group 전체의 anonymous blind-only source를 먼저 읽고 stage barrier를 지킨다.', '',
  ].join('\n');
  for (const id of ids) stagedPackets.set(`data/기본기_연구/prepared_backlog/packets/${id}.md`, Buffer.from(packetMd.replace(`# ${ids[0]} blind packet`, `# ${id} blind packet`), 'utf8'));
}

const newCaseIds = stagedManifest.map((x) => x.case_id);
const newCandidateIds = stagedMappings.map((x) => x.provenance.candidate_id);
const newQuestionIds = stagedMappings.map((x) => x.provenance.question_id);
const duplicate = (xs) => xs.length - new Set(xs).size;
const blindDocs = [...stagedBlind.values()].map((b) => JSON.parse(b.toString('utf8')));
const forbiddenBlindKeys = /answer|sdss|candidate|site_|code|explanation|solution|correct|정답|해설|코드|candidate_id/i;
const inspectKeys = (v, keys = []) => {
  if (Array.isArray(v)) for (const x of v) inspectKeys(x, keys);
  else if (v && typeof v === 'object') for (const [k, x] of Object.entries(v)) {
    keys.push(k);
    if (forbiddenBlindKeys.test(k) && !['blind_only', 'provenance'].includes(k)) continue;
    inspectKeys(x, keys);
  }
  return keys;
};
const blindAnswerLeakage = blindDocs.filter((x) => {
  const keys = inspectKeys(x, []);
  const disallowed = keys.some((k) => forbiddenBlindKeys.test(k) && !['blind_only', 'provenance'].includes(k));
  return disallowed || x.provenance?.source_role !== 'anonymous_blind_source'
    || Object.keys(x.provenance ?? {}).some((k) => k !== 'source_role');
}).length;
const blindSdssLeakage = blindDocs.filter((x) => {
  const keys = inspectKeys(x, []);
  return keys.some((k) => /sdss|site_original_codes|query_catalog_code/i.test(k));
}).length;
const completedOverlap = stagedMappings.filter((x) => usedQuestionIdsForChecks.has(x.provenance.question_id)
  || usedCandidateIdsForChecks.has(x.provenance.candidate_id)
  || usedSourceKeys.has(sourceKey(x.provenance.exam_family, x.provenance.academic_year, x.provenance.exam_label, x.provenance.question_number))).length;
const holdQuestionIds = new Set(mapping.filter((x) => holdCaseIds.has(x.case_id)).map((x) => x.provenance?.question_id).filter(Boolean));
const holdCandidateIds = new Set(mapping.filter((x) => holdCaseIds.has(x.case_id)).map((x) => x.provenance?.candidate_id).filter(Boolean));
const holdOverlap = stagedMappings.filter((x) => x.passage_group === 'G024'
  || holdQuestionIds.has(x.provenance.question_id)
  || holdCandidateIds.has(x.provenance.candidate_id)).length;
const provenanceError = stagedMappings.filter((x) => {
  const p = x.provenance;
  if (!p.question_id || !p.candidate_id || !p.passage_id || !p.source_path || !fs.existsSync(path.join(root, p.source_path))) return true;
  if (!p.source_sha256 || sha256File(path.join(root, p.source_path)) !== p.source_sha256) return true;
  for (const a of p.linked_visual_assets ?? []) {
    const f = path.join(root, a.source_file ?? '');
    const expectedFileHash = a.source_file_sha256 ?? a.source_sha256;
    if (!a.source_file || !fs.existsSync(f) || !expectedFileHash || sha256File(f) !== expectedFileHash) return true;
  }
  for (const page of p.official_pages ?? []) {
    const f = path.join(root, page.file ?? '');
    if (!page.file || !fs.existsSync(f) || !page.sha256 || sha256File(f) !== page.sha256) return true;
  }
  return false;
}).length;
const passageQuestionLinkageError = stagedMappings.filter((x) => {
  const row = candidates.find((c) => c.candidate_id === x.provenance.candidate_id);
  return !row || row.canonical_connection.question_id !== x.provenance.question_id || row.canonical_connection.passage_id !== x.provenance.passage_id;
}).length;
const emptyStem = blindDocs.filter((x) => !x.stem?.trim() || !x.passage_text?.trim()).length;
const invalidChoiceCount = blindDocs.filter((x) => !Array.isArray(x.choices) || x.choices.length !== 5 || x.choices.some((c) => !String(c).trim())).length;
// A view/assumption marker in a prepared blind stem must retain substantive
// content after the marker. Visual-only views are covered by the linked-asset
// check below; this catches an empty textual <보기>/<가정> heading.
const missingRequiredViewOrAssumption = blindDocs.filter((x) => {
  const text = String(x.stem ?? '');
  const markers = [...text.matchAll(/<보기>|〈보기〉|\[보기\]|<가정>|〈가정〉|\[가정\]/gu)];
  return markers.some((m) => {
    const tail = text.slice((m.index ?? 0) + m[0].length)
      .split(/(?:\n\s*\n|\n\s*\[시각 자료\s*\d+\])/u, 1)[0]
      .replace(/[\s|｜—–-]/gu, '');
    return tail.length === 0;
  });
}).length;
const duplicateCandidate = duplicate(newCandidateIds) + newCandidateIds.filter((x) => usedCandidateIdsForChecks.has(x)).length;
const duplicateQuestion = duplicate(newQuestionIds) + newQuestionIds.filter((x) => usedQuestionIdsForChecks.has(x)).length;
const duplicateCase = duplicate(stagedManifest.map((x) => x.case_id)) + stagedManifest.filter((x) => manifest.some((m) => m.case_id === x.case_id)).length;
const missingRequiredVisual = readyGroups.flatMap((g) => g.cases).filter((entry) => {
  const visual = entry.row.canonical_connection.visual_material ?? {};
  const required = visual.status === 'review_required' || /(?:<그림>|<표>|!\[)/u.test(`${entry.blind.passage_text}\n${entry.blind.stem}\n${entry.blind.choices.join('\n')}`);
  if (!required) return false;
  const staged = entry.blind.visual_supplements ?? [];
  const hasSource = (visual.linked_assets ?? []).length > 0;
  const provenanceFiles = (entry.visualProvenance ?? []).map((x) => x.blind_asset).filter(Boolean);
  return !hasSource || !staged.length || provenanceFiles.some((f) => !staged.some((x) => x.file === f));
}).length;
const blindVisualFiles = blindDocs.flatMap((x) => (x.visual_supplements ?? []).map((v) => v.file));
const missingVisualAsset = [...stagingVisualWrites.entries()].filter(([,bytes]) => !bytes?.length).length
  + blindVisualFiles.filter((f) => !stagingVisualWrites.has(f)).length;
const plannedPreparationFiles = [...stagingVisualWrites.keys(), ...stagedBlind.keys(), ...stagedPackets.keys()];
const outputPathConflicts = plannedPreparationFiles.filter((rel) => fs.existsSync(path.join(root, rel))).length
  + (fs.existsSync(reportPath) ? 1 : 0);

const requiredChecks = {
  duplicate_candidate: duplicateCandidate,
  duplicate_question: duplicateQuestion,
  completed_overlap: completedOverlap,
  hold_overlap: holdOverlap,
  blind_answer_leakage: blindAnswerLeakage,
  blind_SDSS_leakage: blindSdssLeakage,
  source_provenance_error: provenanceError,
  passage_question_linkage_error: passageQuestionLinkageError,
  empty_stem: emptyStem,
  invalid_choice_count: invalidChoiceCount,
  missing_required_visual: missingRequiredVisual + missingVisualAsset,
  missing_required_view_or_assumption: missingRequiredViewOrAssumption,
  output_path_conflicts: outputPathConflicts,
  candidate_completed_crosswalk_gap: completionCrosswalkGap,
};
const allCaseIds = [...manifest.map((x) => x.case_id), ...stagedManifest.map((x) => x.case_id)];
const manifestDuplicateCaseIds = duplicate(allCaseIds);
const newCaseIdDuplicates = duplicate(newCaseIds);
const sourceLeakageIds = new Set([...newCandidateIds, ...newQuestionIds]);
const anyReadyStatusBad = stagedManifest.some((x) => x.status !== 'prepared');

const summary = {
  dry_run: dryRun,
  start_group: `G${String(firstNewGroupNumber).padStart(3, '0')}`,
  first_case_id: newCaseIds[0] ?? null,
  ready_groups: readyGroups.length,
  ready_questions: stagedManifest.length,
  ready_group_details: readyGroups.map((g) => ({
    passage_group: `G${String(g.groupNumber).padStart(3, '0')}`,
    source_passage_id: g.passageId,
    family: g.family,
    case_ids: g.cases.map((c) => c.id),
    question_count: g.cases.length,
  })),
  family_counts: Object.fromEntries(families.map((f) => [f, readyGroups.filter((x) => x.family === f).length])),
  family_reconciliation: {
    KICE: readyGroups.filter((x) => x.family === 'KICE').length,
    LEET: readyGroups.filter((x) => x.family === 'LEET').length,
    'MEET/DEET': readyGroups.filter((x) => ['MEET', 'DEET'].includes(x.family)).length,
    Other: readyGroups.filter((x) => !families.includes(x.family)).length,
  },
  visual_groups_restored: [...restoredVisualGroups],
  needs_restore: [...unresolvedById.values()].filter((x) => x.status === 'NEEDS_RESTORE'),
  source_missing: [...unresolvedById.values()].filter((x) => x.status === 'SOURCE_MISSING'),
  hold_count: manifest.filter((x) => x.status === 'prepared').length,
  target_reconciliation: {
    target: candidates.length,
    research_completed_total: Number(projectMetaState?.completed_questions_total ?? 0),
    target_completed: crosswalkCompletedCandidateIds.size,
    target_not_completed: candidates.length - crosswalkCompletedCandidateIds.size,
    candidate_source_crosswalk_completed: crosswalkCompletedCandidateIds.size,
    candidate_source_crosswalk_gap: completionCrosswalkGap,
    candidate_status_counts: Object.fromEntries([...new Set(candidateStatus.values())].sort()
      .map((status) => [status, [...candidateStatus.values()].filter((x) => x === status).length])),
    unassigned_candidate_count: candidates.filter((x) => !candidateStatus.has(x.candidate_id)).length,
    candidate_status_total: candidateStatus.size,
  },
  checks: { ...requiredChecks, manifest_case_id_duplicates: manifestDuplicateCaseIds, new_case_id_duplicates: newCaseIdDuplicates },
};
console.log(JSON.stringify(summary, null, 2));

if (readyGroups.length === 0 || anyReadyStatusBad || Object.values(requiredChecks).some((x) => x !== 0)
    || manifestDuplicateCaseIds !== 0 || newCaseIdDuplicates !== 0) {
  process.exitCode = 1;
} else if (!dryRun) {
  for (const [rel, bytes] of stagingVisualWrites) {
    const abs = path.join(root, rel);
    if (fs.existsSync(abs)) throw new Error(`Refusing to overwrite existing visual supplement ${rel}`);
    fs.writeFileSync(abs, bytes);
  }
  for (const [rel, bytes] of stagedBlind) {
    const abs = path.join(root, rel);
    if (fs.existsSync(abs)) throw new Error(`Refusing to overwrite existing blind source ${rel}`);
    fs.writeFileSync(abs, bytes);
  }
  for (const [rel, bytes] of stagedPackets) {
    const abs = path.join(root, rel);
    if (fs.existsSync(abs)) throw new Error(`Refusing to overwrite existing packet ${rel}`);
    fs.writeFileSync(abs, bytes);
  }
  if (stagedMappings.length) appendJsonl(mappingPath, stagedMappings);
  if (stagedAnswers.length) appendJsonl(answerPath, stagedAnswers);
  if (stagedManifest.length) fs.appendFileSync(manifestPath, stagedManifest.map(JSON.stringify).join('\n') + '\n', 'utf8');
  const report = [
    `# Luna frontier preflight — ${reportDate} ${summary.start_group}`, '',
    '기계적 source preparation만 수행했다. 문항 의미 풀이·정답 판단·코드 판정·SDSS 비교는 수행하지 않았다.', '',
    `- research_completed_total: ${summary.target_reconciliation.research_completed_total}`,
    `- target_completed: ${summary.target_reconciliation.target_completed} / ${summary.target_reconciliation.target}`,
    `- target not completed: ${summary.target_reconciliation.target_not_completed}`,
    `- 새 READY groups / questions: ${readyGroups.length} / ${stagedManifest.length}`,
    `- First READY group / case: ${summary.ready_group_details[0]?.passage_group ?? '없음'} / ${newCaseIds[0] ?? '없음'}`,
    `- Family counts: ${JSON.stringify(summary.family_reconciliation)}`,
    `- Restored MEET visual groups: ${[...restoredVisualGroups].join(', ') || '없음'}`,
    `- NEEDS_RESTORE: ${summary.needs_restore.length}`, `- SOURCE_MISSING: ${summary.source_missing.length}`,
    `- HOLD: ${manifest.filter((x) => x.status === 'prepared').length} (G024 유지)`, '',
    '## READY groups', '',
    ...summary.ready_group_details.map((g) => `- ${g.passage_group}: ${g.family} ${g.source_passage_id} — ${g.case_ids.join(', ')} (${g.question_count}문항)`),
    '', '## NEEDS_RESTORE', '',
    ...(summary.needs_restore.length ? summary.needs_restore.map((x) => `- ${x.family} ${x.passage_group} (${x.question_count}문항): ${x.reason}`) : ['- 없음']),
    '', '## SOURCE_MISSING', '',
    ...(summary.source_missing.length ? summary.source_missing.map((x) => `- ${x.family} ${x.passage_group} (${x.question_count}문항): ${x.reason}`) : ['- 없음']),
    '', '## HOLD', '',
    ...manifest.filter((x) => x.status === 'prepared').map((x) => `- ${x.passage_group}: ${x.group_case_ids?.join(', ') ?? x.case_id} — 기존 상태 유지`),
    '',
    '## Verification', '',
    ...Object.entries(summary.checks).map(([k,v]) => `- ${k}: ${v}`),
    `- blind visual supplements: ${stagingVisualWrites.size}`,
  ].join('\n') + '\n';
  fs.writeFileSync(reportPath, report, 'utf8');
  console.log(JSON.stringify({ wrote: true, report: reportPath, ready_groups: readyGroups.length, ready_questions: stagedManifest.length }, null, 2));
}
