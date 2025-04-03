from PIL import Image
import binascii
from numpy import *
from scipy.ndimage import filters

hex_data1 = "you hex code"

hex_data1 = hex_data1.replace(" ", "")

binary_data = binascii.unhexlify(hex_data1)

with open("image1.jpg", "wb") as file:
    file.write(binary_data)


hex_data2 = "you hex code"

hex_data2 = hex_data2.replace(" ", "")

binary_data = binascii.unhexlify(hex_data2)

with open("image2.jpg", "wb") as file:
    file.write(binary_data)


pil_img1 = Image.open("image1.jpg.jpg")
pil_img1.save("image1.jpg.png")

pil_img2 = Image.open("simage2.jpgun.jpg")
pil_img2.save("image2.jpg.png")

pil_img3 = Image.blend(pil_img1, pil_img2, 0.5)
pil_img3.save("output_image.png")


im = array(pil_img1.convert("L"))
im2 = filters.gaussian_filter(im, 3)
pil_img1 = Image.fromarray(im2)
pil_img1.save("gausian.jpg")

