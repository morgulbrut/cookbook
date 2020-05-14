from flask import Flask
app = Flask(__name__)


'''
@app.route routes a URL to a function

localhost:5000 just shows "Hello Flask" 
'''
@app.route('/') 
def hello_world():
    return '<h1>Hello Flask</h1>'

'''
just some more routes
'''
@app.route("/user/<name>")
def display_user(name):
    # A string of any length(without slashes) can be assigned to the variable name. 
    return '<h1>Hello ' + name + '</h1>'

@app.route("/total/<int:amount>")
def display_total_amount(amount):
    # Amount holds the value in int(Only Positive Integers). No other charcter accepted.
    return amount

'''
route to that renders stuff in a template

needs render_template to be imported
'''

from flask import render_template

@app.route("/template")
def display_home():
    return render_template('template.html',thing_to_say='yay, templates')