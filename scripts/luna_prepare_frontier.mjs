#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';

const root = process.cwd();
const readLines = (file) => fs.readFileSync(file, 'utf8').split(/\r?\n/).filter(Boolean).map(JSON.parse);
const writeJson = (file, value) => fs.writeFileSync(file, JSON.stringify(value, null, 2) + '\n', 'utf8');
const appendJsonl = (file, rows) => fs.appendFileSync(file, rows.map((x) => JSON.stringify(x, null, 0)).join('\n') + (rows.length ? '\n' : ''), 'utf8');

const base = path.join(root, 'data/기본기_연구/prepared_backlog');
const blindDir = path.join(base, 'blind_sources');
const packetDir = path.join(base, 'packets');
const sealedDir = path.join(base, 'sealed');
const manifestPath = path.join(base, 'manifest.jsonl');
const mappingPath = path.join(sealedDir, 'provenance_mapping.jsonl');
const answerPath = path.join(sealedDir, 'answer_sdss.jsonl');
const literatureMappingPath = path.join(root, 'data/corpus_ingest/kice_literature_local_audit_target_mapping.json');
const centralIndexPath = path.join(root, 'data/기출_MD_정본/index.json');
const normalizedAnswerPath = path.join(root, '자료/평가원_정답표/normalized_answer_keys.json');

const passages = readLines(path.join(root, 'data/kice_passages.jsonl'));
const questions = readLines(path.join(root, 'data/kice_questions.jsonl'));
const candidates = readLines(path.join(root, 'data/기본기_연구/code_study_candidates_v2.jsonl'));
const manifest = readLines(manifestPath);
const mapping = readLines(mappingPath);
const sealedAnswers = readLines(answerPath);
const usedPassages = new Set(mapping.map((x) => x.provenance?.passage_id).filter(Boolean));
const existingCases = new Set(manifest.map((x) => x.case_id));
const existingPreparedCandidateIds = new Set([
  ...sealedAnswers.map((x) => x.candidate_id).filter(Boolean),
  ...mapping.map((x) => x.provenance?.candidate_id).filter(Boolean),
]);
const historicalResearchText = [
  path.join(root, 'data/기본기_연구/astra_handoff_queue.jsonl'),
  path.join(root, '분석/기본기_연구/독립연구_03_최초풀이.md'),
  path.join(root, '분석/기본기_연구/독립연구_04_절차와_진행기록.md'),
].filter((file) => fs.existsSync(file)).map((file) => fs.readFileSync(file, 'utf8')).join('\n');

const alpha = (n) => {
  let s = '';
  for (let x = n; x >= 0; x = Math.floor(x / 26) - 1) s = String.fromCharCode(65 + (x % 26)) + s;
  return s;
};
const nextCaseNumber = (() => {
  const ids = [...existingCases].filter((x) => /^[A-Z]+$/.test(x));
  const value = (s) => [...s].reduce((n, c) => n * 26 + c.charCodeAt(0) - 64, 0);
  return Math.max(...ids.map(value));
})();
const nextGroupNumber = (() => {
  const values = manifest.map((x) => String(x.passage_group ?? ''))
    .filter((x) => /^G\d{3}$/.test(x))
    .map((x) => Number(x.slice(1)));
  return Math.max(0, ...values) + 1;
})();
const caseIdAt = (offset) => {
  const value = nextCaseNumber + offset + 1;
  let n = value, out = '';
  while (n > 0) { n--; out = String.fromCharCode(65 + (n % 26)) + out; n = Math.floor(n / 26); }
  return out;
};

const candidateByQuestion = new Map(candidates.map((x) => [x.canonical_connection?.question_id, x]));
const candidateById = new Map(candidates.map((x) => [x.candidate_id, x]));
const answerIsMechanicallyResolved = (q) => {
  if (q.official_answer_verified !== true || q.answer == null) return false;
  const values = Object.values(q.answer_candidates ?? {}).flatMap((value) => Array.isArray(value) ? value : [value]);
  if (!['A', 'B'].includes(q.variant)) {
    return new Set(values).size === 1 && values[0] === q.answer;
  }
  const candidate = q.answer_candidates?.[q.variant];
  return typeof candidate === 'string' && candidate === q.answer;
};
const qByPassage = new Map();
for (const q of questions) {
  if (!qByPassage.has(q.passage_id)) qByPassage.set(q.passage_id, []);
  qByPassage.get(q.passage_id).push(q);
}

