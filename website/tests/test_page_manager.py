# -*- coding: utf-8 -*-
# Part of emdad. See LICENSE file for full copyright and licensing details.

import emdad.tests

@emdad.tests.common.tagged('post_install', '-at_install')
class TestWebsitePageManager(emdad.tests.HttpCase):

    def test_01_page_manager(self):
        if self.env['website'].search_count([]) == 1:
            self.env['website'].create({
                'name': 'My Website 2',
                'domain': '',
                'sequence': 20,
            })
        self.start_tour(self.env['website'].get_client_action_url('/'), 'website_page_manager', login="admin")
