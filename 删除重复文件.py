#  比较文件 删除文件

import os
import filecmp

path='./problem3_files'
all_path=[]
dictories=os.listdir(path)
for d in dictories :
    dic_path=os.path.join(path,d)
    files=os.listdir(dic_path)
    for file_name in files :
        all_path.append(os.path.join(dic_path,file_name))
    for i in all_path :
        for j in all_path :
            if i!=j and os.path.exists(i) and os.path.exists(j) :
                if filecmp.cmp(i,j) :
                    os.remove(j)
    else :
        all_path=[] #处理完一个文件夹后要清空 all_path
