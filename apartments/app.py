from flask import Flask
import requests
app = Flask(__name__)
@app.route('/')
def hello():
    return "This is the apartment microservice!"