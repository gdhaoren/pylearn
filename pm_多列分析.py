#对PM2.5值按年月两列进行统计分析,并使用分组柱状图可视化分析结果 

import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
path = r'C:\Users\gdhao\Desktop\pm2.csv'

data=pd.read_csv(path)
#先处理空值,防止后面的计算由于空值存在出错
data.dropna(inplace=True)

#再对数据进行排序 我希望年从小到大 pm值从大到小
data.sort_values(['Year','PM'],ascending=[True,False],inplace=True)

#按照年月对数据进行分组,并计算均值,不是很适合用于直接显示图形,没有列索引
#以下两种写法是求得的结果是一模一样的 由此可以看出 groupby是一个简化版的pivot_table
grouped_mean_data=data.groupby(by=['Year','Month'])['PM'].mean()
grouped_pivot_mean_data=data.pivot_table(index=['Year','Month'],values='PM',aggfunc='mean')

# #使用年月分组统计数据并不能自动绘制分组柱状图,因为月是层级索引中的一个,不是列名
#grouped_mean_data.plot(kind='bar')
#plt.tight_layout()
#plt.show()


#制作透视表,以年为行索引,月为列索引,填充平均值,适合于直接显示图形,有行列索引
pivot_mean_data=data.pivot_table(index='Year',columns='Month',values='PM',aggfunc='mean')  #默认聚合函数就是平均值计算

#还可以使用pd来调用透视表函数,但是要指定使用的数据集,等价于下面这句话
#pivot_mean_data=pd.pivot_table(data,index='Year',columns='Month',values='PM',aggfunc='mean')

#可以自动绘制分组柱状图
pivot_mean_data.plot(kind='bar')
plt.tight_layout()
plt.show()

