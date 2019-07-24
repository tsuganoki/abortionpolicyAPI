"""Flask server for Javascript assessment.

IMPORTANT: you don't need to change this file at all to finish
the assessment!
"""

from random import randint
from flask import Flask, request, jsonify, render_template, session


import requests

apikey = open('token.txt').read()


url = 'https://api.abortionpolicyapi.com/v1/gestational_limits/states'
headers = { 'token': apikey }
r = requests.get(url, headers=headers)

states = r.json()

limit_at_viability = set(state for state in states.keys() if states[state].get('banned_after_weeks_since_LMP') == 99)


message = f"The states that ban abortion at viability are: {', '.join(limit_at_viability)}"
print(message)

app = Flask(__name__)

@app.route("/")
def show_index():
    """Show the index page"""
    states_list = [state.rstrip() for state in open("seed_data/us_states.txt")]
    # >{f:len(f) for f in fruits}
    states_dict = {}
    for state in states_list:
        states_dict[state[:2]] = state[4:]

    # print(states_dict)
    return render_template("index.html", us_states=states_dict)



@app.route("/result", methods=['GET'])
def get_results():
    """Show the results page"""
    # print(session.get("state",''))

    topics = set(request.args.getlist('topic'))
    # print("topics: ",topics)
    
    state = request.args.get('state','')
    zip_code = request.args.get('zip_code','')

    data = {}
    

    if 'gestational_limits' in topics:
        if state:
            url = 'https://api.abortionpolicyapi.com/v1/gestational_limits/states/'+ state
        elif zip_code:
            url = 'https://api.abortionpolicyapi.com/v1/gestational_limits/zips/' + zip_code
        headers = { 'token': apikey }
        r = requests.get(url, headers=headers)
        data['gestational_limits'] = r.json()
    if 'insurance' in topics:
        if state:
            url = 'https://api.abortionpolicyapi.com/v1/insurance_coverage/states/'+ state
        elif zip_code:
            url = 'https://api.abortionpolicyapi.com/v1/insurance_coverage/zips/' + zip_code
        headers = { 'token': apikey }
        r = requests.get(url, headers=headers)
        data['insurance'] = r.json()

    if 'minors' in topics:
        if state:
            url = 'https://api.abortionpolicyapi.com/v1/minors/states/'+ state
        elif zip_code:
            url = 'https://api.abortionpolicyapi.com/v1/minors/zips/' + zip_code
        headers = { 'token': apikey }
        r = requests.get(url, headers=headers)
        data['minors'] = r.json()

    if 'waiting_periods' in topics:
        if state:
            url = 'https://api.abortionpolicyapi.com/v1/waiting_periods/states/'+ state
        elif zip_code:
            url = 'https://api.abortionpolicyapi.com/v1/waiting_periods/zips/' + zip_code
        headers = { 'token': apikey }
        r = requests.get(url, headers=headers)
        data['waiting_periods'] = r.json()


# states = r.json()

    
    
    return render_template("results.html", data=data)


@app.route("/assessment")
def show_assessment():
    """Show the assessment page."""

    return render_template("js-assessment.html")

@app.route("/starwars_api")
def show_starwars_api():
    return render_template("starwars_api.html")

if __name__ == "__main__":
    app.run(port=5000,debug=True, host='0.0.0.0')
