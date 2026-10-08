

<!-- luna-raw:BLT-answer_check-20261003-01 -->
## Astra raw handoff — answer_check

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G467",
  "selected_answer": 4,
  "official_answer": 4,
  "match": true,
  "original_blind_preserved": true,
  "group_blind_barrier_verified": true,
  "official_answer_source": "자료/LEET_언어이해/원본/2020/2020_answer_2020_LEET_언어이해_정답표.hwp",
  "minimal_logic_without_codes": "A궤도에서K는최근점에서Y보다크고최원점에서Y보다작다.같은중간거리의대칭두지점에서같은K를가지므로Y와같은운동에너지의지점은하나가아닌둘이다.④가부적절하다.",
  "sdss_seen": false,
  "strict_blind_eligible": false,
  "source_restoration_before_disclosure": true,
  "background_knowledge_limit_preserved": "큰타원최원점속력이기존원궤도속력보다작다는기본궤도역학과중심력타원의대칭성을보조사용했다.복원된본문수식은K,U,E뿐이며원문이궤도속력공식전체를명시했다고주장하지않는다."
}
```


<!-- luna-raw:BLT-independent_code-20261003-01 -->
## Astra raw handoff — independent_code

원문 raw 의미를 보존한 기계적 반영이다. Luna는 의미를 재판정하지 않았다.

```json
{
  "passage_group": "G467",
  "minimal_logic_without_codes": "고정된타원궤도에서같은r은같은U와K를주지만같은r의지점은대칭적으로둘일수있다.Y의고정K와일치하는중간에너지에해당하는공간지점을하나로단정하지않는다.",
  "primary": [
    {
      "code": 45,
      "reason": "궤도위치→거리→U→K의대응과역으로같은K를주는지점수를구분한다."
    }
  ],
  "auxiliary": [
    {
      "code": 85,
      "reason": "같은궤도에서E고정하K와U의상보관계를적용한다."
    },
    {
      "code": 86,
      "reason": "A/B/Y의최대·최소에너지를동일질량조건에서대소비교한다."
    },
    {
      "code": 31,
      "reason": "동일에너지값하나와그값을주는공간지점둘의수를구분한다."
    },
    {
      "code": 43,
      "reason": "같은질량과분사후각궤도의에너지보존조건을유지하며궤도간E까지같다고두지않는다."
    }
  ],
  "surface": [
    {
      "code": 92,
      "reason": "공식에변수를대입한정량답을계산하기보다함수대응과부호·극값관계를판독한다."
    }
  ],
  "competing_codes": [
    {
      "code": 11,
      "rejection": "에너지값이하나라고공간위치도하나라는일대일·양방향대응을보장하지않는다."
    },
    {
      "code": 84,
      "rejection": "U분수식은대소관계의근거이지만④의오류는그역상에여러위치가있다는점이다."
    },
    {
      "code": 90,
      "rejection": "지점수를세기는하지만조합이나확률계산보다동일출력의복수입력판독이다."
    }
  ],
  "source_limit": "최원점속력과타원대칭성의보조물리지식사용을최초blind대로보존.원문만으로독립완결했다고승격하지않는다.",
  "confidence": 0.91,
  "sdss_seen": false
}
```
