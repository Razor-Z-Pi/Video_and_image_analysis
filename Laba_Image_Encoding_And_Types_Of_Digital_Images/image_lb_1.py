from PIL import Image, ImageDraw

width, height = 800, 800 

image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

def sierpinski_triangle(draw, x, y, size, depth):
    if depth == 0:
        points = [(x, y), (x + size, y), (x + size / 2, y - size * (3 ** 0.5) / 2)]
        draw.polygon(points, fill="black")
    else:
        new_size = size / 2
        depth -= 1
        sierpinski_triangle(draw, x, y, new_size, depth)
        sierpinski_triangle(draw, x + new_size, y, new_size, depth)
        sierpinski_triangle(draw, x + new_size / 2, y - new_size * (3 ** 0.5) / 2, new_size, depth)

sierpinski_triangle(draw, 50, 700, 700, 6)

image.save("sierpinski_triangle.png")
image.show