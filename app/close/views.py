from flask import Blueprint, render_template, redirect, url_for, request, session
from app.models import answers
from app.models import temperatures

close_page = Blueprint('close', __name__, template_folder='templates', static_folder='static')

@close_page.route('/')
def init():
    return render_template('close-index.html')
    # return redirect(url_for('close.intro'))

@close_page.route('/intro')
def intro():
    return render_template("intro.html")

@close_page.route('/choice')
def get_choices():
    choice_list = answers.get_all()

    # session = request.environ['beaker.session']
    session['my_temperature'] = 36.5
    session['my_choice_list'] = []
    current_choice = choice_list[0]
    print (session['my_temperature'])
    return redirect(url_for('close.choice', choice_id=current_choice['id']))

@close_page.route('/choices/<int:choice_id>', methods=['GET', 'POST'])
def choice(choice_id):
    choice_obj = answers.get(choice_id)
    choice_list = answers.get_all()
    # session = request.environ['beaker.session']

    for my_choice in session['my_choice_list']:
        if choice_id == my_choice['choice_id']:
            session['my_choice_list'].remove(my_choice)

    if request.method == 'POST':
        if not 'my_choice_list' in session:
            return redirect(url_for('close.get_choices'))

        my_choice = dict(choice_id=choice_id,
                         type=request.form.get('type'),
                         point=float(request.form.get('point')))
        session['my_choice_list'].append(my_choice)

        if choice_id == len(choice_list):
            return redirect(url_for('close.result'))
        return redirect(url_for('close.choice', choice_id=choice_id+1))

    return render_template("choice-answer.html", choice_list=choice_list,
                           choice=choice_obj, choice_id=choice_id)

@close_page.route('/previous')
def previous():
    # session = request.environ['beaker.session']
    last_choice = session['my_choice_list'].pop()
    # session['my_temperature'] -= last_choice['point']
    print("temperatures???  ",  session['my_temperature'])
    return redirect(url_for('close.choice', choice_id=last_choice['choice_id']))

@close_page.route('/result')
def result():
    # my_temperature = session['my_temperature']
    # session = request.environ['beaker.session']
    my_choice_list = session['my_choice_list']
    my_temperature = 36.5
    for my_choice in my_choice_list:
        # print("point ??? ",my_choice['point'])
        my_temperature += my_choice['point']
    my_result = temperatures.get(my_temperature)
    return render_template("result.html", my_temperature=my_temperature, my_result=my_result)


@close_page.route('/thanks')
def end():
    return render_template("thanks.html")
