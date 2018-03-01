from flask import Flask, render_template
import mlab
from models.service import Service

mlab.connect()

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

if __name__ == '__main__':
  app.run(debug=True)
