"""metrac.

Usage:
  metrac.py add ([-w] <weight> [-m] <message>)
  metrac.py (-h | --help)
  metrac.py --version
"""
import json
import datetime
import requests
import weight_utils
from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession
from docopt import docopt

# height constant, in inches
HEIGHT = 69
arguments = {}
if __name__ == '__main__':
    arguments = docopt(__doc__, version='metrac 0.0')

url =  "https://metrac-io.firebaseio.com"
ext =  "/rest/messages.json"

now = datetime.datetime.now()

# need to check that we're doing an add
if arguments['add']:
    # get today's key
    key = str(now.year) + str(now.month).zfill(2) + str(now.day).zfill(2)

    # do some weight calculations
    weight = float(arguments['<weight>'])
    bmi =  weight_utils.get_bmi(weight, float(HEIGHT))
    bmr =  weight_utils.get_bmr(weight, float(HEIGHT))
    tdee = weight_utils.get_tdee(float(bmr))
    # format the json we're sending it
    data = {}
    details = {}

    details['weight'] = arguments['<weight>']
    details['message'] = arguments['<message>']
    details['bmi'] = bmi
    details['bmr'] = bmr
    details['tdee'] = tdee

    data[key] = details;
    json_data = json.dumps(data);

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
