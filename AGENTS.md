저장소의 현재 상태를 기준으로 「평가원 문체·100코드 기본기 연구」를 이어서 수행하라. 대화 기억보다 저장소 파일을 authoritative source로 삼는다.

운영 규칙(2026-09-15 추가): 3개 passage group 완전 완료마다 Astra가 due `meta_induction`·`manual_parity_audit`·필요 `depth_backfill`을 먼저 raw로 저장하고, Luna sync 1회를 수행한 뒤 pending raw=0을 검증하고서야 다음 연구를 계속한다. quota emergency 경고가 발생하면 이 규칙보다 emergency whitelist를 우선한다.

먼저 다음을 읽어 현재 진행 상태·절차·기존 판정을 복원하라.

* `새대화용_평가원형_지문문항_생성_인수인계.md`
* `DB_자산_인덱스.md`
* `분석/기본기_연구/00_연구계획과_진행기록.md`
* `분석/기본기_연구/독립연구_03_절차와_진행기록.md`
* `분석/기본기_연구/코드심층_03_독립풀이_증거와경쟁.md`
* `분석/기본기_연구/핵심8코드_경계와_판독기준_v1.md`
* `data/기본기_연구/코드군_통합가설_v1.json`
* `data/sdss_100codes_catalog.json`

실제 파일 상태가 문서의 과거 설명과 다르면 최신 저장소 상태를 우선한다.

### 핵심 절차

새 문항마다 반드시 다음 순서를 지킨다.

**공식 원문 blind 풀이 저장 → 공식 정답 대조 → 코드 없는 실제 논리 구조 고정 → 주/보조/표면 코드 독립 판정 및 경쟁 코드 2~4개 반증 → 마지막에 SDSS 태그 공개·대조 → 사례 간 귀납·반례 검토**

blind 풀이 전에는 해당 문항의 공식 답, SDSS 태그, 기존 프로젝트 해설·코드 판정을 읽지 않는다. 과거 노출 사례는 엄격한 blind 성과에서 제외한다.

준비 사례의 blind 단계에서는 `data/기본기_연구/prepared_backlog/blind_sources/`의 blind-only source만 읽는다. 원래 `data/kice_questions.jsonl`·후속 candidate index·sealed answer/SDSS 파일·기존 해설·기존 코드 판정은 해당 passage group의 모든 blind raw record가 저장될 때까지 읽지 않는다. 같은 passage group의 여러 문항은 group 전체 blind 완료 후에만 answer_check를 시작한다.
동일 group의 stage barrier는 `all_group_blind_records_before_any_group_answer_check` → group 전체 `answer_check` → group 전체 `independent_code`(primary/auxiliary/surface 및 경쟁 코드 2~4개) → `all_group_independent_code_records_before_any_group_sdss_disclosure` 확인 → SDSS 공개·대조 → 필요 시 induction/boundary revision 순서다. 한 case의 SDSS를 본 뒤 같은 group의 다른 case independent_code를 판단하지 않는다.

최초 풀이에는 최소한 다음을 남긴다.

* 선택 답·확신도·노출 여부
* 필요한 정보와 위치
* 코드명 없는 최소 논리 구조
* 중간 추론
* 가장 매력적인 오답과 정확한 오류

공식 답 확인 후에도 최초 기록은 덮어쓰지 않는다.

코드 판정에서는 번호가 다르다는 이유로 억지 경계를 만들지 않는다. 실질적으로 같은 판단 연산이면 통합 가능성을 검토하되 원래 번호·사이트 태그·최초 판정과 재분할 조건을 보존한다.

SDSS는 정답지가 아니라 제3자 후보 색인이다.

### 연구 목표

문항 수 자체보다 다음을 우선한다.

* 인접 코드 경계
* 기존 정의의 반례
* 다중 코드 사례
* SDSS와 독립 판정 불일치
* 동일 코드인데 풀이 행동이 다른 사례
* KICE·LEET·MEET 구현 차이

KICE를 최종 평가원형 생성 규칙의 최우선 근거로 둔다.

prepared backlog가 남아 있고 quota가 충분하면 batch 크기와 현재 소수 frontier 완료를 이유로 종료하지 말고 다음 사례를 계속 소비한다. 기본 연구 시작 경로는 `scripts/cx1m` fresh Astra TUI이며, primary 또는 weekly remaining이 처음 7% 이하로 관측되면 Astra가 즉시 실제 `spawn_agent`로 Luna를 handoff한다. Astra의 판단 결과는 판단 직후 `data/기본기_연구/astra_handoff_queue.jsonl`에 최소 raw record로 append한다. 상세 Markdown/JSONL 반영과 상태 정리는 Luna가 맡는다. 1M context를 DB처럼 채우지 말고 현재 코드군과 판정에 필요한 원문·기준·anchor만 읽는다.

자료 탐색·식별·정본 연결 등 기계적 작업은 보조 에이전트를 써도 되지만, blind 풀이·논리 복원·코드 판정·경계/반례/기준 수정은 주 Astra가 공식 원문을 직접 읽고 수행한다.

모든 분석·진행 보고·연구 기록은 한국어로 작성한다.

### Astra / Luna 역할

**Astra = 고난도 판단 + raw persistence**

