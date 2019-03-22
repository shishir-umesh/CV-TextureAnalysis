import time
import matplotlib.pyplot as plt
import numpy as np
from skimage import io, morphology, exposure
from seed import *
from findMatches import *
import random

"""
We implement the pseudo code for the Efros and Leung, Non-Parametric Sampling Texture Analysis
"""

def textureSynthesis(imageFile, windowSize, outputSize):

    #Reads the image and reduces the value from 0-255 range down to 0-1 range as instructued in the pseudo code
    #Gets the number of rows and coloumns in the the original image
    print(imageFile.split('.')[0]+"-"+str(windowSize)+"-synth.gif")
    img = io.imread(imageFile)
    img = img/255.0
    row, col = np.shape(img)
    #Setting the ErrThreshold, MaxErrThreshold, seed size and the sigma values as mentioned in the NPS pseudo Code
    ErrThreshold = 0.1
    MaxErrThreshold = 0.3
    sigma = windowSize/6.4
    seed = 3
    halfWindow = (windowSize - 1) // 2
    totalPixels = outputSize*outputSize
    print("totalPixels =",totalPixels)
    filledPixels = seed * seed

    # Call the seed_image function which returns a randomly selected square patch from
    # sample of the size - (seed*seed) placed at the center of the new image
    synthesizedImage, filledMap = seed_image(img, seed, outputSize, outputSize)

    # Call the conv patches function that returns all the possible candidate patches
    # that can be convolved on from the image for the given windowSize
    convPatches = convolutionPatches(img,halfWindow)

    # To facilitate easier retrieval of neighbourhood about any point we pad the output image
    # and the filledMap with zeros.
    synthImagePad = np.lib.pad(synthesizedImage, halfWindow, mode='constant', constant_values=0)
    filledMapPad = np.lib.pad(filledMap, halfWindow, mode='constant', constant_values=0)

    # We create a Gaussian Mask of the given windowSize*windowSize for the specified sigma value
    # PSEUDO CODE -----> GaussMask = Gaussian2D(WindowSize,Sigma)
    gaussMask = GaussMask(windowSize,sigma)
    #print(gaussMask)

    # Run a while loop till all our pixels are filled
    while filledPixels < totalPixels:
        # PSEUDO CODE ----->  progress = 0
        progress = False

        # PSEUDO CODE ----->  PixelList = GetUnfilledNeighbors(Image)
        #You get a 2xn array with the first row being the x coordinate
        #and the second row being the y coordinate of all unfilled pixels that have filled pixels as their neighbors
        pixelList = np.nonzero(morphology.binary_dilation(filledMap) - filledMap)

        # PSEUDO CODE ----->  GetNeighborhoodWindow(Pixel)
        neighbors = []
        neighbors.append([np.sum(filledMap[pixelList[0][i] - halfWindow : pixelList[0][i] + halfWindow + 1, pixelList[1][i] - halfWindow : pixelList[1][i] + halfWindow + 1]) for i in range(len(pixelList[0]))])
        decreasingOrder = np.argsort(-np.array(neighbors, dtype=int))

        # PSEUDO CODE ----->  foreach Pixel in PixelList do
        for i in decreasingOrder[0]:

            template = synthImagePad[pixelList[0][i] - halfWindow + halfWindow:pixelList[0][i] + halfWindow + halfWindow + 1, pixelList[1][i] - halfWindow + halfWindow:pixelList[1][i] + halfWindow + halfWindow + 1]
            validMask = filledMapPad[pixelList[0][i] - halfWindow + halfWindow:pixelList[0][i] + halfWindow + halfWindow + 1, pixelList[1][i] - halfWindow + halfWindow:pixelList[1][i] + halfWindow + halfWindow + 1]

            # PSEUDO CODE ----->  BestMatches = FindMatches(Template, SampleImage)
            bestMatches = findMatches(template,convPatches,validMask,gaussMask,windowSize, halfWindow, ErrThreshold)
            # PSEUDO CODE ----->  BestMatch = RandomPick(BestMatches)
            bestMatch = randint(0, len(bestMatches)-1)

            # PSEUDO CODE ----->  if (BestMatch.error < MaxErrThreshold) then
            if bestMatches[bestMatch][0]<=MaxErrThreshold:
                # PSEUDO CODE -----> Pixel.value = BestMatch.value
                synthImagePad[halfWindow+pixelList[0][i]][halfWindow+pixelList[1][i]] = bestMatches[bestMatch][1]
                synthesizedImage[pixelList[0][i]][pixelList[1][i]] = bestMatches[bestMatch][1]
                filledMapPad[halfWindow+pixelList[0][i]][halfWindow+pixelList[1][i]] = 1
                filledMap[pixelList[0][i]][pixelList[1][i]] = 1
                filledPixels+=1

                # PSEUDO CODE -----> progress = 1
                progress = True

        # PSEUDO CODE -----> if progress == 0
        if not progress:
            # PSEUDO CODE -----> then MaxErrThreshold = MaxErrThreshold * 1.1
            MaxErrThreshold *= 1.1
        print(filledPixels)

    io.imsave(imageFile.split('.')[0]+"-"+str(windowSize)+"-synth.gif", synthesizedImage)
    plt.show()
    return


def GaussMask(windowSize, sigma):
    # This creates an windowSize*windowSize square 2D gaussian mask for a given value of sigma
    # PSEUDO CODE -----> GaussMask = Gaussian2D(WindowSize,Sigma)
    x, y = np.mgrid[-windowSize//2 + 1:windowSize//2 + 1, -windowSize//2 + 1:windowSize//2 + 1]
    g = np.exp(-((x**2 + y**2)/(2.0*sigma**2)))
    return g/g.sum()


def convolutionPatches(src_img, halfWindow):
    # PSEUDO CODE ----->  for i,j do
    # PSEUDO CODE ----->  for ii,jj do
    #Finds and stores all the possibel convolution patches possible for each given pixel
    convPatches = []
    for i in range(halfWindow, src_img.shape[0]-halfWindow-1):
        for j in range(halfWindow, src_img.shape[1]-halfWindow-1):
            convPatches.append(np.reshape(src_img[i-halfWindow:i + halfWindow + 1, j - halfWindow: j + halfWindow + 1], (2 * halfWindow + 1) ** 2))
    convPatches = np.double(convPatches)
    return convPatches



if __name__ == '__main__':
    textureSynthesis("textures/T1.gif", 11, 200)
