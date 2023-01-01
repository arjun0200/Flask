###Integrate HTML with Flask
### HTTP verb GET and POST

from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

###WSGI Application
@app.route('/get')
def welcome():
    return "Nice to meet you"

@app.route('/members')
def members():
    return "Welcome to flask members"

###building url dynamically
####variables rules and url building
@app.route('/success/<int:score>')
def success(score):
    return "The person scores " +str(score)


@app.route('/learn/<int:score>')
def learn(score):
    return "The person learn " +str(score)

@app.route('/results/<int:marks>')
def results(marks):
    result = ''
    if marks<50:
        result = "learn"
    else:
        result = "success"
    return redirect(url_for(result, score = marks))
    


if __name__ == '__main__':
    app.run(debug=True)