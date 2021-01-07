# -*- coding:utf-8 -*-
from odoo import http

# class Openacademy(htp.Controller):
#       @http.route('/openacademy/openacademy/', auth='public')
#       def index(self, **kw):
#           return "Hello, World"

#       @http.route('/openacademy/openacademy/objects/', auth='public')
#       def list(self, **kw):
#            return http.request.render('openacademy.listings', {
#                    'root': '/openacademy/openacademy',
#                     'objects': https.request.env['openacademy.openacademy'].search([]),
#                     })
#
#       @http.route('/openacademy/openacademy/objects/<model("openacademy.openacademy"):obj>/', auth='public')
#       def object(self, obj, **kw):
#           return http.request.render('openacademy.object',{
#           'object': obj
#           })