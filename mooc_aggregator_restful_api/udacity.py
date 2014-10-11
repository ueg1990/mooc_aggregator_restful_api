'''
This module retrieves the course catalog and overviews of the Udacity API

Link to Documentation:
https://s3.amazonaws.com/content.udacity-data.com/techdocs/UdacityCourseCatalogAPIDocumentation-v0.pdf

'''


import json
import requests

response = requests.get('https://udacity.com/public-api/v0/courses')
for course in response.json()['courses']:
    print course['title']
    print course['homepage']
