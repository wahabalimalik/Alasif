# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrderExt(models.Model):

	_inherit = 'sale.order'
	sale_person = fields.Many2one('hr.employee','Salesperson', required=True, domain=lambda self:[('job_id','=',self.env.ref('sale_ext_token_money.job_title').id)])

	@api.multi
	def _prepare_invoice(self):
		res = super(SaleOrderExt, self)._prepare_invoice()
		res['sale_person'] = self.sale_person.id
		return res