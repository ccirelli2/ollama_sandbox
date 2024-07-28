"""
Example script in order to convert a pdf to images.
"""
# Libraries
import os

import pytesseract
from PIL import Image

# Globals
DIR_ROOT = "/Users/temp-admin/repositories/ollama_sandbox"
DIR_DATA = os.path.join(DIR_ROOT, 'data')
DIR_IMGS = os.path.join(DIR_DATA, 'imgs')
DIR_TEXT = os.path.join(DIR_DATA, 'text')

# Create Output Directory
if not os.path.exists(DIR_IMGS):
    print(f"Directory does not exist.  Creating at {DIR_TEXT}")
    os.mkdir(DIR_TEXT)
else:
    print(f"Output directory exists at {DIR_TEXT}")

# Convert Image to Text
print("Obtaining images")
images = os.listdir(DIR_IMGS)

# Iterate Images
for img in images:
    # Create Path
    path = os.path.join(DIR_IMGS, img)
    
    # OCR Image
    text = pytesseract.image_to_string(Image.open(path))
    
    # Write Text to Directory
    filename = img.replace("image", "page").replace(".png", ".text")
    path = os.path.join(DIR_TEXT, filename)
    print(f"Writing {filename}")
    with open(path, 'w') as f:
        f.write(text)

print("Process completed")
        


