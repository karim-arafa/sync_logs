# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import datetime

class OpStudent(models.Model):
    _inherit = "op.student"
    
    
    @api.model
    def create(self, vals):
        # OVERRIDE
        res = super(OpStudent, self).create(vals)

        # Create log
        self.env['sync.log'].create({
            'user_id': self.env.user.id,
            'time_stamp': datetime.now(),
            'model': 'op.student',
            'action_type': 'create'
        })

        return res
    
    def write(self, vals):
        # OVERRIDE
        res = super(OpStudent, self).write(vals)
        # Create log
        self.env['sync.log'].create({
            'user_id': self.env.user.id,
            'time_stamp': datetime.now(),
            'model': 'op.student',
            'action_type': 'edit'
        })
        
        return res
    
    def unlink(self):
        # OVERRIDE
        res = super(OpStudent, self).unlink()
        # Create log
        self.env['sync.log'].create({
            'user_id': self.env.user.id,
            'time_stamp': datetime.now(),
            'model': 'op.student',
            'action_type': 'delete'
        })
        return res