from google.cloud import translate_v2 as translate
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./credential.json"


# Initialize the Translation client
client = translate.Client()

def translate_text(texts, target_language):
    """
    Translates text into the target language.

    Args:
        text (str): Text to be translated.
        target_language (str): The language to translate the text into (e.g., 'en' for English, 'es' for Spanish).

    Returns:
        str: Translated text.
    """
    translated_texts = []
    
    for text in texts:
        result = client.translate(text, target_language=target_language, model='nmt')
        print(result)
        translated_texts.append(result['translatedText'])
    
    return translated_texts
