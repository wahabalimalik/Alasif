# -*- coding: utf-8 -*-
{
    'name': "Token Money Computation",

    'summary': """
        Claculating Sale Orders Regarding Token Money""",
    'description': """
        Claculating Sale Orders Regarding Token Money
    """,
    'author': "Wahab Ali Malik",
    'website': "http://www.glareerp.com",
    'category': 'Sales',
    'version': '0.1',
    'depends': ['sale','hr_payroll'],
    'data': [
        'views/sale_ext_token_money.xml',
        'data/saleman_salary_structure.xml',
    ],
}