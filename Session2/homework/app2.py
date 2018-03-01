from flask import Flask, render_template
from mlab import connect
from models.customer import Customer

app = Flask(__name__)

connect()

@app.route('/customer')
def customer():
    customers_list1 = Customer.objects()
    return render_template('customer.html', customers_list= customers_list1)

@app.route('/')
def index():
    customers_list = Customer.objects(gender= "male", contacted= "not_yet_contacted")
    customers_list2 = customers_list[0:10]
    return render_template('index.html', customers_list2= customers_list[0:10])

if __name__ == '__main__':
  app.run(debug=True)
