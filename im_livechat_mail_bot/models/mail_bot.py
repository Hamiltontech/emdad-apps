# -*- coding: utf-8 -*-
# Part of emdad. See LICENSE file for full copyright and licensing details.

from markupsafe import Markup
from emdad import models, _


class MailBot(models.AbstractModel):
    _inherit = 'mail.bot'

    def _get_answer(self, record, body, values, command):
        emdadbot_state = self.env.user.emdadbot_state
        if self._is_bot_in_private_channel(record):
            if emdadbot_state == "onboarding_attachement" and values.get("attachment_ids"):
                self.env.user.emdadbot_failed = False
                self.env.user.emdadbot_state = "onboarding_canned"
                return Markup(_("That's me! 🎉<br/>Try typing %s to use canned responses.", "<span class=\"o_emdadbot_command\">:</span>"))
            elif emdadbot_state == "onboarding_canned" and values.get("canned_response_ids"):
                self.env.user.emdadbot_failed = False
                self.env.user.emdadbot_state = "idle"
                return Markup(_("Good, you can customize canned responses in the live chat application.<br/><br/><b>It's the end of this overview</b>, enjoy discovering emdad!"))
            # repeat question if needed
            elif emdadbot_state == 'onboarding_canned' and not self._is_help_requested(body):
                self.env.user.emdadbot_failed = True
                return _("Not sure what you are doing. Please, type %s and wait for the propositions. Select one of them and press enter.",
                    Markup("<span class=\"o_emdadbot_command\">:</span>"))
        return super(MailBot, self)._get_answer(record, body, values, command)