const literatureEntries = fs.existsSync(literatureMappingPath)
  ? JSON.parse(fs.readFileSync(literatureMappingPath, 'utf8')).entries.filter((x) =>
      x.source_status === 'LOCAL_COMPLETE' &&
      x.preparation_status === 'READY_LOCAL_LITERATURE_SOURCE' &&
      x.additional_download_required === false)
  : [];
const normalizedAnswerTables = fs.existsSync(normalizedAnswerPath)
  ? new Map(JSON.parse(fs.readFileSync(normalizedAnswerPath, 'utf8')).tables.map((x) => [x.source_file, x.answers ?? {}]))
  : new Map();
const literatureOfficialAnswer = (entry) => normalizedAnswerTables.get(entry.official_answer_source_path)?.[String(entry.question_number)] ?? null;
const literatureGroups = new Map();
for (const entry of literatureEntries) {
  if (existingPreparedCandidateIds.has(entry.candidate_id) || historicalResearchText.includes(entry.candidate_id)) continue;
  if (!literatureGroups.has(entry.central_md_path)) literatureGroups.set(entry.central_md_path, []);
  literatureGroups.get(entry.central_md_path).push(entry);
}
const literatureSlug = (entry) => `${entry.academic_year}-${entry.exam}-${path.basename(entry.central_md_path, '.md')}`
  .replace(/[^0-9A-Za-z가-힣]+/g, '_')
  .replace(/^_+|_+$/g, '');
const fileSha256 = (file) => crypto.createHash('sha256').update(fs.readFileSync(file)).digest('hex');
const parseLiteratureMd = (file) => {
  const raw = fs.readFileSync(path.join(root, file), 'utf8');
  const separator = raw.indexOf('\n---\n');
  const body = separator >= 0 ? raw.slice(separator + 5) : raw;
  const heading = body.match(/^\[(\d+)~(\d+)\].*?(\d+)\s*~\s*(\d+)번.*$/m);
  if (!heading) return { error: 'literature question-range heading not found' };
  const questionStart = Number(heading[3]);
  const headingEnd = heading.index + heading[0].length;
  const rest = body.slice(headingEnd);
  const sectionRe = /^(\d{3})\s+([^\n]+)$/gm;
  const sections = [...rest.matchAll(sectionRe)];
  if (!sections.length) return { error: 'literature question sections not found' };
  const passageText = rest.slice(0, sections[0].index).trim();
  const questionsByNumber = new Map();
  for (let i = 0; i < sections.length; i++) {
    const localNumber = Number(sections[i][1]);
    const start = sections[i].index;
    const end = i + 1 < sections.length ? sections[i + 1].index : rest.length;
    const sectionBody = rest.slice(start + sections[i][0].length, end).trim();
    const choiceMarks = [...sectionBody.matchAll(/^([①②③④⑤])\s*/gm)];
    const stem = (choiceMarks.length ? sectionBody.slice(0, choiceMarks[0].index) : sectionBody).trim();
    const choices = [];
    for (let j = 0; j < choiceMarks.length; j++) {
      const cStart = choiceMarks[j].index + choiceMarks[j][0].length;
      const cEnd = j + 1 < choiceMarks.length ? choiceMarks[j + 1].index : sectionBody.length;
      choices.push(sectionBody.slice(cStart, cEnd).trim());
    }
    questionsByNumber.set(questionStart + (localNumber - Number(sections[0][1])), {
      localNumber,
      label: sections[i][2].trim(),
      stem,
      choices,
      raw: sectionBody,
    });
  }
  return { passageText, questionsByNumber, questionStart, firstLocalNumber: Number(sections[0][1]) };
};

const selected = [];
for (const passage of passages) {
  if (usedPassages.has(passage.passage_id)) continue;
  const qs = (qByPassage.get(passage.passage_id) || []).sort((a, b) => a.question_number - b.question_number);
  if (!qs.length) continue;
  selected.push({ passage, questions: qs });
  if (selected.length === 30) break;
}

const rules = [
  'all_group_blind_records_before_any_group_answer_check',
  'all_group_independent_code_records_before_any_group_sdss_disclosure',
];
const rows = [];
const mappingRows = [];
const answerRows = [];
const report = [];
let caseOffset = 0;

