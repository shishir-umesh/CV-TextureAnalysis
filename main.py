import time
import logging
from logging.config import dictConfig
from textureSynthesis import *


if __name__ == '__main__':

    logging.basicConfig(filename="runTime.log", level=logging.INFO)

    filenames = ["T1.gif","T2.gif","T3.gif","T4.gif","T5.gif",]
    outputSize = 200
    for file in filenames:
        for windowSize in [5,9,11,15,17,21,23]:
            start = time.time()
            #Run the Algorithm with the parameters
            textureSynthesis("textures/"+file, windowSize, outputSize)
            end = time.time()
            #Calculate and log the running times
            logging.info("\t"+file+"-"+str(windowSize)+"\t:-  "+str(end-start)+" secs")
