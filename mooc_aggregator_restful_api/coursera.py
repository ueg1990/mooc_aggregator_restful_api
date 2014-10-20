'''
This module retrieves information of all the courses offered by Coursera
through their Catalog APIs

Link to documentation:
https://tech.coursera.org/app-platform/catalog/

'''

import requests


class CourseraAPI(object):
    '''
    This class defines attributes and methods for the Coursera Catalog API

    '''

    COURSERA_CATALOG_API_ENDPOINT_COURSES = 'https://api.coursera.org/api/catalog.v1/courses'
    COURSERA_CATALOG_API_ENDPOINT_UNIVERSITIES = 'https://api.coursera.org/api/catalog.v1/universities'
    COURSERA_CATALOG_API_ENDPOINT_CATEGORIES = 'https://api.coursera.org/api/catalog.v1/categories'
    COURSERA_CATALOG_API_ENDPOINT_INSTRUCTORS = 'https://api.coursera.org/api/catalog.v1/instructors'
    COURSERA_CATALOG_API_ENDPOINT_SESSIONS = 'https://api.coursera.org/api/catalog.v1/sessions'

    def __init__(self):
        self.response_courses = requests.get(CourseraAPI.COURSERA_CATALOG_API_ENDPOINT_COURSES)
        self.response_universities = requests.get(CourseraAPI.COURSERA_CATALOG_API_ENDPOINT_UNIVERSITIES)
        self.response_categories = requests.get(CourseraAPI.COURSERA_CATALOG_API_ENDPOINT_CATEGORIES)
        self.response_instructors = requests.get(CourseraAPI.COURSERA_CATALOG_API_ENDPOINT_INSTRUCTORS)
        self.response_sessions = requests.get(CourseraAPI.COURSERA_CATALOG_API_ENDPOINT_SESSIONS)

    def mongofy_courses(self):
        '''
        Convert list of courses to a format that follows the database schema
        which will be inserted into the MongoDB database

        '''
        pass

if __name__ == '__main__':
    coursera_object = CourseraAPI()
    print coursera_object.response_courses.text
