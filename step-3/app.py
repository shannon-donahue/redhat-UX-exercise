from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def testpage():
	return render_template("UsersList.html")
