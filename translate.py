import json
import re
from google_translate import translate_text

class TranslationProcessor:
    def __init__(self, input_path, output_path):
        """
        Initializes the TranslationProcessor with input and output file paths.
        
        Args:
            input_path (str): Path to the input JSON file.
            output_path (str): Path to save the translated JSON file.
        """
        self.input_path = input_path
        self.output_path = output_path
        self.data = self._load_json()

    def _load_json(self):
        """Loads JSON data from the input file."""
        try:
            with open(self.input_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Input file '{self.input_path}' not found.")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON format in '{self.input_path}'.")

    def _save_json(self):
        """Saves the updated JSON data to the output file."""
        with open(self.output_path, 'w', encoding='utf-8') as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)

    @staticmethod
    def is_strictly_english(text):
        """Checks if the text contains only English characters and allowed symbols."""
        return bool(re.match(r'^[a-zA-Z0-9\s\(\)\-_:;.,{}/\'\"&\’%!@#$^*\?]*$', text))

    def get_untranslated_list(self, num_selected=-1):
        """
        Extracts untranslated English text from the data.
        
        Args:
            num_selected (int): Maximum number of untranslated texts to return (-1 for no limit).

        Returns:
            list: A list of untranslated English texts.
        """
        untranslated_list = []
        for group in self.data.get("group", []):
            if self.is_strictly_english(group["text"]):
                untranslated_list.append(group["text"])
                if num_selected != -1 and len(untranslated_list) >= num_selected:
                    break
        return untranslated_list

    def translate(self, translated_list=None, google=False, num_selected=-1, target_language="bn"):
        """
        Processes translation for the data using provided translations or Google Translate API.
        
        Args:
            translated_list (list): List of translations to update the data.
            google (bool): Whether to use Google Translate API for translation.
            num_selected (int): Maximum number of texts to translate (-1 for no limit).
            target_language (str): Target language code for translation.
        """
        if translated_list is None and not google:
            raise ValueError("Either 'translated_list' must be provided or 'google=True' for Google Translate API.")

        need_to_be_translated = []
        for group in self.data.get("group", []):
            if self.is_strictly_english(group["text"]):
                need_to_be_translated.append(group["text"])
                if num_selected != -1 and len(need_to_be_translated) >= num_selected:
                    break

        if google:
            translated_list = translate_text(need_to_be_translated, target_language=target_language)

        if translated_list is None or len(need_to_be_translated) != len(translated_list):
            raise ValueError("Translation list length doesn't match or is null.")

        index = 0
        for group in self.data.get("group", []):
            if self.is_strictly_english(group["text"]) and index < len(translated_list):
                if group["text"] == need_to_be_translated[index]:
                    group["text"] = translated_list[index]
                    index += 1

        self._save_json()
        print(f"Translation complete. Data saved to '{self.output_path}'.")