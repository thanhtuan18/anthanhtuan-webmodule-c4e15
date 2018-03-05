from mlab import connect
import mongoengine
from random import randint, choice
from faker import Faker
from models.service import Service

connect()
faker = Faker()
for i in range(50):
    service = Service(image = choice(["https://i.ytimg.com/vi/uXPItbPLjKk/hqdefault.jpg",
                                    "http://media.tiin.vn//archive/images/2017/04/19/101414_3.jpg",
                                    "https://i.ytimg.com/vi/32y3RoWtmVE/maxresdefault.jpg"]),
                        name = faker.name(),
                        yob = randint(1990, 2000),
                        gender = randint(0, 1),
                        height = randint(160, 170),
                        description = "ngoan hiền, dễ thương",
                        measurements = [randint(50, 70), 90, 60],
                        phone = faker.phone_number(),
                        address = faker.address(),
                        status = choice([True, False])
                        )
    service.save()
