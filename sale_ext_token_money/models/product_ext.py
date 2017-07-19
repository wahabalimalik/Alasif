# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductTemplateExt(models.Model):
	_inherit = 'product.template'

	token_check = fields.Boolean("Token Check")
	token_money = fields.Integer("Token Money")