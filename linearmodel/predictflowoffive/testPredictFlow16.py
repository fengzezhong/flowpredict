import pandas as pd
import seaborn as sns
import matplotlib as mpl  # 显示中文
from sklearn.model_selection import train_test_split  # 这里是引用了交叉验证
from sklearn.linear_model import LinearRegression  # 线性回归
import numpy as np
import matplotlib.pyplot as plt
import sys
import os

from matplotlib.font_manager import FontProperties  # 字体管理器
from sklearn import metrics

# # 加入预测地市
# if (len(sys.argv) > 1):
#     citydata = sys.argv[1]
# else:
#     citydata = 'guizhou'

root = ''
root = '/Users/fengdong/Downloads/lte_flow01/flowPredictCity'

# 最后生成的数据
# file_out = root + '/flowPredict/lte_flow/trainDataForFiveMin_end/linedata_train_five_' + citydata + '16.csv'

trainworkpath = root + '/flowPredict/lte_flow/dataforCityFive/citytraindata/'
preparedatapath = root + '/flowPredict/lte_flow/dataforCityFive/citypreparedata/'
predictdatapath = root + '/flowPredict/lte_flow/dataforCityFive/predictFlow_city/'
if not os.path.exists(predictdatapath):
    os.mkdir(predictdatapath)
if not os.path.exists(predictdatapath):
    os.mkdir(preparedatapath)

citys = os.listdir(trainworkpath)

for x in citys:
    business = os.listdir(trainworkpath + x)
    if not os.path.exists(predictdatapath + x):
        os.mkdir(predictdatapath + x)
    for y in business:

        # 导入最后训练数据
        pd_data = pd.read_csv(trainworkpath + x + '/' + y)

        # print(pd_data['天'])
        # column_headers = list(pd_data.columns.values)
        # print(column_headers)
        pd_data['流量'] = pd_data['流量'] / 1024
        print(pd_data.head(5))

        #
        # 配置显示样式
        ## 设置字符集，防止中文乱码
        mpl.rcParams['font.sans-serif'] = [u'simHei']
        mpl.rcParams['axes.unicode_minus'] = False
        #
        # mpl.rcParams['font.sans-serif'] = ['FangSong']  # 配置显示中文，否则乱码
        # mpl.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号，如果是plt画图，则将mlp换成plt
        sns.pairplot(pd_data, x_vars=['天'], y_vars='流量', kind="reg", size=10, aspect=0.8)

        plt.show()  # 注意必须加上这一句，否则无法显示。

        # 剔除日期数据，一般没有这列可不执行，选取以下数据
        XX = pd_data.loc[:, ("日期", "月份", "天", "小时")]
        YY = pd_data.loc[:, '流量']

        # 进行数据切割
        X_train, X_test, y_train, y_test = train_test_split(XX, YY, test_size=0.2)
        print('X_train.shape={}\n y_train.shape ={}\n X_test.shape={}\n,  y_test.shape={}'.format(X_train.shape,
                                                                                                  y_train.shape,
                                                                                                  X_test.shape,
                                                                                                  y_test.shape))
        # print('X_test', X_test, '\n')

        # 调用训练模型并训练
        linreg = LinearRegression()
        model = linreg.fit(X_train, y_train)

        print(model)
        # 训练后模型截距
        print(linreg.intercept_)
        # 训练后模型权重（特征个数无变化）
        print(linreg.coef_)
        #
        feature_cols = ["月份", "天", "小时", '流量']
        B = list(zip(feature_cols, linreg.coef_))
        print(B)
        #
        # 预测（测试数据分配的预测结果，和实际结果作对比）
        y_pred = linreg.predict(X_test)
        # print(y_pred)  # 10个变量的预测结果
        #
        sum_mean = 0
        for i in range(len(y_pred)):
            sum_mean += (y_pred[i] - y_test.values[i]) ** 2
        sum_erro = np.sqrt(sum_mean / len(X_test))  # 这个10是你测试级的数量
        # calculate RMSE by hand 计算截距
        print("RMSE by hand:", sum_erro)
        #
        # 做ROC曲线
        plt.figure()
        plt.plot(range(len(y_pred)), y_pred, 'b', label="predict")
        plt.plot(range(len(y_pred)), y_test, 'r', label="traintest")
        plt.legend(loc="upper right")  # 显示图中的标签
        plt.xlabel("shijian")
        plt.ylabel('liuliang(GB)')
        plt.show()

        # 预测未知的数据读取
        file_pre = preparedatapath + x + '/' + y
        pre_data = pd.read_csv(file_pre)
        print(pre_data.head(5))
        #
        # 剔除日期数据，一般没有这列可不执行，选取以下数据
        XX = pre_data.loc[:, ("日期", "月份", "天", "小时")]
        YY = pre_data.loc[:, '流量']
        X_train, X_test, y_train, y_test = train_test_split(XX, YY, test_size=1, random_state=25)
        # print(X_test)
        #
        #
        # # 预测
        y_pred = linreg.predict(XX)
        # print(y_pred)  # 10个变量的预测结果

        arr = np.array(XX)

        with open(predictdatapath + x + '/' + 'line_' + y, 'a+') as f:
            for i in range(len(y_pred)):
                f.write(str(arr[i][0]) + ':' + str(y_pred[i] * 1024) + ', ')
                
            f.write('\n')
        #
        # for i in range(len(y_pred)):
        #     sum_mean += (y_pred[i] - y_test.values[i]) ** 2
        #     sum_erro = np.sqrt(sum_mean / len(pre_data))  # 这个10是你测试级的数量
        #     # calculate RMSE by hand
        #     print("RMSE by hand:", sum_erro)
        # # 做ROC曲线
        # sns.pairplot(pre_data, x_vars=['小时'], y_vars='流量', kind="reg", size=1, aspect=0.7)
        #
        plt.figure()
        plt.plot(range(len(y_pred)), y_pred, 'b', label="predict预测")
        plt.plot(range(len(y_pred)), YY, 'r', label="test真实值")
        plt.legend(loc="upper right")  # 显示图中的标签

        plt.xlabel("Days")
        plt.ylabel('Flow(GB)')
        plt.show()
