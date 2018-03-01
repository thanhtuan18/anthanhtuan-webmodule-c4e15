from flask import Flask, render_template
from mlab import connect
from models.service import Service

# app = Flask(__name__)

connect()

#Ex2:
id_to_find = "5a955b13e090f21bac346a71"
document = Service.objects.get(id = id_to_find)

#Ex3:
document.delete()



# @app.route('/about-me')
# def index():
#     return render_template('index.html')
#
# if __name__ == '__main__':
#   app.run(debug=True)
