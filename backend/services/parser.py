import re
import uuid
import fitz
from backend.models.schemas import ParsedResume

def extract_text_from_pdf(pdf_bytes: bytes) -> str:
    doc = fitz.open(stream = pdf_bytes, filetype = "pdf")
    pages = []
    for page_num in range (len(doc)):
        page = doc[page_num]
        text = page.get_text("text")
        pages.append(text)
    doc.close()
    return "\n".join(pages)

def extract_email(text: str) -> str:
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    match = re.search(pattern, text)
    return match.group(0) if match else None 