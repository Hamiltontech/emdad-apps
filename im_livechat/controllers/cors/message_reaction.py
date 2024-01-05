# Part of emdad. See LICENSE file for full copyright and licensing details.

from emdad.http import route
from emdad.addons.mail.controllers.message_reaction import MessageReactionController
from emdad.addons.im_livechat.tools.misc import force_guest_env


class LivechatMessageReactionController(MessageReactionController):
    @route("/im_livechat/cors/message/reaction", methods=["POST"], type="json", auth="public", cors="*")
    def livechat_message_add_reaction(self, guest_token, message_id, content, action):
        force_guest_env(guest_token)
        return self.mail_message_add_reaction(message_id, content, action)
