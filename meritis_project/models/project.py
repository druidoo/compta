# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProjectProject(models.Model):
    _inherit = 'project.project'

    account_manager_id = fields.Many2one('res.users', string='Account manager')
    project_manager_id = fields.Many2one('res.users', string='Project manager')
    type = fields.Selection([('atu', 'ATU'), ('atg', 'ATG'), ('package', 'Package')])