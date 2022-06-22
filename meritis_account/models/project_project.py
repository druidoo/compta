# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class ProjectProject(models.Model):
    _inherit = 'project.project'
    order_id = fields.Many2one('sale.order')
    order_line = fields.One2many(related="order_id.order_line",  string='Order lines', readonly=False)
    order_state = fields.Selection(related="order_id.state")
    amount = fields.Monetary('Montant', compute="_compute_amount")

    @api.depends('order_line')
    def _compute_amount(self):
        for s in self:
            s.amount = sum(s.order_line.mapped('price_subtotal'))

    @api.model
    def create(self, vals_list):
        project_id = super(ProjectProject, self).create(vals_list)
        sale_order_id = self.env['sale.order'].create({
                                        'name': '%s-%s' % (project_id.name, self.env['ir.sequence'].next_by_code('sale.order', sequence_date=None) or _('New')),
                                        'partner_id': project_id.partner_id.id,
                                       'analytic_account_id': project_id.analytic_account_id.id})
        project_id.write({'order_id': sale_order_id.id})
        return project_id

    def confirm_sale_line(self):
        self.order_id.action_confirm()
