from PIL import Image
import os

for fn in os.listdir('img'):
    filename, filext = os.path.splitext(fn)
    print filename

from PIL import Image

for fn in os.listdir('img'):
    im = Image.open('img/' + fn)
    print im.format, im.size, im.mode # format, dimension, mode
    print os.stat('img/' + fn).st_size # filesize
