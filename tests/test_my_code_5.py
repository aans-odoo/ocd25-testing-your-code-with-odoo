from odoo.tests.common import TransactionCase
from odoo.addons.website.controllers.form import WebsiteForm
from odoo.addons.http_routing.tests.common import MockRequest
from odoo.http import request


class TestWebsiteFormController(TransactionCase):

    # In this test we will check -
    # when a form is submitted a mail record should be created
    def test_mail_record_created_by_form(self):
        
        # Simulate a form submission
        controller = WebsiteForm()
        website = self.env['website'].browse(1)
        mail_model = self.env['ir.model']._get('mail.mail')
        with MockRequest(self.env, website=website):
            controller.insert_record(
                request,
                mail_model,
                {
                    'email_from': 'test@example.com',
                    'subject': 'Test subject',
                    'email_to': 'receiver@example.com',
                },
                'Hello',
            )

        # Time to assert ?
