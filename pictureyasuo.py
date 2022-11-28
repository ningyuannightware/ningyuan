#开发人员：王宁
#开发时间： 2022/10/27 9:37
import cv2


img=cv2.imread(r"E:\666\CA197E629122C5E939B7166B8D2A3235.jpg",1)
cv2.imwrite(r"E:\666\baodaozheng2.jpg",img,[cv2.IMWRITE_JPEG_QUALITY,90])