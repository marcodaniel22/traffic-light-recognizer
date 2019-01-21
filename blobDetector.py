import cv2
import numpy as np
import generalFunctions


def getBlobsFromImage(img):
    params = cv2.SimpleBlobDetector_Params()

    params.filterByCircularity = True
    params.minCircularity = 0.6
    params.maxCircularity = 1

    params.filterByConvexity = True
    params.minConvexity = 0.9
    params.maxConvexity = 1

    # Set  up the detector with default parameters.
    detector = cv2.SimpleBlobDetector_create(params)

    # Detect blobs.
    return detector.detect(img)


def showAllImageBlobs(img, blobs):
    im_with_keypoints = cv2.drawKeypoints(img, blobs, np.array(
        []), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imshow("image-with-blobs", im_with_keypoints)
    cv2.waitKey(0)


def printEachImageBlob(img, blobs):
    for i in range(len(blobs)):
        x = int(blobs[i].pt[0])
        y = int(blobs[i].pt[1])
        area = img[
            generalFunctions.calcMinArea(y, 50):
            generalFunctions.calcMaxArea(y, 50, img.shape[0]),
            generalFunctions.calcMinArea(x, 30):
            generalFunctions.calcMaxArea(x, 30, img.shape[1]),
        ]
        resized_image = cv2.resize(area, (150, 250))
        cv2.imshow("blob{i}", resized_image)
        cv2.waitKey(0)
