# Gmail Categorization Program

## Introduction

This Python program utilizes the Gmail API and machine learning techniques to categorize emails into predefined categories. The classification is based on the content of the emails and user feedback.

## Prerequisites

Before running the program, ensure you have the following:

1. **Gmail API Credentials:**
    - Create a project on the [Google Cloud Console](https://console.cloud.google.com/).
    - Enable the Gmail API for the project.
    - Create credentials and download the JSON file.

2. **Python Libraries:**
    - Install required Python libraries using the following command:
        ```bash
        pip install google-api-python-client google-auth-oauthlib google-auth-httplib2 nltk scikit-learn joblib
        ```

3. **SQLite:**
    - Ensure SQLite is installed, as it's used for the feedback database.

4. **Permissions:**
    - Make sure your Gmail API credentials have the necessary scopes for reading emails.

## Setup

1. **Gmail API Setup:**
    - Place your `credentials.json` file in the working directory.
    - Run `main.py` to authorize the Gmail API and fetch emails.

2. **Run the Program:**
    - Execute `main.py` to start the program.
    - Follow the prompts to categorize emails and provide feedback.

3. **Feedback Database:**
    - A SQLite database (`feedback.db`) will be created in the working directory to store feedback.

## Customization

- **Predefined Categories:**
    - Edit `categories` in `email_classifier.py` to customize predefined categories and keywords.

## Additional Notes

- The program includes a basic machine learning model for email categorization.
- User feedback is utilized to update and improve the model over time.

## Issues and Troubleshooting

- If you encounter any issues or errors, refer to the error messages for guidance.
- Ensure that you have the necessary permissions to access Gmail and modify files in the working directory.

## Author

Moch Riyadh Zahran

Feel free to customize the instructions based on your specific program and use case.
