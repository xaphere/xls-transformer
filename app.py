from flask import Flask, abort, request
from markupsafe import escape
import pandas as pd
import argparse

def transform_file(filename):
    df = pd.read_excel(filename)
    return df.to_csv(header=False)

app = Flask(__name__)

@app.route('/transform', methods=['POST'])
def transform():
    data = request.get_json()
    try:
        csv = transform_file(data['fileURL'])
    except FileNotFoundError:
        abort(404)
    return csv
