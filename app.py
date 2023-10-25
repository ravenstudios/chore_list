from flask import Flask
from flask import redirect
from flask import url_for
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
# import push_notifications
import json
import datetime

app = Flask(__name__, static_url_path='/static')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///chores.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

from schema import db, Chore


@app.route('/')
def index():
    return render_template('show-chores.html', chore=Chore.query.all())



@app.route('/add-new-chore', methods = ['GET', 'POST'])
def add_new_item():
    db.session.add(Chore(request.form.to_dict(flat=False)))
    db.session.commit()
    return render_template('index.html', chore=Chore.query.all())



@app.route('/edit-chore', methods = ['GET', 'POST'])
def edit_chore():
    form = request.form.to_dict(flat=False)
    chore = Chore.query.get(form["_id"])
    chore.name = form["chore-name"][0]
    chore.notes = form["notes"][0]
    chore.assinged_to = form["assinged-to"][0]
    db.session.commit()
    return render_template('index.html', chore=Chore.query.all())


@app.route('/compleated-chore', methods = ['GET', 'POST'])
def compleated_chore():
    id = request.args.get('_id')
    chore = Chore.query.get(id)
    chore.date_compleated = datetime.datetime.now()
    chore.compleated = True
    db.session.commit()
    return render_template('index.html', chore=Chore.query.all())




@app.route('/delete-chore', methods = ['GET', 'POST'])
def delete_chore():
    args = request.args
    Chore.query.filter_by(_id=args.get("_id")).delete()
    db.session.commit()
    return redirect("/")



@app.route('/edit-chore-form', methods = ['GET', 'POST'])
def edit_chore_form():
    id = request.args.get('_id')
    print(f"id:{id}")
    return render_template('edit-chore-form.html', chore=Chore.query.get(id))



@app.route('/add-new-chore-form', methods = ['GET', 'POST'])
def add_new_chore_form():
    return render_template('add-chore-form.html')


if __name__ == "__main__":


    with app.app_context():
        db.create_all()
    app.run(debug=True)
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=5000)
