from transformers import pipeline

# Load text classification pipeline with a public model
classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

def classify_document(text):
    result = classifier(text)
    return result

pdf_names = ["sample1", "sample2", "sample 3", "sample 4"]

for pdf_name in pdf_names:
    with open(f'processed_texts/{pdf_name}.txt', 'r') as file:
        document_text = file.read()
    
    document_category = classify_document(document_text)
    print(f"Document Category for {pdf_name}: {document_category}\n")
    
    with open(f'results/classifications/{pdf_name}_category.txt', 'w') as f:
        f.write(str(document_category))