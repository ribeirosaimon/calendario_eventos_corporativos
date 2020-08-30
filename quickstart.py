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
#KEY = os.environ.get('client_secret.json')

def main():
    SCOPES = ['https://www.googleapis.com/auth/calendar']
    creds = None
    print('processo 1 ok')
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
            print('processo 2 ok')
            print(f'creeds: {creds.valid}')
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
            print('processo 3 ok')
        else:
            #flow = InstalledAppFlow.from_client_secrets_file(KEY, SCOPES)
            flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
            print('processo 4 ok')
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
            print('processo 5 ok')
    service = build("calendar", "v3", credentials=creds)
    baixar_arquivo(site_b3)
    print('processo 6 ok')
    editar_evento(service)
    print('fechou!')

#schedule.every().day.at("23:00").do(main)
#schedule.every(1).minutes.do(main)

if __name__ == '__main__':
    main()

    #while True:
        #schedule.run_pending()
        #main()
        #time.sleep(30)
