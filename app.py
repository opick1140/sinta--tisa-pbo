from flask import Flask, render_template

app = Flask(__name__)

# Data produk (contoh)
products = [
    {"id": 1, "name": "Kaos Polos", "price": 75000, "image": "kaos.jpg"},
    {"id": 2, "name": "Kemeja Flanel", "price": 120000, "image": "flanel.jpg"},
    {"id": 3, "name": "Jaket Hoodie", "price": 150000, "image": "hoodie.jpg"},
    {"id": 4, "name": "Sweater Rajut", "price": 175000, "image": "sweater.jpg"},
    {"id": 5, "name": "Celana Jeans", "price": 200000, "image": "jeans.jpg"},
    {"id": 6, "name": "Celana Chino", "price": 185000, "image": "chino.jpg"},
    {"id": 7, "name": "Sepatu Sneakers", "price": 250000, "image": "sneakers.jpg"},
    {"id": 8, "name": "Topi Baseball", "price": 90000, "image": "topi.jpg"},
    {"id": 9, "name": "Tas Ransel", "price": 300000, "image": "ransel.jpg"},
    {"id": 10, "name": "Jam Tangan", "price": 500000, "image": "jam.jpg"},
]

@app.route('/')
def home():
    return render_template("index.html", products=products)

if __name__ == '__main__':
    app.run(debug=True)
