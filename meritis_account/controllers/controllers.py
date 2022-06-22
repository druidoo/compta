# -*- coding: utf-8 -*-
# from odoo import http


# class MeritisAccount(http.Controller):
#     @http.route('/meritis_account/meritis_account', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/meritis_account/meritis_account/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('meritis_account.listing', {
#             'root': '/meritis_account/meritis_account',
#             'objects': http.request.env['meritis_account.meritis_account'].search([]),
#         })

#     @http.route('/meritis_account/meritis_account/objects/<model("meritis_account.meritis_account"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('meritis_account.object', {
#             'object': obj
#         })
