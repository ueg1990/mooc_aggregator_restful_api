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

    def test_udacity_api_mongofy_courses(self):
        course = self.udacity_test_object.mongofy_courses()[0]
        self.assertEqual(course['title'], 'Intro to Computer Science')
    
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
