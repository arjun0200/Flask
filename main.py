###Integrate HTML with Flask
### HTTP verb GET and POST

###Jinja2 template
'''
{%...%} condition statements
{{   }} expressions to print output
{#...#} this is for comments
'''

from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

###WSGI Application
@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/members')
def members():
    return "Welcome to flask members"

###building url dynamically
####variables rules and url building
@app.route('/success/<int:score>')
def success(score):
    res = ''
    if score>=50:
        res = "PASS"
    else:
        res = "Learn"
    exp = {'score':score, 'res':res}
    return render_template('result.html', result = exp)

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

@app.route('/submit',methods = ['POST', 'GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['data_science'])
        total_score = (science + maths + c + data_science)/4
    res = ''
    if total_score>=50:
        res = 'success'
    else:
        res = 'learn'
    return redirect(url_for(res, score = total_score))


if __name__ == '__main__':
    app.run(debug=True)