from flask import render_template
from flask import Flask
from flask import request
import json
import pandas as pd
import jsonify
import csv
import io


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
	print request.method, "hello"
	return render_template('index.html')

@app.route("/upload_csv", methods=['GET', 'POST'])
def add_numbers():
	uploaded_file = request.files['uploaded_file']

	stream = io.StringIO(uploaded_file.stream.read().decode("UTF8"), newline=None)
	uploaded_csv = csv.reader(stream)
	for row in uploaded_csv:
		print row

	return "File Uploaded"

if __name__ == '__main__':
	app.run(debug=True)