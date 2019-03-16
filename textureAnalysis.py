import time
import matplotlib.pyplot as plt
import numpy as np
from skimage import io, morphology, exposure
from seed import *

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

    synthesizedImage, filledMap = seed_image(img, seed, 200, 200)

    #To facilitate easier retrieval of neighbourhood about any point pad the output image
    # and the filledMap with zeros.
    synthImagePad = np.lib.pad(synthesizedImage, halfWindow, mode='constant', constant_values=0)
    filledMapPad = np.lib.pad(filledMap, halfWindow, mode='constant', constant_values=0)

    return


if __name__ == '__main__':
    textureAnalysis("textures/T2.gif", 11)
