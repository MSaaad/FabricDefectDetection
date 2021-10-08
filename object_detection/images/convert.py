#convert.py
from PIL import Image     
import os
import sys 

path = sys.argv[1] # Source Folder
if path[-1] != '/':
    path = path +'/' 
for file in os.listdir(path):      
        extension = file.split('.')[-1]
        name = file.split('.')[0] + '.jpg'
        fileLoc = path+file
        img = Image.open(fileLoc)
        new = Image.new("RGB", img.size, (255, 255, 255))
        new.paste(img,None) # save the new image with jpg as extension
        new.save(path+name, 'JPEG', quality=100)
        if(extension != 'jpg'): #remove the old image
            os.remove(path+file)