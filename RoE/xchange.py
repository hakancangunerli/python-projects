import requests,json

source = input("what is the source currency? ")
target = input("what is the target currency? ")

url = "https://api.sandbox.transferwise.tech/v1/rates?source=" + source + "&target=" + target 

json_data= requests.get(url).json()

file = open("API_KEY.txt")

API_KEY = file.read().replace("\n", " ")


payload = {}
headers = {
  'Authorization': 'Bearer ' + API_KEY
}

response = requests.request("GET", url, headers=headers, data = payload)



print(response.text.encode('utf8'))