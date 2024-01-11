#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from email_classifier import classify_email, update_model
from gmail_api import get_messages, decode_body
from feedback_db import store_feedback
from datetime import datetime, timedelta

def main():
    # Define the date range for filtering emails
    start_date = datetime(2022, 1, 1)  # Replace with the desired start date
    end_date = datetime(2022, 12, 31)   # Replace with the desired end date

    # Get messages based on the specified date range
    messages = get_messages(start_date, end_date)

    for message in messages:
        email_id = message['id']
        email_body = decode_body(email_id)
        category = classify_email(email_body)

        print(f'Email ID: {email_id}')
        print(f'Category: {category}')

        accuracy = int(input('How accurate is the categorization? (1-100): '))
        store_feedback(email_id, category, email_body, accuracy)

    update_model()

if _name_ == "_main_":
    main()

