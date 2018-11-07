#根据PM2.5值添加对应的等级，统计每年各等级的占比天数,并使用堆叠柱状图进行可视化。等级规则如下： 
#* 0-50: excellent（优） 
#* 50-100: good（良） 
#* 100-500: bad（污染） 


import pandas as pd
import matplotlib.pyplot as plt

path = r'C:\Users\gdhao\Desktop\pm2.csv'

pm_data=pd.read_csv(path)

#去除空值
pm_data.dropna(inplace=True)

#方案一 使用apply函数进行等级添加
#def level (data) :
#    if data<=50 and data>0 :
#        l='优'
#    elif data<=100 :
#        l='良'
#    elif data<=500 :
#        l='污染'
#    return l

#pm_data['Level']=pm_data['PM'].apply(level)

#方案二 使用cut函数实现
#cut方法只能通过pd调用
pm_data['Level']=pd.cut(pm_data['PM'],bins=[0,50,100,500],labels=['优','良','污染'])

#使用数据透视表来实现目的
#每年(index)各等级(columns)的天(values)数(count)
pivot_table_pm_data=pm_data.pivot_table(index='Year',columns='Level',values='Day',aggfunc='count')

#可视化
#设置legend字体
font = {'family' : 'SimSun'
#'weight' : 'normal', #设置字体粗细 类似于bold 一类的参数
#'size'   : 10,
}
pivot_table_pm_data.plot(kind='bar',stacked=True)
plt.legend(prop=font)
plt.tight_layout()
plt.show()



