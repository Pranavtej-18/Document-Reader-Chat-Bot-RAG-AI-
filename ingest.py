from pypdf import PdfReader

pdf_path = "data/Validanagram Notes.pdf"

reader = PdfReader(pdf_path)

try:
    print("Total no. of pages: ",len(reader.pages))

    text = ""

    for index,page in enumerate(reader.pages, start=1):
        print(f"===> Page {index} <===")
        text += page.extract_text()
        print(page.extract_text())

    print("No. of characters in text\n")
    print(len(text))

except Exception as e:
    print(e)