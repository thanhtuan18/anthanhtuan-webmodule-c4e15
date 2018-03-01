import mlab
from models.service import Service
from faker import Faker
from random import randint, choice

mlab.connect()

faker = Faker()

for i in range(50):
    print("Saving service", i + 1, "...")
    service = Service(name = faker.name(),
                        yob = randint(1990, 2000),
                        gender = randint(0, 1),
                        height = randint(150, 180),
                        phone = faker.phone_number(),
                        address = faker.address(),
                        status = choice([True, False]))

    service.save()
