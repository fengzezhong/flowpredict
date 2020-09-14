import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl  # 显示中文
from sklearn.model_selection import train_test_split  # 这里是引用了交叉验证
from sklearn.linear_model import LinearRegression  # 线性回归
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt

file = '/Users/fengdong/Downloads/data-master/Analysis/1到11月数据测试.xlsx'

pd_data = pd.read_excel(file)
print(pd_data)
# print('pd_data.head(6)=\n{}'.format(pd_data.head(6)))
#
# print(pd_data.DataFrame)
mpl.rcParams['font.sans-serif'] = ['yahei']  # 配置显示中文，否则乱码
mpl.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号，如果是plt画图，则将mlp换成plt
sns.pairplot(pd_data, x_vars=['月份'], y_vars='LTE总流量(GB)', kind="reg", size=10, aspect=0.7)
#
plt.show()  # 注意必须加上这一句，否则无法显示。
#
# # 剔除日期数据，一般没有这列可不执行，选取以下数据http://blog.csdn.net/chixujohnny/article/details/51095817
# X = pd_data.loc[:, '日期', '月份', '星期', '节假日']
# y = pd_data.loc[:, 'LTE总流量(GB)']
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=334)
# print('X_train.shape={}\n y_train.shape ={}\n X_test.shape={}\n,  y_test.shape={}'.format(X_train.shape,
#                                                                                           y_train.shape,
#                                                                                           X_test.shape,
#                                                                                           y_test.shape))
# linreg = LinearRegression()
# model = linreg.fit(X_train, y_train)
# print(model)
# # 训练后模型截距
# print(linreg.intercept_)
# # 训练后模型权重（特征个数无变化）
# print(linreg.coef_)
#
# feature_cols = ['LTE总流量(GB)']
# B = list(zip(feature_cols, linreg.coef_))
# print(B)
#
# # 预测
# y_pred = linreg.predict(X_test)
# print(y_pred)  # 10个变量的预测结果
#
# sum_mean = 0
# for i in range(len(y_pred)):
#     sum_mean += (y_pred[i] - y_test.values[i]) ** 2
# sum_erro = np.sqrt(sum_mean / 10)  # 这个10是你测试级的数量
# # calculate RMSE by hand
# print("RMSE by hand:", sum_erro)
# # 做ROC曲线
# plt.figure()
# plt.plot(range(len(y_pred)), y_pred, 'b', label="predict")
# plt.plot(range(len(y_pred)), y_test, 'r', label="test")
# plt.legend(loc="upper right")  # 显示图中的标签
# plt.xlabel("the number of sales")
# plt.ylabel('value of sales')
# plt.show()
