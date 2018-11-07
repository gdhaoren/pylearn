import os
import numpy as np
from tkinter import *
from tkinter.filedialog import *

file_list={ 'path' : [] }

# 制作文件选择界面
def ui_read_path() :
    app=Tk()
    Label(app,text='选择文件:').grid(row=0)
    Listbox(app,name='lbox').grid(row=1)
    Button(app,text='...',command=gt_path).grid(row=2)
    Button(app,text='确定',command=collect_data_cTof_save).grid(row=2,column=1)
    return app

#获取文件地址
def gt_path() :
    paths=askopenfilenames()
    file_list['path']=paths
    lbox=app.children['lbox']
    for path in paths :
        lbox.insert(END,path.split('/')[-1]) 


#读取文件,获取数据并批量转换数据
def collect_data_cTof_save() :
    #获取数据
    data_arr_list=[]
    for path in file_list['path'] :
        data_arr=np.loadtxt(path,delimiter=',',dtype='str',skiprows=1)
        data_arr_list.append(data_arr)
    #处理输出文件目录
    for path in file_list['path'] :
        fname=path.split('/')[-1]
        o_path=path.replace(fname,'')
        out_path='%schanged_%s'%(o_path,fname)
    #处理文件
    for data_arr in data_arr_list :
        c_str_col=data_arr[:,1]
        c_str_col=np.core.defchararray.replace(c_str_col,' C','')
        f=c_str_col.astype('float')*1.8+32
        g=data_arr[:,0].astype('float')
        nf=np.array([g,f]).transpose()
        np.savetxt(out_path,nf,delimiter=',',header='Month,Temperature',fmt='%.2f',comments='')  # 默认表头是注释的 因此会自动加一个#，可以把他取消掉



app=ui_read_path()
app.mainloop()





