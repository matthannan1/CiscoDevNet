# Import modules
import requests
import json

# Disable warnings
requests.packages.urllib3.disable_warnings()

# Variables
apic_em_ip = "https://sandboxapic.cisco.com/api/v1"
api_call = "/ticket"

# Payload contains authentication information
payload = {"username":"devnetuser","password":"Cisco123!"}

# Header info
headers = {"content-type":"application/json"}

# Combine apic_em_ip and api_call vars into one variable call url
url = apic_em_ip + api_call
response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False).json()

# Print the respond body
print("Authentication token: ",response["response"]["serviceTicket"])
