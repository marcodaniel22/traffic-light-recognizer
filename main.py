import cv2
import numpy as np
import imageFilter
import blobDetector
import generalFunctions

img = cv2.imread('t1.jpg')

thresh = imageFilter.binaryImage(img)
inverted_thresh = generalFunctions.invertImage(thresh)
blobs = blobDetector.getBlobsFromImage(thresh)

blobDetector.printEachImageBlob(img, blobs)
