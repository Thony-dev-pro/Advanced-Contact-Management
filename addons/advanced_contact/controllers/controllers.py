# -*- coding: utf-8 -*-
# from odoo import http


# class AdvancedContact(http.Controller):
#     @http.route('/advanced_contact/advanced_contact', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/advanced_contact/advanced_contact/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('advanced_contact.listing', {
#             'root': '/advanced_contact/advanced_contact',
#             'objects': http.request.env['advanced_contact.advanced_contact'].search([]),
#         })

#     @http.route('/advanced_contact/advanced_contact/objects/<model("advanced_contact.advanced_contact"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('advanced_contact.object', {
#             'object': obj
#         })

