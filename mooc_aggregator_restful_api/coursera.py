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

    COURSERA_CATALOG_API_ENDPOINT_COURSES = 'https://api.coursera.org/api/catalog.v1/courses?fields=name,shortDescription,photo,video,faq,aboutTheCourse,courseSyllabus,recommendedBackground,aboutTheInstructor&includes=instructors,categories,universities'
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
        result = []
        for item in self.response_courses['elements']:
            course = {}
            course['mooc'] = 'coursera'
            course['title'] = item['name']            
            course['photo'] = item['photo']
            course['trailer'] = item['video']
            course['short_summary'] = item['shortDescription']
            course['summary'] = item['aboutTheCourse']
            course['recommended_background'] = item['recommendedBackground']
            course['syllabus'] = item['courseSyllabus']
            course['faq'] = item['faq']
            # instructors, categories, universities
            links = item['links']
            if 'instructors' in links:
                pass
            else:
                course['instructors'] = []

            if 'categories' in links:
                pass
            else:
                course['categories'] = []

            if 'universities' in links:
                pass
            else:
                course['universities'] = []

            result.append(course)

if __name__ == '__main__':
    coursera_object = CourseraAPI()
    print coursera_object.response_courses.json()
