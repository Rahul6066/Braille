import pyautogui
import time
import pymsgbox
import pytesseract
from PIL import Image
import pdfplumber
import os

# Set path to Tesseract-OCR
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\rahul\Downloads\tesseract.exe"

# Function to extract text from an image
def extract_text_from_image(image_path):
    image = Image.open(image_path)
    return pytesseract.image_to_string(image, config="--psm 6").strip()

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_path):
    extracted_text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            extracted_text += page.extract_text() + " "
    return extracted_text.strip()

# Get file path from user
file_path = pymsgbox.prompt("Enter the full path of the image or PDF file:", "File Selection")

if not file_path or not os.path.exists(file_path):
    pymsgbox.alert("Invalid file path! Exiting.", "Error")
    exit()

# Extract text
if file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
    extracted_text = extract_text_from_image(file_path)
elif file_path.lower().endswith('.pdf'):
    extracted_text = extract_text_from_pdf(file_path)
else:
    pymsgbox.alert("Unsupported file type! Use an image or a PDF.", "Error")
    exit()

if not extracted_text:
    pymsgbox.alert("No text found in the file!", "Warning")
    exit()

print(f"Extracted Text: {extracted_text}")

# Prompt user to switch to Wokwi Serial Monitor
pymsgbox.alert("Switch to Wokwi Serial Monitor now!\nMake sure it's visible on screen.\nIt will be auto-focused in 3 seconds.", "Wokwi Input Alert")

# Wait and click into Serial Monitor (adjust coordinates based on screen layout)
time.sleep(3)
pyautogui.click(x=800, y=600)  # 💡 Adjust these coordinates as needed!

# Send the text
pyautogui.typewrite(extracted_text, interval=0.03)
pyautogui.press("enter")

print("✅ Text sent to Wokwi automatically!")
