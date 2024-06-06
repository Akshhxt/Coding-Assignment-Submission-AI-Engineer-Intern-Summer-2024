import fitz  # PyMuPDF
import os

def pdf_to_txt(pdf_path, txt_path):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    
    # Create or open the TXT file
    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        # Iterate through each page in the PDF
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            text = page.get_text()
            txt_file.write(text + "\n")
    print(f"Conversion complete: {pdf_path} to {txt_path}")

def convert_multiple_pdfs(pdf_paths, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    for pdf_path in pdf_paths:
        base_name = os.path.basename(pdf_path)
        txt_filename = os.path.splitext(base_name)[0] + ".txt"
        txt_path = os.path.join(output_dir, txt_filename)
        pdf_to_txt(pdf_path, txt_path)

pdf_paths = ["sample1.pdf", "sample2.pdf", "sample 3.pdf", "sample 4.pdf"]
output_dir = "output_texts"
convert_multiple_pdfs(pdf_paths, output_dir)
