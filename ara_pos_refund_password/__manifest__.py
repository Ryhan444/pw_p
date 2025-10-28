# -*- coding: utf-8 -*-
{
    'name': 'Pos Refund Password',
    'version': '18.0.0.0.0',
    'summary': """Pos Restrict Refund Password""",
    'description': """Protection with password for activity refund pos""",
    'category': 'Point of Sale',
    'author': 'ARA SOFT',
    'company': 'ARA SOFT',
    'maintainer': 'ARA SOFT',
    'website': "",
    'depends': ['point_of_sale'],
    'data': [
        'views/pos_config_views.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'ara_pos_refund_password/static/src/js/ticket_screen.js'
        ],
    },
    'images': ['static/description/banner.gif'],
    'license': "OPL-1",
    'installable': True,
    'application': True,
    'auto_install': False,
    'price': 14.28,
    'currency': 'USD',
}
