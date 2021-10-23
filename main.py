import PyPDF2
import pyttsx3
import webbrowser as wb
wb.register('chrome', None)
wb.open("https://www.google.com/")

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
book = open('The Alchemist.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)

speaker = pyttsx3.init()
for num in range(0, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()

book = open('The Alchemist.pdf', 'rb')


