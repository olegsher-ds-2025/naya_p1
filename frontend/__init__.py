from flask import Flask, redirect, url_for, request, render_template
from backend.api import work_with_series


rate = work_with_series()[2]
date_of_course = work_with_series()[1]
l_currencies = [key for key in rate.keys()]
print(rate)

app = Flask(__name__)


# current_data_day = get_current_data_day()

@app.route('/')
def home():   
    return render_template('index.html', data_single_day=rate, data_single_day_date=date_of_course)


@app.route('/rates')
def rates():
    return render_template('my_file.html', data_single_day=rate)
