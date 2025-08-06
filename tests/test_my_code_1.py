from odoo.tests.common import TransactionCase


class TestWebsiteFormController(TransactionCase):

    # In this test we will check -
    # when a form is submitted a mail record should be created
    def test_mail_record_created_by_form(self):

        # But how do we simulate form submit from this backend test??
