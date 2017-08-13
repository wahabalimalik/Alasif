# -*- coding: utf-8 -*-

from odoo import models, fields

class CommissionMoney(models.Model):

	_name = 'comission.money'

	name = fields.Many2one('product.template','Product')
	deduction = fields.Boolean(dafault=False)
	sale_person = fields.Many2one('hr.employee','Sale Person')
	inv_ref = fields.Many2one('account.invoice','Invoice')
	date = fields.Date(related='inv_ref.date_invoice')
	quantity = fields.Integer()
	price_subtotal = fields.Float('Price Subtotal')