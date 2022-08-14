from operator import imod
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Joseph'}
    posts = [
        {
            'author': {'username': 'Joseph'},
            'body': 'nice day!'
        },
        {
            'author': {'username': 'Joseph'},
            'body': 'nice day2222!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)