from flask import Flask, request
from flask import render_template
import json

app = Flask(__name__)

@app.route("/")
def index():
    with open('data/products.json') as f:
        data = json.load(f)

    return render_template('index.html', products=data)

@app.route("/product")
def product_detail():
    with open('data/products.json') as f:
        data = json.load(f)

    productId = request.args.get('q')
    
    productItem = list(filter(
        lambda x: x["id"]==productId,
        data
    ))

    print(productItem)

    if len(productItem)<1:
        return "Product not found"
    else:
        return render_template('product.html', product=productItem[0])

if __name__ == "__main__":
    app.run(debug=True)