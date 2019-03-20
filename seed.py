import numpy as np
from random import randint
from math import ceil, floor

def seed_image(img, seed_size, output_rows, output_cols):

    """
    INPUT:
    1. img - Original sample image from the user.
    2. seed_size - The size of the seed image to be randomly choosen
    output_rows - The number of rows to be present in the output image
    output_cols - The number of cols to be present in the input image

    OUTPUT:
    synthesizedImage - The array with the random seed present at the center
    filledMap - The array with the regions filled set as 1 and the unfilled regions set as 0.
    """

    #Gets the dimensions of the input image
    (rows,cols) = np.shape(img)

    #Generates a random row and coloumn to be choosen as the top left coordinates for the seed patch
    randomRow = randint(0, rows - seed_size)
    randomCol = randint(0, cols - seed_size)

    # A 3-by-3 seed in the center randomly taken from the original image to be synthesized
    seed = img[randomRow:randomRow + seed_size, randomCol:randomCol + seed_size]

    #Creates an empty array with zeros to store the new synthesized image
    synthesizedImage = np.zeros((output_rows,output_cols))

    #Get the coordinates of the center of the original image
    center_row = floor(output_rows / 2)
    center_col = floor(output_cols / 2)
    half_seedSize = floor(seed_size/2)
    #Stores the random seed at the center of the new image array
    synthesizedImage[center_row - half_seedSize : center_row + half_seedSize+1, center_col - half_seedSize : center_col + half_seedSize+1] = seed

    #Create a map of filled regions with 0 and sets the regions with the seed as 1.
    filledMap = np.zeros((output_rows,output_cols),dtype=np.int8)
    filledMap[center_row - half_seedSize : center_row + half_seedSize+1, center_col - half_seedSize : center_col + half_seedSize+1] = np.ones((seed_size, seed_size))

    #Returns the new image and the filled map arrays
    return synthesizedImage,filledMap
