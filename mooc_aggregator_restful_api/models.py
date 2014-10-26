'''
In this module, we define the schema for mooc document that will be stored
in the MongoDB database

'''


from mongoengine import StringField, ListField, EmbeddedDocumentField, EmbeddedDocument, Document


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
    key = StringField()
    title = StringField()
    photo = StringField()
    trailer = StringField()
    short_summary = StringField()
    summary = StringField()
    recommended_background = StringField()
    syllabus = StringField()
    instructors = ListField(EmbeddedDocumentField(Instructor))
    faq = StringField()
    categories = ListField(StringField())
    affiliates = ListField(StringField())
