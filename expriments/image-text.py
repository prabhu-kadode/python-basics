from PIL import Image
import pytesseract
import os

# Ensure that the Tesseract executable is in your PATH or specify the path directly
# Uncomment and set the path to tesseract executable if it's not in your PATH
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Path to the image file
image_path = './expriments/code.png'

# Load the image from file
try:
    image = Image.open(image_path)
except IOError:
    print(f"Error: File '{image_path}' not found or unable to open.")
    exit(1)

# Perform OCR
text = pytesseract.image_to_string(image)

# Print the extracted text
print("Extracted text:")
print(text)
