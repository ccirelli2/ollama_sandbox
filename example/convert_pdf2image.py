"""
Example script in order to convert a pdf to images.
"""
# Libraries
import os

from pdf2image import convert_from_path

# Globals
DIR_ROOT = "/Users/temp-admin/repositories/ollama_sandbox"
DIR_DATA = os.path.join(DIR_ROOT, 'data')
FILE_NAME = "ford10k.pdf"
DIR_IMGS = os.path.join(DIR_DATA, 'imgs')

# Create Output Directory
if not os.path.exists(DIR_IMGS):
    print(f"Directory does not exist.  Creating at {DIR_IMGS}")
    os.mkdir(DIR_IMGS)
else:
    print(f"Output directory exists at {DIR_IMGS}")

# Convert PDF to Image
print("Converting pdf to images")
images = convert_from_path(
    pdf_path=os.path.join(DIR_DATA, FILE_NAME),
    dpi=500,
)
print("\t Process completed")

# Writing Images to File
print("Writing images to file")

for i, image in enumerate(images):
    print(f"\t saving images {i}")
    fname = 'image' + str(i) + '.png'
    image.save(os.path.join(DIR_IMGS, fname), "PNG")

print("Script completed")
