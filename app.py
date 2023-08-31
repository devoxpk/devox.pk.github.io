from flask import Flask, render_template, url_for

app = Flask(_name_, static_folder='static')

@app.route('/')
def home():
    return render_template('templates/index.html')

@app.route('/products')
def products():
    return render_template('templates/products.html')

if _name_ == '_main_':
    app.run(debug=True, port=5500)