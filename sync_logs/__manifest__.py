# -*- coding: utf-8 -*-
{
    'name': 'Sync Logs',
    'version': '14.0.1.0',
    'license': 'LGPL-3',
    'category': 'Education',
    "sequence": 3,
    'summary': 'log user activities',
    'complexity': "easy",
    'author': 'karim arafa',
    'depends': ['base','openeducat_parent','openeducat_core'],
    'data': [
        'security/ir.model.access.csv',
        'views/sync_log.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
