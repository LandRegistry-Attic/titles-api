import unittest
import json
import os
import mock
import requests
import json

from application import app

class TestCaseAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_service(self):
        response = self.app.get('/')
        assert response.status_code == 200

    @mock.patch('requests.post')
    @mock.patch('requests.Response')
    def test_valid_title(self, mock_response, mock_post):
        response_instance = mock_response.return_value
        response_instance.status_code = requests.codes.ok
        response_instance.json.return_value = json.loads('{"validation_result" : 1, "error_message" : "TITLE IS VALID AND ON V_REG_TITLE", "error_message_number":"0"}')
        mock_post.return_value = response_instance
        response = self.app.get('/validate/DN503122')
        response_data = json.loads(response.data)
        assert response_data["error_message"] == "Valid title number"
