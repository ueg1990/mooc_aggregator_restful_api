'''
This module retrieves the course catalog and overviews of the Udacity API

Link to Documentation:
https://s3.amazonaws.com/content.udacity-data.com/techdocs/UdacityCourseCatalogAPIDocumentation-v0.pdf

'''


import json
import requests


class UdacityAPI(object):
    '''
    This class defines attributes and methods for Udaciy API

    '''
    UDACITY_API_ENDPOINT = 'https://udacity.com/public-api/v0/courses'

    def __init__(self):
        self.response = requests.get(UDACITY_API_ENDPOINT)
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

if __name__ == '__main__':
    udacity_object = UdacityAPI()
    print len(udacity_object.get_courses())
    print udacity_object.get_courses()[0].keys()
