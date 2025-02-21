# -*- coding: utf-8 -*-

from odoo import api, models, fields


class PosConfig(models.Model):
    """Inherit pos configuration and add new fields."""
    _inherit = 'pos.config'

    refund_security = fields.Integer(string='Refund Security',
                                     help="Refund security password, used for "
                                          "that specified shop")
    @api.model
    def fetch_global_refund_security(self):
        param = self.env['ir.config_parameter'].sudo().get_param('pos_refund_password.global_refund_security')
        return param
