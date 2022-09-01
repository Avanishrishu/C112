from distutils import extension
import os
import shutil
from_dir = "C:/Users/Rajnish prabhakar/Downloads"
to_dir = "C:/User/Rajnish prabhakar/Desktop/Downloaded_Images"
list_of_files = os.listdir(from_dir)
for fileName in list_of_files:
    name,extension = os.path.splitext(fileName)
    # print(name)
    # print(extension)
    if extension == "":
        continue
    if extension in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        path1 = from_dir + '/' + fileName
        path2 = to_dir + '/' + "Image_Files"
        path3 = to_dir + '/' + "Image_Files" + '/' + fileName
        if os.path.exists(path2):
            print("moving" +fileName +"...")
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("moving" +fileName +"...")
            shutil.move(path1, path3)