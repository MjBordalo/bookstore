#!/usr/bin/env python
"""app.py: Starts a webapp simulating a book renting store.Small projecto to zeev ."""
__author__ = "Miguel Bordalo"

from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

import rent_price
from rent_price import *
from contants import *

app = Flask(__name__)

#init db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

books = {"Ciencia impossivel":{"type":BOOK_TYPE_FICCAO},
       "Big Blang":{"type":BOOK_TYPE_FICCAO},
       "O  meu belo Romance1":{"type":BOOK_TYPE_ROMANCE},
       "Romanticmante":{"type":BOOK_TYPE_ROMANCE},
       "O livro mais normal":{"type":BOOK_TYPE_NORMAL},
         }


#create a model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    book_type = db.Column(db.String(200), nullable=False)
    DateTake = db.Column(db.DateTime, default=datetime.utcnow)
    DateReturn = db.Column(db.DateTime, default=datetime.utcnow)

    #return string when new element is created
    def __repr__(self):
        return '<Task %r>' % self.id


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    type = db.Column(db.String(200), default=datetime.utcnow)

    #return string when new element is created
    def __repr__(self):
        return '<Book %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':

        # task_content = request.form['content']
        DateTake = datetime.strptime(request.form['DateTake'], '%Y-%m-%d')
        DateReturn =datetime.strptime(request.form['DateReturn'], '%Y-%m-%d')

        book_name= request.form['bookDropdown']
        book_type= books[book_name]["type"]

        new_task = Todo(content=book_name,book_type=book_type, DateTake=DateTake,DateReturn=DateReturn)

        # try:
        db.session.add(new_task)
        db.session.commit()
        return redirect('/')
        # except:
        #     return 'There was an issue adding your task'

    else:
        #try:
        tasks = Todo.query.order_by(Todo.DateTake).all()

        sum_extracto = sum([compute_price(task.DateTake.date() ,task.DateReturn.date(),task.book_type) for task in tasks])


        return render_template('index.html', tasks=tasks,books=books, today=datetime.today().strftime("%Y-%m-%d"), compute_price=compute_price,sum_extracto=sum_extracto)

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'

if __name__ == "__main__":
    app.run(debug=True)