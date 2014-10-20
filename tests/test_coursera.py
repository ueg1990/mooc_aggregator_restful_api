import unittest

from mooc_aggregator_restful_api import coursera


class CourseraTestCase(unittest.TestCase):
    '''
    Unit Tests for module udacity

    '''

    def setUp(self):
        self.coursera_test_object = coursera.CourseraAPI()

    def test_coursera_api_courses_response(self):
        self.assertEqual(self.coursera_test_object.response_courses.status_code, 200)

    def test_coursera_api_universities_response(self):
        self.assertEqual(self.coursera_test_object.response_universities.status_code, 200)

    def test_coursera_api_categories_response(self):
        self.assertEqual(self.coursera_test_object.response_categories.status_code, 200)

    def test_coursera_api_instructors_response(self):
        self.assertEqual(self.coursera_test_object.response_instructors.status_code, 200)

    def test_coursera_api_sessions_response(self):
        self.assertEqual(self.coursera_test_object.response_sessions.status_code, 200)

    def test_coursera_api_mongofy_courses(self):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
