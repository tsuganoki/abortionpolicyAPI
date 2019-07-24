


import requests

apikey = open('token.txt').read()
print(apikey)

url = 'https://api.abortionpolicyapi.com/v1/gestational_limits/states'
headers = { 'token': apikey }
r = requests.get(url, headers=headers)

states = r.json()

limit_at_viability = [state for state in states.keys() if states[state].get('banned_after_weeks_since_LMP') == 99]
limit_at_viability.sort()



def bans_at_viability_state(state,limit_at_viability):
	if state in limit_at_viability:
		return True
	return False


