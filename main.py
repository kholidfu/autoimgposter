from PIL import Image
import os

for fn in os.listdir('img'):
    filename, filext = os.path.splitext(fn)
    print filename
