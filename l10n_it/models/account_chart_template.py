# Part of emdad. See LICENSE file for full copyright and licensing details.

from emdad import models


class AccountChartTemplate(models.Model):
    _inherit = 'account.chart.template'

    def _load(self, company):
        """ Set tax calculation rounding method required in Italian localization
        Also to avoid rounding errors when sent with FatturaPA"""
        res = super()._load(company)
        if company.account_fiscal_country_id.code == 'IT':
            company.write({'tax_calculation_rounding_method': 'round_globally'})
        return res
