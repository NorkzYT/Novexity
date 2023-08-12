"""
Unit tests for the `novexity.google_search` module.

This module contains tests that verify the functionality of the `search` function
within the `novexity.google_search` module.
"""

import unittest
from unittest.mock import patch
from novexity.google_search import search


class TestGoogleSearch(unittest.TestCase):
    """
    Test cases for the `search` function of the `novexity.google_search` module.

    This class mocks the responses from Google to verify that the `search` function
    correctly parses and returns search results.
    """

    @patch('novexity.google_search.requests.Session.get')
    def test_search_successful(self, mock_get):
        """Test that the `search` function correctly parses a mock Google result."""
        # Mocking the response from Google
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = '<html><body><div class="tF2Cxc"><h3>Test Result</h3></div></body></html>'

        results = search("Test Query")
        self.assertEqual(len(results['organic_results']), 1)
        self.assertEqual(results['organic_results'][0]['title'], 'Test Result')

    # You can add more tests, for example for the error case, etc.


if __name__ == '__main__':
    unittest.main()
