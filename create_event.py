from dados import *
from datetime import datetime, timedelta


def criar_evento(lista_da_empresa, service):
    nome_empresa = lista_da_empresa[0]
    result_1t = lista_da_empresa[1]
    result_2t = lista_da_empresa[2]
    result_3t = lista_da_empresa[3]
    lista_de_resultados = [result_1t,result_2t,result_3t]

    for index in lista_de_resultados:
        index = index.split('/')
        timezone = 'America/Sao_Paulo'
        mes = int(index[0])
        dia = int(index[1])
        ano = int(index[2])

        start_time = datetime(ano, mes, dia, 8, 00, 0)
        end_time = start_time + timedelta(hours=1)
        event = {
          'summary': f'Resultados da {nome_empresa}',
          'location': 'São Paulo',
          'description': f'Resultados da {nome_empresa}',
          'start': {
            'dateTime': start_time.strftime(f"%Y-%m-%dT%H:%M:%S"),
            'timeZone': timezone,
          },
          'end': {
            'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': timezone,
          },
          'reminders': {
            'useDefault': False,
            'overrides': [
              {'method': 'email', 'minutes': 24 * 60},
              {'method': 'popup', 'minutes': 10},
            ],
          },
        }
        service.events().insert(calendarId='primary', body=event).execute()
