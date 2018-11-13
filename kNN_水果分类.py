#* 题目描述：使用k近邻距离算法创建一个水果识别器，根据水果的属性，判断该水果的种类。 

#* 题目要求: 
#* 使用scikit-learn的kNN算法进行识别 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

DATA_FILE = r"C:\Users\gdhao\Desktop\fruit_data.csv"

#读入数据
fruit_data=pd.read_csv(DATA_FILE)

# 将水果名这个字符串标签 替换为数值标签  
# 也可以不用替换,对于kNN方法的标签使用字符串也是可以的
# 生成数值标签列
fruits=fruit_data['fruit_name'].unique().tolist()
fruits_dict=dict(zip(fruits,range(len(fruits))))
fruit_data['Label']=fruit_data['fruit_name'].map(fruits_dict) # 对向量的每一个元素应用map的映射关系

#选择需要的属性作为特征属性
feat_cols=fruit_data.columns.values[1:-2].tolist()

# 对水果颜色这个连续变量进行颜色分桶        访问某个具体元素时是 dataframe[column][row],列索引在前,行索引在后不然会报错
fruit_data['colour']=pd.cut(fruit_data['color_score'],bins=[0.45,0.65,0.75,0.85,1],labels=[1,2,3,4])

#将数据分解为 特征矩阵 和 标签向量
#特征矩阵 X已经不是dataframe类型 而是np.ndarry
X=fruit_data[feat_cols].values
#标签向量 y已经不是dataframe类型 而是np.ndarry
y=fruit_data['fruit_name'].values

#划分数据集
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=1/5,random_state=10)

#开始进行kNN分类 默认是k=5 找到最近的5个点进行投票票数多的定为预测值的标签
#声明使用的模型
knn_model=KNeighborsClassifier()
#训练模型:指定训练样本集合   X_train(训练集的特征矩阵)和y_train(训练集的标签) 放在一起才是一个有监督的完整的训练数据集
knn_model.fit(X_train,y_train)
#评价/测试模型:计算测试集的预测成功率    X_test(测试集的特征矩阵)和y_test(测试集的标签) 放在一起才是一个有监督的完整的训练数据集
accuracy=knn_model.score(X_test,y_test)

print(f'预测准确率:{accuracy:.2%}')


#取单个测试样本
#样本横坐标
idx=9
#通过横坐标取到测试样本的 特征值集合
test_sample_feat=[X_test[idx,:]]
#获取测试样本的真实标签
y_true=y_test[idx]
#使用模型通过对特征值集合分析预测样本的标签,它返回的是一个np.ndarry
y_pred=knn_model.predict(test_sample_feat)
print(f'真实标签是{y_true},预测标签是{y_pred[0]}')



