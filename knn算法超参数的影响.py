# * 题目描述：使用不同的k值，观察对水果识别器的影响。
#
# * 题目要求:
# * 使用scikit-learn的kNN进行识别
# * 使用k=1, 3, 5, 7观察对结果的影响

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

DATA=r"C:\Users\Jelly\Desktop\fruit_data.csv"

#导入数据
fruit_data=pd.read_csv(DATA)

# 获取分析属性
feat_cols=fruit_data.columns.values[1:-1].tolist()

#制作测试函数
def knn_model_test(data,k_value) :
    # 制作分析数组
    X=data[feat_cols].values
    y=data['fruit_name'].values

    #划分训练集和测试集
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=1/5,random_state=10)

    #使用knn算法
    #声明模型
    knn_model=KNeighborsClassifier(n_neighbors=k_value)
    #训练模型
    knn_model.fit(X_train,y_train)
    #验证模型
    accuracy=knn_model.score(X_test,y_test)
    print(f'当k={k_value}时，准确率为{accuracy:.2%}')


def main() :
    k=3
    knn_model_test(fruit_data,k)


if __name__=='main' :
    main()