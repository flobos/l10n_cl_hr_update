from odoo import models, fields, api

class tramo_hr_contract(models.Model):

    _inherit = 'hr.contract'

    tramo = fields.Selection([
           ('a', "Tramo A"),
           ('b', "Tramo B"),
           ('c', "Tramo C"),
           ('d', "Tramo D"),
           ],required=True, string="Tramo")
    codigo_ips = fields.Char(String="Codigo IPS")

