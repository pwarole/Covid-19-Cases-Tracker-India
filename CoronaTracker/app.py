from flask import Flask , render_template, redirect
import requests
import pandas as pd 
import json
app = Flask('__name__')

@app.route('/')
def home():
    response = requests.get("https://api.covid19india.org/v2/state_district_wise.json")
    data=response.json()
    return render_template('index.html',post=data)

if __name__== "__main__":
    app.run(debug=True)