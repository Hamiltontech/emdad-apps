# Part of emdad. See LICENSE file for full copyright and licensing details.
{
    'name': 'Taiwan - Accounting',
    'website': 'https://www.emdad.com/documentation/17.0/applications/finance/fiscal_localizations.html',
    'icon': '/account/static/description/l10n.png',
    'countries': ['tw'],
    'author': 'emdad PS',
    'version': '1.0',
    'category': 'Accounting/Localizations/Account Charts',
    'description': """
This is the base module to manage the accounting chart for Taiwan in emdad.
==============================================================================
    """,
    'depends': [
        'account',
        'base_address_extended',
    ],
    'data': [
        'data/res.country.state.csv',
        'data/res_currency_data.xml',
        'data/res_country_data.xml',
        'data/res.city.csv',
    ],
    'demo': [
        'demo/demo_company.xml',
    ],
    'license': 'LGPL-3',
}
