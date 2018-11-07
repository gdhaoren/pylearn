import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

path='C:\\Users\\gdhao\\Desktop/temp2.csv'

plt.rcParams['font.sans-serif']=['SimHei']  #仅适用于windows 且由于改变了默认字体集 会污染整个图像所有的字体

def collect_processed_analysis_data() :
    data_arr=np.loadtxt(path,skiprows=1,delimiter=',')
    ls_list=[]
    lx_list=[]
    for i in range(3) :
        data=data_arr[data_arr[:,0]==(i+1)][:,1]
        ls_qw=data[data>=0].shape[0]
        lx_qw=data[data<0].shape[0]
        ls_list.append(ls_qw)
        lx_list.append(lx_qw)
    return ls_list,lx_list

def plot_data(ls,lx) :
    bar_loc=np.arange(3)  # 这里返回的是一个向量 不仅仅是一个数列 他可以进行向量运算
    bar_width=0.35
    xticks_label=['第{}个月'.format(i+1) for i in range(3)]
    plt.figure()
    plt.bar(bar_loc,ls,width=bar_width,color='g',alpha=0.6,label='零上气温')
    plt.bar(bar_loc+bar_width,lx,width=bar_width,color='r',alpha=0.6,label='零下气温')
    plt.xticks(bar_loc+bar_width/2,xticks_label,rotation=45)
    plt.ylabel('气温 (C)')
    plt.title('近三个月气温统计')
    plt.legend(loc='best')   #设置图例 他会把label变成图例名
    plt.tight_layout()
    plt.show()


def main() :
    ls,lx=collect_processed_analysis_data()
    plot_data(ls,lx)

if __name__ == '__main__' :
    main()
