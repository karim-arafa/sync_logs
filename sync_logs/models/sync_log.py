# -*- coding: utf-8 -*-
import datetime

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class SyncLog(models.Model):
    _name = "sync.log"
    _description = "Logs"
    
    
    user_id = fields.Many2one('res.users', string='user')
    model = fields.Char('model')
    time_stamp = fields.Datetime('Time Stamp')
    action_type = fields.Selection([
        ('create', 'Create'),
        ('edit','Edit'),
        ('delete', 'Delete')
    ], string='Action Type', required=True)
    
    action = fields.Char(string='Action', compute='_compute_action', store=True)

    @api.depends('action_type')
    def _compute_action(self):
        for record in self:
            if record.action_type == 'create':
                record.action = 'NEW'
            else:
                record.action = 'REFORM'
            
    