# Copyright (c) 2025. Verimatrix. All Rights Reserved.
# All information in this file is Verimatrix Confidential and Proprietary.
import unittest
from unittest import mock
from unittest.mock import patch, MagicMock
from apsapi.aps_utils import ApsUtils
from apsapi.aps_exceptions import ApsException
import base64

class TestApsUtils(unittest.TestCase):

    @patch('apsapi.aps_requests.ApsRequest.post')  # Mock the ApsRequest.post method
    def test_authenticate_api_key(self, mock_post):
        # Mock the response of the post request
        mock_response = MagicMock()
        mock_response.json.return_value = {'token': 'mocked_token', 'expirationTime': 3600}
        mock_post.return_value = mock_response

        utils = ApsUtils()
        token, expiration_time = utils.authenticate_api_key('mock_url', 'mock_api_key')

        # Assertions
        mock_post.assert_called_once_with('mock_url', json={'apiKey': 'mock_api_key'})
        self.assertEqual(token, 'Bearer mocked_token')
        self.assertEqual(expiration_time, 3600)

    def test_get_os(self):
        utils = ApsUtils()

        # Test Android APK file
        os = utils.get_os('app.apk')
        self.assertEqual(os, 'android')

        # Test Android AAB file
        os = utils.get_os('app.aab')
        self.assertEqual(os, 'android')

        # Test iOS XCArchive
        os = utils.get_os('app.xcarchive.zip')
        self.assertEqual(os, 'ios')

        # Test unsupported file type
        with self.assertRaises(ApsException):
            utils.get_os('unsupported_file.txt')

    @patch('apsapi.aps_utils.ZipFile')  # Mock the ZipFile class
    @patch('apsapi.aps_utils.ApsUtils.extract_file_data_from_zip')  # Mock helper function
    @patch('apsapi.aps_utils.is_zipfile')
    def test_extract_version_info(self, mock_is_zipfile, mock_extract_file_data_from_zip, mock_zipfile):
        # Mock the behavior of is_zipfile to return True
        mock_is_zipfile.return_value = True
        
        # Setup mocks for zip handling
        mock_zip = MagicMock()
        mock_zipfile.return_value = mock_zip
        mock_extract_file_data_from_zip.return_value = 'mocked_base64_data'
        
        utils = ApsUtils()
        
        # Mock supported file types
        mock_zip.namelist.return_value = ['AndroidManifest.xml']
        
        # Call the method to test
        version_info = utils.extract_version_info('app.apk')
        
        # Perform assertions based on your expectationsextract_version_info
        self.assertEqual(version_info, {'androidManifest': 'mocked_base64_data'})           

    @patch('apsapi.aps_utils.ApsUtils.extract_version_info')  # Mock extract_version_info
    @patch('apsapi.aps_utils.APK')  # Mock APK class for package extraction
    def test_extract_package_id(self, mock_apk, mock_extract_version_info):
        # Mock the extract_version_info return value for Android
        mock_extract_version_info.return_value = {'androidManifest': 'mocked_manifest'}
        
        # Mock APK package method for Android
        mock_apk.return_value.package = 'com.example.package'
        
        # Test for Android APK file
        utils = ApsUtils()
        package_id = utils.extract_package_id('app.apk')
        self.assertEqual(package_id, 'com.example.package')
        
        # Test with iOS plist data (both XML and binary plist)
        
        # Mock XML plist data as a properly base64-encoded string
        ios_xml_plist_data = base64.b64encode(b'<?xml version="1.0"?><plist><dict><key>ApplicationProperties</key><dict><key>CFBundleIdentifier</key><string>com.example.ios</string></dict></dict></plist>').decode('utf-8')
        mock_extract_version_info.return_value = {'iosXmlPlist': ios_xml_plist_data}
        
        # Mock iOS plist processing
        mock_plist = {'ApplicationProperties': {'CFBundleIdentifier': 'com.example.ios'}}
        
        package_id = utils.extract_package_id('app.xcarchive.zip')
        self.assertEqual(package_id, 'com.example.ios')

    @patch('apsapi.aps_utils.ZipFile')
    @patch('os.remove')
    def test_extract_file_data_from_zip(self, mock_remove, mock_zipfile):
        # Setup a mock for file extraction
        mock_zip = MagicMock()
        mock_zipfile.return_value = mock_zip
        mock_zip.extract.return_value = 'mocked_file_path'

        # Mock the file content being read
        with patch('builtins.open', mock.mock_open(read_data='mocked_file_content'.encode('utf-8'))) as mock_file:
            utils = ApsUtils()
            file_data = utils.extract_file_data_from_zip(mock_zip, 'mocked_file')
            self.assertEqual(file_data, base64.b64encode(b'mocked_file_content').decode('utf-8'))
            mock_file.assert_called_once_with('mocked_file_path', 'rb')

if __name__ == '__main__':
    unittest.main()
