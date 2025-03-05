from PIL import Image, ImageDraw
import random

width, height = 800, 800 

image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

x, y = 0, 0

def transform(x, y):
    r = random.random()
    if r < 0.01:
        return (0, 0.16 * y)
    elif r < 0.86:
        return (0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6)
    elif r < 0.93:
        return (0.2 * x - 0.26 * y, 0.26 * x + 0.22 * y + 1.6)
    else:
        return (-0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44)

for _ in range(100000):
    x, y = transform(x, y)
    px = int(width / 2 + x * width / 11)
    py = int(height - y * height / 11)
    draw.point((px, py), fill="green")

image.save("barnsley_fern.png");
image.show()