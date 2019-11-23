import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('test.jpg')
plt.imshow(img)
plt.show()