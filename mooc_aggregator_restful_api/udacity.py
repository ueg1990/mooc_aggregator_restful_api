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

    def __init__(self):
        UDACITY_API_ENDPOINT = 'https://udacity.com/public-api/v0/courses'
        self.response = requests.get(UDACITY_API_ENDPOINT)
        self.courses = self.response.json()['courses']
        self.tracks = self.response.json()['tracks']

    def status_code(self):
        return self.response.status_code

    def get_courses(self):
        return self.courses

    def get_tracks(self):
        return self.tracks

if __name__ == '__main__':
    udacity_object = UdacityAPI()
    print len(udacity_object.get_tracks())
