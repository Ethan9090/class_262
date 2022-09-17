from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")

def main():
	return render_template("index.html")

@app.route('/', methods=['POST'])

def meth_operations():
	equation = request.form['text']
	operation = request.form['operation']

	result = 'https://newton.now.sh/api/v2//' + operation +'/' + equation

	data = requests.get(variable).json()

	answer = variable['result']

	render_template(index.html,result=answer,equation=equation)

if __name__ == "__main__":
	app.run