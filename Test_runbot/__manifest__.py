# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Test Runbot',
    'version': '1.0',
    'category': 'Ecuadorian Regulations',
    'description': '''
        Característica: 
            Módulo dummy para probar la funcionalidad basica de runbot.
    ''',
    'author': 'TRESCLOUD CIA LTDA',
    'maintainer': 'TRESCLOUD CIA. LTDA.',
    'website': 'http://www.trescloud.com',
    'license': 'OEEL-1',
    'depends': [
        'base',
        'account',
    ],    
    'data': [
        #Views
        'views/account_invoice_view.xml'
    ],
    'installable': True
}
