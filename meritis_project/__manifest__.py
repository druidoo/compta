# -*- coding: utf-8 -*-
{
    'name': "Meritis Project",

    'summary': """
        This module add more features for project module""",

    'description': """

    """,

    'author': "Arkeup",
    'website': "https://www.arkeup.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Project',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['project', 'meritis_base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/project_views.xml',
    ],
}
