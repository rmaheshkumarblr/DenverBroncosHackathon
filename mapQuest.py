import requests
import json
url = "http://www.mapquestapi.com/directions/v2/optimizedroute"

overall_json = {}
locations = {}
location = []
location.append('Denver');
location.append('Boulder');
locations['locations'] = location

querystring = {"key":"UShjaMayAC4UkuBJ5nu5rqFuraxzEOQU", "json": json.dumps(locations) }

print querystring

headers = {
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

output_of_request = json.loads(response.text)
for maneuver in output_of_request['route']['legs'][0]['maneuvers']:
	print maneuver['narrative']
#for maneuver in output_of_request['route']['maneuvers'][0]:
#	print maneuver

