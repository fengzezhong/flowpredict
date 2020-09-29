import warnings

warnings.filterwarnings("ignore")

import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import datetime

from .. import settings
import pandas as pd
import numpy as np

from sklearn.preprocessing import MinMaxScaler

from keras.models import Sequential, load_model
from keras.layers import Dense, LSTM, Dropout

from keras import backend as K


def pre_predict_data(train_data, scaler):
    '''
    处理训练数据，得到训练集、测试集
    :param train_data: 训练数据 Dataframe类型
    :return: 训练集X:X_train, 训练集y:y_train, 测试集X:X_test, 测试集y:y_test, 归一化器:scaler
    '''
    lag = 12
    attr = 'flow'

    flows = scaler.transform(train_data[attr].values.reshape(-1, 1)).reshape(1, -1)[0]

    n_hour = len(flows)

    train_flow = flows[:n_hour - 24]
    test_flow = flows[n_hour - 24:]

    train_, predict_ = [], []
    for i in range(lag, len(train_flow)):
        train_.append(train_flow[i - lag: i + 1])

    for i in range(lag, len(test_flow)):
        predict_.append(test_flow[i - lag: i + 1])

    train = np.array(train_)
    predict_all = np.array(predict_)
    np.random.shuffle(train)

    X_train = train[:, :-1]
    y_train = train[:, -1]
    X_predict = predict_all[:, :-1]
    y_predict = predict_all[:, -1]

    return X_train, y_train, X_predict, y_predict


def train_model(model, X_train, y_train, config, city, type, model_path):
    '''
    训练模型
    :param model: 训练模型参数
    :param X_train: X_train
    :param y_train: y_train
    :param name: 模型类型名称
    :param config:  模型配置参数
    :return:
    '''
    model.compile(loss="mse", optimizer="adam", metrics=['mape'])
    # early = EarlyStopping(monitor='val_loss', patience=30, verbose=0, mode='auto')
    hist = model.fit(
        X_train, y_train,
        batch_size=config["batch"],
        epochs=config["epochs"],
        validation_split=0.05)

    print(model_path)
    # 每个网元保存模型
    model.save(os.path.join(model_path, config['model_name'] + '_' + city + '_' + type + '.h5'))
    df = pd.DataFrame.from_dict(hist.history)
    df.to_csv(os.path.join(model_path, config['model_name'] + '_' + city + '_' + type + '_loss.csv'), encoding='utf-8',
              index=False)

    return model


def get_lstm(units):
    '''
    模型配置
    :param units: 模型内参数配置
    :return:
    '''
    model = Sequential()
    model.add(LSTM(units[1], input_shape=(units[0], 1), return_sequences=True))
    model.add(LSTM(units[2]))
    model.add(Dropout(0.2))
    model.add(Dense(units[3], activation='sigmoid'))

    return model


def predict_oneday(train_data, city, model, scaler):
    '''
    预测一天的数据
    :param train_data: 训练数据
    :param city: 城市类别
    :param model: 预测模型
    :param scaler: 归一化器
    :return:
    '''
    X_predict_train, y_predict_train, X_predict_test, y_predict_test = pre_predict_data(train_data, scaler)

    # 归一化数据
    X_predict = np.reshape(X_predict_test, (X_predict_test.shape[0], X_predict_test.shape[1], 1))

    # 预测数据，以及反归一化
    predict_data_ = model.predict(X_predict)
    predicteds = scaler.inverse_transform(predict_data_.reshape(-1, 1)).reshape(1, -1)[0]

    predict_times = []
    citys = []

    # 获取最后一天日期
    last_time = train_data.iloc[-1, :]['day']

    last_time = datetime.datetime.strptime(str(last_time), '%Y%m%d%H%M')
    for i in range(1, 13):
        predictday = (last_time + datetime.timedelta(minutes=+i*5)).strftime("%Y%m%d%H%M")
        predict_times.append(predictday)
        citys.append(city)

    pare_hour_data = {'city': citys, 'day': predict_times, 'flow': predicteds}
    pare_hour_datas = pd.DataFrame(pare_hour_data)

    # 保存为下一个预测数据
    train_data = pd.concat([train_data, pare_hour_datas], axis=0)

    return train_data, pare_hour_datas


