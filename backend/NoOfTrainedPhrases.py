import requests

# Set up your Dialogflow project ID and access token

project_id2 = "your project ID"
access_token = ""

# Set up the API endpoint for listing intents
api_endpoint = (
    f"https://dialogflow.googleapis.com/v2/projects/{project_id2}/agent/intents"
)

# Set the request headers with the access token
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
}

# Make the API request to list intents
response = requests.get(api_endpoint, headers=headers)

# Check the status code to ensure the request was successful
if response.status_code == 200:
    intents = response.json().get("intents", [])
    total_training_phrases = sum(
        len(intent.get("trainingPhrases", [])) for intent in intents
    )
    print(f"Number of trained training phrases: {total_training_phrases}")
else:
    print("Error retrieving intents")
