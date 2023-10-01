import csv
import requests


project_id = "your project ID"
access_token = ""
# Set up your API endpoint
api_endpoint = "https://dialogflow.googleapis.com/v2/projects/{project_id}/agent/sessions/kk:detectIntent "

# Read the CSV file
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row if present

    # Loop through each row in the CSV file
    for row in reader:
        text = row[0]  # Assuming the text is in the first column

        # Create the request body
        request_body = {"queryInput": {"text": {"languageCode": "en", "text": text}}}

        # Make the API request
        response = requests.post(api_endpoint, json=request_body)

        # Check the status code to ensure the request was successful
        if response.status_code == 200:
            print(f"Successfully sent text: {text}")
        else:
            print(f"Error sending text: {text}")
