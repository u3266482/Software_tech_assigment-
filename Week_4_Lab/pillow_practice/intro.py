from PIL import Image

# create an image via import
file_name = 'cat.jpg'

image = Image.open(file_name)
# analyze the image 
print(image.size)
print(image.filename)
print(image.format)
# show the image
image.show()

#  flip the image
# image = image.transpose(Image.Transpose.ROTATE_90)

# # show the image 
# image.show()

# exercise 
#cat_rotated = image.rotate(30)
#cat_rotated.save('cat_rotated.png', 'png')