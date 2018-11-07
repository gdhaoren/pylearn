
import os
import numpy as np
import matplotlib.pyplot as plt

path='C:/Users/Jelly/Desktop/temp2.csv'

def collect_process_analysis_data () :
    data_arr=np.loadtxt(path,skiprows=1,delimiter=',')
    his_data,edages=np.histogram(data_arr[:,1],range=(-10,10),bins=10)# 这里得到的桶边界 可以返回成为绘图参数的桶边界设置
    print('1-3月份的温度直方图数据为{}，统计的温度边界为{}'.format(his_data,edages))
    return data_arr[:,1],edages

def draw_picture(data_arr,n_bins) :
    # python画图有一个当前激活图形，使用一次plt.flgure()就是这个当前激活图像，然后对其属性进行设置
    #当再使用plt.sbuplot时候也是激活这个subplot对象 对它进行设计，不影响其他绘图区
    #使用plt.subplot 和  a=plt.add_suplot 是两种思路，第一种是面向过程式的一步一步设置属性绘图，第二种则是通过对象的方式来绘图，调用对象方法设置属性
    #但是这两种方法 都是要使用 plt.show()来显示最终的图像，用plt.tight_layout()来进行最终布局紧凑
    plt.figure()
    plt.hist(data_arr,range=(-10,10),bins=10)
    plt.xticks(n_bins) #就是传入一个数列 range(-10,11,2),注意这里是11，不是10 因为索引不到最后一个数据，而是他前一个
    plt.title('Tem')
    plt.ylabel('tem C')
 #使用汉语的话要额外设置，因为matplotlib中默认是没有中文字体的

    plt.tight_layout()
    plt.show()

def main() :
    data,bin_edage=collect_process_analysis_data()
    draw_picture(data,bin_edage)

if __name__ == '__main__' :
    main()