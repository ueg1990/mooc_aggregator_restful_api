'''
This module aggregates all the course information from different MOOC platforms
and stores them in the database (MongoDB)
'''

from udacity import UdacityAPI

class MOOCAggregator(object):
    '''
    This class defines the attributes and methods for the MOOC aggregator

    '''
    MOOC_PLATFORMS = {'udacity'}

    def __init__(self):
        self.udacity = UdacityAPI()



if __name__ == '__main__':
    pass
