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
        'data/saleman_salary_structure_data.xml',
        'data/saleman_job_title_data.xml',
        'views/account_invoice_ext.xml',
        'views/commission_money.xml',
        'views/product_ext.xml',
        'views/sale_order_ext.xml',
        'views/token_money.xml'
    ],
    'demo': [
        'data/hr_salesman_demo.xml'
    ],

    'auto_install': True,
}