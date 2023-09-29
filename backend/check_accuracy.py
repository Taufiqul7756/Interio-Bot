import csv
import requests

# Set up your API endpoint and access token
api_endpoint = "https://dialogflow.googleapis.com/v2/projects/palette-chat-qljh/agent/sessions/kk:detectIntent"
access_token = "ya29.a0AfB_byDgweAO3iYZvJ4iYFCDvsz0DSg-6U8K9S_H7U0OHh7j18LNw4fTmNRLkf2LFctXwKHx0qClgBHj0S095zfzpqznq0n2UScnShRcwsjnRH4nRq_85G8ydTuH6_QLgiITf7rslnd8ed8qQ6Y7piU7O6ywDQaCgYKAbUSARASFQHsvYls3iF5P6VitICNeRGPoJBkoQ0165"

# Read the CSV file
with open("./accuracy_check_all_12000.csv", "r") as file:
    reader = csv.DictReader(file)

    # Initialize counters for each intent
    intent_counts = {
        "Curious-intent": 0,
        "Incident-intent": 0,
        "Junk-intent": 0,
        "Junk-Intent-Default": 0,
        "Problem-intent": 0,
        "Service-request-intent": 0,
    }

    total_messages = 0

    # Loop through each row in the CSV file
    for row in reader:
        text = row["text"]  # Replace "text" with the actual column name for the text
        actual_intent = row[
            "intent"
        ]  # Replace "intent" with the actual column name for the intent

        # Create the request body
        request_body = {
            "queryInput": {"text": {"languageCode": "en", "text": text}},
            "queryParams": {"timeZone": "America/New_York"},  # Add timezone if needed
        }

        # Set the request headers with the access token
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }

        # Make the API request with authentication
        response = requests.post(api_endpoint, json=request_body, headers=headers)

        # Check the status code to ensure the request was successful
        if response.status_code == 200:
            predicted_intent = (
                response.json()
                .get("queryResult", {})
                .get("intent", {})
                .get("displayName", "")
            )
            intent_counts[predicted_intent] += 1
            total_messages += 1
        else:
            print(f"Error sending text: {text}")

# Calculate percentage for each intent
intent_percentages = {
    intent: (count / total_messages) * 100 for intent, count in intent_counts.items()
}

# Print the results
for intent, percentage in intent_percentages.items():
    print(f"{intent}: {percentage:.2f}%")
