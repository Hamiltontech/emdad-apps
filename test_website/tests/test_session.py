import emdad.tests
from emdad.tools import mute_logger


@emdad.tests.common.tagged('post_install', '-at_install')
class TestWebsiteSession(emdad.tests.HttpCase):

    def test_01_run_test(self):
        self.start_tour('/', 'test_json_auth')
