"""Flask server for Javascript assessment.

IMPORTANT: you don't need to change this file at all to finish
the assessment!
"""

from random import randint
from flask import Flask, request, jsonify, render_template


import requests

apikey = open('token.txt').read()
print(apikey)

url = 'https://api.abortionpolicyapi.com/v1/gestational_limits/states'
headers = { 'token': apikey }
r = requests.get(url, headers=headers)

states = r.json()

limit_at_viability = [state for state in states.keys() if states[state].get('banned_after_weeks_since_LMP') == 99]
limit_at_viability.sort()

message = f"The states that ban abortion at viability are: {', '.join(limit_at_viability)}"
print(message)

app = Flask(__name__)

@app.route("/")
def show_index():
    """Show the index page"""
    
    
    return render_template("index.html")


@app.route("/assessment")
def show_assessment():
    """Show the assessment page."""

    return render_template("js-assessment.html")



if __name__ == "__main__":
    app.run(port=5000,debug=False, host='0.0.0.0')
