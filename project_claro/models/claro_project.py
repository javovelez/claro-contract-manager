#-*- coding: utf-8 -*-

from datetime import timedelta

from odoo import api, fields, models

class Project(models.Model):
    _name = 'claro.project'
    _inherit = ['project.project']
    
class ProjectTaskType():
    _name='claro.stage'
    
 
class Task(models.Model):
    _inherit = ['project.task']
    _name = 'claro.project.task'
    gerencia_claro = fields.Char(string='Gerencia Claro',help='Gerencia a la cual se certificará la tarea')
    supervisor_ids = fields.Many2many(string='Supervisor Claro',comodel_name='res.partner')
    ticket = fields.Char(string='Ticket')
    UT =fields.Char(help='Ubicación técnica',string='UT')    
    sytex = fields.Char(string='Sytex',help='link a formulario Sytex')   
    ejecutor_id_ids = fields.Many2many('res.partner', string='Ejecutores')