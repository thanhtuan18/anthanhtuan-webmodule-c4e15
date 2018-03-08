from flask import Flask, render_template, redirect, url_for, request
import mlab_connect
from models.service import Service

mlab_connect.connect()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/search')
# def search():
#     services = Service.objects()
#     return render_template("search.html", all_services=services)

@app.route('/search/<int:gender>')
def search(gender):
    services = Service.objects(gender=gender, yob__lte = 1998, height__gte = 160, address__contains = "Ha Noi")
    return render_template("search.html", all_services=services)

@app.route('/admin')
def admin():
    services = Service.objects()
    return render_template('admin.html', services = services)

@app.route('/delete/<service_id>')
def delete(service_id):
    service_to_delete = Service.objects().with_id(service_id)

    if service_to_delete is None:
        return "Not found"

    service_to_delete.delete()
    return redirect(url_for("admin"))  #"Deleted " + service_id #url_for dẫn đến hàm

@app.route('/new-service', methods=["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template('new-service.html')
    elif request.method == "POST":
        form = request.form
        name = form["name"]
        yob = form["yob"]
        phone = form["phone"]

        new_service = Service(name=name, yob=yob, phone=phone, gender=1, height=170, address="Hà Nội", status=True)
        new_service.save()
        return "{0} {1} {2} posted".format(name, yob, phone)

if __name__ == '__main__':
  app.run(debug=True)
