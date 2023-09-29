import csv
import requests

# project_id = "palette-chat-qljh"

# Set up your API endpoint and access token
api_endpoint = "https://dialogflow.googleapis.com/v2/projects/palette-chat-qljh/agent/sessions/kk:detectIntent"
access_token = "ya29.a0AfB_byAkz2_qpabrYJaz8zwdb5DdjsxLyR3AL7LQOBn-Ac0wGn-_-TLEYfCgHvNk01x7RKTIDiqrjWeymkpYG4WEcL3odsg24M0MBM-SGYK_0upIDOsypKwvfrjVFBQm4n_GBvI4XldaKcVgEavVbU7gr_ymyxuTNeeu_JUaCgYKAcwSARASFQHsvYlstkYJtYnoR7t4DmfMhJRnCg0174"

# Read the CSV file
with open("./data_12k_to_15k/12.6k_to_12.8k.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row if presents
    # Loop through each row in the CSV file
    for row in reader:
        text = row[0]  # Assuming the text is in the first column

        # Create the request body
        request_body = {"queryInput": {"text": {"languageCode": "en", "text": text}}}

        # Set the request headers with the access token
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }

        # Make the API request with authentication
        response = requests.post(api_endpoint, json=request_body, headers=headers)

        # Check the status code to ensure the request was successful
        if response.status_code == 200:
            print(f"Successfully sent text: {text}")
        else:
            print(f"Error sending text: {text}")
