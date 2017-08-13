# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import UserError, ValidationError

class ProductTemplateExt(models.Model):
	_inherit = 'product.template'

	token_check = fields.Boolean("Token Check")
	token_money = fields.Integer("Token Money")

	origin_code = fields.Char("Origin Code")

	discount = fields.Boolean()
	discount_limit_percentage = fields.Float("Discount Limit")

	@api.constrains('discount_limit_percentage')
	def disc_limit_check(self):
		if self.discount_limit_percentage > 100:
			raise ValidationError(_('Are you insane,How much Discount you want to give...?'))