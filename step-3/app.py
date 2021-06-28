from flask import Flask, render_template
from routes.pageroutes import userRoutes

app = Flask(__name__)


app.register_blueprint(userRoutes)