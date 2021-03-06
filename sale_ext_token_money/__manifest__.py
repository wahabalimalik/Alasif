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
    'depends': ['account_accountant','sale','hr_payroll'],
    'demo': [
        'data/hr_salesman_demo.xml'
    ],
    'data': [
	'security/sale_ext_token_money_security.xml',
	'security/ir.model.access.csv',
        'data/saleman_salary_structure_data.xml',
        'data/saleman_job_title_data.xml',
        'data/sale_config_setting.xml',
        'views/sale_order_ext.xml',
        'views/account_invoice_ext.xml',
        'views/commission_money.xml',
        'views/product_ext.xml',
        'views/token_money.xml'
    ],

    'auto_install': True,
}
