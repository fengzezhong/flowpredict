import sys
import os

# 加入预测地市
# if (len(sys.argv) > 1):
#     citydata = sys.argv[1]
# else:
#     citydata = 'guizhou'

root = ''
# root = '/Users/fengdong/Downloads/lte_flow01'

trainworkpath = root + '/flowPredictCity/lte_flow/dataforCityFive/trainDataForCity5Min_end/'
predictworkpath = root + '/flowPredictCity/lte_flow/dataforCityFive/predictFlow_city/'
warnningpath = root + '/flowPredictCity/lte_flow/dataforCityFive/warnningdata/'

if not os.path.exists(warnningpath):
    os.mkdir(warnningpath)
if not os.path.exists(predictworkpath):
    os.mkdir(predictworkpath)
citys = os.listdir(trainworkpath)

for x in citys:
    business = os.listdir(trainworkpath + x)
    if not os.path.exists(predictworkpath + x):
        os.mkdir(predictworkpath + x)
    for y in business:
        print(trainworkpath + x + '/' + y)

        f0 = open(trainworkpath + x + '/' + y).readlines()
        f1 = open(predictworkpath + x + '/' + 'keras_' + y).readlines()

        data0 = []
        data1 = []
        days = []

        f_len = len(f0)

        print(f_len)
        for i in range(0, 16):
            alldata = f0[f_len - 24 + i].strip().split(',')
            flow = alldata[-1]

            data0.append(flow)
            days.append(alldata[0])

        data = f1[-1]
        for i in data.strip().split(','):
            if i != '':
                data1.append(i)
                # print(i)

        for i in range(len(data1)):
            # print('---' + str(i))
            print(data1[i])

        filename = warnningpath + x + '/'
        if not os.path.exists(filename):
            os.mkdir(filename)

        with open(filename + '/' + 'keras_' + y, 'a+') as f:
            for i in range(len(data0)):
                flow0 = float(data0[i]) / 1024
                flow1 = float(data1[i])

                # print(flow0)
                # print(flow1)
                if flow0 > flow1:
                    arrc = round(flow1 / flow0, 2)
                    f.write(days[i] + ': ' + str(arrc) + ',')
                    print(days[i] + ': ' + str(arrc))
                elif flow0 < flow1:
                    arrc = round(flow0 / flow1, 2)
                    f.write(days[i] + ': ' + str(arrc) + ',')
                    print(days[i] + ': ' + str(arrc))
                else:
                    print('1')
            f.write('\n')
