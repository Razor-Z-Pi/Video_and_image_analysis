from PIL import Image, ImageDraw

width, height = 800, 600

image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

start = (100, 300)
end = (700, 300)

def koch(draw, order, start, end, angle=0):
    if order == 0:
        draw.line([start, end], fill="black")
    else:
        # Разделяем отрезок на 3 части
        delta_x = end[0] - start[0]
        delta_y = end[1] - start[1]
        p1 = (start[0] + delta_x / 3, start[1] + delta_y / 3)
        p3 = (start[0] + 2 * delta_x / 3, start[1] + 2 * delta_y / 3)

        # Вычисляем вершину треугольника
        length = ((delta_x / 3) ** 2 + (delta_y / 3) ** 2) ** 0.5
        p2 = (
            p1[0] + length * (3 ** 0.5 / 2),
            p1[1] - length * 0.5,
        )

        # Рекурсивно рисуем кривую Коха
        koch(draw, order - 1, start, p1, angle)
        koch(draw, order - 1, p1, p2, angle + 60)
        koch(draw, order - 1, p2, p3, angle - 60)
        koch(draw, order - 1, p3, end, angle)


koch(draw, order=4, start=start, end=end)

image.save("koch.png")
print("Изображение кривой Коха сохранено как koch.png")