import pandas as pd
from .. import settings
import os
import logging
import numpy as np
from sklearn.model_selection import train_test_split  # 这里是引用了交叉验证
import seaborn as sns
from sklearn.linear_model import LinearRegression  # 线性回归
import datetime

logger = logging.getLogger('log')

root = ''
root = '/Users/fengdong/PycharmProjects/warn_relaction_interface/flow_predict'

trainworkpath = settings.UPLOAD_URL
preparedatapath = settings.PAREPRE_URL
predictdatapath = settings.DWON_RESU_URL
if not os.path.exists(predictdatapath):
    os.mkdir(predictdatapath)
if not os.path.exists(predictdatapath):
    os.mkdir(preparedatapath)


def file_handle_and_predict(input_path, file_name, work_id):
    try:
        with open(os.path.join(settings.PROCESS_URL, 'process_' + work_id), 'a+') as f:
            print("[" + work_id + "]" + " 开始任务：", file=f)


        suffix = str(os.path.join(input_path, file_name)).split(".")[-1]

        if suffix == 'csv':

            flow_file_path = os.path.join(input_path, file_name)
            print(flow_file_path)
            pd_data = pd.read_csv(flow_file_path)
            print(pd_data.head(5))

            pd_data['流量'] = pd_data['流量'] / 1024
            print(pd_data.head(5))

            sns.pairplot(pd_data, x_vars=['天'], y_vars='流量', kind="reg", size=10, aspect=0.8)

            # plt.show()  # 注意必须加上这一句，否则无法显示。

            # 剔除日期数据，一般没有这列可不执行，选取以下数据
            XX = pd_data.loc[:, ("日期", "月份", "天", "小时")]
            YY = pd_data.loc[:, '流量']

            # 进行数据切割
            X_train, X_test, y_train, y_test = train_test_split(XX, YY, test_size=0.2)
            print('X_train.shape={}\n y_train.shape ={}\n X_test.shape={}\n,  y_test.shape={}'.format(X_train.shape,
                                                                                                      y_train.shape,
                                                                                                      X_test.shape,
                                                                                                      y_test.shape))
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

            # 获取要预测的数据
            parepare_data(input_path, file_name)
            pre_data = pd.read_csv(os.path.join(settings.PAREPRE_URL, file_name))
            print(pre_data.head(5))
            #

            # 剔除日期数据，一般没有这列可不执行，选取以下数据
            XX = pre_data.loc[:, ("日期", "月份", "天", "小时")]
            YY = pre_data.loc[:, '流量']
            # print(X_test)

            # # 预测
            y_pred = linreg.predict(XX)
            # print(y_pred)  # 10个变量的预测结果

            arr = np.array(XX)

            with open(os.path.join(settings.DWON_RESU_URL, file_name), 'a+') as f:
                for i in range(len(y_pred)):
                    f.write(str(arr[i][0]) + ':' + str(y_pred[i] * 1024) + ', ')

                f.write('\n')

            with open(os.path.join(settings.PROCESS_URL, 'process_' + work_id), 'a+') as f:
                print("[" + work_id + "]" + "  当前进度：100%",
                      file=f)
    except Exception as e:
        logging.error("[" + work_id + "]:核心算法处理出错" + str(e))


# 根据最后数据，获取接下来一天的数据
def parepare_data(input_path, file_name):
    file = os.path.join(input_path, file_name)

    f = open(file).readlines()
    f_len = len(f)

    day = f[-1].strip().split(',')[0]
    print('day:' + day)
    code = f[-1].strip().split(',')[1]
    diqu = f[-1].strip().split(',')[2]
    flow = '0'

    thistime = datetime.datetime.strptime(str(day), '%Y%m%d%H%M')

    with open(os.path.join(settings.PAREPRE_URL, file_name), 'w') as f_out:
        f_out.write('日期,编码,地区,流量,月份,天,小时\n')
        for i in range(1, 13):
            predictday = (thistime + datetime.timedelta(minutes=+i * 5)).strftime("%Y%m%d%H%M")

            pre_hour = str(predictday[8:10])

            if pre_hour == '00':
                continue
            elif pre_hour == '01':
                continue
            elif pre_hour == '02':
                continue
            elif pre_hour == '03':
                continue
            elif pre_hour == '04':
                continue
            elif pre_hour == '05':
                continue
            elif pre_hour == '06':
                continue
            elif pre_hour == '07':
                continue
            elif pre_hour == '08':
                continue

            pre_date = str(predictday)
            pre_mouth = str(predictday[4:6])
            pre_day = str(predictday[6:8])

            line = pre_date + ',' + code + ',' + diqu + ',' + flow + ',' + pre_mouth + ',' + pre_day + ',' + pre_hour + '\n'
            print(line)

            f_out.write(line)


def predict_flow(file_name):
    # 导入最后训练数据
    pd_data = pd.read_csv(trainworkpath + file_name)

    # print(pd_data['天'])
    # column_headers = list(pd_data.columns.values)
    # print(column_headers)
    pd_data['流量'] = pd_data['流量'] / 1024
    print(pd_data.head(5))

    sns.pairplot(pd_data, x_vars=['天'], y_vars='流量', kind="reg", size=10, aspect=0.8)

    # plt.show()  # 注意必须加上这一句，否则无法显示。

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

    # 预测未知的数据读取
    file_pre = preparedatapath + file_name
    pre_data = pd.read_csv(file_pre)
    print(pre_data.head(5))
    #
    # 剔除日期数据，一般没有这列可不执行，选取以下数据
    XX = pre_data.loc[:, ("日期", "月份", "天", "小时")]
    YY = pre_data.loc[:, '流量']
    X_train, X_test, y_train, y_test = train_test_split(XX, YY, test_size=1, random_state=25)
    # print(X_test)

    # # 预测
    y_pred = linreg.predict(XX)
    # print(y_pred)  # 10个变量的预测结果

    arr = np.array(XX)

    with open(predictdatapath  + file_name, 'a+') as f:
        for i in range(len(y_pred)):
            f.write(str(arr[i][0]) + ':' + str(y_pred[i] * 1024) + ', ')

        f.write('\n')


def fiest_apply(self, row):
    self.data_num = self.data_num + row.shape[0]
    self.time = self.time + 1
    if int(self.time) % 10000 == 0:
        with open(os.path.join(settings.PROCESS_URL, 'process_' + self.work_id), 'a+') as f:
            print("[" + self.work_id + "]" + "  当前进度：" + str(round(self.data_num / self.data_len * 100, 2)) + "%",
                  file=f)
    if row.shape[0] >= 2:

        row = row.sort_values('TIME_OF_ALARM')

        flag_row = pd.DataFrame()
        flag_array = []
        for k, v in row.iterrows():
            if not flag_row.empty:
                differ = v['TIME_OF_ALARM'] - flag_row['TIME_OF_ALARM']
                if differ.seconds <= self.time_window:
                    flag_array.append(v['TITLE'])
                else:
                    flag_row = v
                    self.all_gr_data.append(flag_array)
                    flag_array = []
            else:
                flag_row = v
                flag_array.append(v['TITLE'])
        return None

    else:
        return None


# def do_apriori(self):
#     for i in self.all_gr_data:
#         if len(i) >= 2:
#             self.apro.append(list(map(lambda x: str(x), i)))
#     results = list(apriori(self.apro, min_confidence=0.001, min_support=0.001, min_lift=1))
#     return results
