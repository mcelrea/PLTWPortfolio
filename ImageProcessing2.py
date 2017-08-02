# -*- coding: utf-8 -*-
'''
Eric_McElrea_1_4_2: Read and show an image.
'''
import matplotlib.pyplot as plt
import PIL.Image
import os.path
import numpy as np # “as” lets us use standard abbreviations
   
'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 

# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'Superman-Metropolis.jpg')
filename1 = os.path.join(directory, 'batman_ledge.PNG')
filename2 = os.path.join(directory, 'Flash207.jpg')

# Read the image as an PIL image
img = PIL.Image.open(filename)
img1 = PIL.Image.open(filename1)
img2 = PIL.Image.open(filename2)

#resize two of the images to be the same height as img (superman)
img2 = img2.resize((500, 800))
img1 = img1.resize((500,800))

#make a new image to paste all 3 images into
together = PIL.Image.new('RGBA', (1550, 800), (5, 5, 5, 0) )

#paste the 3 images back to back
together.paste(img,(0,0),mask=None)
together.paste(img2,(600,0),mask=None)
together.paste(img1,(1050,0),mask=None)

#save the combined image to the disk
together.save("combinedImage.jpg")

#reopen the combinedImage as a plt Image
filename = os.path.join(directory, 'combinedImage.jpg')
combinedImage2 = plt.imread(filename)

#loop through the entire combined image. It's big so this loop with the combined
#math takes some time
height = len(combinedImage2)
width = len(combinedImage2[0])
for r in range(height):
    for c in range(width):
        #sepia toned math pixel calculations
        tr = 0.393 * combinedImage2[r][c][0] + 0.769 * combinedImage2[r][c][1] + 0.189 * combinedImage2[r][c][1]
        tg = 0.349 * combinedImage2[r][c][0] + 0.686 * combinedImage2[r][c][1] + 0.168 * combinedImage2[r][c][1]
        tb = 0.272 * combinedImage2[r][c][0] + 0.534 * combinedImage2[r][c][1] + 0.131 * combinedImage2[r][c][1]
        tr = int(tr)
        tg = int(tg)
        tb = int(tb)
        if tr > 255:
            combinedImage2[r][c][0] = 255
        else:
            combinedImage2[r][c][0] = tr
        if tg > 255:
            combinedImage2[r][c][1] = 255
        else:
            combinedImage2[r][c][1] = tg
        if tb > 255:
            combinedImage2[r][c][2] = 255
        else:
            combinedImage2[r][c][2] = tb

'''Show the image data'''
fig, ax = plt.subplots(1, 1)
ax.axis('off') #turn off the axis
ax.imshow(combinedImage2, interpolation='none')
fig.show()