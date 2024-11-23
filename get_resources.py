import os
import requests
import json

class ResourceFetcher:
    def __init__(self, phpsessid, stripe_mid, folder_path="./resource/"):
        """
        Initializes the ResourceFetcher with the necessary cookies and folder path.
        
        Args:
            phpsessid (str): PHPSESSID for authentication.
            stripe_mid (str): __stripe_mid for authentication.
            folder_path (str): Path to save the fetched resources.
        """
        self.cookies = {
            "PHPSESSID": phpsessid,
            "__stripe_mid": stripe_mid,
        }
        self.folder_path = folder_path
        self._ensure_folder_exists()

    def _ensure_folder_exists(self):
        """Ensures that the resource folder exists."""
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)
            print(f"Folder '{self.folder_path}' created successfully.")
        else:
            print(f"Folder '{self.folder_path}' already exists.")

    def fetch_resource(self, language_code):
        """
        Fetches resources from the server and saves the response as a JSON file.
        
        Args:
            language_code (str): Language code to include in the request.

        Returns:
            bool: True if the resource was successfully fetched and saved, False otherwise.
        """
        url = "https://app.suitedash.com/translation/getResource"  # Static URL matching the original code
        print(f"Fetching resource for language code: {language_code}")

        try:
            response = requests.get(url, cookies=self.cookies)
            if response.status_code == 200:
                data = response.json()
                file_path = os.path.join(self.folder_path, f"{language_code}_response.json")
                with open(file_path, 'w', encoding='utf-8') as json_file:
                    json.dump(data, json_file, indent=4)
                print(f"Resource for '{language_code}' saved to {file_path}.")
                return True
            else:
                print(f"Failed to retrieve data: {response.status_code}")
                return False
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return False
