"""
Code Challenge
  Name: 
    Image Processing using PIL
  Filename: 
    imgprocess.py
  Problem Statement:
    Given an image, perform image processing operations. 

    Keep only one output image i.e perform all tasks on the same image (override) 
    and print only the name of your output image with extension name in the end of your program. 

    Take the Image name from User (Handle the extension for image file name in your code)
    
    The image processing features to be provided by your code are:

        a.     Greyscale
        .b.     Rotate_90 (Rotate the given image file by 90 clockwise)
        c.     Crop (Center) (size = 160(W), 204(H))
        d.     Thumbnail – Generate the thumbnail of the given image (size = 75, 75)
    
"""
from PIL import Image
import os


    
# Open the image and create it's instance
img = Image.open("a.jpg")

# Gives the dimensions or the size of the image
print ("original image size=",img.size)


# Resizing the image 
small_im = img.resize((160, 240), resample=Image.BICUBIC)
small_im.save('b.jpg')
print("resize image :-",small_im.size)

#rotate the image 90`

# ROTATE_90, ROTATE_180, ROTATE_270
# ROTATE_90, ROTATE_180, ROTATE_270
img_rotate = img.transpose(Image.ROTATE_90)
 
# Displays the rotated image
#img_rotate.show()  

img_rotate.save("sample1.jpg")
print("after rotating 90 degree image size=",img_rotate.size)


# Creating Thumbnail
img = Image.open("sample1.jpg")
img.thumbnail((75, 75))
print("thumbnail image size=",img.width, img.height)
img.save('thumb_sample1.jpg')





#gray image
	
import numpy as np
import matplotlib.pyplot as py
 
img = py.imread('a1.jpg')
py.imshow(img)
def rgb2gray(rgb):
    fil = [0.299, 0.587, 0.144, 0]
    return np.dot(rgb, fil)

	
img = rgb2gray(img)
py.imshow(img,cmap='gray')