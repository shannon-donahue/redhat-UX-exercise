from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

#default to get method unless specifically declared
@app.route("/")
def testpage():
	requestusers = requests.get("https://reqres.in/api/users")
	userlist = json.loads(requestusers.content)
	return render_template("UsersList.html", userlist = userlist['data'])
