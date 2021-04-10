import json
import requests
requests.packages.urllib3.disable_warnings()
access_token = "MmI5MjM3ZTctMjFmZi00MDljLWI5NTctY2U3MzNiYjdhNDExMzFjOGYwZTYtYzFh_PF84_consumer"
api_url = "https://10.10.20.48/restconf/data/ietf-interfaces:interfaces"
headers = { "Accept": "application/yang-data+json",
 "Content-type":"application/yang-data+json"
 }
basicauth = ("developer", "C1sco12345")
url = 'https://webexapis.com/v1/messages'
webexheaders = {
'Authorization': 'Bearer {}'.format(access_token),
'Content-Type': 'application/json'
}

resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)
print(resp)
response_json = resp.json()
print(json.dumps(response_json, indent=4))
params = {
  "toPersonEmail": "jayharold@lsu.edu.ph",
  "text": json.dumps(response_json, indent=4)
}
res = requests.post(url, data=json.dumps(params),headers=webexheaders, verify=False)