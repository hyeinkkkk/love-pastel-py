from flask import Blueprint, render_template, redirect, url_for


open_page = Blueprint('open', __name__, template_folder='templates', static_folder='static')

@open_page.route('/')
def init():
    return render_template("index.html")
#     return redirect(url_for('intro'))


# @open_page.route('/intro')
# def intro():
#     return render_template("intro.html")
#
# @open_page.route('/survey')
# def survey():
#     return render_template('survey.html')