import csv
import requests

# Set up your API endpoint and access token
api_endpoint = "https://dialogflow.googleapis.com/v2/projects/project_id/agent/sessions/kk:detectIntent"
access_token = ""

# Read the CSV file
with open("accuracy_check_all_update.csv", "r") as file:
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

    # Initialize a list to store misclassified lines
    misclassified_lines = []

    # Loop through each row in the CSV file
    for i, row in enumerate(reader):
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

            # Check if the predicted intent matches the actual intent
            detected_correctly = "Yes" if predicted_intent == actual_intent else "No"

            # Append the result to the misclassified lines list if it was not detected correctly
            if detected_correctly == "No":
                misclassified_lines.append(
                    {
                        "text": text,
                        "actual_intent": actual_intent,
                        "predicted_intent": predicted_intent,
                    }
                )

        else:
            print(f"Error sending text: {text}")

# Calculate percentage for each intent
intent_percentages = {
    intent: (count / total_messages) * 100 for intent, count in intent_counts.items()
}

# Print the results
for intent, percentage in intent_percentages.items():
    print(f"{intent}: {percentage:.2f}%")

# Print misclassified lines
print("\nMisclassified Lines:")
for line in misclassified_lines:
    print(
        f"Text: {line['text']}, Actual Intent: {line['actual_intent']}, Predicted Intent: {line['predicted_intent']}, Detected Correctly: No"
    )

# Print overall accuracy
overall_accuracy = (total_messages - len(misclassified_lines)) / total_messages * 100
print(f"\nOverall Accuracy: {overall_accuracy:.2f}%")
