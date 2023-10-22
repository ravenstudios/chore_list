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
    print("hjhjhjhjhhhjhjhijhjhkjhkjhkjhkjhkjhkjhkjhkjhkjhkjhkjhkjhkjhkjhkjhkjhkjhkjhkj")
    return render_template('index.html', chore=Chore.query.all())



@app.route('/add-test', methods = ['GET', 'POST'])
def add_new_item():


    # print(type(request.form.to_dict(flat=False)))
    # db.session.add(Chore(request.form["name"]))
    # db.session.add(Chore(request.form["repeat"]))
    # db.session.add(Chore(request.form["late"]))
    # db.session.add(Chore(request.form["compleated"]))
    # db.session.add(Chore(request.form["notes"]))
    db.session.add(Chore(request.form.to_dict(flat=False)))
    #
    # #
    db.session.commit()
    # push_notifications.send_message(item)
    return render_template('index.html', chore=Chore.query.all())



@app.route('/delete-item', methods = ['POST'])
def delete():
    Shopping_list.query.filter_by(_id=request.json["id"]).delete()
    db.session.commit()
    return redirect("/")


@app.route('/delete-multiple-items', methods = ['POST'])
def delete_mul_itmes():
    for id in request.json["data"]:
        Shopping_list.query.filter_by(_id=id).delete()
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":


    with app.app_context():
        db.create_all()
    app.run(debug=True)
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=5000)
