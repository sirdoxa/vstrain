from PIL import Image
import pytesseract


# in this variable you should enter your "tesseract.exe" path location
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def ocr():
    path = input('Enter your image path ==> ')
    img = Image.open(path)
    txt = pytesseract.image_to_string(img)
    print(f"The result is:\n{txt}")

ocr()
