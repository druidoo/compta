# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class ProjectEmployeeCond(models.Model):
    _name = 'project.employee_cond.line'

    project_id = fields.Many2one('project.project')
    employee_id = fields.Many2one('hr.employee')
    type = fields.Selection([('JF', 'JF'), ('Astreinte', 'Astreinte')])
    currency_id = fields.Many2one('res.currency', related='employee_id.currency_id')
    amount = fields.Monetary('Montant', currency_field='currency_id')


class ProjectProject(models.Model):
    _inherit = 'project.sale.line.employee.map'

    currency_id = fields.Many2one('res.currency', related='employee_id.currency_id')
    re_invoice_amount = fields.Monetary('Refacturation', currency_field='currency_id')


class ProjectProject(models.Model):
    _inherit = 'project.project'

    order_id = fields.Many2one('sale.order')
    order_line = fields.One2many(related="order_id.order_line",  string='Order lines', readonly=False)
    order_state = fields.Selection(related="order_id.state")
    amount = fields.Monetary('Montant', compute="_compute_amount")
    employee_condition = fields.One2many('project.employee_cond.line', 'project_id')

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

    def write(self, vals):
        res = super(ProjectProject, self).write(vals)
        if vals.get('order_line') and self.order_id:
            self.order_id.action_confirm()
        return res


    def action_view_project(self):
        view_id = self.env.ref('project.edit_project').id
        return {
            'res_id': self.id,
            'res_model': self._name,
            'type': 'ir.actions.act_window',
            'views': [[view_id, 'form']],
        }