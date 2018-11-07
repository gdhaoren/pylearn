import os
import shutil
import time

def monitor_files(path) :
    files=os.listdir(path)
    return len(files)

def zip_delete(path,output_path,i=1) :
    zip_name='archive%d.zip'%(i)
    zip_file_out=os.path.join(output_path,zip_name)
    zip_file=os.path.join(path,zip_name)
    os.makedirs(zip_file)
    zfiles=os.listdir(path)
    for file in zfiles :
        curt_path=os.path.join(path,file)
        shutil.move(curt_path,zip_file)
    shutil.make_archive(zip_file_out,'zip',zip_file)
    shutil.rmtree(zip_file)  #  os.removdirs()不能用于删除非空文件夹

i=1
path='./image'
output='./output'
while True :
    if monitor_files(path) and monitor_files(path) >= 5 :
        zip_delete(path,output,i)
        i=i+1
    # 每隔1秒钟 检测一次
    time.sleep(1)
