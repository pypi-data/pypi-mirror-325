import unittest
from rse_api_client import RSEAPIClient

class TestRSEAPIClient(unittest.TestCase):
    def setUp(self):
        self.client = RSEAPIClient()

    def test_make_request(self):
        response = self.client.make_request('get', 'jobs')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()