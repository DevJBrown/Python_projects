#IMport Libarys
from gtts import gTTS
import PyPDF2
from tkinter import Tk, filedialog

#open file
pdf_file = filedialog.askopenfilename(
    title="Select a PDF file",
    filetypes=[("PDF Files", "*.pdf")]
)

if not pdf_file:
    print("No file selected. Closing...")
    exit()

#Create reader object
pdf_Reader = PyPDF2.PdfFileReader(pdf_file)
count = pdf_Reader.numPages
textList = []

for i in range(count):
    try:
        page = pdf_Reader.getPages(i)
        textList.append(page.extractText())
    except:
        pass

textString = " ".join(textList)

print(textString)

language = 'en'

myAudio = gTTS(text=textString, lang=language, slow=False)

myAudio.save("Audio.mp3")
