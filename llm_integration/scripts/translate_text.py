from transformers import pipeline

# Load translation pipeline with a public model
translator = pipeline("translation_en_to_fr", model="Helsinki-NLP/opus-mt-en-fr")

def translate_text(text, target_language):
    if target_language == "French":
        translated = translator(text)
        return translated[0]['translation_text']
    else:
        return "Translation for the specified language is not supported."

pdf_names = ["sample1", "sample2", "sample3", "sample4"]
target_language = "French"

for pdf_name in pdf_names:
    with open(f'processed_texts/{pdf_name}.txt', 'r') as file:
        document_text = file.read()
    
    translated_text = translate_text(document_text, target_language)
    print(f"Translated Text for {pdf_name}:\n{translated_text}\n")

    with open(f'results/translations/{pdf_name}_fr.txt', 'w') as f:
        f.write(translated_text)