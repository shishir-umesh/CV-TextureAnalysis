import time
import matplotlib.pyplot as plt
import numpy as np
from skimage import io, morphology, exposure
from seed import *
import random

"""
We implement the pseudo code for the Efros and Leung, Non-Parametric Sampling Texture Analysis
"""

def textureAnalysis(imageFile, windowSize):

    #Reads the image and reduces the value from 0-255 range down to 0-1 range as instructued in the pseudo code
    #Gets the number of rows and coloumns in the the original image
    img = io.imread(imageFile)
    img = img/255.0
    row, col = np.shape(img)

    #Setting the ErrThreshold, MaxErrThreshold, seed size and the sigma values as mentioned in the NPS pseudo Code
    ErrThreshold = 0.1
    MaxErrThreshold = 0.3
    sigma = windowSize/6.4
    seed = 3
    halfWindow = (windowSize - 1) // 2
    totalPixels = 200*200
    filledPixels = seed * seed

    synthesizedImage, filledMap = seed_image(img, seed, 200, 200)

    #To facilitate easier retrieval of neighbourhood about any point pad the output image
    # and the filledMap with zeros.
    synthImagePad = np.lib.pad(synthesizedImage, halfWindow, mode='constant', constant_values=0)
    filledMapPad = np.lib.pad(filledMap, halfWindow, mode='constant', constant_values=0)

    gaussMask = GaussMask(windowSize,sigma)
    #print(gaussMask)

    while filledPixels < totalPixels:
        progress = False
        #You get a 2xn array with the first row being the x coordinate
        #and the second row being the y coordinate of all unfilled pixels that have filled pixels as their neighbors
        pixelList = np.nonzero(morphology.binary_dilation(filledMap) - filledMap)
        neighbors = []
        neighbors.append([np.sum(filledMap[pixelList[0][i] - halfWindow : pixelList[0][i] + halfWindow + 1, pixelList[1][i] - halfWindow : pixelList[1][i] + halfWindow + 1]) for i in range(len(pixelList[0]))])
        decreasingOrder = np.argsort(-np.array(neighbors, dtype=int))

        break
    return


def GaussMask(windowSize, sigma):
    x, y = np.mgrid[-windowSize//2 + 1:windowSize//2 + 1, -windowSize//2 + 1:windowSize//2 + 1]
    g = np.exp(-((x**2 + y**2)/(2.0*sigma**2)))
    return g/g.sum()


if __name__ == '__main__':
    textureAnalysis("textures/T2.gif", 11)
