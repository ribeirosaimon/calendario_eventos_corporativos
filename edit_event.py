from dados import *
from datetime import datetime, timedelta
import time

lista2 = []


def tratamento_de_data(data):
    data = data[:10].split('-')
    data[1] = data[1].replace('0','')
    data[2]= data[2].replace('0','')
    return f'{data[2]}/{data[1]}/{data[0]}'


def editar_evento(service):
    page_token = None
    lista1 = tratamento_datas()
    while True:
        events = service.events().list(calendarId='primary', pageToken=page_token).execute()
        for event in events['items']:
            #time.sleep(1)
            lista = []
            lista.append(event['summary'])
            lista.append(tratamento_de_data(event['start']['dateTime']))
            lista2.append(lista)
        page_token = events.get('nextPageToken')
        if not page_token:
            break
    x = [li for li in lista1 if li not in lista2]
    print(len(lista1), len(lista2))
    #print(x)
