from flask import Flask, render_template, redirect, url_for, session
from datetime import datetime, timedelta

app = Flask(__name__)

app.secret_key = 'ness001'


# greetings
def greet():
    h = datetime.now().hour
    if 4 <= h <= 11:
        return 'Morning'
    if 11 < h <= 18:
        return 'Good afternoon'
    if 18 < h <= 24 or 0 <= h < 4:
        return 'Good Evening'


# date convert session string -> datetime.datetime
def left():
    d = datetime.now()
    dd = datetime.strptime(session['d'], '%a, %d %b %Y %H:%M:%S %Z') - d
    return dd.days

import os
import random
def shuffle_image():
    image_list=os.listdir('/Users/ness001/dayoff/static')
    image=random.choice(image_list)
    if image!='.DS_Store':
        return image
    else:
        return random.choice(image_list)

@app.route("/form", methods=['get', 'post'])
def form():
    form = goal_form()
    # session
    # session must be used inside the request.
    session.permanent = True
    app.permanent_session_lifetime = timedelta(days=100)

    if form.validate_on_submit():
        session['n'] = form.name.data
        session['e'] = form.event.data
        session['d'] = form.due.data
        return redirect(url_for("dayoff"))
    return render_template('form.html', form=form)


# use session to save data
@app.route("/", methods=['get', 'post'])
def dayoff():
    g = greet()
    return render_template('dayoff.html', n=session['n'], e=session['e'], d=left(), g=g,image=shuffle_image())


# user form

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import data_required, input_required


class goal_form(FlaskForm):
    name = StringField('Name', validators=[data_required()])
    event = StringField('Event', validators=[data_required()])
    due = DateField('Due', validators=[input_required()])
    update = SubmitField('Update')
