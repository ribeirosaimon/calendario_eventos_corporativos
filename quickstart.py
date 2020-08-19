from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from teste import *

# If modifying these scopes, delete the file token.pickle.
def main():
    credentials = pickle.load(open("token.pickle", "rb"))
    service = build("calendar", "v3", credentials=credentials)
    result = service.calendarList().list().execute()


if __name__ == '__main__':
    main()
