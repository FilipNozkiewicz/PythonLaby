import PIL as pillow
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image , ImageEnhance
from PIL import Image

import sys


im = Image.open("geralt.png");
rot = im.rotate(90)
w , h = im.size

cr_im = im.crop((0.3 * w , 0.3 * h , 0.7* w , 0.7 * h ))
#cr_im.show()

contrast = ImageEnhance.Contrast(im)

c_c = contrast.enhance(2)


bright = ImageEnhance.Brightness(im)
b_c = bright.enhance(0.65)
#b_c.show()


r , g , b = im.split()

#r.show()
#g.show()
#b.show()

im1 = Image.merge("RGB",(r,g,b))
#im1.show()

im_res = Image.open("geralt.png");
im_res.paste(r);

#im_res.show()

im.thumbnail((400,400) , Image.ANTIALIAS)
rot.thumbnail((400,400) , Image.ANTIALIAS)
cr_im.thumbnail((400,400) , Image.ANTIALIAS)
r.thumbnail((400,400) , Image.ANTIALIAS)
g.thumbnail((400,400) , Image.ANTIALIAS)
b.thumbnail((400,400) , Image.ANTIALIAS)
im1.thumbnail((400,400) , Image.ANTIALIAS)
#b.show()
#g.show()
#rot.show()
list_im = [im , rot , cr_im , r , g , b , im1 , im1 ]
im_finish = Image.new('RGB' , (1800 , 810))
w = 400;
for i in range(0,4):
    im_finish.paste(list_im[i] , (w*i , 0)  )
for i in range(4, 8):
    im_finish.paste(list_im[i], (w * (i-4), 401))
#im_finish.show()
im_finish.save("finish.jpg")

im_f = Image.open("finish.jpg");
im_f.show()



