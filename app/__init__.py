from flask import Blueprint, Flask, render_template, url_for, redirect
app = Flask(__name__)
# app.config.from_object('config')

from app.open.views import open_page

app.register_blueprint(open_page, url_prefix='/open')

@app.route('/')
def hello():
    return redirect('intro')


@app.route('/intro')
def intro():
    return redirect(url_for('open.intro'))
    # return render_template('intro.html')
