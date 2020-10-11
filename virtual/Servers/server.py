from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def main():
	return render_template('index.html')

@app.route('/<string:page_name>')
def pages(page_name):
	return render_template(page_name)


def write_to_database(data):
	with open('database.txt', 'a') as file:
		email = data['email']
		subject = data['subject']
		message = data['message']
		file.write(f'\nemail: {email}, subject = {subject}, message = {message} ')

def write_to_csv(data):
	with open('database.csv', 'a', newline= '') as file2:
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_writer = csv.writer(file2, delimiter=',',  quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		data = request.form.to_dict()
		write_to_database(data)
		write_to_csv(data)
		print(data)
	
		return redirect('Thanks.html')
	else:
		return 'something went wron.Try again!'