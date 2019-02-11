from app import app
from flask import render_template, url_for, redirect

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home', topheader='Welcome', hobbies=hobbies)

hobbies = ['Playing hockey', 'Going to Bruins games', 'Watching sports on TV', 'Playing video games', 'Collecting Air Jordan sneakers']


@app.route('/about')
def about(name = 'Bill'):
    return render_template('about.html', title='About Me', topheader=name, description=description)

description = "My name is Bill and I'm making this website in my class at Coding Temple in Boston. I am enjoying learning how to code, and look forward to learning more. At night you can find me playing goalie in the hockey league I play in, or I will be watching a game, whether it is the Bruins game or another game that is on."
