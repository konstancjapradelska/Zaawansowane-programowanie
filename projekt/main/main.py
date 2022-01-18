import cv2
import imutils

# Initializing the HOG person
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Reading the Image
image = cv2.imread('./images/humans1.jpg')

# Resizing the Image
image = imutils.resize(image,
                       width=min(600, image.shape[1]))

# Detecting all humans
(humans, _) = hog.detectMultiScale(image,
                                   winStride=(4, 4),
                                   padding=(8, 8),
                                   scale=1.07)
# Number of humans on image
print(f'Wykryto ludzi: {len(humans)}')

# Drawing the rectangle regions on hu,ams
for (x, y, w, h) in humans:
    cv2.rectangle(image, (x, y),
                  (x + w, y + h),
                  (0, 300, 0), 2)

# Output images
cv2.imshow("image", image)
cv2.waitKey(0)

cv2.destroyAllWindows()
