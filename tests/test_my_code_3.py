from odoo.tests.common import TransactionCase
from odoo.addons.website.controllers.form import WebsiteForm


class TestWebsiteFormController(TransactionCase):

    # In this test we will check -
    # when a form is submitted a mail record should be created
    def test_mail_record_created_by_form(self):

        # For that we will use WebsiteForm() controller!
        # A request is sent to this controller whenever someone submits a form
        controller = WebsiteForm()
