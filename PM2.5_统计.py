#滚动统计PM2.5指标的3日均值、5日均值、7日均值，并对结果进行可视化 

import pandas as pd
import matplotlib.pyplot as plt

path = r'C:\Users\gdhao\Desktop\pm1.csv'
output= r'C:\Users\gdhao\Desktop\output.csv'

#数据获取和处理
pm_data=pd.read_csv(path)
cln_pm_data=pm_data.dropna()
cln_pm_data['Timestamp']=pd.to_datetime(cln_pm_data['Timestamp'])
cln_pm_data.set_index('Timestamp',inplace=True)

#数据分析
#重采样并计算每日均值
day_mean_pm_data=cln_pm_data.resample('D').mean()
#重采样有可能会产生NA所以要进行一步去空值
day_mean_pm_data.dropna(inplace=True)

#滚动操作计算ma3 ma5 ma7 注意为了画图方便 要新增列并将他们存在原来的dataframe中
#方案一 手写
#使用rolling方法产生的是一个 series 类型的数据
#day_mean_pm_data['Ma 3']=day_mean_pm_data['PM'].rolling(3).mean()
#day_mean_pm_data['Ma 5']=day_mean_pm_data['PM'].rolling(5).mean()
#day_mean_pm_data['Ma 7']=day_mean_pm_data['PM'].rolling(7).mean()

#方案二 使用exec函数 配合 f-string 对{}内的表达式在当前作用域内求值
for i in range(3,9,2) :
    exec(f"day_mean_pm_data['Ma {i}']=day_mean_pm_data['PM'].rolling({i}).mean()")

# 画图
#保存的时候直接对需要保存的 dataframe变量 应用to_csv()方法就行了
day_mean_pm_data.to_csv(output)
day_mean_pm_data[['PM','Ma 3','Ma 5','Ma 7']].plot()
plt.tight_layout()
plt.show()

