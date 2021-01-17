from base import http
from unittest.mock import patch
from tests.test_base import token2user, SetUpUserTest


class TestClientsBase(SetUpUserTest):

    def test_about(self):
        self.api(None, 'GET', '/api/users/about')
        self.show_last_result()
