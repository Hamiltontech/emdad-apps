# -*- coding: utf-8 -*-
# Part of emdad. See LICENSE file for full copyright and licensing details.

from emdad.http import request
from emdad.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSaleSlides(WebsiteSale):

    def _prepare_shop_payment_confirmation_values(self, order):
        values = super()._prepare_shop_payment_confirmation_values(order)
        if order.order_line.product_id.channel_ids:
            channel_partners = request.env['slide.channel.partner'].sudo().search([
                ('partner_id', '=', order.partner_id.id),
                ('channel_id', 'in', order.order_line.product_id.channel_ids.ids),
            ])
            values['course_memberships'] = {
                channel_partner.channel_id: channel_partner
                for channel_partner in channel_partners
            }
        return values
