from crypt import methods
from operator import imod
from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Log In', form=form)