from flask import Blueprint, render_template, redirect, url_for

open_page = Blueprint('open', __name__, template_folder='templates', static_folder='..css')

@open_page.route('/')
def init():
    return redirect(url_for('intro'))

@open_page.route('/intro')
def intro():
    return render_template("intro.html")
