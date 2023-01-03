from flask import Flask, render_template
from random import randint
from sys import maxsize

app = Flask(__name__, template_folder='templates')


@app.route('/')
def welcome_screen():
    return render_template('home.html')


@app.route('/index')
def get_hello():
    return "Hello"


@app.route('/moreload')
def get_sum_number():
    random_list = []

    for i in range(1000):
        number = randint(0, maxsize)
        random_list.append(number)
    return [sum(random_list)]


if __name__ == '__main__':
    app.run()
