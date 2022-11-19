import cv2
from funcs import functs
drfz = functs()
img=cv2.imread('9.jpg')
scale_percent = 80  # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

# resize image
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
gray = drfz.get_grayscale(resized)
thresh = drfz.thresholding(gray)
opening = drfz.opening(gray)
qanny = drfz.kanny(gray)
boxess = drfz.boX(gray)

#image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow("gray", gray)
cv2.imshow("thresh 2", thresh)
cv2.imshow("opening 3", opening)
cv2.imshow("Qany 3", qanny)
cv2.imshow("box 3", boxess)
cv2.waitKey(0)
