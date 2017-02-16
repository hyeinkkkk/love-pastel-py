from flask import Blueprint, render_template, redirect, url_for, request, session
from app.models import answers

close_page = Blueprint('close', __name__, template_folder='templates', static_folder='..css')

@close_page.route('/')
def init():
    session['login'] = True
    return redirect(url_for('close.intro'))

@close_page.route('/intro')
def intro():
    print("session is available ", session['login'])
    return render_template("intro.html")

@close_page.route('/choice')
def get_choices():
    choice_list = answers.get_all()
    current_choice = choice_list[0]
    return redirect(url_for('close.choice', choice_id=current_choice['id']))

@close_page.route('/choices/<int:choice_id>', methods=['GET', 'POST'])
def choice(choice_id):
    choice_obj = answers.get(choice_id)
    choice_list = answers.get_all()
    if request.method == 'POST':
        if choice_id == 1:
            my_temperature = 36.5
        else:
            my_temperature = int(request.form.get('my_temperature'))
            my_temperature += int(request.form.get('point'))
        if choice_id == len(choice_list):
            return redirect(url_for('close.result'))
        else:
            choice_obj = choice_list[choice_id]
            choice_id = choice_obj['id']
    else:
        my_temperature = 36.5
        print("get?? answer_id ?? ", choice_id)
    return render_template("choice-answer.html", choice_list=choice_list,
                           choice=choice_obj, choice_id=choice_id, my_temperature=my_temperature)


@close_page.route('/result')
def result():
    return render_template("result.html")


@close_page.route('/thanks')
def end():
    return render_template("thanks.html")
