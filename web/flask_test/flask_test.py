from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/hello/<name>')
def hello_world(name):
    return render_template('hello.html', name=name)

@app.route('/user/<username>', methods=['POST','GET'])
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/test/<num>')
def print_number(num):
    return num

if __name__ == '__main__':
    app.run()
