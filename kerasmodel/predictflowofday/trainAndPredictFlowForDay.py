import pandas as pd
import seaborn as sns
import matplotlib as mpl  # 显示中文
from sklearn.model_selection import train_test_split  # 这里是引用了交叉验证
from sklearn.linear_model import LinearRegression  # 线性回归
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.font_manager import FontProperties  # 字体管理器
from sklearn import metrics

file = '/Users/fengdong/Downloads/4G流量预测data-master/AnalysisFlowForDay/18年1到19年1月数据_贵州_训练.xlsx'
pd_data = pd.read_excel(file)

# 配置显示样式
## 设置字符集，防止中文乱码
mpl.rcParams['font.sans-serif'] = [u'simHei']
mpl.rcParams['axes.unicode_minus'] = False
#
# mpl.rcParams['font.sans-serif'] = ['FangSong']  # 配置显示中文，否则乱码
# mpl.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号，如果是plt画图，则将mlp换成plt
sns.pairplot(pd_data, x_vars=['月份'], y_vars='LTE总流量(GB)', kind="reg", size=10, aspect=0.8)

plt.show()  # 注意必须加上这一句，否则无法显示。

# 剔除日期数据，一般没有这列可不执行，选取以下数据
X = pd_data.loc[:,
    ("1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月", "星期1", "星期2", "星期3", "星期4",
     "星期5", "星期6", "星期7", "工作日", "周末", "法定假日")]
y = pd_data.loc[:, 'LTE总流量(GB)']

# 进行数据切割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print('X_train.shape={}\n y_train.shape ={}\n X_test.shape={}\n,  y_test.shape={}'.format(X_train.shape,
                                                                                          y_train.shape,
                                                                                          X_test.shape,
                                                                                          y_test.shape))
print('X_test', X_test, '\n')

# 调用训练模型并训练
linreg = LinearRegression()
model = linreg.fit(X_train, y_train)

print(model)
# 训练后模型截距
print(linreg.intercept_)
# 训练后模型权重（特征个数无变化）
print(linreg.coef_)

feature_cols = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月", "星期1", "星期2", "星期3", "星期4",
                "星期5", "星期6", "星期7", "工作日", "周末", "法定假日", 'LTE总流量(GB)']
B = list(zip(feature_cols, linreg.coef_))
print(B)

# 预测（测试数据分配的预测结果，和实际结果作对比）
y_pred = linreg.predict(X_test)
print(y_pred)  # 10个变量的预测结果

sum_mean = 0
for i in range(len(y_pred)):
    sum_mean += (y_pred[i] - y_test.values[i]) ** 2
sum_erro = np.sqrt(sum_mean / 365)  # 这个10是你测试级的数量
# calculate RMSE by hand 计算截距
print("RMSE by hand:", sum_erro)

# 做ROC曲线
plt.figure()
plt.plot(range(len(y_pred)), y_pred, 'b', label="predict预测")
plt.plot(range(len(y_pred)), y_test, 'r', label="test测试")
plt.legend(loc="upper right")  # 显示图中的标签
plt.xlabel("shijian")
plt.ylabel('liuliang(GB)')
plt.show()

# 预测未知的数据读取
file = '/Users/fengdong/Downloads/4G流量预测data-master/AnalysisFlowForDay/2019年2月数据集_预测_贵州.xlsx'
pd_data = pd.read_excel(file)
print(pd_data)

# 剔除日期数据，一般没有这列可不执行，选取以下数据
X = pd_data.loc[:,
    ("1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月", "星期1", "星期2", "星期3", "星期4",
     "星期5", "星期6", "星期7", "工作日", "周末", "法定假日")]
y = pd_data.loc[:, 'LTE总流量(GB)']
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1, random_state=25)
# print(X_test)


# 预测
y_pred = linreg.predict(X)
print(y_pred)  # 10个变量的预测结果

for i in y_pred:
    print(i)

for i in range(len(y_pred)):
    sum_mean += (y_pred[i] - y_test.values[i]) ** 2
    sum_erro = np.sqrt(sum_mean / len(y_pred))  # 这个10是你测试级的数量
    # calculate RMSE by hand
    print("RMSE by hand:", sum_erro)
    # 做ROC曲线
# sns.pairplot(pd_data, x_vars=['月份'], y_vars='LTE总流量(GB)', kind="reg", size=1, aspect=0.7)

plt.figure()
plt.plot(range(len(y_pred)), y_pred, 'b', label="predict预测")
plt.plot(range(len(y_pred)), y, 'r', label="test真实值")
plt.legend(loc="upper right")  # 显示图中的标签

plt.xlabel("Days")
plt.ylabel('Flow(GB)')
plt.show()
