import pytesseract
from PIL import Image
import fitz  # PyMuPDF
import os

# Set the path for tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Akshat\tesseract.exe'

def extract_images_from_pdf(pdf_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    pdf_document = fitz.open(pdf_path)
    image_list = []
    
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        images = page.get_images(full=True)
        
        for img_index, img in enumerate(images):
            xref = img[0]
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]
            image_filename = f"{output_dir}/image{page_num + 1}_{img_index + 1}.png"
            
            with open(image_filename, "wb") as image_file:
                image_file.write(image_bytes)
            image_list.append(image_filename)
            print(f"Extracted image: {image_filename}")
            
    return image_list

def ocr_images(image_list):
    ocr_texts = []
    for image_path in image_list:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        ocr_texts.append(text)
        print(f"OCR text from {image_path}: {text[:100]}")  # Print the first 100 characters of the OCR text for debugging
    return ocr_texts

def pdf_text_and_ocr(pdf_path):
    pdf_document = fitz.open(pdf_path)
    pdf_text = ""
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        text = page.get_text()
        pdf_text += text
        print(f"Extracted text from page {page_num + 1}: {text[:100]}")  # Print the first 100 characters of the page text for debugging
    return pdf_text

def process_multiple_pdfs(pdf_paths, images_output_dir, ocr_output_dir):
    if not os.path.exists(images_output_dir):
        os.makedirs(images_output_dir)
    if not os.path.exists(ocr_output_dir):
        os.makedirs(ocr_output_dir)
        
    for pdf_path in pdf_paths:
        base_name = os.path.basename(pdf_path)
        base_name_no_ext = os.path.splitext(base_name)[0]
        pdf_images_dir = os.path.join(images_output_dir, base_name_no_ext)
        
        # Extract text from PDF
        pdf_text = pdf_text_and_ocr(pdf_path)
        
        # Extract images from PDF and perform OCR
        image_list = extract_images_from_pdf(pdf_path, pdf_images_dir)
        ocr_texts = ocr_images(image_list)
        
        # Combine PDF text and OCR text
        combined_text = pdf_text + "\n" + "\n".join(ocr_texts)
        
        # Save combined text to output file
        ocr_output_path = os.path.join(ocr_output_dir, base_name_no_ext + ".txt")
        with open(ocr_output_path, 'w', encoding='utf-8') as ocr_output_file:
            ocr_output_file.write(combined_text)
        print(f"OCR complete: {pdf_path} to {ocr_output_path}")

# Example usage
pdf_paths = ["sample1.pdf", "sample2.pdf", "sample 3.pdf", "sample 4.pdf"]
images_output_dir = "extracted_images" 
ocr_output_dir = "ocr_texts"
process_multiple_pdfs(pdf_paths, images_output_dir, ocr_output_dir)
