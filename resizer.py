import PIL
from PIL import Image
import os

default_basewidth = 1024

def get_images_list(dir_loc):
    dict_pics_details = {}
    """ Get only image files """
    all_files_list = os.listdir(dir_loc)
    accepted_formats_tuple = ('bmp', 'jpg', 'jpeg', 'png')
    final_files_list = []
    if all_files_list:
        for f in all_files_list:
            if f.split('.')[-1] in accepted_formats_tuple:
                final_files_list.append(os.path.join(dir_loc, f))
    return final_files_list

def resize_image(f, basewidth=None, suffix='resized', QUALITY=80):  # f is filename with complete path
    import imghdr  # This module can tell us what is the type of image e.g jpeg, bmp etc
    image_type = imghdr.what(f)
    if not basewidth:
        basewidth = default_basewidth

    try:
        img = Image.open(f)
    except IOError:
        return 'Invalid file'

    outfile = f.split('.')[0] + '_%s.%s' % (suffix, image_type)  # We chip the extension and append a suffix
    if basewidth:
        wpercent = (basewidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))

    img_new = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    img_new.save(outfile, image_type.upper(), quality=QUALITY)  # Saving the new image with the name %outfile%
    del image_type
    new_size = size_of_photo_in_kilobytes(outfile)  # Calculating size of new file
    return new_size

def resolution_of_file(file_path):
    """Returns resolution as tuple"""
    img = Image.open(file_path)
    return img.size

def get_photo_extension(file_path):
    """"Returns format of file"""
    img = Image.open(file_path)
    return img.format

def size_of_photo_in_megabytes(full_file_path):
    round(os.stat(full_file_path).st_size, 3)

def size_of_photo_in_kilobytes(full_file_path):
    return os.stat(full_file_path).st_size/1024

def resize_list_of_images(list_image, basewidth=None, percent=None):
    #Note: list_image must be a list of full image paths
    list_converted = []  # Will contain sizes of converted images
    for image in list_image:
        new_size = resize_image(image, basewidth, percent)
        list_converted.append(new_size)
    return list_converted


if __name__ == '__main__':
    #loc = raw_input('Enter location of folder')
    loc = r'D:\inchowar\Desktop\Pics'
    list_images = get_images_list(loc)
    resize_list_of_images(list_images)

