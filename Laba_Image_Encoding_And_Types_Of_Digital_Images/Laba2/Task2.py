from PIL import Image
import numpy as np

# Создаем массив с данными изображения

image_data = np.array([
    [[255, 0, 0], [0, 255, 0], [0, 0, 255]],
    [[255, 255, 0], [255, 0, 255], [0, 255, 255]],
    [[255, 255, 255], [128, 128, 128], [0, 0, 0]]
], dtype=np.uint8)

# Создадим объект изображения из массива
image = Image.fromarray(image_data)
image.save("colors_3x3.png")