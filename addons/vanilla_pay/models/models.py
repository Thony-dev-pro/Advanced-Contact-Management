# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class vanilla_pay(models.Model):
#     _name = 'vanilla_pay.vanilla_pay'
#     _description = 'vanilla_pay.vanilla_pay'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

