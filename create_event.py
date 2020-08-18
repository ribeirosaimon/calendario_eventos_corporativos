from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from datetime import datetime


SCOPES = "https://www.googleapis.com/auth/calendar"
store = file.Storage ('token.json')
creds = store.get ()
se não for creds ou creds.invalid:
    flow = client.flow_from_clientsecrets ('credentials.json', SCOPES)
    creds = tools.run_flow (fluxo, armazenamento)
    service = build ('calendar', 'v3', http = creds.authorize (Http ()))
