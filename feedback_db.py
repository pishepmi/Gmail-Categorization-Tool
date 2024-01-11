#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sqlite3
import os

def store_feedback(email_id, category, email_body, accuracy):
    if not os.path.exists('feedback.db'):
        # If the database doesn't exist, create a new one
        conn = sqlite3.connect('feedback.db')
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS feedback (
                email_id TEXT PRIMARY KEY,
                category TEXT,
                email_body TEXT,  -- Include a column for storing email body
                accuracy INTEGER
            )
        ''')

        conn.commit()
        conn.close()

    conn = sqlite3.connect('feedback.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO feedback (email_id, category, email_body, accuracy)
        VALUES (?, ?, ?, ?)
    ''', (email_id, category, email_body, accuracy))

    conn.commit()
    conn.close()

