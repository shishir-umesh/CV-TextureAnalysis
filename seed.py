import numpy as np
from random import randint
from math import ceil, floor

def seed_image(img, seed_size, output_rows, output_cols):

    #Gets the dimensions of the input image
    (rows,cols) = np.shape(img)

    #Generates a random row and coloumn to be choosen as the top left coordinates for the seed patch
    randomRow = randint(0, rows - seed_size)
    randomCol = randint(0, cols - seed_size)

    # A 3-by-3 seed in the center randomly taken from the original image to be synthesized
    seed = img[randomRow:randomRow + seed_size, randomCol:randomCol + seed_size]

    synthesizedImage = np.zeros((output_rows,output_cols))

    #Get the coordinates of the center of the original image
    center_row = floor(output_rows / 2)
    center_col = floor(output_cols / 2)
    half_seedSize = floor(seed_size/2)
    synthesizedImage[center_row - half_seedSize : center_row + half_seedSize+1, center_col - half_seedSize : center_col + half_seedSize+1] = seed

    #Create a map of filled regions and set it to zeros
    filledMap = np.zeros((output_rows,output_cols),dtype=np.int8)
    filledMap[center_row - half_seedSize : center_row + half_seedSize+1, center_col - half_seedSize : center_col + half_seedSize+1] = np.ones((seed_size, seed_size))

    return synthesizedImage,filledMap
