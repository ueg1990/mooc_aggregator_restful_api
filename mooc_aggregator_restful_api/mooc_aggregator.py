'''
This module aggregates all the course information from different MOOC platforms
and stores them in the database (MongoDB)
'''
from mongoengine import connect
from flask.ext.mongoengine import MongoEngine

from udacity import UdacityAPI
from coursera import CourseraAPI
from models import Mooc, Instructor


class MOOCAggregator(object):
    '''
    This class defines the attributes and methods for the MOOC aggregator

    '''

    def __init__(self):
        self.udacity = UdacityAPI()
        self.coursera = CourseraAPI()
        connect('moocs')

    def update_database(self):
        '''
        Add MOOCs to the MongoDB database

        '''
        udacity_courses = self.udacity.mongofy_courses()
        coursera_courses = self.coursera.mongofy_courses()
        self._update_udacity_courses(udacity_courses)
        self._update_coursera_courses(coursera_courses)

    def _update_udacity_courses(self, courses):
    	'''
        Add Udactiy courses to the MongoDB database

        '''
        for course in courses:
            if not Mooc.objects(mooc=course['mooc'], title=course['title']):
                instructors = [Instructor(name=item['name'], bio=item['bio'], image=item['image'])
                               for item in course['instructors']]
                affiliates = [item['name'] for item in course['affiliates']]
                mooc = Mooc(course['mooc'], course['key'],course['title'],
                            course['photo'], course['trailer'], course['short_summary'],
                            course['summary'], course['recommended_background'],
                            course['syllabus'], instructors, course['faq'],
                            course['categories'], affiliates)
                mooc.save()

    def _update_coursera_courses(self, courses):
    	'''
        Add Coursera courses to the MongoDB database

        '''
        for course in courses:
            if not Mooc.objects(mooc=course['mooc'], title=course['title']):
                instructors = [Instructor(name=item['fullName'], bio=item['bio'], image=item['photo150'])
                               for item in course['instructors']]
                affiliates  = [item['name'] for item in course['universities']]
                categories  = [item['name'] for item in course['categories']]
                mooc = Mooc(course['mooc'], course['key'],course['title'],
                            course['photo'], course['trailer'], course['short_summary'],
                            course['summary'], course['recommended_background'],
                            course['syllabus'], instructors, course['faq'],
                            categories, affiliates)
                mooc.save()

if __name__ == '__main__':
    mooc = MOOCAggregator()
    mooc.update_database()
