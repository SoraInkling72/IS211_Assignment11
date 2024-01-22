from flask import Flask, request, redirect, render_template, flash
import re
import pickle
import os

app = Flask(__name__)

todo_file = 'todo_list.pkl'

if os.path.exists(todo_file):
    with open(todo_file, 'rb') as file:
        task_list = pickle.load(file)
else:
    task_list = []


@app.route("/")
def index():
    return render_template("to_do_list.html", task_list=task_list)


@app.route("/submit", methods=["POST"])
def submit():
    task = request.form["task"]
    email = request.form["email"]
    priority = request.form["priority"]

    # validate email
    if not re.match(r"[\w.+-]+@[\w-]+\.[\w.-]+", email):
        flash("Invalid email")
        return redirect("/")

    # validate priority
    if priority not in ["Low", "Medium", "High"]:
        flash("Invalid choice")
        return redirect("/")

    task_list.append({"task": task, "email": email, "priority": priority})
    return redirect("/")

@app.route('/clear', methods=['POST'])
def clear_list():
    global task_list
    task_list = []
    return redirect("/")

@app.route('/delete/<int:index>', methods=['POST'])
def delete_todo(index):
    # Delete the specified To-Do item
    if 0 <= index < len(task_list):
        del task_list[index]
    return redirect('/')

@app.route('/save', methods=['POST'])
def save_todo():
    # Save To Do list to file using pickle
    with open(todo_file, 'wb') as file:
        pickle.dump(task_list, file)
    return redirect('/')



if __name__ == "__main__":
    app.run(port=5000)
