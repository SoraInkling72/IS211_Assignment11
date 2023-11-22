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
    validate_email = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+')
    validate_priority_level = re.findall('[Low , Medium , High]')
    if re.match(validate_email):
        return True
        print(f"Valid email")
    if re.match(validate_priority_level):
        return True
        print(f"Valid choice")
    else:
        return False
        print(f"Please check your information and try again")

if __name__ == '__main__':
    app.run()
