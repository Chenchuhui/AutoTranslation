# Auto Translation

This repository automates the translation workflow for JSON files, including resource fetching, data extraction, translation, and posting the results back to a server.

---

## Features

1. **Fetch Resources**:
   - Downloads translation resources from a specified server endpoint using authentication credentials.

2. **Extract Data**:
   - Extracts key fields (`uid`, `text`) from the fetched JSON for processing.

3. **Translate**:
   - Supports automatic translation using the Google Translate API or manual input for translations.

4. **Post Translated Data**:
   - Sends translated JSON files back to the server.

---

## How to Use

### Run the Full Workflow

To execute the entire workflow in a single step, run the `main.py` script:

```bash
python3 main.py
```

You will be prompted to provide the following inputs:

- **`PHPSESSID`**: Your session ID for API authentication.
- **`__stripe_mid`**: Your Stripe MID for API authentication.
- **Language Code**: The target language code for translation (e.g., `bn` for Bengali, `en` for English).

### Example Input:

```plaintext
Enter PHPSESSID: 13i3sleubcnuj5ekqvduv0n6ri
Enter __stripe_mid: 1f34f841-0bed-4ce7-9e2c-c9fb66431afb516c56
Enter language code (e.g., 'bn', 'en'): bn
```

---

## Server Details

The script interacts with the following server endpoints:

1. **Fetch Resources**:
   - URL: `https://app.suitedash.com/translation/getResource`

2. **Post Translated Data**:
   - URL: `https://app.suitedash.com/translation/saveGroup`

Authentication is handled via cookies:
- **`PHPSESSID`**
- **`__stripe_mid`**

---

## Directory Structure

- **`/formdata`**: Stores extracted and translated JSON files.
- **`/resource`**: Stores fetched raw resource files.

---

## Requirements

1. **Python**: 3.7 or higher.
2. **Dependencies**:
   - `requests`: For making API calls.
   - `googletrans` (optional): For using Google Translate.

Install dependencies with:
```bash
pip install -r requirements.txt
```

---

## License

This project is licensed under the MIT License.
```
