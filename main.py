import json
import datetime
import requests
from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession

url =  "https://metrac-io.firebaseio.com"
ext =  "/rest/messages.json"
now = datetime.datetime.now()


# get today's key
key = str(now.year) + str(now.month).zfill(2) + str(now.day).zfill(2)
data = {}
data['date'] = key;
json_data = json.dumps(data);


with open('./secrets/metrac-io-firebase-adminsdk-3o30f-0ea8c2fa69.json') as data_file:
    secrets = json.load(data_file)

# Define the required scopes
scopes = [
  "https://www.googleapis.com/auth/userinfo.email",
  "https://www.googleapis.com/auth/firebase.database"
]

# Authenticate a credential with the service account
credentials = service_account.Credentials.from_service_account_file(
    "./secrets/metrac-io-firebase-adminsdk-3o30f-0ea8c2fa69.json", scopes=scopes)

# Use the credentials object to authenticate a Requests session.
authed_session = AuthorizedSession(credentials)
response = authed_session.put(url+ext, json_data)
print response

response = authed_session.get(url+ext)
print response.content
