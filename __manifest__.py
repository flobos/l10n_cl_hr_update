# -*- coding: utf-8 -*-
{
    'name': "l10n_cl_hr_update",

    'summary': """
        Modifica opciones en payroll chile (l10n_cl_hr)""",

    'description': """
        Modifica opciones en payroll chile (l10n_cl_hr)
    """,

    'author': "Fimar",
    'website': "http://www.fimarcorp.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hr_payroll','hr_contract','hr_holidays'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}