from flask import Blueprint, render_template, redirect, url_for, request, session
from app.models import answers
from app.models import temperatures

close_page = Blueprint('close', __name__, template_folder='templates', static_folder='..css')

@close_page.route('/')
def init():
    return redirect(url_for('close.intro'))

@close_page.route('/intro')
def intro():
    return render_template("intro.html")

@close_page.route('/choice')
def get_choices():
    choice_list = answers.get_all()
    session['my_temperature'] = 36.5
    current_choice = choice_list[0]
    return redirect(url_for('close.choice', choice_id=current_choice['id']))

@close_page.route('/choices/<int:choice_id>', methods=['GET', 'POST'])
def choice(choice_id):
    choice_obj = answers.get(choice_id)
    choice_list = answers.get_all()

    if request.method == 'POST':
        if choice_id == len(choice_list):
            return redirect(url_for('close.result'))

        if not 'my_temperature' in session:
            return redirect(url_for('close.get_choices'))
        session['my_temperature'] += float(request.form.get('point'))
        print("my temperature?? ",session['my_temperature'])
        return redirect(url_for('close.choice', choice_id=choice_id+1))

    return render_template("choice-answer.html", choice_list=choice_list,
                           choice=choice_obj, choice_id=choice_id)


@close_page.route('/result')
def result():
    my_temperature = session['my_temperature']
    my_result = temperatures.get(my_temperature)
    print(my_result)
    return render_template("result.html", my_temperature=my_temperature, my_result=my_result)


@close_page.route('/thanks')
def end():
    return render_template("thanks.html")
