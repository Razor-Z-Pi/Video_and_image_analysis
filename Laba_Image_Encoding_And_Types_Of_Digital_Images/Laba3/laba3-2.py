from PIL import Image

input_image = "./pixel.jpg"  # Путь к исходному изображению
output_image = "output.jpg"  # Путь для сохранения результата

img = Image.open(input_image)
    
width, height = img.size
    
new_img = Image.new('RGB', (width, height))
    
for x in range(width):
    for y in range(height):
        # Получаем оригинальные значения RGB
        r, g, b = img.getpixel((x, y))
        new_r = g 
        new_g = b  
        new_b = r
            
        # Устанавливаем новый пиксель
        new_img.putpixel((x, y), (new_r, new_g, new_b))
    
new_img.save(output_image)
print(f"Изображение сохранено как {output_image}")