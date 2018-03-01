import mlab
from models.service import Service

mlab.connect()

all_services = Service.objects() # lay tat car documents trong collection

first_service = all_services[0]

print(first_service.name) # lay key name trong dict
