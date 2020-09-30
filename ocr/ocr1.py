from PIL import Image 
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

page = "img.jpg"
outfile = "out_text.txt"
f = open(outfile, "a")
text = str(pytesseract.image_to_string(Image.open(page)))
text = text.replace('-\n', '')
f.write(text)
f.close()