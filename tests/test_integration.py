from base import http
from unittest.mock import patch
from tests.test_base import token2user, SetUpIntegrationTest


class TestaAboutAllServices(SetUpIntegrationTest):

    def test_about(self):
        self.api(None, 'GET', '/api/users/about')
        self.show_last_result()
        self.api(None, 'GET', '/api/app/about')
        self.show_last_result()
