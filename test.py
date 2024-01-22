from flask import Flask, request, redirect, render_template, flash
import re


app = Flask(__name__)

task_list = []


@app.route('/')
def to_do_list():
    return render_template('to_do_list.html', task_list=task_list)



if __name__ == '__main__':
    app.run()