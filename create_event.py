from dados import *
from datetime import datetime, timedelta


def criar_evento(lista_da_empresa, service):
    nome_empresa = lista_da_empresa[0]
    result_1t = lista_da_empresa[1].split('/')
    timezone = 'America/Sao_Paulo'
    mes = int(result_1t[0])
    dia = int(result_1t[1])
    ano = int(result_1t[2])
    start_time = datetime(ano, mes, dia, 8, 00, 0)
    end_time = start_time + timedelta(hours=1)
    event = {
      'summary': nome_empresa,
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
          {'method': 'popup', 'minutes': 12 * 60},
        ],
      },
    }
    print(f'Agendado a empresa: {nome_empresa} para data {ano}/{mes}/{dia}')
    service.events().insert(calendarId='primary', body=event).execute()
