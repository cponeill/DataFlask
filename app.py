from flask import Flask , render_template, jsonify
#from scraper import get_data

app = Flask(__name__)

@app.route("/")
def page():
	return render_template("index.html")

@app.route("/data")
def data():
	return jsonify(get_data())




if __name__ == "__main__":
	app.run()