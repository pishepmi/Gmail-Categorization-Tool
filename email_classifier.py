#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# email_classifier.py
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import sqlite3

# Predefined categories and keywords
categories = {
    'Promotion': ['sale', 'discount', 'promo', 'offer'],
    'Social': ['facebook', 'twitter', 'instagram', 'linkedin'],
    'Personal': ['friend', 'family', 'birthday'],
    'Work': ['meeting', 'deadline', 'project'],
    'Finance': ['invoice', 'payment', 'transaction'],
    'News': ['newsletter', 'update', 'announcement'],
}

def classify_email(email_body):
    # Check if any keyword from predefined categories is present in the email body
    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword.lower() in email_body.lower():
                return category

    return 'Uncategorized'

def update_model():
    conn = sqlite3.connect('feedback.db')
    cursor = conn.cursor()

    cursor.execute('SELECT email_id, category, email_body, accuracy FROM feedback')  # Include email body in feedback data
    rows = cursor.fetchall()

    if len(rows) > 0:
        feedback_data = [(row[0], row[2]) for row in rows]  # Use email body for training data
        feedback_labels = [row[1] for row in rows]

        X_train, X_test, y_train, y_test = train_test_split(feedback_data, feedback_labels, test_size=0.2, random_state=42)

        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        print(f'Model Accuracy: {acc}')

        joblib.dump(model, 'email_classifier_model.joblib')

    conn.close()

if os.path.exists('email_classifier_model.joblib'):
    model = joblib.load('email_classifier_model.joblib')
else:
    model = make_pipeline(TfidfVectorizer(), MultinomialNB())
