import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

# Ensure the required NLTK data packages are downloaded
nltk.download('punkt')

def clean_text(text):
    # Remove irrelevant characters, extra spaces, and formatting
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with single space
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)  # Remove non-ASCII characters
    text = text.strip()
    return text

def preprocess_text(txt_path):
    with open(txt_path, 'r', encoding='utf-8') as file:
        text = file.read()
        
    cleaned_text = clean_text(text)
    sentences = sent_tokenize(cleaned_text)
    tokenized_sentences = [word_tokenize(sentence) for sentence in sentences]
    
    return tokenized_sentences

preprocessed_data = preprocess_text("output.txt")
print(preprocessed_data)
