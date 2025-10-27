import pdfplumber

pdf_path = 'portfolio[1].pdf'

with pdfplumber.open(pdf_path) as pdf:
    for i, page in enumerate(pdf.pages):
        print(f"\n{'='*60}")
        print(f"PAGE {i+1}")
        print('='*60)
        text = page.extract_text()
        print(text)
