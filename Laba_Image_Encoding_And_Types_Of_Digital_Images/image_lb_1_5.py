from PIL import Image

width, height = 800, 600

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z * z + c
        n += 1
    return n

def create_mandelbrot(width, height, max_iter=100):
    image = Image.new("RGB", (width, height), "white")
    pixels = image.load()

    for x in range(width):
        for y in range(height):
            # Масштабируем координаты
            re = (x - width / 2) / (width / 4)
            im = (y - height / 2) / (height / 4)
            c = complex(re, im)

            # Вычисляем значение для точки
            m = mandelbrot(c, max_iter)

            # Цвет в зависимости от количества итераций
            color = 255 - int(m * 255 / max_iter)
            pixels[x, y] = (color, color, color)

    return image

image = create_mandelbrot(width, height, max_iter=100)

image.save("mandelbrot.png")
print("Изображение множества Мандельброта сохранено как mandelbrot.png")