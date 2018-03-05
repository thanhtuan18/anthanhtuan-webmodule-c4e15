from flask import Flask, render_template, request
from models.service import Service
import mlab

app = Flask(__name__)

mlab.connect()

#Serious Exercise 3:

@app.route('/')
def index():
    services = Service.objects()
    services1 = services[0:5]
    return render_template('index.html', services = services1)

@app.route('/detail/<id_to_find>')
def detail(id_to_find):
    get_info = Service.objects().get(id = id_to_find)
    return render_template('detail.html', get_info = get_info)

#Serious Exercise 4:
@app.route('/admin')
def admin():
    services2 = Service.objects()
    return render_template('admin.html', services = services2)

@app.route('/new_service', methods=["GET", "POST"])
def new_service():
    if request.method == "GET":
        return render_template('form.html')
    elif request.method == "POST":
        form = request.form
        name = form["name"]
        yob = form["yob"]
        phone = form["phone"]
        gender = form["gender"]

        new_service = Service(name=name, yob=yob, phone=phone, gender=gender)
        new_service.save()

        return "{0} {1} {2} {3} posted".format(name, yob, phone, gender)

#Serious Exercise 6:
@app.route('/updateservice/<id_to_find2>', methods=["GET", "POST"])
def updateservice(id_to_find2):
    get_service = Service.objects().get(id = id_to_find2)
    if request.method == "GET":
        return render_template('update.html', get_service=get_service)
    elif request.method == "POST":
        form = request.form
        name = form["name"]
        yob = form["yob"]
        phone = form["phone"]
        get_service.update(set__name=name, set__yob=yob, set__phone=phone)
        return "{0} {1} {2} posted".format(name, yob, phone)

if __name__ == '__main__':
  app.run(debug=True)
