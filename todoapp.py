from flask import Flask, render_template

app = Flask(__name__)

to_do_list = []
@app.route('/to_do_list.html')

def to_do_list():
    return render_template('to_do_list.html', to_do_list_items=to_do_list_items)

if __name__ == '__main__':
    app.run()
