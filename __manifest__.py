{
    'name': 'Test Driven Development (TDD)',
    'summary': 'A simple module having different type of tests cases to showcase types of tests in Odoo',
    'version': '1.0',
    'category': 'Session',
    'author': 'Arib Ansari',
    'depends': ['website'],
    'assets': {
        'web.assets_unit_tests': [
            'test_your_code/static/tests/my_hoot.test.js',
        ],
        'web.assets_tests': [
            'test_your_code/static/tests/tours/my_tour.js',
        ],
    },
    'installable': True,
    'application': False,
    'license': 'AGPL-3'
}