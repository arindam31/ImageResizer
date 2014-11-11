import PIL
from PIL import Image
import os

def get_images_list(loc):
    """ Get only image files """
    all_files_list = os.listdir(loc)
    accepted_formats_tuple = ('bmp', 'jpg', 'jpeg', 'png')
    final_files_list = []
    if all_files_list:
        for f in all_files_list:
            if f.split('.')[-1] in accepted_formats_tuple:
                final_files_list.append(f)
    return final_files_list
    
    

def resize_image(f, basewidth):  # f is filename with complete path
    img = Image.open(f)
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
    img.save(img)
