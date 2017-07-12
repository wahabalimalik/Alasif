# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleExt(models.Model):
	_inherit = 'sale.order'

	@api.multi
	def action_confirm(self):
		res = super(SaleExt, self).action_confirm()
		token_money = self.env['token.money']
		wo_token_money = self.env['wo.token.money']
		for rec in self.order_line:
			if rec.product_id.product_tmpl_id.token_check == True:
				token_money.create({
					'name' : rec.product_id.product_tmpl_id.id,
					'so_ref' : self.name,
					'qunatity' : rec.product_uom_qty
				})
			else:
				wo_token_money.create({
					'name' : rec.product_id.product_tmpl_id.id,
					'so_ref' : self.name,
				})
		return res

class TokenMoneyProductExt(models.Model):
    _inherit = 'product.template'

    token_check = fields.Boolean("Token Check")
    token_money = fields.Integer("Token Money")

class TokenMoney(models.Model):
    _name = 'token.money'

    name = fields.Many2one('product.template',)
    so_ref = fields.Char('Sale Order')
    ttl_tok_money = fields.Float('Token Money',compute='_compute_total_money')
    qunatity = fields.Integer()

    @api.depends('name')
    def _compute_total_money(self):
    	for rec in self:
		    if rec.name:
		        rec.ttl_tok_money = rec.name.token_money * rec.qunatity

class WithoutTokenMoney(models.Model):
    _name = 'wo.token.money'

    name = fields.Many2one('product.template')
    so_ref = fields.Char('Sale Order')