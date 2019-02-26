from PIL import Image
import os

image1=Image.open('ven.png')
image1.rotate(180).save('ven_mod.png')

image1=Image.open('ven_mod.png')
image1.convert(mode='L').save('ven_mod.png')

