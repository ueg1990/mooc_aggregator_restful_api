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
    COURSERA_CATALOG_API_ENDPOINT_UNIVERSITIES = 'https://api.coursera.org/api/catalog.v1/universities?fields=name'
    COURSERA_CATALOG_API_ENDPOINT_CATEGORIES = 'https://api.coursera.org/api/catalog.v1/categories'
    COURSERA_CATALOG_API_ENDPOINT_INSTRUCTORS = 'https://api.coursera.org/api/catalog.v1/instructors?fields=fullName,bio,photo150'
    
    def __init__(self):
        self.response_courses = requests.get(CourseraAPI.COURSERA_CATALOG_API_ENDPOINT_COURSES)
        self.response_universities = requests.get(CourseraAPI.COURSERA_CATALOG_API_ENDPOINT_UNIVERSITIES)
        self.response_categories = requests.get(CourseraAPI.COURSERA_CATALOG_API_ENDPOINT_CATEGORIES)
        self.response_instructors = requests.get(CourseraAPI.COURSERA_CATALOG_API_ENDPOINT_INSTRUCTORS)

    def mongofy_courses(self):
        '''
        Convert list of courses to a format that follows the database schema
        which will be inserted into the MongoDB database

        '''
        result = []
        for item in self.response_courses.json()['elements']:
            course = {}
            course['mooc'] = 'coursera'
            course['key'] = item['shortName']
            course['title'] = item['name']            
            course['photo'] = item['photo']
            course['trailer'] = item['video']
            course['short_summary'] = item['shortDescription']
            course['summary'] = item['aboutTheCourse']
            course['recommended_background'] = item['recommendedBackground']
            course['syllabus'] = item['courseSyllabus']
            course['faq'] = item['faq']
            
            links = item['links']
            if 'instructors' in links:
                instructors = []
                for item_x in links['instructors']:
                    for item_y in self.response_instructors.json()['elements']:
                        if item_x == item_y['id']:
                            instructors.append(item_y)
                course['instructors'] = instructors
            else:
                course['instructors'] = []

            if 'categories' in links:
                categories = []
                for item_x in links['categories']:
                    for item_y in self.response_categories.json()['elements']:
                        if item_x == item_y['id']:
                            categories.append(item_y)
                course['categories'] = categories
            else:
                course['categories'] = []

            if 'universities' in links:
                universities = []
                for item_x in links['universities']:
                    for item_y in self.response_universities.json()['elements']:
                        if item_x == item_y['id']:
                            universities.append(item_y)
                course['universities'] = universities
            else:
                course['universities'] = []

            result.append(course)
        return result

if __name__ == '__main__':
    coursera_object = CourseraAPI()
    print coursera_object.response_courses.json()
