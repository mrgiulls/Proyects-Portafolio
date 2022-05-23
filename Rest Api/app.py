from crypt import methods
from click import edit
from flask import Flask, jsonify, request
from itsdangerous import json

app = Flask(__name__)

from products import products

@app.route('/ping')
def ping():
    return jsonify({"message":"Pong!"})

@app.route('/products', methods=['GET'])
def getProducts():
    return jsonify(products)

@app.route('/products/<string:product_name>')
def getProduct(product_name):
    listpro = [product for product in products if product['name'] == product_name]
    if (len(listpro) >0):
        return jsonify({"product": listpro[0]})
    return jsonify({"message":"Product not found"})

@app.route('/products', methods=['POST'])
def addProduct():
   new_product = {
       "nombre": request.json['name'],
       "precio": request.json['price'],
       "cantidad": request.json['quantity']
   }
   products.append(new_product)
   return jsonify({"message":"Product added Succesully", "product": products})

@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    editproduct = [product for product in products if product ['name'] == product_name]
    if (len(editproduct) >0):
        editproduct[0]['name'] = request.json['name']
        editproduct[0]['price'] = request.json['price']
        editproduct[0]['quantity']= request.json['quantity']
        return jsonify({
            "message": "Producto Update", 
            "Product": editproduct[0]
        })
    return jsonify({"message":"Product not found"})

@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    deleteproduct = [product for product in products if product ['name'] == product_name]
    if len(deleteproduct) >0:
        products.remove(deleteproduct[0])
        return jsonify({
            "message": "Product Deleted",
            "products": products
        })
    return jsonify({"message": "Product not found"})

if __name__ == '__main__':
    app.run(debug=True, port=4000)
    