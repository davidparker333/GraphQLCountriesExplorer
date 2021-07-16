from flask import Flask, render_template, jsonify
import requests
import json

app = Flask(__name__)

headers = {"Content-Type": "application/json"}
base = 'https://countries.trevorblades.com'

@app.route('/')
def index():
    cont_query = json.dumps({"query": "{ continents { name code }}"})
    continents = requests.post(base, headers=headers, data=cont_query).json()['data']['continents']
    return render_template('index.html', continents=continents)

@app.route('/countries/<continent_code>')
def countries(continent_code):
    query = "".join(['{ continent(code:"', continent_code, '") { countries { name code } }'])
    print(query)
    countries_query = json.dumps({"query": query})
    print(countries_query)
    countries = requests.post(base, headers=headers, data=countries_query).json()
    print(countries)
    return render_template('countries.html')