from flask import Blueprint, Flask, render_template, url_for, redirect, request
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import models,loads

from app.open.views import open_page
from app.close.views import close_page

from app.common import make_plain_dict, create_or_update_query
from json import JSONEncoder
from app.models import players
from app.models import songs
from app.models import types
from app.models import votes
from app.models import answers
from app.models import temperatures

app.register_blueprint(open_page, url_prefix='/open')
app.register_blueprint(close_page, url_prefix='/close')

@app.route('/')
def hello():
    return redirect('close')


@app.route('/open')
def open():
    return redirect(url_for('open.init'))
    # return render_template('intro.html')

@app.route('/close')
def close():
    return redirect(url_for('close.init'))


@app.route('/add-player/<age>/<gender>')
def add_player(age=0, gender=''):
    if age == 0 or gender == '':
        return
    player = players.add(age, gender)
    return JSONEncoder(ensure_ascii=False).encode({'player_id': player.id})


@app.route('/songs')
def get_songs():
    song_list = songs.get_all()
    return JSONEncoder(ensure_ascii=False).encode({'song_list': song_list})

@app.route('/submit-vote', methods=['POST'])
def vote():
    request_data = request.get_json()
    selected_song_list = request_data['vote']
    player_id = request_data['player_id']
    player_type_id = request_data['player_type']

    player_type = types.get(player_type_id)
    for song in selected_song_list:
        votes.add(player_id, song['id'], song['priority'])
    return JSONEncoder(ensure_ascii=False).encode({'player_type': player_type})

@app.route('/choices')
def get_choices():
    choice_list = answers.get_all()
    return JSONEncoder(ensure_ascii=False).encode({'choice_list': choice_list})

@app.route('/temperatures', methods=['POST'])
def get_temperature():
    temper = request.get_json()
    my_result = temperatures.get(temper)
    return JSONEncoder(ensure_ascii=False).encode({'my_result': my_result, 'my_temperature':temper})