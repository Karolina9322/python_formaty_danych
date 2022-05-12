from flask import Flask,render_template,request
import  requests
import datetime

current_date = (datetime.datetime.now().strftime("%d.%m.%Y"))

response = requests.get('http://api.nbp.pl/api/exchangerates/tables/A/')
data = response.json()

def convert(quantity, currency):
    for rate in data[0]['rates']:
        if currency == rate['code']:
            resultPLN = float(quantity) * float(rate['mid'])
            return round(resultPLN,2)


app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def currency_converter():
    if request.method == "POST":
      
        currency = request.form['currency']
        quantity = request.form['quantity']
        resultPLN = convert(quantity,currency)

        return render_template("kalkulator_walut.html", quantity=quantity, currency=currency, resultPLN=resultPLN, current_date=current_date)


    if request.method == 'GET':
        return render_template("kalkulator_walut.html")

if __name__ == '__main__':
    app.run(debug=True)
