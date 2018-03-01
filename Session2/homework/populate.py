from mlab import connect
from models.customer import Customer
from faker import Faker
from random import randint, choice

connect()

faker = Faker()

for i in range(30):
    customer = Customer(name = faker.name(),
                        gender = choice(["male", "female"]),
                        email = "abc@gmail.com",
                        phone = faker.phone_number(),
                        job = faker.job(),
                        company = faker.company(),
                        contacted = choice(["not_yet_contacted", "contacted"])
                        )
    customer.save()
