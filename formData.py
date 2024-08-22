import json

# Load the JSON data from the file
with open('./resource/arabic_response.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Initialize a new structure to store the extracted data
extracted_data = {"group": []}

# Function to extract uids and translated text
def extract_uid(data: dict):
    for value in data.values():
        for item in value['data']:
            extracted_data["group"].append({
                "uid": item['uid'],
                "text": item['text'],
                "locked": False,
                "variants": []
            })

# Call the function
extract_uid(data)

# Save the extracted data to a new JSON file
with open('./formdata/arabic_data.json', 'w', encoding='utf-8') as file:
    json.dump(extracted_data, file, ensure_ascii=False, indent=4)

print("Data successfully extracted and saved to extracted_data.json")
