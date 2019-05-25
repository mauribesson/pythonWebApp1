from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

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

if __name__ == '__main__':
    app.run(debug=True)