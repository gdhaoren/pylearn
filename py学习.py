#将文件从其他文件夹 移动到另一个文件夹

import os 
import shutil

path =  './problem2_files'

image_suffix=['jpg','png','gif']
path_image = os.path.join(path,'image')

for i in image_suffix :
    fpath= os.path.join(path,i)
    files = os.listdir(fpath)
    for f in files :
        if os.path.exists(path_image) :
           shutil.move(os.path.join(fpath,f),path_image)  # shutil.move函数的两个变量都要是路径
        else :
            os.makedirs(path_image)
            shutil.move(os.path.join(fpath,f),path_image)
        
else :
    print("成功移动")
    for i in image_suffix :
        os.removedirs(os.path.join(path,i))



