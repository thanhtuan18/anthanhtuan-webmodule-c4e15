from mongoengine import Document, StringField, IntField, BooleanField, ImageField, ListField, URLField

# create collection
# Service la ten class
class Service(Document):
    image = URLField()
    name = StringField()
    yob = IntField()
    gender = IntField() # 0: female, 1: markle
    height = IntField()
    description = StringField()
    measurements = ListField()
    phone = StringField()
    address = StringField()
    status = BooleanField()
