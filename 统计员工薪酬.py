#统计不同专业背景的员工的平均薪资，并用柱状图显示结果 
import os
import pandas as pd
import matplotlib.pyplot as plt
#from matplotlib.font_manager import FontProperties


#文件位置
path=r'C:\Users\gdhao\Desktop\data_employee'
fname=['employee_edu.csv','employee_info.csv']

# 读取数据并存入,但是并没有显式表明变量中存入的信息
#data_df=[]
#for name in fname :
#    data_df.append(pd.read_csv(os.join.path(path,name)))

employee_edu=pd.read_csv(os.path.join(path,fname[0]))
employee_info=pd.read_csv(os.path.join(path,fname[1]))

# 数据处理
# 表连接(合并)
merged_df=pd.merge(employee_edu,employee_info,how='inner',on='EmployeeNumber')

# 数据分析
edu_mean=merged_df.groupby('EducationField')['MonthlyIncome'].mean()
edu_mean.sort_values(ascending=False,inplace=True)  # inplace 激活表示不用新变量来储存操作后的数据而是直接存入原始数据中去,ascending默认是True升序 改成False表示降序

# 显示数据
edu_mean.plot(kind='bar')
#使用fontproperties参数来设置字体灵活且不污染全局字体 从而不用对负号再单独处理
plt.title('不同职业背景的收入情况',fontproperties='SimHei')
plt.ylabel('收入',fontproperties='SimHei')
plt.xlabel('专业背景',fontproperties='SimHei')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()