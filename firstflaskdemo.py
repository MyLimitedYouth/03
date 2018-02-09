from flask import Flask
from flask import request
from flask import render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def hello_world():
    return render_template('index.html')
    #user_agent = request.headers.get('User-Agent')
    #return '<p>Your browser is %s</p>' % user_agent
    #return 'Hello World!'

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
    #return '<h1>Hello,%s!</h1>' % name

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    render_template('500.html'), 500
if __name__=='__main__':
    app.run(debug=True)
