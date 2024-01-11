#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import base64
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from datetime import datetime, timedelta

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/gmail.modify']
creds = None

if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json')

if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)

    with open('token.json', 'w') as token:
        token.write(creds.to_json())

service = build('gmail', 'v1', credentials=creds)

def get_messages(start_date=None, end_date=None):
    # Construct the query to filter emails based on date range
    query = 'in:inbox'

    if start_date:
        query += f' after:{start_date.strftime("%Y/%m/%d")}'
    
    if end_date:
        query += f' before:{end_date.strftime("%Y/%m/%d")}'

    # Fetch messages based on the constructed query
    results = service.users().messages().list(userId='me', q=query).execute()
    messages = results.get('messages', [])
    return messages

def decode_body(email_id):
    # Decode the email body from base64
    message = service.users().messages().get(userId='me', id=email_id).execute()
    msg_str = base64.urlsafe_b64decode(message['body']['data'].encode('UTF-8')).decode('UTF-8')
    return msg_str

