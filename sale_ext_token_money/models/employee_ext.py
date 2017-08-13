# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EmplyeeExt(models.Model):
	_inherit = 'hr.employee'

	@api.multi
	def _all_token_money(self,date_from,date_to):
		record = self.env['token.money'].search([
			('sale_person','=',self.name),
			('deduction','!=',True),
			('date','>=',date_from),
			('date','<=',date_to)
			])
		return sum(rec.ttl_tok_money for rec in record)

	@api.multi
	def _all_sale_commission(self,date_from,date_to):
		record = self.env['comission.money'].search([
			('sale_person','=',self.name),
			('deduction','!=',True),
			('date','>=',date_from),
			('date','<=',date_to)
			])
		return ((sum(rec.price_subtotal for rec in record)) / 100) * 1

	@api.multi
	def _all_token_money_ded(self,date_from,date_to):
		record = self.env['token.money'].search([
			('sale_person','=',self.name),
			('deduction','=',True),
			('date','>=',date_from),
			('date','<=',date_to)
			])
		return -(sum(rec.ttl_tok_money for rec in record))

	@api.multi
	def _all_sale_commission_ded(self,date_from,date_to):
		record = self.env['comission.money'].search([
			('sale_person','=',self.name),
			('deduction','=',True),
			('date','>=',date_from),
			('date','<=',date_to)
			])
		return ((sum(rec.price_subtotal for rec in record)) / 100) * -1