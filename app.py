from flask import Flask,redirect,render_template,url_for,request
from flask_sqlalchemy import SQLAlchemy
from datetime import  datetime
from forms import DayForm
import time
from datetime import datetime





app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///diary.db'
app.config['SECRET_KEY']='c520e1a52a97a1ca670db1ec943ea40fbf4a'

db=SQLAlchemy(app)


#model

class Day(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20),nullable=False)
    day=db.Column(db.String(200),nullable=False)
    date_posted=db.Column(db.DateTime,default= datetime.utcnow().strftime('%d/%m/%Y %H:%M'))

@app.route('/')
def index():
    days = Day.query.all()

    return render_template('index.html',title="Home",days=days)
@app.route('/day')
def Daily():
    form=DayForm()

    return render_template('add.html', title="How's Today?", form=form)

@app.route('/add', methods=['POST'])
def AddData():
    form=DayForm()

    name=request.form.get('name')
    day=request.form.get('day')

    Days=Day(name=name,day=day)
    db.session.add(Days)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)