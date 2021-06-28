from flask import Blueprint, render_template
import requests
import json

userRoutes = Blueprint('userRoutes', __name__)

@userRoutes.route("/")
def UsersList():
	requestusers = requests.get("https://reqres.in/api/users")
	userlist = json.loads(requestusers.content)
	return render_template("UsersList.html", userlist = userlist['data'])

@userRoutes.route("/user/<userID>")
def UserDetail(userID):
	requestuser = requests.get("https://reqres.in/api/users/" + userID)
	user = json.loads(requestuser.content)
	return render_template("UserDetail.html", user = user['data'])