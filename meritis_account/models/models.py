# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProjectProject(models.Model):
    _inherit = 'project.project'
    order_id = fields.Many2one('sale.order')
    order_line = fields.One2many(related="order_id.order_line",  string='Order lines', readonly=False)

    @api.model
    def create(self, vals_list):
        project_id = super(ProjectProject, self).create(vals_list)
        sale_order_id = self.env['sale.order'].create({'partner_id' : project_id.partner_id.id,
                                       'analytic_account_id': project_id.analytic_account_id.id})
        project_id.write({'order_id': sale_order_id.id})
        return project_id
