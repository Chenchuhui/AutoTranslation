# Translation Processing Automation

This repository automates the process of translating JSON files using APIs and uploading the translated data back to the server. The project includes scripts for fetching resources, extracting and translating data, and posting the translated files.

---

## Features

1. **Fetch Resources**:
   - Downloads translation resources from a specified API endpoint using authentication credentials.

2. **Extract and Save Data**:
   - Extracts untranslated content (`uid`, `text`) from JSON files for processing.

3. **Translation**:
   - Supports automated translation via Google Translate API or manually provided translations.

4. **Post Translated Data**:
   - Sends the translated data back to the server via HTTP POST.

---

## File Descriptions

### Scripts

- `get_resource.py`:
  - Fetches translation resources from the API.
  - Saves the raw response as a JSON file.

- `formData.py`:
  - Extracts `uid` and `text` from the fetched resources.
  - Saves extracted data in a simplified JSON format.

- `translate.py`:
  - Processes translations for extracted JSON files.
  - Supports automated translation using Google Translate API or custom translations.

- `post.py`:
  - Sends translated JSON data back to the server.

- `main.py`:
  - The entry point script that integrates all steps:
    1. Fetch resource.
    2. Extract and generate form data.
    3. Translate data.
    4. Post translated data.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository
