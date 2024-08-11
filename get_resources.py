import os
import requests
import json

# Define the path for the folder you want to create
folder_path = "./json_files/"

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
    "PHPSESSID": "ksju93ktq17ovqjtqs37qqjd4a",
    # "TOKEN": "73a0f129-cd56-40cd-a266-548a52558983e0e219",
    "__stripe_mid": "73a0f129-cd56-40cd-a266-548a52558983e0e219",
    "translationStoreCreationDate": "2e4c6e9e111d06196a5aa79622ef8acd07e14c33i%3A1723348513%3B"
}

# Make the GET request with the cookies
response = requests.get(url, cookies=cookies)

# Check if the response is successful
if response.status_code == 200:
    # Convert the response to JSON
    data = response.json()
    
    # Save the JSON response to a file
    with open(f'{folder_path}/russian_response.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
    
    print("Response saved to response.json")
else:
    print(f"Failed to retrieve data: {response.status_code}")

