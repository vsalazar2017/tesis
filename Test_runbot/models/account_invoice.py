# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'
    
 
    #Columns
    check = fields.Boolean(
        string='check', 
        readonly=True,
        default=True,
        help='',
        )