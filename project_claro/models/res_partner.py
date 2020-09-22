# -*- coding: utf-8 -*-

from odoo import models, fields

class ResPartner(models.Model):
    """ Inherits partner and adds Tasks information in the partner form """
    _inherit = 'res.partner'
    
    es_subcontratista = fields.Boolean(
        string='Es subcontratista?',
    )
    
    es_supervisor_Claro = fields.Boolean(
        string='Es supervisor de Claro?',
    )
    