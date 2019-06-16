
"""
Mini Project 1

Certificate Generator

Develop a Python code that can generate certificates in image format. 
It must take names and other required information from the user and generates 
certificate of participation in a Python Bootcamp conducted by Forsk.

Certificate should have Forsk Seal, Forsk Signature, Different Fonts

"""

	
name1=input("enter participants name>.")
date=input("date of start training >")


if name and date:
     
    from PIL import Image, ImageDraw, ImageFont
    import os 
    # create Image object with the input image
     
    image = Image.open('cat.jpg')
    print (image.size) 
    # initialise the drawing context with
    # the image object as background
     
    draw = ImageDraw.Draw(image)
    
    
    font = ImageFont.truetype('Roboto-Medium.ttf', size=45)
    font1 = ImageFont.truetype('Roboto-Medium.ttf', size=85)
 
    # starting position of the message
    
    # draw the message on the background
       
    (x, y) = (670, 1709)
    message = date
    color = 'rgb(0, 0, 0)' # black color
    draw.text((x, y), message, fill=color, font=font)
    
    
    (x, y) = (2100, 1709)
    name = 'Silvester Franades'
    color = 'rgb(0,0,0)' # white color
    draw.text((x, y), name, fill=color, font=font)
    
    (x, y) = (1200, 1100)
    message = name1
    color = 'rgb(0, 0, 0)' # black color
    draw.text((x, y), message, fill=color, font=font1)
    
    # save the edited image
     
    image.save(name1+'.png')


else:
    print("Please enter participants name")
# import required classes
