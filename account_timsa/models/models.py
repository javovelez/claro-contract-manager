# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class /home/javo/odoo13/cusmod13/timsa_customization/account_timsa/(models.Model):
#     _name = '/home/javo/odoo13/cusmod13/timsa_customization/account_timsa/./home/javo/odoo13/cusmod13/timsa_customization/account_timsa/'
#     _description = '/home/javo/odoo13/cusmod13/timsa_customization/account_timsa/./home/javo/odoo13/cusmod13/timsa_customization/account_timsa/'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
