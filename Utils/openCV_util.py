import math
import tesserocr
from PIL import Image
# OCR 当前版本未对图像进行处理，接下来学习cv2对图像进行处理防止背景对识图的干扰
import cv2
# img = cv2.imread('../image.png')
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# blurred = cv2.GaussianBlur(img_gray, (5,5), 0)
# binary_img = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
# cv2.imshow("binary",binary_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# edges = cv2.Canny(img, 40, 150)
# edges = Image.fromarray(cv2.cvtColor(edges, cv2.COLOR_BGR2RGB))
# cv2.imshow('Edges', edges)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# edges = Image.open('../image.png')
# result = tesserocr.image_to_text(edges, lang='chi_sim+eng+jpn')
# print(result)
def get_line():
    edges = Image.open('image.png')
    result = tesserocr.image_to_text(edges, lang='chi_sim+eng+jpn')
    return result