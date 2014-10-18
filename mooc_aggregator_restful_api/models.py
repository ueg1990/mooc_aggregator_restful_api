'''
In this module, we define the schema for mooc document that will be stored
in the MongoDB database

'''


from mongoengine import *


class Instructor(EmbeddedDocument):
    '''
    Define Embedded Document for Instructor object

    '''

    name = StringField()
    bio = StringField()
    image = StringField()


class Mooc(Document):
    '''
    Define schema for Mooc object

    '''

    mooc = StringField()
    title = StringField()
    subtitle = StringField()
    photo = StringField()
    trailer = StringField()
    short_summary = StringField()
    summary = StringField()
    recommended_background = StringField()
    syllabus = StringField()
    instructors = ListField(EmbeddedDocumentField(Instructor))
    faq = StringField()
    categories = ListField(StringField())
