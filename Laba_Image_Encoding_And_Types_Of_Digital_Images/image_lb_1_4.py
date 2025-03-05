from PIL import Image, ImageDraw

width, height = 800, 600

image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

start = (200, 300)
end = (600, 300)

def dragon(draw, order, start, end, sign=1):
    if order == 0:
        draw.line([start, end], fill="black")
    else:
        # Находим середину отрезка
        mid_x = (start[0] + end[0]) / 2 - sign * (end[1] - start[1]) / 2
        mid_y = (start[1] + end[1]) / 2 + sign * (end[0] - start[0]) / 2
        mid = (mid_x, mid_y)

        # Рекурсивно рисуем дракона
        dragon(draw, order - 1, start, mid, 1)
        dragon(draw, order - 1, mid, end, -1)

dragon(draw, order=12, start=start, end=end)

image.save("dragon.png")
print("Изображение дракона Хартера-Хейтуэя сохранено как dragon.png")