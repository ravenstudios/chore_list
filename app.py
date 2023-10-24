from flask import Flask
from flask import redirect
from flask import url_for
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
# import push_notifications
import json


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
    #
    # #
    db.session.commit()
    # push_notifications.send_message(item)
    return render_template('index.html', chore=Chore.query.all())



@app.route('/delete-item', methods = ['GET', 'POST'])
def delete():
    args = request.args
    print(args.get("id"))
    Chore.query.filter_by(_id=args.get("_id")).delete()
    db.session.commit()
    return redirect("/")


@app.route('/add-new-chore-form', methods = ['GET', 'POST'])
def add_new_chore_form():
    return render_template('add-chore-form.html')

# @app.route('/add-new-chore', methods = ['GET', 'POST'])
# def add_new_chore():
#     return render_template('add-new-chore.html')
#

if __name__ == "__main__":


    with app.app_context():
        db.create_all()
    app.run(debug=True)
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=5000)
