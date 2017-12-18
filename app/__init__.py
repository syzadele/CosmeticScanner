from flask import Flask, request


app = Flask(__name__)

from app import routes

app.run(debug=True)
