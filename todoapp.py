from flask import Flask, render_template

app = Flask(__name__)

to_do_list = []

@app.route('/')
def to_do_list():
    return render_template('to_do_list.html', to_do_list=to_do_list)

if __name__ == '__main__':
    app.run()
