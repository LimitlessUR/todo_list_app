from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Todo:
    db_name = 'todo'

    def __init__(self,db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.description = db_data['description']
        self.date = db_data['date']
        self.user_id = db_data['user_id']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO todos (name, description, date, user_id) VALUES (%(name)s,%(description)s,%(date)s,%(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @staticmethod
    def validate_todo(todo):
        is_valid = True
        if len(todo['name']) < 3:
            is_valid = False
            flash("Name must be at least 3 characters","todo")
        if len(todo['description']) < 3:
            is_valid = False
            flash("Description must be at least 3 characters","todo")
        if todo['date'] == "":
            is_valid = False
            flash("Please enter a date","todo")
        return is_valid