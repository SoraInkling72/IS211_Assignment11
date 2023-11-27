from flask import Flask, request, redirect, render_template, flash
from typing import NoReturn
import re


app = Flask(__name__)

to_do_list = []

@app.route('/add_task', methods = ['POST'])
def new_task():
    task = request.form['task']
    email = request.form['email']
    priority = request.form['priority']
    to_do_list.append(task)
    to_do_list.append(email)
    to_do_list.append(priority)
    print(to_do_list)
    return redirect('/')

@app.route('/to_do_list.html')
def to_do_list():
    return render_template('to_do_list.html', to_do_list=to_do_list)

@app.route('/submit.html', methods = ['GET', 'POST'])
def validation():
    validate_email = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+')
    validate_priority_level = re.findall('[Low , Medium , High]')
    if re.match(validate_email):
        return True
        flash(f"Valid email")
    if re.match(validate_priority_level):
        return True
        flash(f"Valid choice")
    else:
        return redirect('/')
        flash(f"Please check your information and try again")
    return render_template('submit.html')

@app.route('/clear.html', methods = ['GET', 'POST'])
def clear():
    del to_do_list
    return redirect('/to_do_list.html')

if __name__ == '__main__':
    app.run()
