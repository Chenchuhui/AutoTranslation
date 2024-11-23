import os
import json

class JSONExtractor:
    def __init__(self, resource_folder="./resource/", formdata_folder="./formdata/"):
        """
        Initializes the JSONExtractor with folder paths for input and output.
        
        Args:
            resource_folder (str): Path to the resource folder containing input JSON files.
            formdata_folder (str): Path to the formdata folder for saving output JSON files.
        """
        self.resource_folder = resource_folder
        self.formdata_folder = formdata_folder
        self._ensure_folder_exists(self.formdata_folder)

    def _ensure_folder_exists(self, folder_path):
        """Ensures the specified folder exists, creating it if necessary."""
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Folder '{folder_path}' created successfully.")
        else:
            print(f"Folder '{folder_path}' already exists.")

    def extract_uid(self, language_code):
        """
        Extracts data from a JSON file based on the specified language code and saves it to a new file.
        
        Args:
            language_code (str): Language code for the input file and output file naming.
        
        Returns:
            bool: True if the extraction was successful, False otherwise.
        """
        input_file = os.path.join(self.resource_folder, f"{language_code}_response.json")
        output_file = os.path.join(self.formdata_folder, f"{language_code}_data.json")

        # Check if the input file exists
        if not os.path.exists(input_file):
            print(f"Error: Input file '{input_file}' does not exist.")
            return False

        try:
            # Load the input JSON file
            with open(input_file, 'r', encoding='utf-8') as file:
                data = json.load(file)

            # Initialize the extracted data structure
            extracted_data = {"group": []}

            # Extract the relevant data
            for value in data.values():
                for item in value['data']:
                    extracted_data["group"].append({
                        "uid": item['uid'],
                        "text": item['text'],
                        "locked": False,
                        "variants": []
                    })

            # Save the extracted data to a new JSON file
            with open(output_file, 'w', encoding='utf-8') as file:
                json.dump(extracted_data, file, ensure_ascii=False, indent=4)

            print(f"Data successfully extracted and saved to '{output_file}'.")
            return True
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return False
