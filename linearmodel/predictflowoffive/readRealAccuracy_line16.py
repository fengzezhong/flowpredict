import sys
import os
import contrastdata as con

# 加入预测地市
# if (len(sys.argv) > 1):
#     citydata = sys.argv[1]
# else:
#     citydata = 'guizhou'

root = ''
root = '/Users/fengdong/Downloads/lte_flow01/flowPredictCity'

# f_train = open(root + '/flowPredict/lte_flow/trainDataForFiveMin_end/linedata_train_five_' + citydata + '16.csv')
# f_predict = open(root + '/flowPredict/lte_flow/predictFlow_five/predictData_five_' + citydata + '_line16.csv')

trainworkpath = root + '/flowPredict/lte_flow/dataforCityFive/trainDataForCity5Min_end/'
predictworkpath = root + '/flowPredict/lte_flow/dataforCityFive/predictFlow_city/'
warnningpath = root + '/flowPredict/lte_flow/dataforCityFive/warnningdata/'

if not os.path.exists(warnningpath):
    os.mkdir(warnningpath)
citys = os.listdir(trainworkpath)

for x in citys:
    business = os.listdir(trainworkpath + x)
    if not os.path.exists(predictworkpath + x):
        os.mkdir(predictworkpath + x)
    for y in business:

        print(y)
        if y.count('congjiang') > 0 or y.count('jianhe') > 0 or y.count('liping') > 0 or y.count(
                'jinhaihu') > 0 or y.count('guian') > 0:
            print('----------111111111----------------')
        else:
            print('callphone')
        f0 = open(trainworkpath + x + '/' + y).readlines()
        f1 = open(predictworkpath + x + '/' + 'line_' + y).readlines()

        data_train = f0[-1].split(',')[4]
        # print(data_train)
        # '201911151130,854,黔南,都匀市,240870.25'
        # print(f0)
        # print(f1)
        predictall = f1[-2].split(',')[0]

        data_day = predictall.split(':')[0]
        data_predict = predictall.split(':')[1]

        # filename = root + '/flowPredict/lte_flow/predictFlow_five/predictAccuracyOf_five_' + citydata + 'line16.csv'
        filename = warnningpath + x + '/'
        if not os.path.exists(filename):
            os.mkdir(filename)

        with open(filename + 'line_' + y, 'a+') as f:
            flow0 = float(data_train)
            flow1 = float(data_predict)

            if flow0 > flow1:
                arrc = round(flow1 / flow0, 2)
                if arrc < 1:
                    # print(data_day[0:4] + '年' + data_day[4:6] + '月' + data_day[6:8] + '日' + data_day[
                    #                                                                         8:10] + '时' + data_day[
                    #                                                                                       10:13] + '分')
                    quxian = y.split('_')[-1].split('.')[0]
                    msg = '地区:' + con.citydata[x] + ',' + '区县:' + con.quxiandata[quxian] + ',' + data_day + ': ' + str(
                        arrc) + '\n'
                    f.write(msg)
                    # print('地区:' + x + ',' +  '区县:' + y + ',' + data_day + ': ' + str(arrc))
                    # client.service.SendIvrData(now, now, '流量预测', 1, 10, 1, 2, sendtime, sendtime, 9000, '13984819884','13984819884', msg, 1, 60, 0, '', '82516', '1', '')
            elif flow0 < flow1:
                arrc = round(flow0 / flow1, 2)
                if arrc < 1:
                    quxian = y.split('_')[-1].split('.')[0]
                    msg = '地区:' + con.citydata[x] + ',' + '区县:' + con.quxiandata[quxian] + ',' + data_day + ': ' + str(
                        arrc) + '\n'
                    f.write(msg)
                    # print('地区:' + x + ',' +  '区县:' + y + ',' + data_day + ': ' + str(arrc))
                    # client.service.SendIvrData(now, now, '流量预测', 1, 10, 1, 2, sendtime, sendtime, 9000, '13984819884','13984819884', msg, 1, 60, 0, '', '82516', '1', '')
            else:
                print('1')
                f.write('地区:' + x + ',' + '区县:' + y.split('_')[-1].split('.')[0] + ',' + data_day + ': ' + str(
                    '1.0') + '\n')
