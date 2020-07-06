from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def home():
	return render_template('home.html')


@app.route('/about')
def about():
	return render_template('about.html')


@app.route('/destinations')
def destinations():
	return render_template('destinations.html')


@app.route('/application')
def application():
	return render_template('application.html')


@app.route('/form', methods=["POST"])
def form():
	firstname = request.form.get('firstname')
	lastname = request.form.get('lastname')
	phone = request.form.get('phone')
	email = request.form.get('email')
	trip = request.form.get('trip')
	return render_template('form.html', firstname=firstname, 
		lastname=lastname, phone=phone, email=email, trip=trip)
