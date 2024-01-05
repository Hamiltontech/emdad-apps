# Part of emdad. See LICENSE file for full copyright and licensing details.

from emdad.http import route
from emdad.addons.mail.controllers.webclient import WebclientController
from emdad.addons.im_livechat.tools.misc import force_guest_env


class WebClient(WebclientController):
    @route("/im_livechat/cors/init_messaging", methods=["POST"], type="json", auth="public", cors="*")
    def livechat_init_messaging(self, guest_token):
        force_guest_env(guest_token)
        return self.mail_init_messaging()
