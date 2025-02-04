# Copyright (c) 2025. Verimatrix. All Rights Reserved.
# All information in this file is Verimatrix Confidential and Proprietary.
import unittest
from unittest import mock
from unittest.mock import patch
import requests
from apsapi.aps_requests import check_requests_response, request_with_retry, ApsRequest 

class TestApsRequest(unittest.TestCase):
    @patch("requests.request")
    def test_check_requests_response_success(self, mock_request):
        # Mock a successful response with no errorMessage
        mock_response = mock.Mock()
        mock_response.headers = {'Content-Type': 'application/json'}
        mock_response.json.return_value = {}
        
        try:
            check_requests_response(mock_response)
        except Exception as e:
            self.fail(f"check_requests_response raised an exception: {e}")

    def test_check_requests_response_with_aps_error_message(self):
        # Mock a response with an errorMessage
        mock_response = mock.Mock()
        mock_response.headers = {'Content-Type': 'application/json'}
        mock_response.json.return_value = {'errorMessage': 'Some error occurred'}
        
        # Should not raise an exception
        check_requests_response(mock_response)

    def test_check_requests_response_raise_exception(self):
        # Mock a response with a status code indicating failure
        mock_response = mock.Mock()
        mock_response.headers = {}
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("HTTP Error")
        
        with self.assertRaises(requests.exceptions.HTTPError):
            check_requests_response(mock_response)

    @patch("requests.request")
    def test_request_with_retry_success(self, mock_request):
        # Mock a successful request
        mock_response = mock.Mock()
        mock_response.json.return_value = {}
        mock_request.return_value = mock_response

        response = request_with_retry("get", "http://example.com")
        self.assertEqual(response, mock_response)
        mock_request.assert_called_once_with("get", "http://example.com")

    @patch("requests.request")
    def test_request_with_retry_failure(self, mock_request):
        # Mock a failing request
        mock_request.side_effect = requests.exceptions.RequestException("Request failed")

        with self.assertRaises(requests.exceptions.RequestException):
            request_with_retry("get", "http://example.com")

        self.assertEqual(mock_request.call_count, 3)  # Ensure it retries 3 times

    @patch("requests.request")
    def test_aps_request_get(self, mock_request_with_retry):
        # Mock the get method
        mock_response = mock.Mock()
        mock_response.json.return_value = {}
        mock_request_with_retry.return_value = mock_response

        response = ApsRequest.get("http://example.com")
        self.assertEqual(response, mock_response)
        mock_request_with_retry.assert_called_once_with("get", "http://example.com")

    @patch("requests.request")
    def test_aps_request_post(self, mock_request_with_retry):
        # Mock the post method
        mock_response = mock.Mock()
        mock_response.json.return_value = {}
        mock_request_with_retry.return_value = mock_response

        response = ApsRequest.post("http://example.com", json={"key": "value"})
        self.assertEqual(response, mock_response)
        mock_request_with_retry.assert_called_once_with("post", "http://example.com", json={"key": "value"})

    @patch("requests.request")
    def test_aps_request_put(self, mock_request_with_retry):
        # Mock the put method
        mock_response = mock.Mock()
        mock_response.json.return_value = {}
        mock_request_with_retry.return_value = mock_response

        response = ApsRequest.put("http://example.com", json={"key": "value"})
        self.assertEqual(response, mock_response)
        mock_request_with_retry.assert_called_once_with("put", "http://example.com", json={"key": "value"})

    @patch("requests.request")
    def test_aps_request_patch(self, mock_request_with_retry):
        # Mock the patch method
        mock_response = mock.Mock()
        mock_response.json.return_value = {}
        mock_request_with_retry.return_value = mock_response

        response = ApsRequest.patch("http://example.com", json={"key": "value"})
        self.assertEqual(response, mock_response)
        mock_request_with_retry.assert_called_once_with("patch", "http://example.com", json={"key": "value"})

    @patch("requests.request")
    def test_aps_request_delete(self, mock_request_with_retry):
        # Mock the delete method
        mock_response = mock.Mock()
        mock_response.json.return_value = {}
        mock_request_with_retry.return_value = mock_response

        response = ApsRequest.delete("http://example.com")
        self.assertEqual(response, mock_response)
        mock_request_with_retry.assert_called_once_with("delete", "http://example.com")

if __name__ == "__main__":
    unittest.main()
