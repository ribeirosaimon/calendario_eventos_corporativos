from __future__ import print_function
import datetime
import pickle
import os.path
import schedule
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from create_event import *
from edit_event import *
from dados import *
from donwload_arquivo import *


site_b3 = 'http://www.b3.com.br/data/files/41/60/CE/23/BA3DF6107DF7ACF6AC094EA8/Cronograma%20de%20Eventos%20Corporativos%202020.xlsx'

def main():
    SCOPES = ['https://www.googleapis.com/auth/calendar']
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    service = build("calendar", "v3", credentials=creds)
    baixar_arquivo(site_b3)
    editar_evento(service)

schedule.every().day.at("23:00").do(main)

if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)
