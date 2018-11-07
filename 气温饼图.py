import os
import numpy as np
import matplotlib.pyplot as plt



path='C:/Users/gdhao/Desktop/data_temp'
file_name=['201801_temp.csv','201802_temp.csv','201803_temp.csv']

def data_collect_process_analysis_plot() :
    data_arr=[]
    for i in range(3) :
        data=np.loadtxt(os.path.join(path,file_name[i]),skiprows=1)
#        data=data.reshape(-1,1)  # 将已知需要转换的行/列填入,在对应的列/行出填入-1
        data_arr.append(data)
    processed_data=np.concatenate(data_arr)
    #分析数据
    ls_qw=processed_data[processed_data>=0].shape[0]
    lx_qw=processed_data[processed_data<0].shape[0]
    #画图
    plt.figure()
    plt.pie([ls_qw,lx_qw],labels=['>=0','<0'], autopct='%.2f%%')
    plt.axis('equal')  #绘制的饼图为正圆形而不是椭圆 
    plt.tight_layout()  #防止元素超出画布
    plt.show()


if __name__ == '__main__' :
    data_collect_process_analysis_plot()


