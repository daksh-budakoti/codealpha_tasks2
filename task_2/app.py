from flask import Flask, render_template, request
from database import init_db, insert_ticket

app = Flask(__name__)
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        name = request.form['name']
        route = request.form['route']
        date = request.form['date']
        price = calculate_price(route)
        insert_ticket(name, route, date, price)
        return render_template('success.html', name=name, route=route, date=date, price=price)
    return render_template('book.html')

def calculate_price(route):
    prices = {
        "Route A": 10.0,
        "Route B": 15.0,
        "Route C": 20.0
    }
    return prices.get(route, 12.0)

if __name__ == '__main__':
    app.run(debug=True)
