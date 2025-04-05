from PyPDF2 import PdfReader


file = PdfReader("CV Luke 2024.pdf", "rb")
data = ""
for page in file.pages:
    data += page.extract_text()

print(data)