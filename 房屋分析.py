#1. 可视化不同卧室个数对应的房屋价格的分布  (一个离散变量在另一个离散变量上的分布,可以用者盒形图来分析,这是一个双变量的分布)   柱状图是一个单变量分析.它描述了单一离散变量的分布
#2. 分析卫生间个数与房屋价格的关系  (分析两个离散变量之间的关系.可以使用双变量图)
#3. 可视化变量间的关系 (可视化全变量的相关关系.使用热图)


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

path=r'C:\Users\gdhao\Desktop\house_data.csv '

col=['price','bedrooms','bathrooms']
data_arr=pd.read_csv(path,usecols=col)

i=data_arr.shape[0]
cl_data=data_arr.dropna()
j=cl_data.shape[0]

if i==j :
    print('没有空值数据')
else :
    print('存在空值,已丢弃')

#盒形图分析
sns.boxplot(x=col[1],y=col[0],data=cl_data)
plt.show()

#双变量图分析
sns.jointplot(x=col[2],y=col[0],data=cl_data)
plt.show()

#全变量相关关系热图显示
corr_arr=cl_data.corr()
sns.heatmap(corr_arr,annot=True)
plt.show()



