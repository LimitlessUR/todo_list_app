from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.todo import Todo
from flask_app.models.user import User


@app.route('/new/todo')
def new_todo():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template('new.html',user=User.get_by_id(data))


@app.route('/create/todo',methods=['POST'])
def create_todo():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Todo.validate_todo(request.form):
        return redirect('/new/todo')
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "date": request.form["date"],
        "user_id": session["user_id"]
    }
    Todo.save(data)
    return redirect('/dashboard')