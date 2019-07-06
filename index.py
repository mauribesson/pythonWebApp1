from flask import Flask, render_template, request
from database import Database

import hashlib

database = Database() 

app = Flask(__name__)

@app.route('/')
def home():
    data = database.query('SELECT id, username, password FROM public."user";')
    print(data)
    return render_template('home.html', users=data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/post')
@app.route('/post/<post_id>')
def post(post_id=''):
    return render_template('post.html', post_id=post_id)

@app.route('/load_user')
def load_users():
    passwordAux = "12345678".encode()
    password = hashlib.md5(passwordAux)
    database.query('INSERT INTO public."user"( "username", password) VALUES ("mrobles", "{}");'.format(password)) 
    return None


#Inicio de aplicacion
if __name__ == '__main__':
    app.run(debug=True)