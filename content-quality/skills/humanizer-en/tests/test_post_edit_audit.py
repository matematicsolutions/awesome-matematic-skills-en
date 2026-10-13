"""Tests for the post-edit audit gate (stdlib unittest).

Run from the skill directory:  python -m unittest discover -s tests -v
Synthetic cases written for the phenomenon (lost date, changed force of a norm), not for a regex.
"""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "post_edit_audit.py"
sys.path.insert(0, str(SCRIPT.parent))

import post_edit_audit as A  # noqa: E402

TEXT = (
    "The deadline for filing objections is 15 March 2026. The client will pay GBP 12,500 in fees, "
    "and the Tenant may terminate the lease on 30 days' notice. "
    "Basis: Article 6(1)(f) GDPR and the ruling in Case C-311/18."
)


def check(result, name):
    return next(k for k in result["checks"] if k["name"] == name)


class Input(unittest.TestCase):
    def test_identical_text_is_ok_and_no_change_is_a_result(self):
        r = A.audit(TEXT, TEXT)
        self.assertEqual(r["status"], "OK")
        self.assertTrue(r["unchanged"])

    def test_empty_output_blocks(self):
        self.assertEqual(A.audit(TEXT, "  \n")["status"], "BLOCK")

    def test_empty_original_blocks(self):
        self.assertEqual(A.audit("", TEXT)["status"], "BLOCK")

    def test_full_denominator_even_when_ok(self):
        r = A.audit(TEXT, TEXT)
        self.assertEqual({k["name"] for k in r["checks"]}, set(A.CHECKS))
        self.assertTrue(all(k["status"] == "OK" for k in r["checks"]))


class SensitiveValues(unittest.TestCase):
    def test_lost_date_blocks(self):
        out = TEXT.replace("15 March 2026", "mid-March")
        self.assertEqual(check(A.audit(TEXT, out), "sensitive_values")["status"], "BLOCK")

    def test_reformatted_date_passes(self):
        out = TEXT.replace("15 March 2026", "March 15, 2026")
        self.assertEqual(check(A.audit(TEXT, out), "sensitive_values")["status"], "OK")

    def test_changed_amount_blocks(self):
        out = TEXT.replace("GBP 12,500", "GBP 12,000")
        self.assertEqual(check(A.audit(TEXT, out), "sensitive_values")["status"], "BLOCK")

    def test_invented_number_blocks(self):
        out = TEXT + " This cuts the process by 30%."
        self.assertEqual(check(A.audit(TEXT, out), "sensitive_values")["status"], "BLOCK")

    def test_lost_provision_blocks(self):
        out = TEXT.replace("Article 6(1)(f) GDPR", "the GDPR")
        self.assertEqual(check(A.audit(TEXT, out), "sensitive_values")["status"], "BLOCK")

    def test_changed_case_number_blocks(self):
        out = TEXT.replace("C-311/18", "C-311/19")
        self.assertEqual(check(A.audit(TEXT, out), "sensitive_values")["status"], "BLOCK")

    def test_changed_quotation_blocks(self):
        before = 'The court held that "the contract expired by operation of law" and dismissed the claim.'
        after = 'The court held that "the contract expired" and dismissed the claim.'
        self.assertEqual(check(A.audit(before, after), "sensitive_values")["status"], "BLOCK")

    def test_quote_style_change_passes(self):
        before = 'The court held that "the contract expired by operation of law" and dismissed the claim.'
        after = "The court held that “the contract expired by operation of law” and dismissed the claim."
        self.assertEqual(check(A.audit(before, after), "sensitive_values")["status"], "OK")

    def test_placeholder_replaced_with_invented_value_blocks(self):
        before = "The deposit is [amount], payable by the end of the month."
        after = "The deposit is GBP 2,000, payable by the end of the month."
        self.assertEqual(check(A.audit(before, after), "sensitive_values")["status"], "BLOCK")