for (let i = 0; i < selected.length; i++) {
  const { passage, questions: qs } = selected[i];
  const groupId = `G${String(nextGroupNumber + i).padStart(3, '0')}`;
  const ids = qs.map(() => caseIdAt(caseOffset++));
  const visual = qs.some((q) => q.contains_visual_placeholder === true);
  const malformed = !passage.passage_text || !passage.passage_text.trim() || qs.some((q) => !q.stem || !Array.isArray(q.choices) || q.choices.length !== 5 || q.choice_parse_status !== 'complete');
  const status = malformed ? 'UNRESOLVED' : visual ? 'NEEDS_RESTORE' : 'READY';
  const reasons = [];
  if (malformed) reasons.push('passage/stem/choices completeness or choice parse check failed');
  if (visual) reasons.push('one or more cases declare visual material; no linked blind-safe asset was found in the canonical KICE record');

  for (let j = 0; j < qs.length; j++) {
    const q = qs[j], id = ids[j];
    const candidate = candidateByQuestion.get(q.question_id);
    const source = {
      blind_only: true,
      passage_group: groupId,
      case_id: id,
      provenance: { source_role: 'anonymous_blind_source' },
      passage_text: passage.passage_text,
      stem: q.stem,
      choices: q.choices,
    };
    const sourceFile = path.join(blindDir, `${id}.json`);
    if (status === 'READY') {
      writeJson(sourceFile, source);
      const manifestRow = {
        case_id: id,
        status: 'prepared',
        passage_group: groupId,
        group_case_ids: ids,
        group_release_rules: rules,
        blind_source: `data/기본기_연구/prepared_backlog/blind_sources/${id}.json`,
        exclusion_checks: {
          exposure_status: 'unknown',
          semantic_review: 'not_reviewed',
          source_quality: {
            visual_placeholder: false,
            canonical_link: 'exact',
            choice_parse: 'complete',
            text_markers_preserved: true,
          },
        },
      };
      rows.push(manifestRow);
      mappingRows.push({
        case_id: id,
        passage_group: groupId,
        group_case_ids: ids,
        provenance: {
          exam_family: passage.exam_family,
          academic_year: passage.academic_year,
          exam_label: passage.exam_label,
          question_number: q.question_number,
          question_id: q.question_id,
          passage_id: passage.passage_id,
        },
        source_status: 'exact_canonical_kice_question',
        source_role: 'sealed_provenance_mapping',
      });
      answerRows.push({
        case_id: id,
        candidate_id: candidate?.candidate_id ?? null,
        official_answer: answerIsMechanicallyResolved(q) ? q.answer : null,
        official_answer_source: 'data/kice_questions.jsonl (answer field; mechanical linkage only)',
        site_original_codes: candidate?.site_candidate?.site_original_codes ?? [],
        site_marked_answer: candidate?.site_candidate?.site_marked_answer ?? null,
        source_role: 'sealed_for_after_blind',
        passage_group: passage.passage_id,
        release_rule: rules[0],
      });
    }
  }
  const packetIds = ids.join(', ');
  if (status === 'READY') {
    fs.writeFileSync(path.join(packetDir, `${ids[0]}.md`), `# ${ids[0]} blind packet\n\n- passage_group: ${groupId}\n- group_case_ids: ${packetIds}\n- blind_sources: ${ids.map((id) => `data/기본기_연구/prepared_backlog/blind_sources/${id}.json`).join('; ')}\n- group_rules: ${rules.join('; ')}\n\nAstra는 group 전체의 anonymous blind-only source를 먼저 읽고 stage barrier를 지킨다.\n`, 'utf8');
    for (const id of ids.slice(1)) fs.writeFileSync(path.join(packetDir, `${id}.md`), `# ${id} blind packet\n\n- passage_group: ${groupId}\n- group_case_ids: ${packetIds}\n- blind_source: data/기본기_연구/prepared_backlog/blind_sources/${id}.json\n- group_rules: ${rules.join('; ')}\n\nAstra는 anonymous blind-only source만 읽고 group barrier를 지킨다.\n`, 'utf8');
  }
  report.push({ index: i + 1, passage_group: groupId, case_ids: ids, passage_id: passage.passage_id, status, reasons, sdss_linked_cases: status === 'READY' ? qs.filter((q) => candidateByQuestion.has(q.question_id)).length : 0, sdss_unlinked_cases: status === 'READY' ? qs.filter((q) => !candidateByQuestion.has(q.question_id)).length : 0 });
}

