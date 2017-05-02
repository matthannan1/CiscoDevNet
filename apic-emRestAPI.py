import requests

url = "https://sandboxapic.cisco.com/api/v1/ticket"

payload = "{\n\t\"username\" : \"devnetuser\",\n\t\"password\" : \"Cisco123!\"\n}"
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "bddefe31-a222-f1fc-e2f6-f57921ad33eb"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)