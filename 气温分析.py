import numpy as np

def collect_process_data() :
    # data_arr=np.loadtxt(path,delimiter=',',dtype='str',skiprows=1)
    # clean_data_arr=data_arr.astype('float')  #向量化编程 不要使用for遍历每一个元素然后处理每一个值
    #由于原始数据没有 int/float和str混在一起的数据存在，因此读入的时候不用全部按照str读入可以直接按默认的数值类型读入
    data_arr=np.loadtxt(path,delimiter=',',skiprows=1)
    processed_data = []
    for i in range(3) :
        month_bool_arr=clean_data_arr[:,0]==i+1
        data=clean_data_arr[month_bool_arr][:,1]   #使用布尔数组抽取过的数据可以直接提取它的第二列数据[]就是对列表的切片
        processed_data.append(data)
    return processed_data

# 对于这个程序，这两个函数完全可以放在一起收集 处理 分析数据一个循环完成 不用写这么多函数和循环
def analysis_data(processed_data) :
    analysised_data=[]
    for i,data in enumerate(processed_data) :  #使用enumerate()来记录是第几个月的数据
        data_mean=np.mean(data)
        data_max=np.max(data)
        data_min=np.min(data)
        print('第{}个月的平均气温为{:.2f}，最高气温为{}，最低气温为{}'.format(i+1,data_mean,data_max,data_min))
        analysised_data.append([data_mean,data_max,data_min])
    return analysised_data

def main() :
    p_data=collect_process_data()
    a_data=analysis_data(p_data)


if __name__ == '__main__' :
    path = 'C:/Users/Jelly/Desktop/temp2.csv'
    main()