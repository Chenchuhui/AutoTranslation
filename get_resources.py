import requests
import json

# Define the URL and cookies
url = "https://app.suitedash.com/translation/getResource"
cookies = {
    "PHPSESSID": "YOUR_PHPSESSID_VALUE",
    "TOKEN": "YOUR_TOKEN_VALUE",
    "__stripe_mid": "YOUR_STRIPE_MID_VALUE",
    "translationStoreCreationDate": "YOUR_TRANSLATION_STORE_CREATION_DATE"
}

# Make the GET request with the cookies
response = requests.get(url, cookies=cookies)

# Check if the response is successful
if response.status_code == 200:
    # Convert the response to JSON
    data = response.json()
    
    # Save the JSON response to a file
    with open('.json_files/response.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
    
    print("Response saved to response.json")
else:
    print(f"Failed to retrieve data: {response.status_code}")

