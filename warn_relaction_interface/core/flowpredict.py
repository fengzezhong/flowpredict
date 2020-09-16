import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split  # 这里是引用了交叉验证
from sklearn.linear_model import LinearRegression  # 线性回归
import numpy as np
import matplotlib.pyplot as plt
import os

root = ''
root = '/Users/fengdong/PycharmProjects/warn_relaction_interface/flow_predict'

trainworkpath = root + '/static/upload/'
preparedatapath = root + '/static/prepare_predict/'
predictdatapath = root + '/static/download/'
if not os.path.exists(predictdatapath):
    os.mkdir(predictdatapath)
if not os.path.exists(predictdatapath):
    os.mkdir(preparedatapath)

citys = os.listdir(trainworkpath)


def file_deal(self, path, work_id):
    try:
        with open(os.path.join(settings.PROCESS_URL, 'process_' + work_id), 'a+') as f:
            print("[" + work_id + "]" + " 开始任务：", file=f)
        self.work_id = work_id
        suffix = str(path).split(".")[-1]
        warn_data = None
        if suffix == 'csv':
            warn_data = pd.read_csv(path, encoding='utf-8')
        elif suffix == 'xlsx' or suffix == 'xls':
            warn_data = pd.read_excel(path)
        warn_data.columns = ['TIME_OF_ALARM', 'MAJOR', 'MANUFACTURER', 'NETWORK_ELEMENT_NAME', 'TITLE']
        self.data_len = warn_data.shape[0]
        warn_data['TIME_OF_ALARM'] = pd.to_datetime(pd.to_datetime(warn_data['TIME_OF_ALARM']), unit='ms')
        warn_data.groupby(['NETWORK_ELEMENT_NAME']).apply(self.fiest_apply)
        results = self.do_apriori()
        j_resu = {'rule': [], 'support': []}
        for k, v in enumerate(results):
            # 只看有两个及以上元素的关联集合。单独一个元素的集合没有意义。
            if len(v.items) >= 2:
                j_resu['rule'].append(' '.join(list(v.items)))
                j_resu['support'].append(v.support)
        z_resu = pd.DataFrame(j_resu)
        z_resu.to_csv(os.path.join(settings.DWON_RESU_URL, work_id + ".csv"), encoding="utf-8", index=None)
        with open(os.path.join(settings.PROCESS_URL, 'process_' + self.work_id), 'a+') as f:
            print("[" + self.work_id + "]" + "  当前进度：100%",
                  file=f)
    except Exception as e:
        logging.error("[" + work_id + "]:核心算法处理出错" + str(e))


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


def do_apriori(self):
    for i in self.all_gr_data:
        if len(i) >= 2:
            self.apro.append(list(map(lambda x: str(x), i)))
    results = list(apriori(self.apro, min_confidence=0.001, min_support=0.001, min_lift=1))
    return results


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
    #
    # 做ROC曲线
    # plt.figure()
    # plt.plot(range(len(y_pred)), y_pred, 'b', label="predict")
    # plt.plot(range(len(y_pred)), y_test, 'r', label="traintest")
    # plt.legend(loc="upper right")  # 显示图中的标签
    # plt.xlabel("shijian")
    # plt.ylabel('liuliang(GB)')
    # plt.show()

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

    with open(predictdatapath + 'line_' + file_name, 'a+') as f:
        for i in range(len(y_pred)):
            f.write(str(arr[i][0]) + ':' + str(y_pred[i] * 1024) + ', ')

        f.write('\n')

    # plt.figure()
    # plt.plot(range(len(y_pred)), y_pred, 'b', label="predict预测")
    # plt.plot(range(len(y_pred)), YY, 'r', label="test真实值")
    # plt.legend(loc="upper right")  # 显示图中的标签
    #
    # plt.xlabel("Days")
    # plt.ylabel('Flow(GB)')
    # plt.show()