const literatureReport = [];
let literatureGroupOffset = selected.length;
for (const [centralMdPath, rawEntries] of literatureGroups.entries()) {
  const entries = rawEntries
    .filter((x) => !existingPreparedCandidateIds.has(x.candidate_id))
    .sort((a, b) => a.question_number - b.question_number);
  if (!entries.length) continue;
  const groupId = `G${String(nextGroupNumber + literatureGroupOffset).padStart(3, '0')}`;
  literatureGroupOffset += 1;
  const ids = entries.map(() => caseIdAt(caseOffset++));
  const reasons = [];
  let parsed;
  try {
    const sourcePath = path.join(root, centralMdPath);
    if (!fs.existsSync(sourcePath)) throw new Error(`missing central_md:${centralMdPath}`);
    const sourceHash = fileSha256(entries[0].source_original_path);
    if (sourceHash !== entries[0].source_sha256) throw new Error(`source_sha256 mismatch:${entries[0].candidate_id}`);
    parsed = parseLiteratureMd(centralMdPath);
    if (parsed.error) throw new Error(parsed.error);
  } catch (error) {
    reasons.push(String(error.message || error));
  }
  const cases = parsed ? entries.map((entry, index) => {
    const q = parsed.questionsByNumber.get(entry.question_number);
    const id = ids[index];
    if (!q || !q.stem || q.choices.length !== 5) reasons.push(`incomplete literature question:${entry.candidate_id}`);
    return { entry, q, id };
  }) : [];
  const status = reasons.length ? 'UNRESOLVED' : 'READY';
  if (status === 'READY') {
    for (const { entry, q, id } of cases) {
      const source = {
        blind_only: true,
        passage_group: groupId,
        case_id: id,
        provenance: { source_role: 'anonymous_blind_source' },
        passage_text: parsed.passageText,
        stem: `Q${entry.question_number} ${q.label}\n\n${q.stem}`,
        choices: q.choices,
      };
      writeJson(path.join(blindDir, `${id}.json`), source);
      rows.push({
        case_id: id,
        status: 'prepared',
        passage_group: groupId,
        group_case_ids: ids,
        group_release_rules: rules,
        blind_source: `data/기본기_연구/prepared_backlog/blind_sources/${id}.json`,
        exclusion_checks: {
          exposure_status: 'unknown',
          semantic_review: 'not_reviewed',
          source_quality: {
            visual_placeholder: false,
            canonical_link: 'literature_central_md',
            choice_parse: 'complete',
            text_markers_preserved: true,
          },
        },
      });
      const candidate = candidateById.get(entry.candidate_id);
      const slug = literatureSlug(entry);
      const passageId = `KICE-LIT-${slug}`;
      const questionId = `${passageId}-Q${entry.question_number}`;
      mappingRows.push({
        case_id: id,
        passage_group: groupId,
        group_case_ids: ids,
        provenance: {
          candidate_id: entry.candidate_id,
          exam_family: 'KICE',
          academic_year: entry.academic_year,
          exam_label: entry.exam,
          question_number: entry.question_number,
          question_id: questionId,
          passage_id: passageId,
          source_original_path: entry.source_original_path,
          source_filename: entry.source_filename,
          source_sha256: entry.source_sha256,
          central_md_path: entry.central_md_path,
          official_answer_source_path: entry.official_answer_source_path,
          source_type: 'mother_tong_hwp_or_hwpx_transcription',
          source_role: 'literature_source',
        },
        source_status: 'local_complete_literature',
        source_role: 'sealed_provenance_mapping',
      });
      answerRows.push({
        case_id: id,
        candidate_id: candidate?.candidate_id ?? entry.candidate_id,
        official_answer: literatureOfficialAnswer(entry),
        official_answer_source: entry.official_answer_source_path,
        site_original_codes: [],
        site_marked_answer: null,
        source_role: 'sealed_for_after_blind',
        passage_group: passageId,
        release_rule: rules[0],
      });
    }
    const packetIds = ids.join(', ');
    fs.writeFileSync(path.join(packetDir, `${ids[0]}.md`), `# ${ids[0]} blind packet\n\n- passage_group: ${groupId}\n- group_case_ids: ${packetIds}\n- blind_sources: ${ids.map((id) => `data/기본기_연구/prepared_backlog/blind_sources/${id}.json`).join('; ')}\n- group_rules: ${rules.join('; ')}\n\nAstra는 문학 group 전체의 anonymous blind-only source를 먼저 읽고 stage barrier를 지킨다.\n`, 'utf8');
    for (const id of ids.slice(1)) fs.writeFileSync(path.join(packetDir, `${id}.md`), `# ${id} blind packet\n\n- passage_group: ${groupId}\n- group_case_ids: ${packetIds}\n- blind_source: data/기본기_연구/prepared_backlog/blind_sources/${id}.json\n- group_rules: ${rules.join('; ')}\n\nAstra는 anonymous blind-only source만 읽고 group barrier를 지킨다.\n`, 'utf8');
  }
  literatureReport.push({ passage_group: groupId, central_md_path: centralMdPath, case_ids: ids, status, reasons, target_count: entries.length });
}

