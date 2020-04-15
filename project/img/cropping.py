import cv2
import numpy as np
import os, sys

length = float(sys.argv[1])
height = float(sys.argv[2])

fname = os.listdir('origin/')
fname = [t for t in fname if t[-1] != 'y' and t[-1] != 'd' and t[-1]!='e']

for f in fname:
    print(f)
    img = cv2.imread('origin/'+f)
    ratio = height / length
    h, s, _ = img.shape
    print(h,s)
    if float(h) / s > ratio:
        #print(ratio, float(h) / s)
        ns = int(h / ratio)
        st = (ns - s) // 2
        #print(st,st+ns,s)
        nimg = cv2.copyMakeBorder(img, 0, 0, st, st, cv2.BORDER_CONSTANT,value=[255,255,255])
        #nimg = img[:,st:st+ns]
    else:
        nh = int(s * ratio)
        st = (nh - h) // 2
        nimg = cv2.copyMakeBorder(img, st, st, 0, 0, cv2.BORDER_CONSTANT,value=[255,255,255])
        #nimg = img[st:st+nh]
    nimg = cv2.resize(nimg,(int(length),int(height)))
    cv2.imwrite('processed/%s'%f,nimg)

