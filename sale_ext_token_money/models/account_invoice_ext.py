# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AccountInvoiceExt(models.Model):

	_inherit = 'account.invoice'
	sale_person = fields.Many2one('hr.employee','Salesperson', required=True, domain=lambda self:[('job_id','=',self.env.ref('sale_ext_token_money.job_title').id)])

	@api.multi
	def action_invoice_open(self):
		res = super(AccountInvoiceExt, self).action_invoice_open()
		self._create_commission_money()
		self._create_token_money()
		return res

	@api.multi
	def _create_commission_money(self):
		for rec in self.invoice_line_ids:
			if rec.product_id.token_check != True:
				self.env['comission.money'].create({
					'name' : rec.product_id.product_tmpl_id.id,
					'deduction': True if self.type == 'out_refund' else False,
					'sale_person' : self.sale_person.id,
					'inv_ref' : self.id,
					'price_subtotal' : rec.price_subtotal,
					'quantity' : rec.quantity
				})

	@api.multi
	def _create_token_money(self):
		for rec in self.invoice_line_ids:
			if rec.product_id.token_check == True:
				self.env['token.money'].create({
					'name' : rec.product_id.product_tmpl_id.id,
					'deduction': True if self.type == 'out_refund' else False,
					'sale_person' : self.sale_person.id,
					'inv_ref' : self.id,
					'ttl_tok_money' : rec.product_id.token_money * rec.quantity,
					'price_subtotal' : rec.price_subtotal,
					'quantity' : rec.quantity
				})
