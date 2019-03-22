import time
from textureSynthesis import *


if __name__ == '__main__':

    filenames = ["T1.gif","T2.gif","T3.gif","T4.gif","T5.gif",]
    outputSize = 200
    for file in filenames:
        for windowSize in [5,9,11,15,21,23]:
            start = time.time()
            #Run the Algorithm with the parameters
            textureSynthesis("textures/"+file, windowSize, outputSize)
            end = time.time()
            #Calculate and print the running times
