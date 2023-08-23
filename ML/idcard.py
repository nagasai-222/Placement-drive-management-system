import pytesseract
import cv2
import pytesseract
!pip install pytesseract



!sudo apt install tesseract-ocr

# Read the image
image1 = cv2.imread('/content/idcard.png')
image2 = cv2.imread('/content/idback.png')


# Get the text from the image using pytesseract
text1 = pytesseract.image_to_string(image1)
# for i in text1:
#   print(i,end="")
text2 = pytesseract.image_to_string(image2)

# Print the text
print(text1)
print(text2)
