import os, sys, cv2

src =cv2.imread('./image/airplane.bmp', cv2.IMREAD_COLOR)
mask =cv2.imread('./image/mask_plane.bmp', cv2.IMREAD_GRAYSCALE)
dst =cv2.imread('./image/field.bmp', cv2.IMREAD_COLOR)
mas = [src,mask,dst]

if src is None or mask is None or dst is None:
    print('fail')
    sys.exit()

cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.imshow('mask',mask)
cv2.waitKey()
cv2.destroyAllWindows()
