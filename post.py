import os
import requests
import json

# Define the directory containing the JSON files
directory = "./formdata"  # Change this to your actual directory

# Define the URL and cookies
url = "https://app.suitedash.com/translation/saveGroup"
cookies = {
    "PHPSESSID": "csh175a2q1163nrk6c0snjj0uo",
    "__stripe_mid": "51fee4a9-d150-4f21-9fa8-3ee2c97319212639e6",
}

# Function to process each JSON file
def process_json_file(filepath, filename):
    with open(filepath, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Prepare form-data as required by the API
    form_data = {'group': json.dumps(data['group'])}

    # # Print the form_data for debugging
    # print(f"Processing file: {filename}")
    # print("Form Data:", form_data)

    # Make the POST request with the form-data and cookies
    response = requests.post(f'{url}', data=form_data, cookies=cookies)

    # Print the response status and text
    print(f"Response for {filename}: {response.status_code}")
    print(response.text)

# Iterate over all JSON files in the specified directory
filename = "arabic_data_t.json"
filepath = os.path.join(directory, filename)
process_json_file(filepath, filename[:-5])  # Remove the .json extension for the filename

print("All files processed.")
