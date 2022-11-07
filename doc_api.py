import requests

response = requests.get("https://api.monzo.com/transactions")
print(response.status_code)
#python doc_api.py in Terminal
