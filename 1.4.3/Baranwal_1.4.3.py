""" 1.4.3 """

#4 Arrays and lists are similar in form of indexing values, but arrays are more 
#  mathematically manipulative and can be multidimentional tensors

#5: 


from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path
import numpy as np      # 'as' lets us use standard abbreviations

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')
# Saves the figure
###
# Make a rectangle of pixels yellow
###

###
# Change a region if condition is True
###

height = len(img)
width = len(img[0])
for r in range(155):
    for c in range(width):
        if sum(img[r][c])>500: # brightness R+G+B goes up to 3*255=765
            img[r][c]=[255,0,255] # R + B = magenta

height = len(img)
width = len(img[0])
for r in range(415, 470):
    for c in range(135, 165):
        if sum(img[r][c]) > 400:
            img[r][c]=[255,255, 0] # R + B = magenta

fig.savefig('women_sky_earing')


#5 :
# 960
# 584
# 94
# 63
# 69

#7:
# a: The code runs through each and every pixel and checks if it is bright enough, then changes it to magenta
# b: 