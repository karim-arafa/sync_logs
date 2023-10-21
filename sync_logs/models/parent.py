# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import datetime


class OpParent(models.Model):
    _inherit = "op.parent"
    
    
    @api.model
    def create(self, vals):
        # OVERRIDE
        res = super(OpParent, self).create(vals)

        # Create log
        self.env['sync.log'].create({
            'user_id': self.env.user.id,
            'time_stamp': datetime.now(),
            'model': 'op.parent',
            'action_type': 'create'
        })

        return res
    
    def write(self, vals):
        # OVERRIDE
        res = super(OpParent, self).write(vals)
        # Create log
        self.env['sync.log'].create({
            'user_id': self.env.user.id,
            'time_stamp': datetime.now(),
            'model': 'op.parent',
            'action_type': 'edit'
        })
        
        return res
    
    def unlink(self):
        # OVERRIDE
        res = super(OpParent, self).unlink()
        # Create log
        self.env['sync.log'].create({
            'user_id': self.env.user.id,
            'time_stamp': datetime.now(),
            'model': 'op.parent',
            'action_type': 'delete'
        })
        return res
    
    