from __main__ import app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy(app)



class Chore(db.Model):

    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    repeat = db.Column(db.Boolean())
    late = db.Column(db.Boolean())
    compleated = db.Column(db.Boolean())
    notes = db.Column(db.String(300))
    assinged_to = db.Column(db.String(100))
    date_entered = db.Column(db.Date())
    date_compleated = db.Column(db.Date())


    def __init__(self, chore):

        print(f" repeat chore {'repeat' in chore.keys()}")
        self.name = chore["name"][0]
        self.repeat = "repeat" in chore.keys()
        self.late = "late" in chore.keys()
        self.compleated = "compleated" in chore.keys()
        self.notes = chore["notes"][0]
        self.assinged_to = chore["assinged_to"][0]
        self.date_entered = datetime.now()
        self.date_compleated = datetime.now()
