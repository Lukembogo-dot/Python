from PyPDF2 import PdfReader

try:
    file = PdfReader("receipt (1).pdf", "rb")
    data = ""
    for page in file.pages:
        data += page.extract_text()
    print(data)
except:
    print("An error occurred.")
finally:
    print("Execution completed.")