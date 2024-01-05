# -*- coding: utf-8 -*-
# Part of emdad. See LICENSE file for full copyright and licensing details.

{
    'name': "Sale Product Configurators Tests",
    'summary': "Test Suite for Sale Product Configurator",
    'category': "Hidden",
    'depends': [
        'event_sale',
        'sale_management',
        'sale_product_configurator',
        'sale_product_matrix',
    ],
    'assets': {
        'web.assets_tests': [
            'test_sale_product_configurators/static/src/js/tour_utils.js',
            'test_sale_product_configurators/static/tests/tours/**/*',
        ],
    },
    'license': 'LGPL-3',
}
