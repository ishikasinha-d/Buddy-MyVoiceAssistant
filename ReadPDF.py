import pyttsx3 as ptx
import PyPDF2

book= open('Dummyfile.pdf', 'rb')
pdfReader= PyPDF2.PdfFileReader(book)
pages=pdfReader.numPages
print(pages)
speaker= ptx.init()
for num in range(pages):
    page=pdfReader.getPage(num)
    text=page.extractText()
    speaker.say(text)
    speaker.runAndWait()
