from dados import *
from datetime import datetime, timedelta


def editar_evento(service):
    result = service.calendarList().list().execute()
    calendar_id = result['items'][0]['id']
    result = service.events().list(calendarId=calendar_id, timeZone='America/Sao_Paulo').execute()
    print(result['items'][0])