def file_handle_and_predict_min(file_path, work_id, type, is_train):
    # 设置预测的临时文件
    temp_files_path = os.path.join(settings.DWON_RESU_URL, 'temp_files')

    # 保存模型的文件
    model_path = os.path.join(settings.DWON_RESU_URL, 'models')

    if not os.path.exists(temp_files_path):
        os.mkdir(temp_files_path)
    if not os.path.exists(model_path):
        os.mkdir(model_path)

    # LSTM 训练参数配置
    config = {"batch": 200, "epochs": 5, 'model_name': 'lstm'}

    # 读取第一行 判断是否有表头
    # 如果输入的有表头 就有第一种读取，如果没有，按第二种读取
    flow_file_name = os.path.join(file_path, work_id + ".csv")
    line = open(flow_file_name).readlines()[0]
    if 'flow' not in line:
        df_all = pd.read_csv(os.path.join(file_path, work_id + ".csv"), header=['day', 'city', 'flow'])
    else:
        df_all = pd.read_csv(os.path.join(file_path, work_id + ".csv"), header=0)

    # 汇总预测类别数据 并按类别分组
    city_len = len(df_all['city'].unique())
    city_flow_datas = df_all.groupby('city')  # 地市分组

    # 配置LSTM训练参数
    model_name = config['model_name']
    model = get_lstm([12, 64, 64, 1])

    i = 0  # 记录类别个数
    # 分别读取每个类别的数据
    for city, city_flow_data in city_flow_datas:

        if city is not None:  # 类别中有一个是nul 不知为什么，需要过滤

            i += 1  # 记录到多少个类别了
            print(city)
            print('当前城市是: ', city, '是第: ', i, ' 个城市', '总的城市个数: ', city_len)

            city_flow_data.set_index(['day'])  # 按时间排序

            city_flow_data.fillna(city_flow_data.mean(), inplace=True)  # 空缺值填充

            # 全局归一化器
            scaler = MinMaxScaler(feature_range=(0, 1)).fit(city_flow_data['flow'].values.reshape(-1, 1))

            # 切分训练预测数据
            X_train, y_train, X_test, y_test = pre_predict_data(city_flow_data, scaler)

            # 归一化数据
            X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
            y_test = scaler.inverse_transform(y_test.reshape(-1, 1)).reshape(1, -1)[0]
            X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

            try:
                if is_train == 'train':
                    # 训练模型
                    print('开始训练')
                    model = train_model(model, X_train, y_train, config, city, type, model_path)

                elif is_train == 'predict':
                    # 加载模型
                    model = load_model(os.path.join(model_path, model_name + '_' + city + '_' + type + '.h5'))

                print('开始预测')
                # 预测第一天的数据 24小时
                train_data, pare_hour_datas = predict_oneday(city_flow_data, city, model, scaler)

                # 保存到暂存目录
                save_path = os.path.join(temp_files_path, work_id + '_' + city + '.csv')
                pare_hour_datas.to_csv(save_path, mode='a', header=False, index=False)

            except Exception as e:
                print('模型加载加错，错误原因' + str(e))

            # 清理该模型的数据
            K.clear_session()

    # 加工预测生成的文件
    files = os.listdir(temp_files_path)
    files_len = len(files)
    if files_len > 0:
        if work_id in files[0]:

            # 写入到一个文件中 以任务ID为标识
            with open(os.path.join(settings.DWON_RESU_URL, work_id + '.csv'), 'w+') as f_write:
                for i in range(files_len):

                    # 获取表头，标识地区
                    lines = open(os.path.join(temp_files_path, files[i])).readlines()
                    one_line = lines[0].split(',')[0] + ','

                    # 分别读取流量
                    for line in lines:
                        city_day_flow = line.split(',')
                        one_line = one_line + city_day_flow[1] + ':' + str(round(float(city_day_flow[2]), 2)) + ','
                    # print(one_line)

                    # 写入并删除临时文件
                    f_write.write(one_line + '\n')
                    os.remove(os.path.join(temp_files_path, files[i]))
