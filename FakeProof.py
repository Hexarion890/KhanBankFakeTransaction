from PIL import Image, ImageDraw, ImageFont
import os
import re
from datetime import datetime

# --- CONFIG ---------------------------------------------------------
IMAGE_PATH = "FakeProof.jpg"
OUTPUT_BASENAME = "output"
EXT = ".jpg"
FONT_PATH = r"arial.ttf"

FONT_SIZES = {
    "MONGO": 86,
    "NER": 50,
    "DANS": 51,
    "UTAG": 50,
    "TIME": 56,
    "TIME2": 40
}

TEXT_COLORS = {
    "DEFAULT": (0, 0, 0),       # black
    "TIME":    (74, 81, 100),   # grey
    "TIME2":   (76, 76, 76)      # dark red
}

POSITIONS = {
    "MONGO": (355, 815),     # X will be centered
    "NER":   (95, 1517),
    "DANS":  (95, 1599),
    "UTAG":  (96, 1849),
    "TIME":  (355, 970),
    "TIME2": (60, 35)
}

CHAR_SPACING = {
    "DANS": 3
}

IMAGE_WIDTH = 1080
# --------------------------------------------------------------------

def next_free_filename(basename, ext):
    pattern = re.compile(rf"^{re.escape(basename)}(\d+){re.escape(ext)}$")
    max_n = 0
    for fname in os.listdir("."):
        m = pattern.match(fname)
        if m:
            max_n = max(max_n, int(m.group(1)))
    return f"{basename}{max_n + 1}{ext}"

def draw_spaced_text(draw, position, text, font, fill, spacing):
    x, y = position
    for char in text:
        draw.text((x, y), char, font=font, fill=fill)
        x += font.getlength(char) + spacing

# Load image and create draw object
img = Image.open(IMAGE_PATH)
draw = ImageDraw.Draw(img)

# Ask user input
MONGO = input("Enter the MONGO (amount): ")
NER   = input("Enter the NER (name): ")
DANS  = input("Enter the DANS (account number): ")
UTAG  = input("Enter the UTAG (transaction note): ")

# Get current time and define second time
current_time = datetime.now().strftime("%Y/%m/%d %H:%M")
second_time = datetime.now().strftime("%H:%M")

# Draw all fields
for field, text in [
    ("MONGO", MONGO),
    ("NER", NER),
    ("DANS", DANS),
    ("UTAG", UTAG),
    ("TIME", current_time),
    ("TIME2", second_time)
]:
    font = ImageFont.truetype(FONT_PATH, FONT_SIZES[field])
    fill_color = TEXT_COLORS.get(field, TEXT_COLORS["DEFAULT"])

    if field in ("MONGO", "TIME"):
        text_width = font.getlength(text)
        centered_x = (IMAGE_WIDTH - text_width) // 2
        y = POSITIONS[field][1]
        draw.text((centered_x, y), text, fill=fill_color, font=font)

    elif field in CHAR_SPACING:
        draw_spaced_text(draw, POSITIONS[field], text, font=font, fill=fill_color, spacing=CHAR_SPACING[field])

    else:
        draw.text(POSITIONS[field], text, fill=fill_color, font=font)

# Save output
output_path = next_free_filename(OUTPUT_BASENAME, EXT)
img.save(output_path)
img.show()
print(f"Saved to {output_path}")
