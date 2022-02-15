import sys
from PIL import Image

try:
    img = Image.open(sys.argv[1])
except:
    img = Image.open("./image/berke.jpg")

width, height = img.size
aspect_ratio = width / height
new_width = 120
new_height = aspect_ratio * new_width * 0.30
img = img.resize((new_width, int(new_height)))
img = img.convert("L")
pixels = img.getdata()

chars = ["B", "S", "#", "&", "@", "$", "%", "*", "!", ":", "."]
new_pixels = [chars[pixel // 25] for pixel in pixels]
new_pixels = "".join(new_pixels)

new_pixels_count = len(new_pixels)
ascii_image = [
    new_pixels[index : index + new_width]
    for index in range(0, new_pixels_count, new_width)
]
ascii_image = "\n".join(ascii_image)

with open(f"ascii_image.txt", "w") as f:
    f.write(ascii_image)
