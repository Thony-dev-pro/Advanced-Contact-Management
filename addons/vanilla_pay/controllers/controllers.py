# -*- coding: utf-8 -*-
# from odoo import http


# class VanillaPay(http.Controller):
#     @http.route('/vanilla_pay/vanilla_pay', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vanilla_pay/vanilla_pay/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('vanilla_pay.listing', {
#             'root': '/vanilla_pay/vanilla_pay',
#             'objects': http.request.env['vanilla_pay.vanilla_pay'].search([]),
#         })

#     @http.route('/vanilla_pay/vanilla_pay/objects/<model("vanilla_pay.vanilla_pay"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vanilla_pay.object', {
#             'object': obj
#         })

