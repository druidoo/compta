# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class ProjectProject(models.Model):
    _inherit = 'project.project'

    invoiced_analytics_amount = fields.Monetary(compute='compute_analytic_amount', string='Invoiced analytics')
    uninvoiced_analytics_amount = fields.Monetary(compute='compute_analytic_amount', string='Uninvoiced analytics')

    @api.depends('analytic_account_id')
    def compute_analytic_amount(self):
        AnalyticLine = self.env['account.analytic.line']
        invoiced = AnalyticLine.read_group([('timesheet_invoice_id', '!=', False), ('account_id', '=',
                                                                                    self.analytic_account_id.id)],
                                           ['account_id',
                                            'amount'],
                                           ['account_id'])
        uninvoiced = AnalyticLine.read_group([('timesheet_invoice_id', '=', False), ('account_id', '=',
                                                                                     self.analytic_account_id.id),
                                              ('move_id', '=', False)],
                                             ['account_id',
                                              'amount'],
                                             ['account_id'])
        self.invoiced_analytics_amount = invoiced[0]['amount'] if invoiced else 0.0
        self.uninvoiced_analytics_amount = uninvoiced[0]['amount'] if uninvoiced else 0.0

    def action_open_invoiced_analytic(self):
        self.ensure_one()
        action = self.action_view_analytic_account_entries()
        action['name'] = _('Invoiced')
        action['domain'] = [('account_id', '=', self.analytic_account_id.id), ('timesheet_invoice_id', '!=', False)]
        return action

    def action_open_uninvoiced_analytic(self):
        self.ensure_one()
        action = self.action_view_analytic_account_entries()
        action['name'] = _('Uninvoiced')
        action['domain'] = [('account_id', '=', self.analytic_account_id.id), ('timesheet_invoice_id', '=', False),
                            ('move_id', '=', False)]
        return action
