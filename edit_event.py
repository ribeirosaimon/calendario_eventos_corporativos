from dados import *
from datetime import datetime, timedelta


def editar_evento(service):
    page_token = None
    while True:
      events = service.events().list(calendarId='primary', pageToken=page_token).execute()
      for event in events['items']:
        if event['summary'] == 'Resultados da VIVER':
        #    eventId = event['id']
        #    service.events().delete(calendarId='primary', eventId=eventId).execute()
            print(event['summary'])
      page_token = events.get('nextPageToken')
      if not page_token:
        break
