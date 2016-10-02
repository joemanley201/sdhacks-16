from flask import render_template
from flask import Flask
from flask import request
import json
import pandas as pd
import json
import csv
import io
from analyze import analyze_csv_file

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
	
	return json.dumps(analyze_csv_file(uploaded_csv))

if __name__ == '__main__':
	app.run(debug=True)