import json
import unittest

from normalize_kice_reading_corpus import answer_is_mechanically_resolved, choose_answer


def tables(*items):
    return {table["table_id"]: table for table in items}


def table(table_id, variant, answer):
    return {"table_id": table_id, "variant": variant, "answers": {"17": answer}}


class ChooseAnswerTest(unittest.TestCase):
    def test_explicit_variant_does_not_fall_back_to_other_variant(self):
        answer, candidates = choose_answer(
            {"answer_table_ids": ["a"]}, tables(table("a", "A", "2")), 17, "B"
        )
        self.assertIsNone(answer)
        self.assertEqual(candidates, {"A": "2"})

    def test_conflicting_tables_of_requested_variant_stay_unresolved(self):
        answer, candidates = choose_answer(
            {"answer_table_ids": ["a", "b"]},
            tables(table("a", "B", "2"), table("b", "B", "4")),
            17,
            "B",
        )
        self.assertIsNone(answer)
        self.assertEqual(candidates, {"B": ["2", "4"]})
        json.dumps(candidates, ensure_ascii=False)

    def test_identical_duplicate_variant_is_accepted(self):
        answer, candidates = choose_answer(
            {"answer_table_ids": ["a", "b"]},
            tables(table("a", "B", "4"), table("b", "B", "4")),
            17,
            "B",
        )
        self.assertEqual(answer, "4")
        self.assertEqual(candidates, {"B": "4"})

    def test_explicit_variant_rejects_common_only(self):
        answer, _ = choose_answer(
            {"answer_table_ids": ["a"]}, tables(table("a", None, "4")), 17, "B"
        )
        self.assertIsNone(answer)

    def test_exact_variant_match(self):
        answer, candidates = choose_answer(
            {"answer_table_ids": ["a", "b"]},
            tables(table("a", "A", "2"), table("b", "B", "4")),
            17,
            "B",
        )
        self.assertEqual(answer, "4")
        self.assertEqual(candidates, {"A": "2", "B": "4"})

    def test_variantless_unambiguous_agreement_is_preserved(self):
        answer, candidates = choose_answer(
            {"answer_table_ids": ["a", "b"]},
            tables(table("a", None, "3"), table("b", None, "3")),
            17,
            None,
        )
        self.assertEqual(answer, "3")
        self.assertEqual(candidates, {"common": "3"})

    def test_answer_provenance_guard_rejects_stale_or_unresolved_values(self):
        base = {"official_answer_verified": True, "variant": "B", "answer": "4", "answer_candidates": {"B": "2"}}
        self.assertFalse(answer_is_mechanically_resolved(base))
        self.assertFalse(answer_is_mechanically_resolved({**base, "answer_candidates": {"A": "4"}}))
        self.assertFalse(answer_is_mechanically_resolved({**base, "answer_candidates": {"B": ["2", "4"]}}))

    def test_answer_provenance_guard_requires_variantless_unique_match(self):
        base = {"official_answer_verified": True, "variant": None, "answer": "3", "answer_candidates": {"common": "3"}}
        self.assertTrue(answer_is_mechanically_resolved(base))
        self.assertFalse(answer_is_mechanically_resolved({**base, "answer": "4"}))
        self.assertFalse(answer_is_mechanically_resolved({**base, "answer_candidates": {"common": "3", "A": "4"}}))


if __name__ == "__main__":
    unittest.main()
