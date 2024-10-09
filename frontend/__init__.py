from flask import Flask, redirect, url_for, request, render_template
from backend.api import data_single_day, current_data_day

app = Flask(__name__)

@app.route('/')
def home():   
    return render_template('index.html', data_single_day=data_single_day, current_data_day = current_data_day)


@app.route('/rates')
def rates():
    return render_template('my_file.html', data_single_day = data_single_day)
