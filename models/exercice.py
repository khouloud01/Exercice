# -*- coding: utf-8 -*-
from odoo import api, models, fields,_
from odoo.tools import float_compare, pycompat


class sale_order(models.Model):
    _inherit = 'sale.order'
    exercice = fields.Text(string="Exercice", translate=True)
    image = fields.Binary(attachment=True, string="Image")
