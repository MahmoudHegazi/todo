#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import render_template, request, jsonify, flash
from flask_sqlalchemy import SQLAlchemy
from db_class import List, Todo, db, app
import requests
import os
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename



@app.route('/')
def index():
    todos = Todo.query.all()
    #todo = Todo(name='Lovely Todo')
    #db.session.add(todo)
    #db.session.commit()
    return render_template('index.html', todos=todos)

@app.route('/delete_todo', methods=['POST','GET'])
def deleteTodo():
    if request.method == 'POST':
        todo_id = request.form.get("todo_id")
        todo_delete = Todo.query.filter_by(id=todo_id).first()
        db.session.delete(todo_delete)
        db.session.commit()
        db.session.close()
        flash_message = todo_id
        flash_message += '| Item Deleted ID: ' + str(todo_id)
        return flash_message
    return
if __name__ == '__main__':
    app.secret_key = 'S&Djry636qyye21777346%%^&&&#^$^^y___'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
