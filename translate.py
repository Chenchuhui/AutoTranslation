from google_translate import translate_text
import json
import re

def is_strictly_english(text):
    return bool(re.match(r'^[a-zA-Z0-9\s\(\)\-_:;.,{}/\'\"&\’%!@#$^*\?]*$', text))

def get_untranslated_list(data, num_selected):
    untranslated_list = []
    for group in data["group"]:
        if is_strictly_english(group["text"]):
            untranslated_list.append(group["text"])
            if num_selected != -1 and len(untranslated_list) >= num_selected:
                break
    return untranslated_list

def process_translation(data, translated_list=None, google=False, return_untranslated=False, num_selected=None):
    if return_untranslated:
        return get_untranslated_list(data, num_selected)

    if translated_list is None and not google:
        raise ValueError("Either 'translated_list' must be provided or 'google_api_key' for Google Translate API must be set.")

    need_to_be_translated = []
    for group in data["group"]:
        if is_strictly_english(group["text"]):
            need_to_be_translated.append(group["text"])
            if num_selected != -1 and len(need_to_be_translated) >= num_selected:
                break

    if google:
        translated_list = translate_text(need_to_be_translated, target_language="ar")

    if translated_list is None or len(need_to_be_translated) != len(translated_list):
        raise ValueError("Translation list length doesn't match or is null.")

    index = 0
    for group in data["group"]:
        if is_strictly_english(group["text"]) and index < len(translated_list):
            if group["text"] == need_to_be_translated[index]:
                group["text"] = translated_list[index]
                index += 1

    with open('./formdata/arabic_data_t.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# Example usage:
# Load JSON data
with open('./formdata/arabic_data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Get untranslated list
# untranslated_list = process_translation(data, return_untranslated=True, num_selected=-1)
# print(untranslated_list)

# If using ChatGPT for translation
# translated_list = []
# process_translation(data, translated_list=translated_list, num_selected=-1)

# If using Google Translate API
process_translation(data, google=True, num_selected=-1)
