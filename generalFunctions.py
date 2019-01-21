def calcMinArea(point, size):
    minPoint = point

    if point >= size:
        minPoint = point - size
    if minPoint < 0:
        minPoint = 0

    return minPoint


def calcMaxArea(point, size, maxSize):
    maxPoint = point

    if (point + size) <= maxSize:
        maxPoint = (point + size)
    else:
        maxPoint = maxSize

    return maxPoint


def invertImage(img):
    return (255-img)
