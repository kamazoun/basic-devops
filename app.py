from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)


with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return 'Hi'


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/edit')
def edit():
    todo_list = Todo.query.all()
    return render_template('edit.html', todo_list=todo_list)


@app.route('/list')
def list_todos():
    todo_list = Todo.query.all()
    return render_template('list.html', todo_list=todo_list)


@app.post('/add')
def add():
    title = request.form.get('title')
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('list_todos'))


@app.route('/update/<int:todo_id>')
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for('list_todos'))


@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('list_todos'))


if __name__ == "__main__":
    app.run()
