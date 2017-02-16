from datetime import datetime
from app import db


def create_or_update_query(obj):
    db.session.add(obj)
    db.session.flush()
    db.session.commit()
    return obj


def make_plain_dict_list(obj):
    result = []
    for element in obj:
        result.append(make_plain_dict(element))

    return result


def make_plain_dict(obj):
    if obj is None:
        return {}
    row = obj.__dict__.copy()
    del row['_sa_instance_state']
    for key in row:
        if isinstance(row[key], datetime):
            row[key] = int(row[key].strftime("%s"))

    return row