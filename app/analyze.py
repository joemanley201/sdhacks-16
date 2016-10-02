import csv
from collections import Counter

def analyze_csv_file(uploaded_csv_file):
    headers = uploaded_csv_file.next()
    
    col_num = len(headers)
    data = {}
    for col_idx in range(len(headers[2:len(headers)])):
        data[headers[col_idx + 2]] = []
        
    for row in uploaded_csv_file:
        for col_idx in range(len(headers[2:col_num])):
            data[headers[col_idx + 2]].append(row[col_idx + 2])
    
    output = dict()
    for key in data.keys():
        output[key] = dict(Counter(data[key]))
    return output