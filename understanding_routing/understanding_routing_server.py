# Understanding Routing assignment
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def say(name):
    return 'Hi' +' '+ name

@app.route('/repeat/<num>/<str>')
def repeat(num, str):
    return (str+' ') * int(num)


@app.route('/bonus/<int:num>')
def bonus(num):
    return "Ninja Bonus!"

@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again."

if __name__=="__main__":
    app.run(debug=True)