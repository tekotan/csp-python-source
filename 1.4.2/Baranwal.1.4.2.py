""" 1.4.2 """

#5:../Users/Student login/Desktop/nice.jpg

#6: Cloud 9 is a linux file system so does not have C:\ or any of such windows file paths

# 7:

'''
JDoe_JSmith_1_4_2: Read and show an image.
'''
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path
import numpy as np      # 'as' lets us use standard abbreviations

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'PCWmice1.jpg')
# Read the image data into an array
img = plt.imread(filename)

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img)
ax.plot(40, 45, 'ro')
ax.plot(140, 40, 'ro')
ax.plot(115, 40, 'ro')
# Show the figure on the screen
# fig.show()
fig.savefig('crazy_mice')

#7a: 300, 400
#8a: Figure, AxesSubplot
#8b: savefig, fig, filename, Figure
#9a: imshow, ax[0]

#10: The interpolation keyword overrides the global blurring of the pixels to prevent the pixelation

#12: One of the methods of the Axes class is annotate, which adds text to the x, y
#    coordinates given. One optional parameter is xytext which is where exactly to 
#    place the annotate. defaults to xy

