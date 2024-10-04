from flask import Flask, redirect, url_for, request, render_template
from backend.api import x,y,z

# print(y)
# print(x)
print(z.get('Date'))
print(z.get(' USD'))


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', x=x, y=y)


@app.route('/rates')
def rates():
    return render_template('my_file.html', z = z.get('Date'), usd = z.get(' USD'))
