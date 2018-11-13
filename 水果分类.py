#* 题目描述：创建一个水果识别器，根据水果的属性，判断该水果的种类。 
#* 题目要求: 
#* 模仿课堂的讲解内容，根据“近朱者赤”的原则，手工实现一个简单的分类器 
#* 选取1/5的数据作为测试集 

#kNN算法 k=1

import pandas as pd
from sklearn.model_selection import train_test_split
from scipy.spatial.distance import euclidean
import numpy as np

DATA_FILE=r'C:\Users\gdhao\Desktop\fruit_data.csv'

#预测函数
def get_pred_label(test_sample_feat,train_data) :
    
    #保存计算获得的距离
    dis_list=[]

    for idx,row in train_data.iterrows() :
        #训练样本的特征
        train_sample_feat=row[feat_cols].values

        #计算距离 近朱者赤
        dis=euclidean(test_sample_feat,train_sample_feat)

        #保存距离
        dis_list.append(dis)

    #找到距离最小的那条数据的水果名
    #找到最小值点的位置
    pos=np.argmin(dis_list)
    #iloc 通过行号来索引,loc可以通过标签来索引,调用后获得的是一个series数据类型
    pred_label=train_data.iloc[pos]['fruit_name']

    return pred_label



#读入数据
fruit_data=pd.read_csv(DATA_FILE)

#水果种类获取
fruit_name=fruit_data['fruit_name'].unique().tolist()

#获取特征信息
#.values 得到的是一个数组
feat_cols=fruit_data.columns.values[1:].tolist()

#设置训练集和测试集
#设置训练集和测试集  random_state 相当于随机种子（伪随机） 每次种子相同 随机的结果也相同
train_data,test_data=train_test_split(fruit_data,test_size=1/5,random_state=10)



#对测试集中的数据进行预测
#对于dataframe的行遍历 使用 .iterrows()的迭代器是合适的，dataframe的行操作比起整列的向量操作要慢很多
for idx,row in test_data.iterrows() :
    #在使用.values之前 获得的是一个series类型的数据,使用.values后 变成了一个数组ndarray
    test_sample_feat=row[feat_cols].values

    #预测水果类型
    pred_label=get_pred_label(test_sample_feat,train_data)

    #实际水果类型
    true_label=row['fruit_name']

    print(f'样本{idx}的真实标签是{true_label},样本的预测标签是{pred_label}')

    #计算准确率
    counter=0
    if pred_label == true_label :
        counter+=1

accuracy=counter/test_data.shape[0]
print(f'预测准确率为{accuracy:.2%}')