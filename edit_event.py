from dados import *
from datetime import datetime, timedelta
import time
from create_event import *

lista2 = []

def tratamento_de_data(data):
    data = data[:10].split('-')
    if data[1][0] == '0':
        data[1] = data[1].replace('0','')
    if data[2][0] == '0':
        data[2] = data[2].replace('0','')
    return f'{data[1]}/{data[2]}/{data[0]}'



def editar_evento(service):
    page_token = None
    lista1 = tratamento_dos_dados_da_b3()
    while True:
        events = service.events().list(calendarId='primary', pageToken=page_token).execute()
        for event in events['items']:
            time.sleep(3)
            print(event)
            lista = []
            lista.append(event['summary'])
            lista.append(tratamento_de_data(event['start']['dateTime']))
            lista2.append(lista)
        page_token = events.get('nextPageToken')
        if not page_token:
            break
    dados_faltantes = [li for li in lista1 if li not in lista2]
    if len(dados_faltantes) != 0:
        for dados in dados_faltantes:
            criar_evento(dados,service)
    else:
        print('A lista está atualizada')
