import sys
from pytesseract import image_to_string
import requests
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
import numpy as np

# %matplotlib inline

# Just a random picture from search
img = 'https://ohscurrent.org/wp-content/uploads/2015/09/domus-01-google.jpg'
img = requests.get(img)

img = Image.open(BytesIO(img.content))
# show image
img_arr = np.array(img)
plt.imshow(img_arr)

img = Image.open(BytesIO(img.content))
text = image_to_string(img)
print(text)