class DeonticProfile(unittest.TestCase):
    def test_may_to_must_blocks(self):
        out = TEXT.replace("may terminate", "must terminate")
        self.assertEqual(check(A.audit(TEXT, out), "deontic_profile")["status"], "BLOCK")

    def test_prohibition_to_permission_blocks(self):
        before = "The Supplier must not subcontract the Services without consent."
        after = "The Supplier may subcontract the Services without consent."
        self.assertEqual(check(A.audit(before, after), "deontic_profile")["status"], "BLOCK")

    def test_need_not_counts_as_permission(self):
        p = A.deontic_profile("The client need not sign the addendum.")
        self.assertEqual(p["permission"], 1)
        self.assertEqual(p["obligation"], 0)

    def test_discourse_frame_is_not_a_norm(self):
        p = A.deontic_profile("It should be noted that the deadline passed. It must be said that one thing matters.")
        self.assertEqual(sum(p.values()), 0)

    def test_removing_discourse_frame_passes(self):
        before = "It is worth noting that the client must file the application on time."
        after = "The client must file the application on time."
        self.assertEqual(check(A.audit(before, after), "deontic_profile")["status"], "OK")

    def test_might_to_may_is_the_same_modal_of_possibility(self):
        before = "The tools might help some teams."
        after = "The tools may help some teams."
        self.assertEqual(check(A.audit(before, after), "deontic_profile")["status"], "OK")

    def test_equivalent_obligation_passes(self):
        before = "The Tenant must return the keys on the handover date."
        after = "The Tenant is required to return the keys on the handover date."
        self.assertEqual(check(A.audit(before, after), "deontic_profile")["status"], "OK")

    def test_removing_chat_wrapper_with_you_can_passes(self):
        before = ("Here's a draft letter. The Tenant must not sublet the premises. "
                  "You can adjust the tone for the recipient. I can also prepare a shorter version.")
        after = "The Tenant must not sublet the premises."
        self.assertEqual(check(A.audit(before, after), "deontic_profile")["status"], "OK")

    def test_wrapper_does_not_mask_norm_change_in_body(self):
        before = "The Tenant may sublet the premises. You can adjust the tone for the recipient."
        after = "The Tenant must sublet the premises."
        self.assertEqual(check(A.audit(before, after), "deontic_profile")["status"], "BLOCK")


class Certainty(unittest.TestCase):
    def test_removed_uncertainty_blocks(self):
        self.assertEqual(check(A.audit("The court will likely rule in March.", "The court will rule in March."),
                               "certainty")["status"], "BLOCK")

    def test_thinning_stacked_hedges_passes(self):
        before = "It could potentially possibly be argued that the policy might have some effect on outcomes."
        after = "The policy may affect outcomes."
        self.assertEqual(check(A.audit(before, after), "certainty")["status"], "OK")

    def test_added_uncertainty_is_a_warning(self):
        self.assertEqual(check(A.audit("The court will rule in March.", "The court will likely rule in March."),
                               "certainty")["status"], "WARN")


class ToolTraces(unittest.TestCase):
    def test_unfilled_placeholder_blocks_readiness(self):
        before = "The deposit is [amount], payable by the end of the month."
        r = A.audit(before, before)
        self.assertEqual(check(r, "tool_traces")["status"], "BLOCK")
        self.assertEqual(check(r, "sensitive_values")["status"], "OK")

    def test_to_be_completed_marker_blocks_readiness_but_is_not_an_invented_value(self):
        before = "Adoption has grown across the industry."
        after = "Adoption has grown [to be completed: source for the claim that adoption has grown across the industry]."
        r = A.audit(before, after)
        self.assertEqual(check(r, "tool_traces")["status"], "BLOCK")
        self.assertEqual(check(r, "sensitive_values")["status"], "OK")

    def test_chatbot_closer_blocks(self):
        self.assertEqual(check(A.audit(TEXT, TEXT + " I hope this helps!"), "tool_traces")["status"], "BLOCK")

    def test_heres_opener_blocks(self):
        self.assertEqual(check(A.audit(TEXT, "Here's the revised version: " + TEXT), "tool_traces")["status"],
                         "BLOCK")

    def test_assistant_offer_blocks(self):
        out = TEXT + " You can adjust the tone for the recipient."
        self.assertEqual(check(A.audit(TEXT, out), "tool_traces")["status"], "BLOCK")

    def test_email_sign_off_is_not_a_chat_trace(self):
        t = "Please find the draft resolution attached. Happy to discuss any questions."
        self.assertEqual(check(A.audit(t, t), "tool_traces")["status"], "OK")


class ProtectedTerms(unittest.TestCase):
    def test_deposit_to_advance_payment_blocks(self):
        before = "The buyer paid a deposit in the amount set out in the preliminary agreement."
        after = "The buyer paid an advance payment in the amount set out in the preliminary agreement."
        self.assertEqual(check(A.audit(before, after), "protected_terms")["status"], "BLOCK")

    def test_replaced_defined_term_blocks(self):
        before = ('Acme Ltd (the "Customer") orders the work. '
                  "The Customer accepts the Deliverables within 7 days.")
        after = "Acme Ltd orders the work. The client accepts the Deliverables within 7 days."
        self.assertEqual(check(A.audit(before, after), "protected_terms")["status"], "BLOCK")

    def test_fewer_uses_of_defined_term_is_a_warning(self):
        before = ('Acme Ltd (the "Customer") orders the work. '
                  "The Customer accepts the Deliverables. The Customer pays within 7 days.")
        after = ('Acme Ltd (the "Customer") orders the work. '
                 "The Customer accepts the Deliverables and pays within 7 days.")
        r = A.audit(before, after)
        self.assertEqual(check(r, "protected_terms")["status"], "WARN")
        self.assertEqual(r["status"], "WARN")

    def test_term_from_parameter_is_protected_verbatim(self):
        before = "We use the Fast Track procedure for urgent matters."
        after = "We use a quick procedure for urgent matters."
        r = A.audit(before, after, protected=["Fast Track"])
        self.assertEqual(check(r, "protected_terms")["status"], "BLOCK")

    def test_dropping_an_everyday_use_of_a_listed_word_is_only_a_warning(self):
        before = "The tools show the interplay between automation and human judgment. We guarantee fast delivery."
        after = "The tools combine automation with human review. Delivery is fast."
        self.assertEqual(check(A.audit(before, after), "protected_terms")["status"], "WARN")

    def test_new_listed_term_appearing_still_blocks(self):
        before = "The Supplier gives a warranty for twelve months."
        after = "The Supplier gives a guarantee for twelve months."
        self.assertEqual(check(A.audit(before, after), "protected_terms")["status"], "BLOCK")

    def test_removing_wrapper_does_not_change_term_counts(self):
        before = "Here's a draft appeal. The appeal concerns the whole judgment. I can also prepare a shorter appeal."
        after = "The appeal concerns the whole judgment."
        self.assertEqual(check(A.audit(before, after), "protected_terms")["status"], "OK")


