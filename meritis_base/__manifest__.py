# -*- coding: utf-8 -*-
{
    'name': "Meritis Base",

    'summary': """
        All Meritis' module depend on this module""",

    'description': """
        
    """,

    'author': "Arkeup",
    'website': "https://www.arkeup.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
}
