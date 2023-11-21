from flask import Flask, request, redirect, render_template
import re

app = Flask(__name__)

to_do_list = []

@app.route('/signup', methods = ['POST'])
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

@app.route('/submit.html', methods = ['POST'])
def validation():
    validate_email = re.search('^["@yahoo.com" , "@gmail.com , @aol.com , @outlook.com]')
    validate_priority_level = re.search('[Low , Medium , High]')
    if validate_email == re.search('^["@yahoo.com" , "@gmail.com , @aol.com , @outlook.com]'):
        return True
    if validate_priority_level == re.search('[Low , Medium , High]'):
        return True
    else:
        return False
        print(f"Please check your information and try again")

if __name__ == '__main__':
    app.run()
