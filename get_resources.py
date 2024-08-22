import os
import requests
import json

# Define the path for the folder you want to create
folder_path = "./resource/"

# Check if the folder already exists
if not os.path.exists(folder_path):
    # If it doesn't exist, create it
    os.makedirs(folder_path)
    print(f"Folder '{folder_path}' created successfully.")
else:
    print(f"Folder '{folder_path}' already exists.")


# Define the URL and cookies
url = "https://app.suitedash.com/translation/getResource"
cookies = {
    "PHPSESSID": "csh175a2q1163nrk6c0snjj0uo",
    "__stripe_mid": "51fee4a9-d150-4f21-9fa8-3ee2c97319212639e6",
}

# Make the GET request with the cookies
response = requests.get(url, cookies=cookies)

# Check if the response is successful
if response.status_code == 200:
    # Convert the response to JSON
    data = response.json()
    
    # Save the JSON response to a file
    with open(f'{folder_path}/arabic_response.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
    
    print("Response saved to response.json")
else:
    print(f"Failed to retrieve data: {response.status_code}")