class ShorteningLimit(unittest.TestCase):
    BEFORE = " ".join(f"word{i}" for i in range(100))

    def test_cut_over_limit_blocks(self):
        out = " ".join(f"word{i}" for i in range(50))
        self.assertEqual(check(A.audit(self.BEFORE, out), "shortening_limit")["status"], "BLOCK")

    def test_cut_within_limit_passes(self):
        out = " ".join(f"word{i}" for i in range(80))
        self.assertEqual(check(A.audit(self.BEFORE, out), "shortening_limit")["status"], "OK")

    def test_short_text_over_limit_is_a_warning(self):
        before = "It is worth noting that in today's world the firm should adopt a comprehensive solution."
        after = "The firm should adopt this solution."
        self.assertEqual(check(A.audit(before, after), "shortening_limit")["status"], "WARN")

    def test_limit_is_a_parameter(self):
        out = " ".join(f"word{i}" for i in range(50))
        self.assertEqual(check(A.audit(self.BEFORE, out, max_cut=0.6), "shortening_limit")["status"], "OK")


class FoundInMeasurement(unittest.TestCase):
    """False alarms found on the blind set (2026-10-13), rebuilt here as synthetic cases."""

    def test_abbreviation_inside_a_word_is_not_a_provision(self):
        before = "We received the items. 5 of them were damaged."
        after = "We received the items; 5 of them were damaged."
        self.assertEqual(check(A.audit(before, after), "sensitive_values")["status"], "OK")

    def test_neutral_citation_is_not_a_field_to_fill_in(self):
        t = "The court followed [2026] EWHC 1432 (Comm) and footnote [1] explains why."
        self.assertEqual(check(A.audit(t, t), "tool_traces")["status"], "OK")

    def test_removing_the_chat_wrapper_does_not_count_against_the_cut_limit(self):
        body = ("The Supplier must deliver the Goods to the Customer's warehouse within 14 days of the order. "
                "Late delivery entitles the Customer to liquidated damages of 0.5% of the price per week. "
                "The Customer may reject Goods that do not match the specification within 7 days of delivery.")
        wrapper_open = "Here's a clear and professional version of the clause you asked me to tidy up for the contract."
        wrapper_close = ("I hope this helps with your negotiation! Let me know if you'd like me to adjust the tone. "
                         "I can also prepare a shorter version for the summary sheet.")
        r = A.audit(f"{wrapper_open} {body} {wrapper_close}", body)
        self.assertEqual(check(r, "shortening_limit")["status"], "OK")


class Cli(unittest.TestCase):
    def run_cli(self, before, after, *args):
        with tempfile.TemporaryDirectory() as d:
            a, b = Path(d, "before.txt"), Path(d, "after.txt")
            a.write_text(before, encoding="utf-8")
            b.write_text(after, encoding="utf-8")
            return subprocess.run([sys.executable, str(SCRIPT), str(a), str(b), *args],
                                  capture_output=True, text=True, encoding="utf-8")

    def test_exit_0_when_ok(self):
        r = self.run_cli(TEXT, TEXT)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("POST-EDIT AUDIT: OK", r.stdout)  # exit 0 alone proves nothing

    def test_exit_20_when_blocked(self):
        r = self.run_cli(TEXT, TEXT.replace("GBP 12,500", "GBP 12,000"))
        self.assertEqual(r.returncode, 20, r.stdout + r.stderr)
        self.assertIn("BLOCK", r.stdout)

    def test_exit_2_on_bad_call(self):
        self.assertEqual(subprocess.run([sys.executable, str(SCRIPT)], capture_output=True, text=True).returncode, 2)


if __name__ == "__main__":
    unittest.main()
