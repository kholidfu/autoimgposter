from PIL import Image # pip install pillow
import os
from datetime import datetime
import shutil
import pymongo

"""
1. semua image yg belum dimasukkan ke database ditaruh ke dalam folder "temp"
2. masing-masing image kemudian di-extract info nya sebagai input untuk dbase
3. deteksi resolusi image resize menjadi lebih kecil, misal
resolusi asli:
1920 x 1200, maka resize:
800x600
1024x768
1152x864
1280x960
1400x1050
1600x1200
1360x768
1366x768
1600x900
1920x1080
1280x800
1440x900
1680x1050
4. setiap image yang selesai di-extract & resize dimasukkan ke dalam folder img
5. done!

info yang paling penting untuk di-extract adalah unique id, biar tidak ada
yang duplikat, caranya menggunakan exiftool?

data

{
'filename': 'thefilename',
'title': 'thetitle',
'size': 'imgsize',
'dim': 'img_dimension', # tuple
'format': 'img_type', # jpeg, png
'added': datetime.now(),
'hits': 0,
}

shutil.move(src, dest)
"""

c = pymongo.Connection()
c.drop_database('autoimg')
db = c['autoimg']

for fn in os.listdir('img'):
    filename, filext = os.path.splitext(fn)
    im = Image.open('img/' + fn)
    if db.image.find_one({'title': filename.replace('_', ' ')}) is None:
        db.image.insert({
            'filename': filename+filext,
            'title': filename.replace('_', ' '),
            'size': os.stat('img/' + fn).st_size,
            'format': im.format,
            'dim': im.size,
            'added': datetime.now(),
            'hits': 0,
            })
    # move the image into img folder
    # shutil.move('temp/filename', 'img/filename')

from pprint import pprint
pprint(db.image.find_one())
