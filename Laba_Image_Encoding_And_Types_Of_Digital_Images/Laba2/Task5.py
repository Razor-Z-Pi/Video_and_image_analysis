from PIL import Image

width = 159  # Ширина изображения
height = 162  # Высота изображения
bits_per_pixel = 24  # Глубина цвета

# Загрузка сырых данных пикселей из файла
with open('khsu.bmp', 'rb') as f:
    pixel_data = f.read()

# Проверка размера данных
expected_size = width * height * (bits_per_pixel // 8)  # Ожидаемый размер данных
if len(pixel_data) < expected_size:
    raise ValueError(f"Недостаточно данных. Ожидалось {expected_size} байт, получено {len(pixel_data)} байт.")

# Формат пиксельных данных: RGB (3 байта на пиксель)
try:
    image = Image.frombytes('RGB', (width, height), pixel_data)
except ValueError as e:
    print(f"Ошибка при создании изображения: {e}")
    # Обрезаем данные до ожидаемого размера
    pixel_data = pixel_data[:expected_size]
    image = Image.frombytes('RGB', (width, height), pixel_data)

image.save('new_image.bmp')
image.show()