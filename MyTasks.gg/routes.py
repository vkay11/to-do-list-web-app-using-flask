from app import app
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from forms import AddTaskForm, DeleteTaskForm
from models import Task, db
from datetime import datetime

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    tasks = Task.query.all()
    
    return render_template('index.html', tasks=tasks)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddTaskForm()
    if form.validate_on_submit():
        task = Task(text=form.text.data, date=datetime.now())
        db.session.add(task)
        db.session.commit()
        flash('The Task was successfully added to the Database.!')
        return redirect(url_for('index'))

    return render_template('add.html', form=form)


@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit(task_id):
    task = Task.query.get(task_id)
    form = AddTaskForm()
    if task:
        if form.validate_on_submit():
            task.text = form.text.data
            task.data = datetime.now()
            db.session.commit()
            flash('The Task was successfully updated.!')
            return redirect(url_for('index'))

        form.text.data = task.text
        return render_template('edit.html', form=form, task_id=task_id)
    else:
        flash("The Task ID does not exist.!")
    return redirect(url_for('index'))


@app.route('/delete/<int:task_id>', methods=['GET', 'POST'])
def delete(task_id):
    task = Task.query.get(task_id)
    form = DeleteTaskForm()

    if task:
        if form.validate_on_submit():
            db.session.delete(task)
            db.session.commit()
            flash("The Task was successfully deleted from the Database.!")
            return redirect(url_for('index'))
        
        return render_template('delete.html', form=form, task_id=task_id, text=task.text)

    else:
        flash("The Task ID does not exist.!")
    return redirect(url_for('index'))
