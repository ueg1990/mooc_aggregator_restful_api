'''
In this module, we define the schema for mooc document that will be stored
in the MongoDB database

'''


from mongoengine import *


class Mooc(Document):
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


class Instructor(EmbeddedDocument):
    name = StringField()
    bio = StringField()
    image = StringField()
