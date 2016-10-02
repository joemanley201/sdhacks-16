from flask import render_template
from flask import Flask
from flask import request
import json
import pandas as pd


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
	print request.method, "hello"
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)