import PIL
from PIL import Image
import os

def getfiles(loc):
    """ Get only image files """
    all_files_list = os.listdir(loc)
    accepted_formats_tuple = (bmp, jpg, jpeg)
    final_files_list = []
    for f in all
    

def resize(loc): # loc is folder location
    files = getfiles(loc)
    img = Image.open(loc)
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
    img.save(new_name)
