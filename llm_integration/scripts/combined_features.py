from transformers import pipeline

# Load pipelines with public models
ner = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english")
classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")
translator = pipeline("translation_en_to_fr", model="Helsinki-NLP/opus-mt-en-fr")

def extract_information(text):
    entities = ner(text)
    return entities

def classify_document(text):
    result = classifier(text)
    return result

def translate_text(text, target_language):
    if target_language == "French":
        translated = translator(text)
        return translated[0]['translation_text']
    else:
        return "Translation for the specified language is not supported."

pdf_names = ["sample1", "sample2", "sample 3", "sample 4"]
target_language = "French"

for pdf_name in pdf_names:
    with open(f'processed_texts/{pdf_name}.txt', 'r', encoding='utf-8') as file:
        document_text = file.read()
    
    extracted_info = extract_information(document_text)
    document_category = classify_document(document_text)
    translated_text = translate_text(document_text, target_language)
    
    print(f"Extracted Information for {pdf_name}:\n{extracted_info}\n")
    print(f"Document Category for {pdf_name}: {document_category}\n")
    print(f"Translated Text for {pdf_name}:\n{translated_text}\n")

    with open(f'results/extracted_info/{pdf_name}_info.txt', 'w', encoding='utf-8') as f:
        f.write(str(extracted_info))
    with open(f'results/classifications/{pdf_name}_category.txt', 'w', encoding='utf-8') as f:
        f.write(str(document_category))
    with open(f'results/translations/{pdf_name}_fr.txt', 'w', encoding='utf-8') as f:
        f.write(translated_text)
