# ChatBot- Dialogflow

This project is a chatbot developed using JavaScript, Node.js, and Dialogflow. It incorporates a simple messaging UI where users can interact with the chatbot by asking questions, and it provides responses based on the training data stored in a CSV file.

## Table of Contents

- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Training](#training)
- [License](#license)

## Introduction

This chatbot project aims to provide users with an interactive messaging interface to ask questions and receive responses based on pre-trained data. It leverages the following technologies: JavaScript, Node.js, and Dialogflow. The chatbot's responses are generated using the Dialogflow platform, which was trained using Python scripts and data from a CSV file.

## Technologies Used

- JavaScript
- Node.js
- Dialogflow
- Python (for training)
- CSV file (for training data)

## Installation

1. Clone the repository to your local machine.
2. Install Node.js if not already installed.
3. Run `npm install` to install project dependencies.
4. Configure Dialogflow with your project's credentials and training data.
5. Start the chatbot server using `npm start`.

## Usage

Once the chatbot is running, users can interact with it by sending messages through the provided UI. The chatbot will respond to user queries based on the training data and responses defined in Dialogflow.

![Project Image 1](/client//img/Ui.PNG)

<h3> ChatBot - UI</h3>

![Project Image 2](./client/img/response.PNG)

<h3> ChatBot - When responding ...</h3>
Chatbot will reply according to your query (Chatbot have a inputted response. Read your query and will reply according to your ask)

## Training

Training the chatbot is a crucial step to ensure accurate and meaningful responses to user queries. Here's how to train the chatbot effectively using Dialogflow:

Divide Data into Small Files:
Divide your training data into small files containing 100 to 200 text samples each. Keeping files small allows for easier management and validation on Dialogflow.

Review and Manually Adjust Training Data:
After uploading the small CSV files to Dialogflow, review the training data in the "Training" section. If Dialogflow detects the wrong intent for a query, you can manually select the correct intent. Check the "Intents" section to verify that your queries are correctly mapped to training phrases.

Create Responses for Training Phrases:
Craft responses tailored to each training phrase. These responses should provide relevant and helpful information based on the user's query. Ensure responses are clear, concise, and align with the intent of the user's input.

Automate Training Data Upload (Python Example):
Use Python to automate the process of pushing queries to Dialogflow. Below is an example of how you can send a query to Dialogflow using the requests library:

        import csv
        import requests

        api_endpoint = "https://dialogflow.googleapis.com/v2/projects/project_id/agent/sessions/kk:detectIntent"
        access_token = "input your access token"

        with open("./data_12k_to_15k/12.6k_to_12.8k.csv", "r") as file:
        reader = csv.reader(file)
        next(reader) # Skip the header row if presents # Loop through each row in the CSV file
        for row in reader:
        text = row[0] # Assuming the text is in the first column

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

Remember, Dialogflow processes a single query at a time, so you may need to wait a bit if you're dealing with a large number of queries.

Continuously Validate and Refine:
Regularly validate the chatbot's responses to user queries. If users are not getting the expected responses, review the training data and make necessary adjustments. Continuous validation and refinement are key to an effective and accurate chatbot.

By following these steps and automating the training process, you can ensure that your chatbot responds accurately to a variety of user queries, providing a seamless user experience.

## License

This project is licensed under the [MIT License](LICENSE).
