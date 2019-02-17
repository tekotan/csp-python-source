import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import numpy as np
import PIL
import os
def make_mask(rows, columns, stripe_width):
    '''An example mask generator
    Makes slanted stripes of width stripe_width
    image
    returns an ndarray of an RGBA image rows by columns
    '''
    
    img = PIL.Image.new('RGBA', (columns, rows))
    image = np.array(img)
    rows = [round(i**1.1) for i in range(rows) if i**1.1 < rows]
    columns = [round(i**1.3) for i in range(columns) if round(i**1.3) < columns]
    for row in rows:
        for column in columns:
            image[row][column] = np.random.randint(high=255, low=0, size=[4])*255
    return image
    
if __name__ == "__main__":
    image = make_mask(1999,1999,20)
    directory = os.path.dirname(os.path.abspath(__file__)) 
    # Build an absolute filename from directory + filename
    filename = os.path.join(directory, 'woman.jpg')
    # Read the image data into an array
    img = plt.imread(filename).copy()
    
    '''Show the image data'''
    # Create figure with 1 subplot
    fig, ax = plt.subplots(1, 2)
    # Show the image data in a subplot
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
    ax[1].imshow(img, interpolation='none')
    ax[0].imshow(image)
    fig.savefig('mask')