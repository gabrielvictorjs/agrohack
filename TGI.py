import cv2
img = cv2.imread("principal.png", 0)

## threshold
th, threshed = cv2.threshold(img, 100, 255,cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)

## findcontours
cnts = cv2.findContours(threshed, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2]



cv2.namedWindow('final', cv2.WINDOW_NORMAL)
cv2.imshow('final',threshed)
cv2.waitKey(0)
cv2.destroyAllWindows()




## filter by area
s1= 9
s2 = 15
xcnts = []
for cnt in cnts:
    if s1<cv2.contourArea(cnt) <s2:
        xcnts.append(cnt)
        print(cv2.contourArea(cnt))

print("Dots number: {}".format(len(xcnts)))


