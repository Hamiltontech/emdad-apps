# -*- coding: utf-8 -*-

import emdad

def migrate(cr, version):
    registry = emdad.registry(cr.dbname)
    from emdad.addons.account.models.chart_template import migrate_set_tags_and_taxes_updatable
    migrate_set_tags_and_taxes_updatable(cr, registry, 'l10n_in')
