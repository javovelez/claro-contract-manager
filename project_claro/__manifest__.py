# -*- coding: utf-8 -*-
{
    'name': "Timsa Customization",

    'summary': """
        Customización para Timsa""",

    'description': """
    """,

    'author': "javo",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '13.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','project','account','sales','purchase','stock','hr_expense'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    """"
    'demo': [
        
    ],""""
}
