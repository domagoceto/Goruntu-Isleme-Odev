import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("C:\Users\bjk_k\Desktop\image\got\1261441.jpg",0)

def histogram_hesapla(image):
    histogram = np.zeros((256,), dtype=int)
    height, width = image.shape

    for i in range(height):
        for j in range(width):
            pixel_value = image[i, j]
            histogram[pixel_value] += 1

    return histogram

histogram = histogram_hesapla(img)

plt.plot(histogram)
plt.title('Gri Resim Histogrami')
plt.xlabel('Piksel Değeri')
plt.ylabel('Piksel Sayisi')
plt.show()


cv2.waitKey()
cv2.destroyAllWindows()
