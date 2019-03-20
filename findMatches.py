import numpy as np

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
