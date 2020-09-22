# -*- coding: utf-8 -*-
# from odoo import http


# class /home/javo/odoo13/cusmod13/timsaCustomization/purchaseTimsa/(http.Controller):
#     @http.route('//home/javo/odoo13/cusmod13/timsa_customization/purchase_timsa///home/javo/odoo13/cusmod13/timsa_customization/purchase_timsa//', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//home/javo/odoo13/cusmod13/timsa_customization/purchase_timsa///home/javo/odoo13/cusmod13/timsa_customization/purchase_timsa//objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/home/javo/odoo13/cusmod13/timsa_customization/purchase_timsa/.listing', {
#             'root': '//home/javo/odoo13/cusmod13/timsa_customization/purchase_timsa///home/javo/odoo13/cusmod13/timsa_customization/purchase_timsa/',
#             'objects': http.request.env['/home/javo/odoo13/cusmod13/timsa_customization/purchase_timsa/./home/javo/odoo13/cusmod13/timsa_customization/purchase_timsa/'].search([]),
#         })

#     @http.route('//home/javo/odoo13/cusmod13/timsa_customization/purchase_timsa///home/javo/odoo13/cusmod13/timsa_customization/purchase_timsa//objects/<model("/home/javo/odoo13/cusmod13/timsa_customization/purchase_timsa/./home/javo/odoo13/cusmod13/timsa_customization/purchase_timsa/"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/home/javo/odoo13/cusmod13/timsa_customization/purchase_timsa/.object', {
#             'object': obj
#         })
