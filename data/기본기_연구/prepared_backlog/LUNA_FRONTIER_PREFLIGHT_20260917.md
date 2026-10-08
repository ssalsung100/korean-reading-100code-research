# Luna frontier preflight — 2026-09-17

기계적 corpus preparation만 수행했다. 의미적 풀이·정답 추론·코드 판정은 수행하지 않았다.

- 시작 frontier: G071 / KF
- 검사한 passage group: 30개 (G071~G100)
- 새 READY passage group / case: 18개 / 66건
- NEEDS_RESTORE group: G081(LN,LO,LP), G090(MW,MX)
- UNRESOLVED group: G071(KF,KG,KH,KI), G072(KJ,KK,KL,KM), G073(KN,KO,KP), G074(KQ,KR,KS,KT), G075(KU,KV,KW), G084(LZ,MA,MB,MC), G086(MH,MI,MJ,MK), G095(NK,NL,NM,NN,NO), G096(NP,NQ,NR,NS,NT), G098(OA,OB,OC,OD,OE)
- 복원한 visual/source asset: 없음 (필요한 시각자료가 canonical record에 연결되지 않은 group은 복원 대기)
- SDSS linkage 연결 case: 0건
- SDSS linkage 미연결 case: 66건
- 다음 preparation frontier: G101 이후
- Astra 즉시 연구 가능한 첫 READY group: G076

## group 판정

| group | case IDs | status | reason |
|---|---|---|---|
| G071 | KF, KG, KH, KI | UNRESOLVED | passage/stem/choices completeness or choice parse check failed |
| G072 | KJ, KK, KL, KM | UNRESOLVED | passage/stem/choices completeness or choice parse check failed |
| G073 | KN, KO, KP | UNRESOLVED | passage/stem/choices completeness or choice parse check failed |
| G074 | KQ, KR, KS, KT | UNRESOLVED | passage/stem/choices completeness or choice parse check failed |
| G075 | KU, KV, KW | UNRESOLVED | passage/stem/choices completeness or choice parse check failed |
| G076 | KX, KY, KZ, LA | READY | all mechanical checks passed |
| G077 | LB, LC, LD, LE | READY | all mechanical checks passed |
| G078 | LF, LG, LH, LI | READY | all mechanical checks passed |
| G079 | LJ, LK | READY | all mechanical checks passed |
| G080 | LL, LM | READY | all mechanical checks passed |
| G081 | LN, LO, LP | NEEDS_RESTORE | one or more cases declare visual material; no linked blind-safe asset was found in the canonical KICE record |
| G082 | LQ, LR, LS, LT | READY | all mechanical checks passed |
| G083 | LU, LV, LW, LX, LY | READY | all mechanical checks passed |
| G084 | LZ, MA, MB, MC | UNRESOLVED | passage/stem/choices completeness or choice parse check failed |
| G085 | MD, ME, MF, MG | READY | all mechanical checks passed |
| G086 | MH, MI, MJ, MK | UNRESOLVED | passage/stem/choices completeness or choice parse check failed |
| G087 | ML, MM, MN, MO, MP | READY | all mechanical checks passed |
| G088 | MQ, MR, MS, MT | READY | all mechanical checks passed |
| G089 | MU, MV | READY | all mechanical checks passed |
| G090 | MW, MX | NEEDS_RESTORE | one or more cases declare visual material; no linked blind-safe asset was found in the canonical KICE record |
| G091 | MY, MZ, NA | READY | all mechanical checks passed |
| G092 | NB, NC | READY | all mechanical checks passed |
| G093 | ND, NE, NF | READY | all mechanical checks passed |
| G094 | NG, NH, NI, NJ | READY | all mechanical checks passed |
| G095 | NK, NL, NM, NN, NO | UNRESOLVED | passage/stem/choices completeness or choice parse check failed |
| G096 | NP, NQ, NR, NS, NT | UNRESOLVED | passage/stem/choices completeness or choice parse check failed |
| G097 | NU, NV, NW, NX, NY, NZ | READY | all mechanical checks passed |
| G098 | OA, OB, OC, OD, OE | UNRESOLVED | passage/stem/choices completeness or choice parse check failed |
| G099 | OF, OG, OH, OI | READY | all mechanical checks passed |
| G100 | OJ, OK, OL, OM | READY | all mechanical checks passed |

## provenance

- KICE canonical source: data/kice_passages.jsonl, data/kice_questions.jsonl
- 기존 consumed passage 중복: 0건 (used passage_id set으로 제외)
- 새 manifest rows: 66; sealed mapping rows: 66; sealed answer rows: 66
