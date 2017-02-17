from app import db
from app.common import make_plain_dict_list, make_plain_dict,create_or_update_query


class PlayerChoices(db.Model):
    __tablename__ = 'playerChoices'
    id = db.Column(db.Integer, primary_key=True)
    player_temperature_id = db.Column(db.Integer)
    choice_id = db.Column(db.Integer)
    choice_type = db.Column(db.String)


def add(p_t_id, choice_id, choice_type):
    player_choice = PlayerChoices(player_temperature_id=p_t_id,
                                  choice_id=choice_id,
                                  choice_type=choice_type)
    return create_or_update_query(player_choice)


def add_list(p_t_id, choice_list):
    for choice in choice_list:
        add(p_t_id, choice['choice_id'], choice['type'])
    return