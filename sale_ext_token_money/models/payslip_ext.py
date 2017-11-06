# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PayslipExt(models.Model):
	_inherit = 'hr.payslip'

	advance = fields.Integer()
	adv = fields.Boolean(default=False)
