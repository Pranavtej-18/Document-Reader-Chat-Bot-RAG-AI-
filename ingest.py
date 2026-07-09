from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter

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

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 200
    )

    chunks = text_splitter.split_text(text);
    print(f"Total chunks: {len(chunks)}")
    print("chunks after splitting the text:")
    for chunk in chunks:
        print("c1: \n", chunk+"\n")

except Exception as e:
    print(e)