Astra는 공식 원문의 blind 풀이, 정답 판단·대조, 코드명 없는 논리 복원, 주/보조/표면 코드 판정, 경쟁 코드 2~4개 반증, 경계·반례·통합/분리 판단, SDSS 의미 비교, 사례 간 귀납 및 기존 기준 수정 여부 판단을 직접 수행한다. 각 의미 있는 판단 단계가 끝나는 즉시 최소 record를 `data/기본기_연구/astra_handoff_queue.jsonl`에 append한다. 상세 Markdown 편집, CURRENT 갱신, 진행률 계산, 파일 정리, 반복 hash/audit, checkpoint 정리는 원칙적으로 하지 않는다.

**Luna = formatting + state management + checkpoint + audit**

Luna는 queue raw record를 기존 연구 MD/JSONL에 반영하고 `astra_handoff_processed.jsonl`, CURRENT, 다음 frontier와 handoff를 관리한다. Luna는 Astra 판정의 의미를 임의로 수정하지 않는다. 애매하거나 불완전하거나 의미적 재판단이 필요한 record는 추론으로 보완하지 않고 `needs_astra_review` 등으로 남긴다.

### Persistence policy

연구 판단을 대화 context에만 보관하지 않는다. `astra_handoff_queue.jsonl`은 앞으로의 신규 판단을 위한 append-only immutable raw 원장이고, 처리 여부는 `astra_handoff_processed.jsonl`에서 별도로 추적한다. Astra는 queue에 기록되지 않은 판단을 완료된 연구 결과로 간주하지 않으며, raw 저장 후 상세 문서나 CURRENT 갱신 때문에 다음 판단을 지연하지 않는다. 기존 연구 자산은 queue로 소급 변환하지 않는다.

### Session / Context policy

대화 세션은 임시 작업공간이며 저장소 파일을 장기 기억의 기준으로 삼는다. 새 Astra batch는 원칙적으로 새 세션에서 시작하고, 기본 초기 로드는 `AGENTS.md`, `분석/기본기_연구/CURRENT.md`, `분석/기본기_연구/ASTRA_START.md`로 제한한다. 전체 archive는 매번 다시 읽지 않으며, 과거 상세 파일은 현재 판단에 실제로 필요할 때만 선택적으로 읽는다. CURRENT의 상세 상태 관리와 갱신은 기본적으로 Luna가 담당한다.

Astra는 CURRENT의 frontier와 `data/기본기_연구/prepared_backlog/manifest.jsonl`를 순서대로 소비하고 raw queue를 지속적으로 남긴다. 5시간 primary 또는 weekly remaining이 처음 7% 이하(`used_percent >= 93`)면 신규 case·group·semantic stage·SDSS compare·induction·boundary revision을 시작하지 않고 안전한 atomic stage와 raw/checkpoint만 저장한 뒤 Luna를 즉시 spawn한다. Runtime의 `less than 5% of your 5h limit left` 경고는 quota helper 성공·unavailable 여부와 무관한 emergency trigger이며 재조회하지 않는다. quota unavailable은 값을 추정하지 않고 보존하되 그 자체는 handoff가 아니다. hard limit으로 Astra가 먼저 종료되면 다음 `cxresearch`는 queue/processed를 비교하고 Luna recovery를 먼저 수행한다. 한 batch, frontier, induction, 진행 보고의 완료는 종료 사유가 아니다. 세션이 갑자기 종료되어도 queue의 마지막 저장 record까지 복구 가능해야 한다. Astra TUI는 quota threshold에서 Luna subagent를 호출하고, `cxcycle`은 unattended fallback으로 보존한다.

### Continuous Research Policy

Runtime `<5%` warning action whitelist: after `less than 5% of your 5h limit left` or an equivalent warning, immediately enter emergency handoff. Only an already-completed atomic raw append, one emergency checkpoint/hold, Luna spawn, and Astra termination are permitted. Do not call quota helpers again, read new files or sealed sources, search, or continue semantic reasoning; an incomplete atomic stage is held with its next work and exposure state. This warning overrides helper results, unavailable status, prior quota values, and weekly remaining.

`분석/기본기_연구/ASTRA_START.md`의 지속 실행 지시를 따른다. Astra가 “지정된 frontier를 완료했다”는 이유로 멈추지 않는다. 준비된 사례가 있으면 다음 Excel-style case ID로 이동한다. quota 정보가 runtime에 노출되지 않으면 존재한다고 가정하지 않고 Codex의 실제 경고·rate-limit 오류를 fail-safe로 사용한다.

이제 설명만 하지 말고 실제 작업을 시작하라.

1. 현재 완료 지점을 확인한다.
2. 미완료된 대조·귀납만 마무리한다.
3. 다음 연구 가치가 높은 코드군을 선택한다.
4. 새 blind 사례 묶음의 직접 풀이를 시작한다.
5. 새 발견과 기준 수정은 저장소에 반영한다.

최종 목적은 사이트 태그를 맞히는 것이 아니라, 공식 기출에서 반복되는 실제 판단 연산을 바탕으로 100코드의 의미·경계·중복·반례를 신뢰할 수 있는 연구 자산으로 구축하는 것이다.
