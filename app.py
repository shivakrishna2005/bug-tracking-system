from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Bug Tracking System Running"

app.run(debug=True)
