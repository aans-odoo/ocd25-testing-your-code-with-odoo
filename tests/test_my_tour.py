from odoo.tests import tagged, HttpCase

class TestForm(HttpCase):

    def test_form_submit(self):
        self.start_tour(
            "/contactus",
            "my_tour",
        )
