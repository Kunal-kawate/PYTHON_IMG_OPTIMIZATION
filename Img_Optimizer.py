# Image Optimizing
# pip install Pillow
from PIL import Image
# Croping 
im = Image.open("kunya.jpg")
im = im.crop((34, 23, 100, 100))
# Resizing
im = Image.open("Image1.jpg")
im = im.resize((50, 50))
# Flipping
im = Image.open("Image1.jpg")
im = im.transpose(Image.FLIP_LEFT_RIGHT)
# Rotating
im = Image.open("Image1.jpg")
im = im.rotate(360)
# Compressing
im = Image.open("kunya.jpg")
im.save("xxxxxxx.jpg", optimize=True, quality=50)
# Bluring
im = Image.open("Image1.jpg")
im = im.filter(Image.ImageFilter.BLUR)
# Sharpening
im = Image.open("Image1.jpg")
im = im.filter(Image.ImageFilter.SHARPEN)
# Set Brightness
im = Image.open("Image1.jpg")
im = Image.ImageEnhance.Brightness(im)
im = im.enhance(1.5)
# Set Contrast
im = Image.open("Image1.jpg")
im = Image.ImageEnhance.Contrast(im)
im = im.enhance(1.5)
# Adding Filters
im = Image.open("Image1.jpg")
im = Image.ImageOps.grayscale(im)
im = Image.ImageOps.invert(im)
im = Image.ImageOps.posterize(im, 4)
# Saving
im.save("Image1.jpg")