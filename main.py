from get_resources import ResourceFetcher
from formData import JSONExtractor
from translate import TranslationProcessor
from post import PostProcessor

def main():
    # Input credentials
    phpsessid = input("Enter PHPSESSID: ").strip()
    stripe_mid = input("Enter __stripe_mid: ").strip()

    # Input language code
    language_code = input("Enter language code (e.g., 'en', 'bn'): ").strip()

    # Step 1: Fetch Resource
    print("Fetching resource...")
    fetcher = ResourceFetcher(phpsessid, stripe_mid)
    resource_success = fetcher.fetch_resource(language_code)
    if not resource_success:
        print("Failed to fetch resources.")
        return

    # Step 2: Extract and Save Form Data
    print("Extracting and saving form data...")
    extractor = JSONExtractor()
    extraction_success = extractor.extract_uid(language_code)
    if not extraction_success:
        print("Failed to extract form data.")
        return

    # Step 3: Translate Data
    print("Translating data...")
    input_path = f"./formdata/{language_code}_data.json"
    output_path = f"./formdata/{language_code}_data_t.json"
    translator = TranslationProcessor(input_path, output_path)
    translator.translate(google=True, target_language=language_code)

    # Step 4: Post Translated Data
    print("Posting translated data...")
    poster = PostProcessor(phpsessid=phpsessid, stripe_mid=stripe_mid)
    post_success = poster.process_json_file(language_code)
    if not post_success:
        print("Failed to post translated data.")
        return

    print("Process completed successfully.")

if __name__ == "__main__":
    main()
