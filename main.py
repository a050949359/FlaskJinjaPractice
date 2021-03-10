import flask
from flask import render_template
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = flask.Flask(__name__)
app.config["DEBUG"] = True
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="首页")


@app.route('/login')
def login():
    return render_template('x/login.html', title='登录')


@app.route('/register')
def register():
    return render_template('register.html', title='注册')

if __name__ == '__main__':
    app.run(port=5000)

