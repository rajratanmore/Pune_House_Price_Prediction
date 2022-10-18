from distutils.command.config import config 
from flask import Flask, jsonify, render_template, request
from models.util import HousePrice 

app = Flask(__name__)

@app.route('/')
def hello_flast():
    print('welcome to pune House price prediciton site')
    return render_template('index.html')

@app.route('/predict', methods = ['POST', 'GET'])
def get_house_price():
    if request.method =='GET':
        print('we are using GET method')
        bath = float(request.args.get('bath'))
        balcony = float(request.args.get(balcony))
        print('bath, balcony ..>', bath, balcony)
        House = HousePrice(bath, balcony)
        charges = House.get_predicted_price()

        return render_template('index.html', prediction = charges)

    else:
        print('we are using POST method')

        bath = float(request.form.get('bath'))
        balcony = float(request.form.get('balcony'))

        print('bath, balcony from post--->', bath, balcony)

        House = HousePrice(bath, balcony)
        charges = House.get_predicted_price()

        return render_template('index.html', prediciton =charges)

    if __name__ == '__main__':
        app.run(host = '0.0.0.0', port = config.PORT_NUMBER, debug =True)
