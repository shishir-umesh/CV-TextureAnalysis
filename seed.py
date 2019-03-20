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


def findMatches(template,convPatches, valid_mask, gauss_mask, windowSize, halfWindow, ErrThreshold):

    #Reshaping them into a coloumn vector
    template = np.reshape(template, windowSize*windowSize)
    gauss_mask = np.reshape(gauss_mask, windowSize*windowSize)
    valid_mask = np.reshape(valid_mask, windowSize*windowSize)
    # PSEUDO CODE ----->   TotWeight = sum i,j GaussiMask(i,j)*ValidMask(i,j)
    total_weight = np.sum(np.multiply(gauss_mask, valid_mask))
    # PSEUDO CODE ----->   dist = (Template(ii,jj)-SampleImage(i-ii,j-jj))^2
    distance = (convPatches-template)**2
    # PSEUDO CODE ----->   SSD(i,j) = SSD(i,j) + dist*ValidMask(ii,jj)*GaussMask(ii,jj)
    # PSEUDO CODE ----->   SSD(i,j) = SSD(i,j) / TotWeight
    ssd = np.sum((distance*gauss_mask*valid_mask) / total_weight, axis=1)
    min_error = min(ssd)
    # print "Min err mat= "+str(min_error)
    mid = int(((2 * halfWindow + 1) ** 2) / 2)
    return [[err, convPatches[i][mid]] for i, err in enumerate(ssd) if err <= min_error*(1+ErrThreshold)]
