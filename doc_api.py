from wsgiref import headers
import requests

#keys
#access_token = "eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJlYiI6Ik55Nkw4WlM1OW1NQk9pR3k3aEp5IiwianRpIjoiYWNjdG9rXzAwMDBBUEVMN1BwNzNKZzhnbVZ3Y1UiLCJ0eXAiOiJhdCIsInYiOiI2In0.AIp4LEbLRjkfDi73ziPVLJQkmxhTkpAYijfyK9XiehhUXVPb93cRDlxKa-XCTuzGL9m2FAX6KmE_HxPkANs-dA"
# account_id = "acc_00009WGyW4k4JDWYo0SJxB"

# #authenticate
# access_url = "https://auth.monzo.com/?\
#     client_id=oauth2client_0000APELfVhlgvhA7qz8xV\
#     &redirect_uri=https://localhost\
#     &response_type=code"

# res = requests.post(access_url).text

# authorization_url = "https://api.monzo.com/oauth2/token" \
#     "grant_type=authorization_code" \
#     "client_id=$client_id" \
#     "client_secret=$client_secret" \
#     "redirect_uri=$redirect_uri" \
#     "code=$authorization_code"

transaction_url = "https://api.monzo.com/transactions"

params_data =  {
            "account_id": "acc_00009WGyW4k4JDWYo0SJxB"}

access_token= "eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJlYiI6IkpVZHY3aDFSY1Fldm5VL3hzTktPIiwianRpIjoiYWNjdG9rXzAwMDBBUE42SHNGQ1VQRHAwY0dQbFUiLCJ0eXAiOiJhdCIsInYiOiI2In0.LyC3UlSUBoZ92i0oo5jQwJ5Gwh0_jNkL_DtgEyPdqGLfCT3XLg8-Vy6Bv9rDiz5FipsRyffvPv2EoIGFUet2bg"
response = requests.get(transaction_url, headers={"Authorization": "Bearer {}".format(access_token)}, params=params_data)

print(response.status_code) #print status code

response_dict = response.json() #response in json format - allows dict format
print(response_dict)