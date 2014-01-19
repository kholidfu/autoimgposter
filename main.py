from PIL import Image # pip install pillow
import os
from datetime import datetime
import shutil
import pymongo

"""
1. semua image yg belum dimasukkan ke database ditaruh ke dalam folder "temp"
2. masing-masing image kemudian di-extract info nya sebagai input untuk dbase
3. setiap image yang selesai di-extract dimasukkan ke dalam folder img
4. done!

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
