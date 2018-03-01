from mongoengine import Document, StringField, IntField, BooleanField

# create collection
# Service la ten class
class Service(Document):
    name = StringField()
    yob = IntField()
    gender = IntField() # 0: female, 1: markle
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()
