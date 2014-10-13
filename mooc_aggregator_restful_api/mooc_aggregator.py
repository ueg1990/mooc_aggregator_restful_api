'''
This module aggregates all the course information from different MOOC platforms
and stores them in the database (MongoDB)
'''

from udacity import UdacityAPI


class MOOCAggregator(object):
    '''
    This class defines the attributes and methods for the MOOC aggregator

    '''
    MOOC_PLATFORMS = {'udacity', 'coursera'}

    def __init__(self):
        self.udacity = UdacityAPI()
        self.coursera = CourseraAPI()

if __name__ == '__main__':
    pass
