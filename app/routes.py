# !/usr/bin/env python
import os
import time
from flask import redirect, url_for, render_template, send_from_directory

from app import app, db
from app.models import *


@app.errorhandler(404)
def page_404(e):
    print("[404]")
    print(f". URL: {request.url}")
    print(f". METHOD: {request.method}")
    print(f". ERROR: {e}")
    print(f". REROUTING")
    time.sleep(.25)
    return redirect(url_for('index'))


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico')


@app.route('/robots.txt')
def robots():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'robots.txt')


@app.route('/')
@app.route('/index')
def index():
    """
    
    """
    print("[STATUS] [INDEX]")
    c = Covid.query.get(1)
    if not c:
        print(". CREATING ID 1 FOR DB")
        c = Covid(id=1)
        db.session.add(c)
        db.session.commit()
    else:
        print(". BATHROOM:", c.bathroom)
        print(". KITCHEN:", c.kitchen)
    time.sleep(.25)
    return render_template("index.html", bathroom_bool=c.bathroom, kitchen_bool=c.kitchen)


@app.route('/bathroom')
def bathroom():
    print ("bathroom")
    c = Covid.query.get(1)
    c.bathroom = not c.bathroom
    db.session.commit()
    return ("nothing")


@app.route('/kitchen')
def kitchen():
    print ("kitchen")
    c = Covid.query.get(1)
    c.kitchen = not c.kitchen
    db.session.commit()
    return ("nothing")


