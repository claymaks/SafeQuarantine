# !/usr/bin/env python
from flask import redirect, url_for

from app import app


@app.errorhandler(404)
def page_404(e):
    print("[404]")
    print(f". URL: {request.url}")
    print(f". METHOD: {request.method}")
    print(f". ERROR: {e}")
    print(f". REROUTING")
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
    print(". LIVE")
    return render_template("index.html")


