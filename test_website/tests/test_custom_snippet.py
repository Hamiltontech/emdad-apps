# -*- coding: utf-8 -*-
# Part of emdad. See LICENSE file for full copyright and licensing details.

import emdad.tests
from emdad.tools import mute_logger


@emdad.tests.common.tagged('post_install', '-at_install')
class TestCustomSnippet(emdad.tests.HttpCase):

    @mute_logger('emdad.addons.http_routing.models.ir_http', 'emdad.http')
    def test_01_run_tour(self):
        self.start_tour(self.env['website'].get_client_action_url('/'), 'test_custom_snippet', login="admin")
