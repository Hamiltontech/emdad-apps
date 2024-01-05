import emdad.tests
from emdad.tools import mute_logger


@emdad.tests.common.tagged('post_install', '-at_install')
class TestWebsiteError(emdad.tests.HttpCase):

    @mute_logger('emdad.addons.http_routing.models.ir_http', 'emdad.http')
    def test_01_run_test(self):
        self.start_tour("/test_error_view", 'test_error_website')
