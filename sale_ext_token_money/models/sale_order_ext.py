# -*- coding: utf-8 -*-

import logging
from odoo import models, fields, api,_
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)

class SaleOrderExt(models.Model):

	_inherit = 'sale.order'
	sale_person = fields.Many2one('hr.employee','Salesperson', domain=lambda self:[('job_id','=',self.env.ref('sale_ext_token_money.job_title').id)])

	@api.onchange('partner_id')
	def _onchange_partner_id(self):
		return {'domain':{'partner_id':[('company_id','=',self.env.user.company_id.id)]}}

	@api.constrains('sale_person')
	def sale_person_check(self):
		if not self.sale_person:
			raise ValidationError(_('You must have to select Salesman'))

	@api.multi
	def _prepare_invoice(self):
		res = super(SaleOrderExt, self)._prepare_invoice()
		res['sale_person'] = self.sale_person.id
		return res

class SaleOrderLineExt(models.Model):

	_inherit = 'sale.order.line'
	hard_discount = fields.Float()

	@api.model
	def write(self, vals):
		rec = self.env['product.product'].search([('id', '=', self.product_id.id)])
		vals['discount'] = (vals['hard_discount'] *100) / rec.lst_price
		vals['hard_discount'] = 0.0
		return super(SaleOrderLineExt, self).write(vals)

	@api.model
	def create(self, vals):
		rec = self.env['product.product'].search([('id', '=', vals['product_id'])])
		vals['discount'] = (vals['hard_discount'] *100) / rec.lst_price
		vals['hard_discount'] = 0.0
		return super(SaleOrderLineExt, self).create(vals)

	# @api.onchange('product_id')
	# def _onchange_product_id(self):
	# 	return {'domain':{'product_id':[('company_id','=',self.env.user.company_id.id)]}}

	@api.constrains('discount','hard_discount')
	def discount_cal(self):
		if self.discount and self.hard_discount:
			raise ValidationError(_('You can not give percentage and hard discount to one product'))
			
		if self.discount or self.hard_discount:
			if self.discount:
				if not self.product_id.discount:
					raise ValidationError(_('Youu are not allowed to give discount on Product : %s' %(self.product_id.name)))
				else:
					if self.discount > self.product_id.discount_limit_percentage:
						raise ValidationError(_('Youe are not allowed to give discount more then %s percent on Product : %s' %(self.product_id.discount_limit_percentage,self.product_id.name)))

			else:
				if not self.product_id.discount:
					raise ValidationError(_('You are not allowed to give discount on Product : %s' %(self.product_id.name)))
				else:
					pth = (self.product_id.discount_limit_percentage * self.product_id.lst_price) / 100 
					if self.hard_discount > (pth * self.product_uom_qty):
						raise ValidationError(_('You are not allowed to give discount more then %s rupees on Product : %s' %(pth * self.product_uom_qty,self.product_id.name)))


class ResBaseConfigSettings(models.TransientModel):
	_name = "sale.config.settings"
	_inherit = "sale.config.settings"

	@api.model 
	def _write_disc(self):
		_logger.info(">>>> Settings discount parameters to 'Allow discounts on sales order lines'")
		settings = self.env['sale.config.settings'].create({
            'group_discount_per_so_line': 1,
        }).execute()
		_logger.info(">>>> ... done.")