from transformers import pipeline
# Load NER pipeline with a public model
ner = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english")

def extract_information(text):
    entities = ner(text)
    return entities

pdf_names = ["sample1", "sample2", "sample 3", "sample 4"]

for pdf_name in pdf_names:
    with open(f'processed_texts/{pdf_name}.txt', 'r') as file:
        document_text = file.read()
    
    extracted_info = extract_information(document_text)
    print(f"Extracted Information for {pdf_name}:\n{extracted_info}\n")

    with open(f'results/extracted_info/{pdf_name}_info.txt', 'w') as f:
        f.write(str(extracted_info))