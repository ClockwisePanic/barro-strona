from PIL import Image
from rembg import remove
import io

INPUT  = "images/IMG-20260620-WA0003.jpg"
OUTPUT = "images/IMG-20260620-WA0003_test.jpg"
BG_COLOR = (245, 245, 245)  # #f5f5f5

with open(INPUT, "rb") as f:
    raw = f.read()

print("Usuwam tło...")
result_bytes = remove(raw)

fg = Image.open(io.BytesIO(result_bytes)).convert("RGBA")

bg = Image.new("RGBA", fg.size, BG_COLOR + (255,))
bg.paste(fg, mask=fg.split()[3])

bg.convert("RGB").save(OUTPUT, "JPEG", quality=92)
print(f"Zapisano: {OUTPUT}")
