# -*- coding: utf-8 -*-
# from odoo import http


# class Teste(http.Controller):
#     @http.route('/teste/teste', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/teste/teste/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('teste.listing', {
#             'root': '/teste/teste',
#             'objects': http.request.env['teste.teste'].search([]),
#         })

#     @http.route('/teste/teste/objects/<model("teste.teste"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('teste.object', {
#             'object': obj
#         })

