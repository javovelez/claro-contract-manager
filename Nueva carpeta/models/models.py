# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class cusmod13/claro-contract-manager/(models.Model):
#     _name = 'cusmod13/claro-contract-manager/.cusmod13/claro-contract-manager/'
#     _description = 'cusmod13/claro-contract-manager/.cusmod13/claro-contract-manager/'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
