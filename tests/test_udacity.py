import unittest

from mooc_aggregator_restful_api import udacity


class UdacityTestCase(unittest.TestCase):
    '''
    Unit Tests for module udacity

    '''

    def setUp(self):
        self.udacity_test_object = udacity.UdacityAPI()

    def test_udacity_api_response(self):
        self.assertEqual(self.udacity_test_object.status_code(), 200)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
