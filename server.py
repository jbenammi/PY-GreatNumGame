from flask import Flask, render_template, redirect, session, request
import random
app = Flask(__name__)
app.secret_key = "I<3secrets"

@app.route('/')
def index():

	if "numnum" not in session:
		session["numnum"] = random.randint(1,101)
	if "guess" not in session:
		session["guess"] = ""
	return render_template('main.html')


@app.route('/guess', methods = ['POST'])
def guessing():
	del session['guess']
	if int(request.form["number"]) == session["numnum"]:
		session['guess'] = "win"
	elif int(request.form["number"]) > session["numnum"]:
		session['guess'] = "high"
	else:
		session['guess'] = "low"
	return redirect('/')

@app.route('/clear')
def reset():
	del session['numnum']
	del session['guess']
	return redirect('/')
	
app.run(debug=True)
