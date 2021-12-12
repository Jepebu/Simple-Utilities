def find(template, searchArea):
    import cv2 as cv
    searchFor = cv.imread(template, cv.IMREAD_COLOR)
    searchIn = cv.imread(searchArea, cv.IMREAD_COLOR)
    findImage = cv.matchTemplate(searchIn, searchFor, cv.TM_CCOEFF_NORMED)
    minConfidence, maxConfidence, minLocation, maxLocation = cv.minMaxLoc(findImage)
    maxX, maxY = maxLocation
    return maxConfidence, maxX, maxY
