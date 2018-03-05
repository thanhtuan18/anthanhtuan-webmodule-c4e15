from mlab import connect
from models.service import Service

connect()

Serious Exercise 1:
all_services = Service.objects()
for service in all_services:
    service.delete()

:
