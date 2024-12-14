# -*- coding: utf-8 -*-
{
    'name': "SD Colors",

    'summary': """
        """,

    'description': """
        
    """,

    'author': "Arash Homayounfar",
    'website': "https://giladoo.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Service Desk/Service Desk',
    'application': False,
    'version': '18.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web', ],

    # always loaded
    'data': [
    ],
    'assets': {
        'web.assets_backend': [
            'sd_colors/static/src/css/styles.scss',
        ],
    },


    'license': 'LGPL-3',

}
