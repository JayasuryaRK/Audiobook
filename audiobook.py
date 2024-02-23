import pyttsx3
import fitz
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def save_file(audio):
    engine.save_to_file(audio,'test.mp3')
    engine.runAndWait()
def read_pdf(file_path):
    content = ""
    try:
        with fitz.open(file_path) as pdf_document:
            # Iterate through all pages and concatenate text
            for page_num in range(pdf_document.page_count):
                page = pdf_document[page_num]
                content += page.get_text()
        return content
    except Exception as e:
        print(f"Error: {e}")
        return None



pdf_file_path = 'pdf.pdf'
pdf_content = read_pdf(pdf_file_path)
if pdf_content:
    print("PDF content:")
    print(pdf_content)
    save_file(pdf_content)
    c=str(input("Do you want the audio book to be played?[y/n]"))
    if c=='y':
        speak(pdf_content)
    elif c=='Y':
        speak(pdf_content)
else:
    print("Failed to read PDF content.")
    speak("Failed to read PDF content.")
print("THANK YOU!!!")