if (fs.existsSync(centralIndexPath)) {
  const centralIndex = JSON.parse(fs.readFileSync(centralIndexPath, 'utf8'));
  const existingIndexPaths = new Set((centralIndex.entries ?? []).map((x) => x.path));
  for (const entry of literatureEntries) {
    const rel = entry.central_md_path.replace(/^data\/기출_MD_정본\//, '');
    if (existingIndexPaths.has(rel)) continue;
    centralIndex.entries.push({
      academic_year: entry.academic_year,
      exam_label: entry.exam,
      area: '문학',
      path: rel,
      source_original_path: entry.source_original_path,
      source_sha256: entry.source_sha256,
      status: 'CENTRALIZED_MOTHERTONG_LITERATURE_SOURCE',
      source_type: 'mother_tong_hwp_or_hwpx_transcription',
    });
    existingIndexPaths.add(rel);
  }
  fs.writeFileSync(centralIndexPath, JSON.stringify(centralIndex, null, 2) + '\n', 'utf8');
}

if (rows.length) fs.appendFileSync(manifestPath, rows.map((x) => JSON.stringify(x)).join('\n') + '\n', 'utf8');
if (mappingRows.length) appendJsonl(mappingPath, mappingRows);
if (answerRows.length) appendJsonl(answerPath, answerRows);

const reportGroups = [...report, ...literatureReport];
const reportDate = new Date().toISOString().slice(0, 10).replaceAll('-', '');
const reportPath = path.join(base, `LUNA_FRONTIER_PREFLIGHT_${reportDate}.md`);
const lines = [
  `# Luna frontier preflight — ${reportDate}`, '',
  '기계적 corpus preparation만 수행했다. 의미적 풀이·정답 추론·코드 판정은 수행하지 않았다.', '',
  `- 시작 frontier: G${String(nextGroupNumber).padStart(3, '0')}`,
  `- 검사한 passage group: ${reportGroups.length}개`,
  `- 새 READY passage group / case: ${reportGroups.filter((x) => x.status === 'READY').length}개 / ${rows.length}건`,
  `- 문학 target: ${literatureEntries.length}개 후보, 새 prepare ${literatureReport.reduce((n, x) => n + (x.status === 'READY' ? x.target_count : 0), 0)}건`,
  `- NEEDS_RESTORE group: ${reportGroups.filter((x) => x.status === 'NEEDS_RESTORE').map((x) => `${x.passage_group}(${x.case_ids.join(',')})`).join(', ') || '없음'}`,
  `- UNRESOLVED group: ${reportGroups.filter((x) => x.status === 'UNRESOLVED').map((x) => `${x.passage_group}(${x.case_ids.join(',')})`).join(', ') || '없음'}`,
  '- 복원한 visual/source asset: 없음 (필요한 시각자료가 canonical record에 연결되지 않은 group은 복원 대기)',
  `- SDSS linkage 연결 case: ${answerRows.filter((x) => x.site_original_codes.length > 0).length}건`,
  `- SDSS linkage 미연결 case: ${answerRows.filter((x) => x.site_original_codes.length === 0).length}건`,
  `- 다음 preparation frontier: G${String(nextGroupNumber + reportGroups.length).padStart(3, '0')} 이후`,
  `- Astra 즉시 연구 가능한 첫 READY group: ${reportGroups.find((x) => x.status === 'READY')?.passage_group ?? '없음'}`,
  '', '## group 판정', '',
  '| group | case IDs | status | reason |', '|---|---|---|---|',
  ...reportGroups.map((x) => `| ${x.passage_group} | ${x.case_ids.join(', ')} | ${x.status} | ${x.reasons?.join('; ') || 'all mechanical checks passed'} |`),
  '', '## provenance', '',
  `- KICE canonical source: data/kice_passages.jsonl, data/kice_questions.jsonl`,
  `- 기존 consumed passage 중복: 0건 (used passage_id set으로 제외)`,
  `- 새 manifest rows: ${rows.length}; sealed mapping rows: ${mappingRows.length}; sealed answer rows: ${answerRows.length}`,
  `- literature source mapping: ${literatureMappingPath}`,
];
fs.writeFileSync(reportPath, lines.join('\n') + '\n', 'utf8');
console.log(JSON.stringify({ inspected: reportGroups.length, ready_groups: reportGroups.filter((x) => x.status === 'READY').length, ready_cases: rows.length, literature_candidates: literatureEntries.length, literature_ready_cases: literatureReport.reduce((n, x) => n + (x.status === 'READY' ? x.target_count : 0), 0), needs_restore: reportGroups.filter((x) => x.status === 'NEEDS_RESTORE').map((x) => x.passage_group), unresolved: reportGroups.filter((x) => x.status === 'UNRESOLVED').map((x) => x.passage_group), report: reportPath }, null, 2));
