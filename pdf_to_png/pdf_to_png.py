from pdf2image import convert_from_path
from PIL import Image

# Convert PDF pages to images
pages = convert_from_path("C:\\Users\\Administrator\\Desktop\\school-materials\\Unofficial Transcript_unlocked.pdf", dpi=150)

# Combine pages vertically
width = max(p.width for p in pages)
height = sum(p.height for p in pages)

combined = Image.new("RGB", (width, height), "white")

y_offset = 0
for page in pages:
    combined.paste(page, (0, y_offset))
    y_offset += page.height

combined.save("output.png")