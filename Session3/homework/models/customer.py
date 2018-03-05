from mongoengine import Document, StringField, EmailField, IntField, BooleanField

class Customer(Document):
    name = StringField()
    gender = StringField()
    email = EmailField()
    phone = StringField()
    job = StringField()
    company = StringField()
    contacted = StringField()
