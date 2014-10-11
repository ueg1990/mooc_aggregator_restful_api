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

    def status_code(self):
        return self.response.status_code

    def courses(self):
        return self.response.json()['courses']

    def tracks(self):
        return self.response.json()['tracks']

if __name__ == '__main__':
    pass
