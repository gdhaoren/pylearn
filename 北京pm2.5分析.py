import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#1. 添加一列diff用于比较中国环保部和美国使馆检测的PM2.5值的差异（两列数据的绝对值差） 
#2. 找出差别最大的10天的记录 
#3. 使用分组柱状图比较中国环保部和美国使馆检测的每年平均PM2.5的值 

path=r'C:\Users\gdhao\Desktop\Beijing_PM.csv '



def collect_data() :
    data_df=pd.read_csv(path)   #数据类型是dataframe
    return data_df

    

    #取出某一列进行 去重 看有哪些分类
    #data_year=data_df['year']   #数据类型是series
    #print(data_year.unique())




def inspect_data(data_df) :
    #显示数据信息
    #print(data_df.info())
    #print(data_df.head())
    #print(data_df.describe())
    pass



def process_data(data_df) :

    #处理缺失值
    #fil_Na_processed_data=data_df.fillna(value=0)
    data_df.dropna(inplace=True)  #inplace=True表示在原始数据上进行操作.如果要将结果赋值给一个新的变量则使用inplace=False, 默认是false

    ##添加diff列
    #fil_Na_processed_data['diff']=fil_Na_processed_data['PM_China']-fil_Na_processed_data['PM_US']

  


    #按年份分组 求取平均值
    year_group_data=data_df.groupby('year')[['PM_China','PM_US']].mean()
    

    #画图
    year_group_data.plot(kind='bar')
    plt.tight_layout()
    plt.show()






    
    

    pass



def analysis_data() :
    pass


def save_show_results () :
    pass



def main() :

    data=collect_data()
    process_data(data)
    pass


if  __name__ == '__main__' :
    main()