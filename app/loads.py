# coding:UTF-8
from os import path
from xlrd import open_workbook
from app.common import create_or_update_query
from app.models.singers import Singer
from app.models.songs import Song
from app.models.types import Type
from app.models.answers import Answer
from app.models.temperatures import Temperature
from app.models.concert import Concert
from app.models.players import Player
from app.models.votes import Vote
from app.models.player_choices import PlayerChoices
from app.models.player_temperatures import PlayerTemperatures

from app import db


intro_xl_path = '/import/intro_event.xlsx'
end_xl_path = '/import/end_event.xlsx'
cwd_xl = path.dirname(path.abspath(__file__))
dir_strings = cwd_xl.split("/")
dir_strings = [i for i in dir_strings]
import_xl_path = "/".join(dir_strings)


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Excel(metaclass=Singleton):
    def load_wb(self, path):
        self.wb = open_workbook(path)
        return self.wb

    def create_all_data(self):
        self.create_concert()
        self.create_type_data(excel_session.load_wb(import_xl_path+intro_xl_path))
        self.create_singer_data(excel_session.load_wb(import_xl_path+intro_xl_path))
        self.create_song_data(excel_session.load_wb(import_xl_path+intro_xl_path))
        self.create_answer_data(excel_session.load_wb(import_xl_path+end_xl_path))
        self.create_temperature_data(excel_session.load_wb(import_xl_path+end_xl_path))

    def create_concert(self):
        if Concert.query.count():
            return
        c = Concert(name="사랑의 단상", state="open")
        create_or_update_query(c)

    def create_song_data(self,wb):
        if Song.query.count():
            return
        target_sheet = wb.sheet_by_name("songs")
        keys = [ target_sheet.cell_value(0,i) for i in range(target_sheet.ncols)]

        for row in range(target_sheet.nrows-1):
            song_row = {}
            for col, key in enumerate(keys):
                song_row[key] = target_sheet.cell_value(row+1, col)

            s = Song(title=str(song_row["title"]),
                     lyric=str(song_row["lyric"]),
                     singer_id=song_row["singer_id"],
                     type_id=song_row["type_id"])
            db.session.add(s)
        db.session.commit()

    def create_singer_data(self,wb):
        if Singer.query.count():
            return
        target_sheet = wb.sheet_by_name("singers")
        keys = [ target_sheet.cell_value(0,i) for i in range(target_sheet.ncols)]

        for row in range(target_sheet.nrows-1):
            singer_row = {}
            for col, key in enumerate(keys):
                singer_row[key] = target_sheet.cell_value(row+1, col)

            s = Singer(name=str(singer_row["name"]))
            db.session.add(s)
        db.session.commit()

    def create_type_data(self,wb):
        if Type.query.count():
            return
        target_sheet = wb.sheet_by_name("types")
        keys = [ target_sheet.cell_value(0,i) for i in range(target_sheet.ncols)]

        for row in range(target_sheet.nrows-1):
            type_row = {}
            for col, key in enumerate(keys):
                type_row[key] = target_sheet.cell_value(row+1, col)

            s = Type(name=str(type_row["name"]),
                     description=str(type_row["description"]))
            db.session.add(s)
        db.session.commit()

    def create_answer_data(self,wb):
        if Answer.query.count():
            return
        target_sheet = wb.sheet_by_name("answers")
        keys = [target_sheet.cell_value(0, i) for i in range(target_sheet.ncols)]

        for row in range(target_sheet.nrows - 1):
            answer_row = {}
            for col, key in enumerate(keys):
                answer_row[key] = target_sheet.cell_value(row + 1, col)

            s = Answer(type_a=str(answer_row["type_a"]),
                       type_b=str(answer_row["type_b"]),
                       type_a_point=answer_row["type_a_point"],
                       type_b_point=answer_row["type_b_point"])
            db.session.add(s)
        db.session.commit()

    def create_temperature_data(self,wb):
        if Temperature.query.count():
            return
        target_sheet = wb.sheet_by_name("temperatures")
        keys = [target_sheet.cell_value(0, i) for i in range(target_sheet.ncols)]

        for row in range(target_sheet.nrows - 1):
            t_row = {}
            for col, key in enumerate(keys):
                t_row[key] = target_sheet.cell_value(row + 1, col)

            s = Temperature(description=str(t_row["description"]),
                            range_start=t_row["range_start"],
                            range_end=t_row["range_end"])
            db.session.add(s)
        db.session.commit()



db.create_all()
excel_session = Excel()
excel_session.create_all_data()
# excel_session.create_keyword_table()
