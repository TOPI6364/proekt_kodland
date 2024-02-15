from flask import Flask, render_template
import random

app = Flask(__name__)

#Первая страница
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/two')
def index1():
    return render_template('index1.html')

app.run(debug=True)