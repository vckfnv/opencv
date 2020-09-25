#영상  생성
import numpy as np
import cv2

img1 = np.empty((240,320), dtype=np.uint8)
img2 = np.zeros((240,320,3), dtype=np.uint8)
img3 = np.ones((240,320), dtype=np.uint8)
img4 = np.ones((240,320), dtype=np.uint8) * 255
img5 = np.full((240,320,3), 128, dtype=np.uint8)
img6 = np.full((240,320,3),(0,255,255), dtype=np.uint8)

images = [img1,img2,img3,img4,img5,img6]
for i,x in enumerate(images):
    cv2.imshow(str(i),x)
cv2.waitKey()
cv2.destroyAllWindows()