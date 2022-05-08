#Import required Image library
from PIL import Image

#Create an Image Object from an Image
im = Image.open("/home/kali/Downloads/1.png")

#Display actual image
im.show()

#Make the new image half the width and half the height of the original image
resized_im = im.resize((64, 64))

#Display the resized imaged
resized_im.show()

#Save the cropped image
resized_im.save('64x64.png')