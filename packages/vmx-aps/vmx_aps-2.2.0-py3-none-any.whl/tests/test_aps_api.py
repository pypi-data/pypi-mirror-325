# Copyright (c) 2025. Verimatrix. All Rights Reserved.
# All information in this file is Verimatrix Confidential and Proprietary.
import json
import unittest
from unittest import mock
from unittest.mock import mock_open, patch, MagicMock

import requests
from apsapi.aps_api import OPENAPI_VERSION, ApsApi, construct_headers, upload_data

class TestApsApi(unittest.TestCase):

    def setUp(self):
        # Initialize a mock instance of ApsApi
        self.api = ApsApi(api_key="test-api-key",)
        self.api.api_gateway_url = "http://example.com"
        self.api.headers = {"Authorization": "Bearer test-token"}
        self.api.wait_seconds = 0  # Disable delays for testing

    @patch("apsapi.aps_requests.ApsRequest.put")
    def test_upload_data(self, mock_put):
        # Mock the response
        mock_response = MagicMock()
        mock_response.json.return_value = {"success": True}
        mock_put.return_value = mock_response

        url = "http://example.com/upload"
        data = b"test data"

        response = upload_data(url, data)
        self.assertEqual(response, mock_response)
        mock_put.assert_called_once_with(url, data=data)

    def test_construct_headers(self):
        token = "test-token"
        expected_headers = {
            "Authorization": token,
            "Accept": f'application/vnd.aps.appshield.verimatrixcloud.net;version={OPENAPI_VERSION}',
        }
        headers = construct_headers(token)
        self.assertEqual(headers, expected_headers)

    @patch("apsapi.aps_requests.ApsRequest.get")
    @patch('apsapi.aps_utils.ApsUtils.authenticate_api_key')
    def test_get_account_info(self, mock_authenticate_api_key, mock_get):

        mock_authenticate_api_key.return_value = ('Bearer mocked_token', 3600)

        mock_response = MagicMock()
        mock_response.json.return_value = {"account": "info"}
        mock_get.return_value = mock_response

        response = self.api.get_account_info()
        self.assertEqual(response, {"account": "info"})
        mock_get.assert_called_once_with(
            "http://example.com/report/account", headers=self.api.headers
        )

    @patch("apsapi.aps_requests.ApsRequest.post")
    @patch('apsapi.aps_utils.ApsUtils.authenticate_api_key')
    def test_add_application(self, mock_authenticate_api_key, mock_post):

        mock_authenticate_api_key.return_value = ('Bearer mocked_token', 3600)

        mock_response = MagicMock()
        mock_response.json.return_value = {"application": "created"}
        mock_post.return_value = mock_response

        permissions = {"private": True, "no_upload": False, "no_delete": False}
        response = self.api.add_application(
            name="test-app", package_id="pkg-id", os_name="android", permissions=permissions
        )
        self.assertEqual(response, {"application": "created"})
        mock_post.assert_called_once_with(
            "http://example.com/applications",
            headers=self.api.headers,
            data=mock.ANY,
        )

    @patch("apsapi.aps_requests.ApsRequest.patch")
    @patch('apsapi.aps_utils.ApsUtils.authenticate_api_key')
    def test_update_application(self, mock_authenticate_api_key, mock_patch):
        mock_authenticate_api_key.return_value = ('Bearer mocked_token', 3600)
        mock_response = MagicMock()
        mock_response.json.return_value = {"application": "updated"}
        mock_patch.return_value = mock_response

        permissions = {"private": True, "no_upload": False, "no_delete": False}
        response = self.api.update_application(
            application_id="app-id", name="new-name", permissions=permissions
        )
        self.assertEqual(response, {"application": "updated"})
        mock_patch.assert_called_once_with(
            "http://example.com/applications/app-id",
            headers=self.api.headers,
            data=mock.ANY,
        )

    @patch("apsapi.aps_requests.ApsRequest.get")
    @patch('apsapi.aps_utils.ApsUtils.authenticate_api_key')
    def test_list_applications(self, mock_authenticate_api_key, mock_get):
        mock_authenticate_api_key.return_value = ('Bearer mocked_token', 3600)
        mock_response = MagicMock()
        mock_response.json.return_value = [{"application": "app1"}, {"application": "app2"}]
        mock_get.return_value = mock_response

        response = self.api.list_applications(application_id=None)
        self.assertEqual(response, [{"application": "app1"}, {"application": "app2"}])
        mock_get.assert_called_once_with(
            "http://example.com/applications", headers=self.api.headers, params={}
        )

    @patch("apsapi.aps_requests.ApsRequest.delete")
    @patch('apsapi.aps_utils.ApsUtils.authenticate_api_key')
    def test_delete_application(self, mock_authenticate_api_key, mock_delete):
        mock_authenticate_api_key.return_value = ('Bearer mocked_token', 3600)
        mock_response = MagicMock()
        mock_response.json.return_value = {"application": "deleted"}
        mock_delete.return_value = mock_response

        response = self.api.delete_application(application_id="app-id")
        self.assertEqual(response, {"application": "deleted"})
        mock_delete.assert_called_once_with(
            "http://example.com/applications/app-id", headers=self.api.headers
        )

    @patch("apsapi.aps_requests.ApsRequest.get")
    @patch('apsapi.aps_utils.ApsUtils.authenticate_api_key')
    def test_get_account_info_error(self, mock_authenticate_api_key, mock_get):
        mock_authenticate_api_key.return_value = ('Bearer mocked_token', 3600)
        mock_get.side_effect = requests.exceptions.RequestException("Failed request")

        with self.assertRaises(requests.exceptions.RequestException):
            self.api.get_account_info()
        mock_get.assert_called_once_with(
            "http://example.com/report/account", headers=self.api.headers
        )

    @patch("apsapi.aps_requests.ApsRequest.get")
    @patch('apsapi.aps_utils.ApsUtils.authenticate_api_key')
    def test_list_applications_with_application_id(self, mock_authenticate_api_key, mock_get):
        mock_authenticate_api_key.return_value = ('Bearer mocked_token', 3600)
        mock_response = MagicMock()
        mock_response.json.return_value = {"application": "app-details"}
        mock_get.return_value = mock_response

        response = self.api.list_applications(application_id="app-id")
        self.assertEqual(response, {"application": "app-details"})
        mock_get.assert_called_once_with(
            "http://example.com/applications/app-id", headers=self.api.headers, params={}
        )

    @patch("apsapi.aps_requests.ApsRequest.get")
    @patch('apsapi.aps_utils.ApsUtils.authenticate_api_key')
    def test_list_applications_empty_response(self, mock_authenticate_api_key, mock_get):
        mock_authenticate_api_key.return_value = ('Bearer mocked_token', 3600)
        mock_response = MagicMock()
        mock_response.json.return_value = []
        mock_get.return_value = mock_response

        response = self.api.list_applications("com.example.app")
        self.assertEqual(response, [])
        mock_get.assert_called_once_with(
            "http://example.com/applications/com.example.app", headers=self.api.headers, params={}
        )

    @patch("apsapi.aps_requests.ApsRequest.get")
    @patch('apsapi.aps_utils.ApsUtils.authenticate_api_key')
    def test_token_expiry_and_reauthentication(self, mock_authenticate_api_key, mock_get):
        # Simulate token expiry
        mock_get.side_effect = requests.exceptions.HTTPError("401 Unauthorized")

        # Mock reauthentication
        mock_authenticate_api_key.return_value = ('Bearer new-test-token', 3600)

        # Attempt an API call
        with self.assertRaises(requests.exceptions.HTTPError):
            self.api.get_account_info()

        # Reauthenticate
        self.api.ensure_authenticated()
        self.assertEqual(self.api.headers["Authorization"], "Bearer new-test-token")
        mock_authenticate_api_key.assert_called_once()

    @patch("apsapi.aps_requests.ApsRequest.get")
    @patch('apsapi.aps_utils.ApsUtils.authenticate_api_key')
    def test_list_builds(self, mock_authenticate_api_key, mock_get):
        mock_authenticate_api_key.return_value = ('Bearer mocked_token', 3600)
        # Test listing builds
        mock_response = MagicMock()
        mock_response.json.return_value = [{"id": "build1"}, {"id": "build2"}]
        mock_get.return_value = mock_response

        response = self.api.list_builds(application_id="app1", build_id=None)
        self.assertEqual(response, [{"id": "build1"}, {"id": "build2"}])
        mock_get.assert_called_once_with(
            "http://example.com/builds", headers=self.api.headers, params={"app": "app1"}
        )

    @patch("apsapi.aps_requests.ApsRequest.post")
    @patch('apsapi.aps_utils.ApsUtils.authenticate_api_key')
    def test_create_build(self, mock_authenticate_api_key, mock_post):
        mock_authenticate_api_key.return_value = ('Bearer mocked_token', 3600)
        # Test creating a build
        mock_response = MagicMock()
        mock_response.json.return_value = {"id": "new-build"}
        mock_post.return_value = mock_response

        response = self.api.create_build(application_id="app1", subscription_type="trial")
        self.assertEqual(response, {"id": "new-build"})
        mock_post.assert_called_once_with(
            "http://example.com/builds",
            headers=self.api.headers,
            data=json.dumps({"applicationId": "app1", "subscriptionType": "trial"}),
        )

    @patch("apsapi.aps_requests.ApsRequest.put")
    @patch('apsapi.aps_utils.ApsUtils.authenticate_api_key')
    def test_set_build_metadata(self, mock_authenticate_api_key, mock_put):
        mock_authenticate_api_key.return_value = ('Bearer mocked_token', 3600)
        # Test setting build metadata
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "success"}
        mock_put.return_value = mock_response

        with patch("apsapi.aps_utils.ApsUtils.extract_version_info", return_value={"version": "1.0.0"}):
            response = self.api.set_build_metadata(build_id="build1", file="test.apk")
            self.assertEqual(response, {"status": "success"})
            mock_put.assert_called_once_with(
                "http://example.com/builds/build1/metadata",
                headers=self.api.headers,
                data=json.dumps({"os": "android", "osData": {"version": "1.0.0"}}),
            )

    @patch("apsapi.aps_requests.ApsRequest.post")
    @patch('apsapi.aps_utils.ApsUtils.authenticate_api_key')
    def test_update_build_metadata(self, mock_authenticate_api_key, mock_post):
        mock_authenticate_api_key.return_value = ('Bearer mocked_token', 3600)
        # Test updating build metadata
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "updated"}
        mock_post.return_value = mock_response

        response = self.api.update_build_metadata(build_id="build1", sign_final_binary=True)
        self.assertEqual(response, {"status": "updated"})
        mock_post.assert_called_once_with(
            "http://example.com/builds/build1/metadata",
            headers=self.api.headers,
            data=json.dumps({"signFinalBinary": True}),
        )

    @patch("apsapi.aps_requests.ApsRequest.get")
    @patch('apsapi.aps_utils.ApsUtils.authenticate_api_key')
    def test_upload_start(self, mock_authenticate_api_key, mock_get):
        mock_authenticate_api_key.return_value = ('Bearer mocked_token', 3600)
        # Test starting a multipart upload
        mock_response = MagicMock()
        mock_response.json.return_value = {"UploadId": "upload1"}
        mock_get.return_value = mock_response

        with patch("apsapi.aps_api.os.path.basename", return_value="file.zip"):
            response = self.api.upload_start(build_id="build1", file="file.zip")
            self.assertEqual(response, ("upload1", "file.zip"))
            mock_get.assert_called_once_with(
                "http://example.com/uploads/build1/start-upload",
                headers=self.api.headers,
                params={"uploadName": "file.zip", "uploadType": "application/zip"},
            )

    @patch("apsapi.aps_requests.ApsRequest.post")
    @patch('apsapi.aps_utils.ApsUtils.authenticate_api_key')
    def test_upload_complete(self, mock_authenticate_api_key, mock_post):
        mock_authenticate_api_key.return_value = ('Bearer mocked_token', 3600)
        # Test completing a multipart upload
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "completed"}
        mock_post.return_value = mock_response

        response = self.api.upload_complete(
            build_id="build1",
            upload_id="upload1",
            upload_name="file.zip",
            upload_parts=[{"ETag": "etag1", "PartNumber": 1}],
        )
        self.assertEqual(response, None)
        mock_post.assert_called_once_with(
            "http://example.com/uploads/build1/complete-upload",
            headers=self.api.headers,
            data=json.dumps({
                "parts": [{"ETag": "etag1", "PartNumber": 1}],
                "uploadId": "upload1",
                "uploadName": "file.zip",
            }),
        )

    @patch("apsapi.aps_requests.ApsRequest.post")
    @patch('apsapi.aps_utils.ApsUtils.authenticate_api_key')
    def test_upload_abort(self, mock_authenticate_api_key, mock_post):
        mock_authenticate_api_key.return_value = ('Bearer mocked_token', 3600)
        # Test aborting a multipart upload
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "aborted"}
        mock_post.return_value = mock_response

        response = self.api.upload_abort(
            build_id="build1",
            upload_id="upload1",
            upload_name="file.zip",
            message="User cancelled",
        )
        self.assertEqual(response, None)
        mock_post.assert_called_once_with(
            "http://example.com/uploads/build1/abort-upload",
            headers=self.api.headers,
            data=json.dumps({
                "uploadId": "upload1",
                "uploadName": "file.zip",
                "message": "User cancelled",
            }),
        )

    @patch("apsapi.aps_requests.ApsRequest.patch")
    @patch('apsapi.aps_utils.ApsUtils.authenticate_api_key')
    def test_protect_start(self, mock_authenticate_api_key, mock_patch):
        mock_authenticate_api_key.return_value = ('Bearer mocked_token', 3600)
        # Test starting build protection
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "started"}
        mock_patch.return_value = mock_response

        response = self.api.protect_start(build_id="build1")
        self.assertEqual(response, {"status": "started"})
        mock_patch.assert_called_once_with(
            "http://example.com/builds/build1",
            headers=self.api.headers,
            params={"cmd": "protect"},
        )

    @patch("apsapi.aps_requests.ApsRequest.patch")
    @patch('apsapi.aps_utils.ApsUtils.authenticate_api_key')
    def test_protect_cancel(self, mock_authenticate_api_key, mock_patch):
        mock_authenticate_api_key.return_value = ('Bearer mocked_token', 3600)
        # Test canceling protection
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "cancelled"}
        mock_patch.return_value = mock_response

        response = self.api.protect_cancel(build_id="build1")
        self.assertEqual(response, {"status": "cancelled"})
        mock_patch.assert_called_once_with(
            "http://example.com/builds/build1",
            headers=self.api.headers,
            params={"cmd": "cancel"},
        )

    @patch("apsapi.aps_requests.ApsRequest.get")
    @patch('apsapi.aps_utils.ApsUtils.authenticate_api_key')
    def test_protect_download(self, mock_authenticate_api_key, mock_get):
        mock_authenticate_api_key.return_value = ('Bearer mocked_token', 3600)
        # Test downloading a protected build file
        mock_response = MagicMock()
        mock_response.text = "http://example.com/protected/file.zip"
        mock_get.return_value = mock_response

        with patch("apsapi.aps_api.shutil.copyfileobj") as mock_copy, patch(
            "apsapi.open", mock.mock_open()
        ):
            self.api.protect_download(build_id="build1")
            mock_get.assert_called_with(
                "http://example.com/protected/file.zip", stream=True
            )
            mock_copy.assert_called_once()  # Verify file was copied

    
    @patch("apsapi.aps_requests.ApsRequest.put")
    @patch('apsapi.aps_utils.ApsUtils.authenticate_api_key')
    def test_add_build_to_application(self, mock_authenticate_api_key, mock_put):
        mock_authenticate_api_key.return_value = ('Bearer mocked_token', 3600)
        # Mock the response for add_build_to_application
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "success"}
        mock_put.return_value = mock_response

        response = self.api.add_build_to_application(build_id="build1", application_id="app1")
        self.assertEqual(response, {"status": "success"})

        mock_put.assert_called_once_with(
            "http://example.com/builds/build1/app",
            headers=self.api.headers,
            data=json.dumps({"applicationId": "app1"}),
        )

    @patch("apsapi.aps_api.ApsApi.protect_start")
    @patch("apsapi.aps_api.ApsApi.protect_get_status")
    @patch("apsapi.aps_api.time.sleep", return_value=None)  # Mock time.sleep to avoid delays
    def test_protect_build(self, mock_sleep, mock_protect_get_status, mock_protect_start):
        # Mock the start protection response
        mock_protect_start.return_value = {"status": "started"}

        # Mock the protect_get_status responses
        mock_protect_get_status.side_effect = [
            {"state": "protect_queue"},
            {"state": "protect_in_progress", "progressData": {"progress": 50}},
            {"state": "protect_done"},
        ]

        response = self.api.protect_build(build_id="build1")
        self.assertTrue(response)

        mock_protect_start.assert_called_once_with("build1")
        self.assertEqual(mock_protect_get_status.call_count, 3)  # 3 iterations of the loop

    @patch("apsapi.aps_api.ApsApi.add_build_without_app")
    @patch("apsapi.aps_api.ApsApi.list_applications")
    @patch("apsapi.aps_api.ApsApi.add_application")
    @patch("apsapi.aps_api.ApsApi.add_build_to_application")
    @patch("apsapi.aps_api.ApsApi.multipart_upload")
    @patch("apsapi.aps_api.ApsApi.protect_build")
    @patch("apsapi.aps_api.ApsApi.protect_download")
    def test_protect(self, mock_protect_download, mock_protect_build, mock_multipart_upload, mock_add_build_to_application, mock_add_application, mock_list_applications, mock_add_build_without_app):
        # Mock responses for dependencies
        mock_add_build_without_app.return_value = {"id": "build1", "applicationPackageId": "package1"}
        mock_list_applications.return_value = [{"id": "app1", "applicationPackageId": "package1", "os": "android"}]
        mock_multipart_upload.return_value = True
        mock_protect_build.return_value = True

        # Test the protect method
        response = self.api.protect(file="test.apk", subscription_type="trial")
        self.assertTrue(response)

        mock_add_build_without_app.assert_called_once_with('test.apk', subscription_type='trial')
        mock_add_build_to_application.assert_called_once_with("build1", "app1")
        mock_protect_download.assert_called_once_with("build1")

    @patch("apsapi.aps_requests.ApsRequest.get")
    @patch("apsapi.aps_api.shutil.copyfileobj")
    @patch("apsapi.open", new_callable=unittest.mock.mock_open)
    @patch('apsapi.aps_utils.ApsUtils.authenticate_api_key')
    def test_get_build_artifacts(self, mock_authenticate_api_key, mock_open, mock_copyfileobj, mock_get):
        mock_authenticate_api_key.return_value = ('Bearer mocked_token', 3600)
        # Mock response for artifact URLs
        mock_get.side_effect = [
            # First call to get the list of artifact URLs
            MagicMock(json=MagicMock(return_value=["http://example.com/file1.zip", "http://example.com/file2.zip"])),
            # Subsequent calls to download artifacts
            MagicMock(raw=MagicMock(headers={"Content-Type": "application/zip"})),
            MagicMock(raw=MagicMock(headers={"Content-Type": "application/zip"})),
        ]
        with patch("apsapi.aps_api.os.getcwd", return_value="/tmp"):
            self.api.get_build_artifacts(build_id="build1")

        mock_get.assert_any_call("http://example.com/report/artifacts?buildId=build1", headers=self.api.headers)
        mock_copyfileobj.assert_called()  # Ensure file contents were copied

    @patch("apsapi.aps_requests.ApsRequest.get")
    @patch('apsapi.aps_utils.ApsUtils.authenticate_api_key')
    def test_get_statistics(self, mock_authenticate_api_key, mock_get):
        mock_authenticate_api_key.return_value = ('Bearer mocked_token', 3600)
        # Mock response for statistics
        mock_response = MagicMock()
        mock_response.json.return_value = {"stats": "data"}
        mock_get.return_value = mock_response

        with patch("apsapi.aps_api.dateutil.parser.parse") as mock_parse:
            mock_parse.side_effect = lambda x: x  # Mock date parsing to return input
            response = self.api.get_statistics(start="2025-01-01", end="2025-01-31")
            self.assertEqual(response, {"stats": "data"})

            mock_get.assert_called_once_with(
                "http://example.com/report/statistics?start=2025-01-01&end=2025-01-31",
                headers=self.api.headers,
                params={},
            )

    @patch("apsapi.aps_utils.ApsUtils.extract_package_id")
    def test_display_application_package_id(self, mock_extract_package_id):
        # Mock the package ID extraction
        mock_extract_package_id.return_value = "package1"

        result = self.api.display_application_package_id(file="test.apk")
        self.assertEqual(result, "package1")

        mock_extract_package_id.assert_called_once_with("test.apk")

    @patch("apsapi.aps_requests.ApsRequest.put")
    @patch("apsapi.aps_api.json.load", return_value={"config_key": "config_value"})
    @patch("apsapi.aps_api.open", new_callable=unittest.mock.mock_open)
    @patch('apsapi.aps_utils.ApsUtils.authenticate_api_key')
    def test_set_protection_configuration(self, mock_authenticate_api_key, mock_open, mock_json_load, mock_put):
        mock_authenticate_api_key.return_value = ('Bearer mocked_token', 3600)
        # Mock response for set protection configuration
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "configured"}
        mock_put.return_value = mock_response

        response = self.api.set_protection_configuration(application_id="app1", file="config.json")
        self.assertEqual(response, {"status": "configured"})

        mock_open.assert_called_once_with("config.json", "rb")
        mock_put.assert_called_once_with(
            "http://example.com/applications/app1/protection-configuration",
            headers=self.api.headers,
            data=json.dumps({"configuration": {"config_key": "config_value"}}),
        )

    @patch("apsapi.aps_requests.ApsRequest.delete")
    @patch('apsapi.aps_utils.ApsUtils.authenticate_api_key')
    def test_delete_protection_configuration(self, mock_authenticate_api_key, mock_delete):
        mock_authenticate_api_key.return_value = ('Bearer mocked_token', 3600)
        # Mock response for delete protection configuration
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "deleted"}
        mock_delete.return_value = mock_response

        response = self.api.delete_protection_configuration(application_id="app1")
        self.assertEqual(response, {"status": "deleted"})

        mock_delete.assert_called_once_with(
            "http://example.com/applications/app1/protection-configuration",
            headers=self.api.headers,
        )

    @patch("apsapi.aps_requests.ApsRequest.put")
    @patch("apsapi.aps_api.open", new_callable=mock_open, read_data=json.dumps({"key": "value"}))
    @patch('apsapi.aps_utils.ApsUtils.authenticate_api_key')
    def test_set_build_protection_configuration(self, mock_authenticate_api_key, mock_open, mock_put):
        mock_authenticate_api_key.return_value = ('Bearer mocked_token', 3600)
        # Mock the response
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "configured"}
        mock_put.return_value = mock_response

        response = self.api.set_build_protection_configuration(build_id="build1", file="config.json")
        self.assertEqual(response, {"status": "configured"})

        # Check that the file was opened and the request was made
        mock_open.assert_called_once_with("config.json", "rb")
        mock_put.assert_called_once_with(
            "http://example.com/builds/build1/protection-configuration",
            headers=self.api.headers,
            data=json.dumps({"configuration": {"key": "value"}}),
        )

    @patch("apsapi.aps_requests.ApsRequest.delete")
    @patch('apsapi.aps_utils.ApsUtils.authenticate_api_key')
    def test_delete_build_protection_configuration(self, mock_authenticate_api_key, mock_delete):
        mock_authenticate_api_key.return_value = ('Bearer mocked_token', 3600)
        # Mock the response
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "deleted"}
        mock_delete.return_value = mock_response

        response = self.api.delete_build_protection_configuration(build_id="build1")
        self.assertEqual(response, {"status": "deleted"})

        # Verify the correct API call was made
        mock_delete.assert_called_once_with(
            "http://example.com/builds/build1/protection-configuration",
            headers=self.api.headers,
        )

    @patch("apsapi.aps_requests.ApsRequest.put")
    @patch('apsapi.aps_utils.ApsUtils.authenticate_api_key')
    def test_set_report_and_exit_flag(self, mock_authenticate_api_key, mock_put):
        mock_authenticate_api_key.return_value = ('Bearer mocked_token', 3600)
        # Mock the response
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "updated"}
        mock_put.return_value = mock_response

        response = self.api.set_report_and_exit_flag(application_id="app1", flagValue=True)
        self.assertEqual(response, {"status": "updated"})

        # Verify the correct API call was made
        mock_put.assert_called_once_with(
            "http://example.com/applications/app1/report-and-exit?enabled=True",
            headers=self.api.headers,
        )

    @patch("apsapi.aps_requests.ApsRequest.put")
    @patch("apsapi.aps_api.open", new_callable=mock_open, read_data="certificate-content")
    @patch('apsapi.aps_utils.ApsUtils.authenticate_api_key')
    def test_set_signing_certificate(self, mock_authenticate_api_key, mock_open, mock_put):
        mock_authenticate_api_key.return_value = ('Bearer mocked_token', 3600)
        # Mock the response
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "configured"}
        mock_put.return_value = mock_response

        response = self.api.set_signing_certificate(application_id="app1", file="cert.pem")
        self.assertEqual(response, {"status": "configured"})

        # Check that the file was opened and the request was made
        mock_open.assert_called_once_with("cert.pem", "r")
        mock_put.assert_called_once_with(
            "http://example.com/applications/app1/signing-certificate",
            headers=self.api.headers,
            data=json.dumps({"certificate": "certificate-content", "certificateFileName": "cert.pem"}),
        )

    @patch("apsapi.aps_requests.ApsRequest.put")
    @patch("apsapi.aps_api.open", new_callable=mock_open, read_data="certificate-content")
    @patch('apsapi.aps_utils.ApsUtils.authenticate_api_key')
    def test_set_secondary_signing_certificate(self, mock_authenticate_api_key, mock_open, mock_put):
        mock_authenticate_api_key.return_value = ('Bearer mocked_token', 3600)
        # Mock the response
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "configured"}
        mock_put.return_value = mock_response

        response = self.api.set_secondary_signing_certificate(application_id="app1", file="cert.pem")
        self.assertEqual(response, {"status": "configured"})

        # Check that the file was opened and the request was made
        mock_open.assert_called_once_with("cert.pem", "r")
        mock_put.assert_called_once_with(
            "http://example.com/applications/app1/secondary-signing-certificate",
            headers=self.api.headers,
            data=json.dumps({"certificate": "certificate-content", "certificateFileName": "cert.pem"}),
        )

    @patch("apsapi.aps_requests.ApsRequest.delete")
    @patch('apsapi.aps_utils.ApsUtils.authenticate_api_key')
    def test_delete_secondary_signing_certificate(self, mock_authenticate_api_key, mock_delete):
        mock_authenticate_api_key.return_value = ('Bearer mocked_token', 3600)
        # Mock the response
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "deleted"}
        mock_delete.return_value = mock_response

        response = self.api.delete_secondary_signing_certificate(application_id="app1")
        self.assertEqual(response, {"status": "deleted"})

        # Verify the correct API call was made
        mock_delete.assert_called_once_with(
            "http://example.com/applications/app1/secondary-signing-certificate",
            headers=self.api.headers,
        )

    @patch("apsapi.aps_api.ApsApi.multipart_upload")
    @patch('apsapi.aps_utils.ApsUtils.authenticate_api_key')
    def test_set_mapping_file(self, mock_authenticate_api_key, mock_multipart_upload):
        mock_authenticate_api_key.return_value = ('Bearer mocked_token', 3600)
        # Mock the response
        mock_multipart_upload.return_value = {"status": "success"}

        response = self.api.set_mapping_file(build_id="build1", file="mapping.txt")
        self.assertEqual(response, {"status": "success"})

        # Verify the correct method was called
        mock_multipart_upload.assert_called_once_with("build1", "mapping.txt", "MAPPING_FILE")

    @patch("apsapi.aps_requests.ApsRequest.get")
    @patch('apsapi.aps_utils.ApsUtils.authenticate_api_key')
    def test_get_sail_config(self, mock_authenticate_api_key, mock_get):
        mock_authenticate_api_key.return_value = ('Bearer mocked_token', 3600)
        # Mock the response
        mock_response = MagicMock()
        mock_response.json.return_value = {"config": "data"}
        mock_get.return_value = mock_response

        response = self.api.get_sail_config(os_type="android", version="1.0")
        self.assertEqual(response, {"config": "data"})

        # Verify the correct API call was made
        mock_get.assert_called_once_with(
            "http://example.com/sail_config",
            headers=self.api.headers,
            params={"os": "android", "version": "1.0"},
        )

    @patch("apsapi.aps_requests.ApsRequest.get")
    @patch('apsapi.aps_utils.ApsUtils.authenticate_api_key')
    def test_get_version(self, mock_authenticate_api_key, mock_get):
        mock_authenticate_api_key.return_value = ('Bearer mocked_token', 3600)
        # Mock the response
        mock_response = MagicMock()
        mock_response.json.return_value = {"version": "1.0.0"}
        mock_get.return_value = mock_response

        response = self.api.get_version()
        self.assertEqual(response, {"version": "1.0.0"})

        # Verify the correct API call was made
        mock_get.assert_called_once_with(
            "http://example.com/version",
            headers=self.api.headers,
        )


if __name__ == "__main__":
    unittest.main()
