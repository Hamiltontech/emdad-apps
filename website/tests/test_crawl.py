# -*- coding: utf-8 -*-
# Part of emdad. See LICENSE file for full copyright and licensing details.

import logging
import time

import lxml.html
from werkzeug import urls

import emdad
import re

from emdad.addons.base.tests.common import HttpCaseWithUserDemo

_logger = logging.getLogger(__name__)


@emdad.tests.common.tagged('post_install', '-at_install', 'crawl')
class Crawler(HttpCaseWithUserDemo):
    """ Test suite crawling an emdad CMS instance and checking that all
    internal links lead to a 200 response.

    If a username and a password are provided, authenticates the user before
    starting the crawl
    """

    def setUp(self):
        super(Crawler, self).setUp()
        self.env.ref('website.default_website').write({
            'social_facebook': "https://www.facebook.com/emdad",
            'social_twitter': 'https://twitter.com/emdad',
            'social_linkedin': 'https://www.linkedin.com/company/emdad',
            'social_youtube': 'https://www.youtube.com/user/OpenERPonline',
            'social_github': 'https://github.com/emdad',
            'social_instagram': 'https://www.instagram.com/explore/tags/emdad/',
            'social_tiktok': 'https://www.tiktok.com/@emdad',
        })

        if hasattr(self.env['res.partner'], 'grade_id'):
            # Create at least one published parter, so that /partners doesn't
            # return a 404
            grade = self.env['res.partner.grade'].create({
                'name': 'A test grade',
                'website_published': True,
            })
            self.env['res.partner'].create({
                'name': 'A Company for /partners',
                'is_company': True,
                'grade_id': grade.id,
                'website_published': True,
            })

    def crawl(self, url, seen=None, msg=''):
        if seen is None:
            seen = set()

        url_slug = re.sub(r"[/](([^/=?&]+-)?[0-9]+)([/]|$)", '/<slug>/', url)
        url_slug = re.sub(r"([^/=?&]+)=[^/=?&]+", '\g<1>=param', url_slug)
        if url_slug in seen:
            return seen
        else:
            seen.add(url_slug)

        _logger.info("%s %s", msg, url)
        r = self.url_open(url, allow_redirects=False)
        if r.status_code in (301, 302, 303):
            # check local redirect to avoid fetch externals pages
            new_url = r.headers.get('Location')
            current_url = r.url
            if urls.url_parse(new_url).netloc != urls.url_parse(current_url).netloc:
                return seen
            r = self.url_open(new_url)

        code = r.status_code
        self.assertIn(code, range(200, 300), "%s Fetching %s returned error response (%d)" % (msg, url, code))

        if r.headers['Content-Type'].startswith('text/html'):
            doc = lxml.html.fromstring(r.content)
            for link in doc.xpath('//a[@href]'):
                href = link.get('href')

                parts = urls.url_parse(href)
                # href with any fragment removed
                href = parts.replace(fragment='').to_url()

                # FIXME: handle relative link (not parts.path.startswith /)
                if parts.netloc or \
                    not parts.path.startswith('/') or \
                    parts.path == '/web' or\
                    parts.path.startswith('/web/') or \
                    parts.path.startswith('/en_US/') or \
                    (parts.scheme and parts.scheme not in ('http', 'https')):
                    continue

                self.crawl(href, seen, msg)
        return seen

    def test_10_crawl_public(self):
        t0 = time.time()
        t0_sql = self.registry.test_cr.sql_log_count
        seen = self.crawl('/', msg='Anonymous Coward')
        count = len(seen)
        duration = time.time() - t0
        sql = self.registry.test_cr.sql_log_count - t0_sql
        _logger.runbot("public crawled %s urls in %.2fs %s queries, %.3fs %.2fq per request, ", count, duration, sql, duration / count, float(sql) / count)

    def test_20_crawl_demo(self):
        # Demo user without sales/crm/helpdesk/... rights won't be able to access to
        # portals like /my/leads. Grant him those rights if exists.
        groups = self.env['res.groups']
        group_xmlids = [
            'sales_team.group_sale_salesman',
            'purchase.group_purchase_user',
            'helpdesk.group_helpdesk_user',
        ]
        for group_xmlid in group_xmlids:
            group = self.env.ref(group_xmlid, raise_if_not_found=False)
            if group:
                groups += group
        self.env.ref('base.group_user').write({'implied_ids': [(4, group.id) for group in groups]})
        t0 = time.time()
        t0_sql = self.registry.test_cr.sql_log_count
        self.authenticate('demo', 'demo')
        seen = self.crawl('/', msg='demo')
        count = len(seen)
        duration = time.time() - t0
        sql = self.registry.test_cr.sql_log_count - t0_sql
        _logger.runbot("demo crawled %s urls in %.2fs %s queries, %.3fs %.2fq per request", count, duration, sql, duration / count, float(sql) / count)

    def test_30_crawl_admin(self):
        # If no forum.post is existing, the route /forum//ask will be called instead -> 404
        if 'forum.post' in self.env:
            self.env['forum.post'].create({
                'name': 'Very Smart Question',
                'forum_id': self.env.ref('website_forum.forum_help').id,
            })
        t0 = time.time()
        t0_sql = self.registry.test_cr.sql_log_count
        self.authenticate('admin', 'admin')
        seen = self.crawl('/', msg='admin')
        count = len(seen)
        duration = time.time() - t0
        sql = self.registry.test_cr.sql_log_count - t0_sql
        _logger.runbot("admin crawled %s urls in %.2fs %s queries, %.3fs %.2fq per request", count, duration, sql, duration / count, float(sql) / count)
