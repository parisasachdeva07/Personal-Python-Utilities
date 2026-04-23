import pyttsx3
import PyPDF2
import os

def read_my_pdf(file_path):
    if not os.path.exists(file_path):
        print("❌ File not found! Please check the path.")
        return

    try:
        # Initialize the speaker engine
        speaker = pyttsx3.init()
        
        with open(file_path, 'rb') as book:
            pdf_reader = PyPDF2.PdfReader(book)
            pages = len(pdf_reader.pages)
            print(f"📖 Found {pages} pages. Starting to read...")

            for num in range(pages):
                page = pdf_reader.pages[num]
                text = page.extract_text()
                print(f"Reading page {num + 1}...")
                speaker.say(text)
                speaker.runAndWait()
                
    except Exception as e:
        print(f"❌ An error occurred: {e}")

# Usage: Put the name of your PDF file here
# Example: read_my_pdf('DS_Notes.pdf')
read_my_pdf('sample.pdf')
