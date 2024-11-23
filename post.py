import os
import json
import requests


class PostProcessor:
    def __init__(self, directory="./formdata", url="https://app.suitedash.com/translation/saveGroup", phpsessid=None, stripe_mid=None):
        """
        Initializes the PostProcessor with directory, URL, and authentication cookies.
        
        Args:
            directory (str): Directory containing the JSON files.
            url (str): URL to send POST requests to.
            phpsessid (str): PHPSESSID for authentication.
            stripe_mid (str): Stripe MID for authentication.
        """
        self.directory = directory
        self.url = url
        self.cookies = {
            "PHPSESSID": phpsessid,
            "__stripe_mid": stripe_mid,
        }

    def process_json_file(self, language_code):
        """
        Processes the JSON file corresponding to the given language code by sending its content to the API.
        
        Args:
            language_code (str): The language code to identify the file to process.

        Returns:
            dict: A dictionary containing the status code and response text.
        """
        filename = f"{language_code}_data_t.json"
        filepath = os.path.join(self.directory, filename)

        # Check if the file exists
        if not os.path.exists(filepath):
            return {
                "status_code": 404,
                "message": f"Error: File '{filepath}' not found.",
            }

        try:
            # Load the JSON data
            with open(filepath, 'r', encoding='utf-8') as file:
                data = json.load(file)

            # Prepare form-data
            form_data = {'group': json.dumps(data['group'])}

            # Send the POST request
            response = requests.post(self.url, data=form_data, cookies=self.cookies)

            # Return the response details
            return {
                "status_code": response.status_code,
                "message": response.text,
            }

        except Exception as e:
            return {
                "status_code": 500,
                "message": f"An error occurred: {str(e)}",
            }

