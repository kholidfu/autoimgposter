from PIL import Image # pip install pillow
import os
from datetime import datetime
import shutil

"""
1. semua image yg belum dimasukkan ke database ditaruh ke dalam folder "temp"
2. masing-masing image kemudian di-extract info nya sebagai input untuk dbase
3. setiap image yang selesai di-extract dimasukkan ke dalam folder img
4. done!

data

{
'title': 'thetitle',
'size': 'imgsize',
'dim': 'img_dimension', # tuple
'format': 'img_type', # jpeg, png
'added': datetime.now(),
'hits': 0,
}

shutil.move(src, dest)
"""

for fn in os.listdir('img'):
    filename, filext = os.path.splitext(fn)
    print filename

from PIL import Image

for fn in os.listdir('img'):
    im = Image.open('img/' + fn)
    print im.format, im.size, im.mode # format, dimension, mode
    print os.stat('img/' + fn).st_size # filesize


# TODO: inserting into mongodb
# cek dulu apakah filename sudah ada, jika sudah lewat, jika belum masukkan
