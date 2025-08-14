from odoo.tests import HttpCase

class TestForm(HttpCase):

    def test_form_submit(self):
        self.start_tour(
            "/contactus",
            "my_tour",
            watch=True
        )
