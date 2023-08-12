"""
Unit tests for the `novexity.search` module.

This module contains tests that verify the functionality of the `search` function
within the `novexity.search` module.
"""

import unittest
from unittest.mock import patch, Mock
from novexity.search import search


class TestGoogleSearch(unittest.TestCase):

    @patch('novexity.search.requests.Session.get')
    @patch('novexity.search.ApiGateway.start')
    @patch('novexity.search.ApiGateway.shutdown')
    # This ensures time.sleep call won't delay the test
    @patch('novexity.search.time.sleep')
    def test_search_successful(self, mock_sleep, mock_shutdown, mock_start, mock_get):
        """Test that the `search` function correctly parses a mock Google result."""
        # Mocking the response from Google
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = '<html><body><div class="tF2Cxc"><h3>Test Result</h3></div></body></html>'

        mock_get.return_value = mock_response
        mock_start.return_value = None
        mock_shutdown.return_value = None
        mock_sleep.return_value = None

        results = search("Test Query")
        self.assertEqual(len(results['organic_results']), 1)
        self.assertEqual(results['organic_results'][0]['title'], 'Test Result')


if __name__ == '__main__':
    unittest.main()
