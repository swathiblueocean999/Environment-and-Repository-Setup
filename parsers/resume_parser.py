import pdfplumber

def parse_resume(file_path):
    try:
        with pdfplumber.open(file_path) as pdf:
            first_page = pdf.pages[0]
            text = first_page.extract_text()
            return {"extracted_text": text[:100]} 
    except Exception as e:
        return {"error": str(e)}

print(parse_resume("sample_resume.pdf"))