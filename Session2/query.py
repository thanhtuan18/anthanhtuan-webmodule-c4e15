import mlab_connect
from models.service import Service

mlab_connect.connect()

# all_services = Service.objects() # lay tat car documents trong collection
#
# first_service = all_services[0]
#
# print(first_service.name) # lay key name trong dict

id_to_find = "5a955b13e090f21bac346a71"

# hera = Service.objects.get(id = id_to_find) # chương trình sẽ dừng
hera = Service.objects().with_id(id_to_find)

print(hera.to_mongo()) # print tất cả của Doc

if hera is not None:
    print(hera.name) # print name của Doc
    hera.update(set__status=False, set__yob=2000) # update gía trị  mới cho Doc
    hera.reload() #cập nhật lại giá trị cho biến đang lưu trên máy, lấy từ database trên mạng
    print(hera.to_mongo()) # print tất cả của Doc
else:
    print("not found")
