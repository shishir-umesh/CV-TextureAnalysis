import time
from textureSynthesis import *


if __name__ == '__main__':

    filenames = ["T1.gif","T2.gif","T3.gif","T4.gif","T5.gif",]

    for file in filenames:
        #for windowSize in [5,9,11,15,21,23,25]:
        start = time.time()
        #Run the Algorithm with the parameters
        textureAnalysis("textures/"+file, 11)
        end = time.time()
        #Calculate and print the running times
