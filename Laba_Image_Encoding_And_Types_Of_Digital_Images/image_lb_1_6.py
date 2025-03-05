from PIL import Image

width, height = 800, 600

c = complex(-0.7, 0.27015)  # Параметр для множества Жулиа

def julia(c, z, max_iter):
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z * z + c
        n += 1
    return n

def create_julia(width, height, c, max_iter=100):
    image = Image.new("RGB", (width, height), "white")
    pixels = image.load()

    for x in range(width):
        for y in range(height):
            # Масштабируем координаты
            re = (x - width / 2) / (width / 4)
            im = (y - height / 2) / (height / 4)
            z = complex(re, im)

            # Вычисляем значение для точки
            m = julia(c, z, max_iter)

            # Цвет в зависимости от количества итераций
            color = 255 - int(m * 255 / max_iter)
            pixels[x, y] = (color, color, color)

    return image

image = create_julia(width, height, c, max_iter=100)

image.save("julia.png")
print("Изображение множества Жулиа сохранено как julia.png")