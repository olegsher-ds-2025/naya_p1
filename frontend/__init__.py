from flask import Flask, redirect, url_for, request, render_template
from backend.api import work_with_series

app = Flask(__name__)

data_single_day = work_with_series()
# current_data_day = get_current_data_day()

@app.route('/')
def home():   
    return render_template('index.html', data_single_day=data_single_day)


@app.route('/rates')
def rates():
    return render_template('my_file.html', data_single_day = data_single_day)
