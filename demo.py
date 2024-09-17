import fitz  # PyMuPDF
import pandas as pd
import difflib

# Extract text from PDF
def extract_text_from_pdf(pdf_path):
    document = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()
    return text

# Placeholder for extracting tables from PDF (use libraries like tabula-py or camelot-py for better results)
def extract_tables_from_pdf(pdf_path):
    return []

# Compare text content
def compare_text(pdf_text, excel_text):
    d = difflib.Differ()
    diff = d.compare(pdf_text.splitlines(), excel_text.splitlines())
    return '\n'.join(diff)

# Compare tabular data
def compare_tables(pdf_tables, excel_data):
    missing_rows = []
    for _, excel_row in excel_data.iterrows():
        if not any((pdf_row == excel_row).all() for pdf_row in pdf_tables):
            missing_rows.append(excel_row)
    return pd.DataFrame(missing_rows)

# Paths to files
pdf_path = "C:\Users\aa067\Downloads\purchase-order_Smith & Nephew Healthcare Pvt. Ltd._POI1-2425-015 (1).pdf"
excel_path = "C:\Users\aa067\Downloads\Smith & Nephew Healthcare Pvt. Ltd. _POI1-2425-007-BUY-BACK ORDER.xlsx"

# Extract content
pdf_text = extract_text_from_pdf(pdf_path)
pdf_tables = extract_tables_from_pdf(pdf_path)
excel_data = pd.read_excel(excel_path)

# Compare content
excel_text = "\n".join(excel_data.astype(str).apply(lambda x: ' '.join(x), axis=1))
text_diff = compare_text(pdf_text, excel_text)
missing_content = compare_tables(pdf_tables, excel_data)

# Output results
print("Text Differences:")
print(text_diff)

print("Missing Content:")
print(missing_content)
