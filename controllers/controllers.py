# -*- coding: utf-8 -*-
# from odoo import http


# class Cusmod13/claro-contract-manager/(http.Controller):
#     @http.route('/cusmod13/claro-contract-manager//cusmod13/claro-contract-manager//', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cusmod13/claro-contract-manager//cusmod13/claro-contract-manager//objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cusmod13/claro-contract-manager/.listing', {
#             'root': '/cusmod13/claro-contract-manager//cusmod13/claro-contract-manager/',
#             'objects': http.request.env['cusmod13/claro-contract-manager/.cusmod13/claro-contract-manager/'].search([]),
#         })

#     @http.route('/cusmod13/claro-contract-manager//cusmod13/claro-contract-manager//objects/<model("cusmod13/claro-contract-manager/.cusmod13/claro-contract-manager/"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cusmod13/claro-contract-manager/.object', {
#             'object': obj
#         })
