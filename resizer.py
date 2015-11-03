import PIL
from PIL import Image
import os

def get_images_list(dir_loc):
    """ Get only image files """
    all_files_list = os.listdir(dir_loc)
    accepted_formats_tuple = ('bmp', 'jpg', 'jpeg', 'png')
    final_files_list = []
    if all_files_list:
        for f in all_files_list:
            if f.split('.')[-1] in accepted_formats_tuple:
                final_files_list.append(os.path.join(dir_loc,f))
    return final_files_list
    
    

def resize_image(f, basewidth = 1024, suffix='new'):  # f is filename with complete path
    img = Image.open(f)
    print f
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img_new = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
    img_new.save(f, format='BMP')

def resize_list_of_images(list_image):
    for image in list_image:
        resize_image(image)

if __name__ == '__main__':
    #loc = raw_input('Enter location of folder')
    loc = r'C:\Users\Arindam\Desktop\Test_Image'
    list_images = get_images_list(loc)
    resize_list_of_images(list_images)


