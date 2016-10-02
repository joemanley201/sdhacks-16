from flask import render_template
from flask import Flask
from flask import request
import json
import pandas as pd
import json
import csv
import io
from analyze import analyze_csv_file
from form_groups import form_groups

app = Flask(__name__)

uploaded_stream = None
analyzed_result = None

@app.route("/", methods=['GET', 'POST'])
def index():
	return render_template('index.html')

@app.route("/upload_csv", methods=['GET', 'POST'])
def upload_csv():
	global uploaded_stream
	global analyzed_result
	uploaded_file = request.files['uploaded_file']

	stream = io.StringIO(uploaded_file.stream.read().decode("UTF8"), newline=None)
	uploaded_stream = stream
	
	uploaded_csv = csv.reader(stream)
	
	analyzed_result = analyze_csv_file(uploaded_csv)
	return json.dumps(analyzed_result)

@app.route("/finalize_groups_send_mail", methods=['GET', 'POST'])
def finalize_groups_send_mail():
	global uploaded_stream
	global analyzed_result
	
	columns = ['country','university']
	number_of_groups = 10

	groups = form_groups(columns, number_of_groups, uploaded_stream, analyzed_result)
	
	return json.dumps(groups)

if __name__ == '__main__':
	app.run(debug=True)