'''
This module retrieves the course catalog and overviews of the Udacity API

Link to Documentation:
https://s3.amazonaws.com/content.udacity-data.com/techdocs/UdacityCourseCatalogAPIDocumentation-v0.pdf

'''

import requests


class UdacityAPI(object):
    '''
    This class defines attributes and methods for Udaciy API

    '''
    UDACITY_API_ENDPOINT = 'https://udacity.com/public-api/v0/courses'

    def __init__(self):
        self.response = requests.get(UdacityAPI.UDACITY_API_ENDPOINT)
        self.courses = self.response.json()['courses']
        self.tracks = self.response.json()['tracks']

    def status_code(self):
        '''
        Return status code of response object

        '''

        return self.response.status_code

    def get_courses(self):
        '''
        Return list of course objects for all courses offered by Udacity

        '''
        return self.courses

    def get_tracks(self):
        '''
        Return list of tracks offered by Udacity

        '''
        return self.tracks

    def mongofy_courses(self):
        '''
        Convert list of courses to a format that follows the database schema
        which will be inserted into the MongoDB database

        '''
        return [{'mooc': 'udacity', 'title': item['title'],
                 'photo': item['image'], 'trailer': item['teaser_video']['youtube_url'],
                 'short_summary': item['short_summary'], 'summary': item['summary'],
                 'recommended_background': item['required_knowledge'], 'syllabus': item['syllabus'],
                 'instructors': item['instructors'], 'faq': item['faq'], 'categories': item['tracks'],
                 'affiliates' : item['affiliates']} for item in self.get_courses()]
        # result = []
        # for item in self.get_courses():
        #     course = {}
        #     course['mooc'] = 'udacity'
        #     course['title'] = item['title']
        #     course['subtitle'] = item['subtitle']
        #     course['photo'] = item['image']
        #     course['trailer'] = item['teaser_video']['youtube_url']
        #     course['short_summary'] = item['short_summary']
        #     course['summary'] = item['summary']
        #     course['recommended_background'] = item['required_knowledge']
        #     course['syllabus'] = item['syllabus']
        #     course['instructors'] = item['instructors']
        #     course['faq'] = item['faq']
        #     course['categories'] = item['tracks']

if __name__ == '__main__':
    udacity_object = UdacityAPI()
    courses = udacity_object.get_courses()[0]
    print udacity_object.mongofy_courses()[0]
