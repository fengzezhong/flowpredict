import sys
import os
from suds.client import Client
import time
import contrastdata as con

now = time.strftime("%Y%m%d%H%M%S", time.localtime())
sendtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
url = 'http://10.198.104.58:8080/IVRService.asmx?wsdl'
client = Client(url)
def callphone(msg):
    client.service.SendIvrData(now, now, '流量预测', 1, 10, 1, 2, sendtime, sendtime, 9000, '13984819884', '13984819884',msg, 1, 3, 0, '','82516', '1', '')

# 加入预测地市
# if (len(sys.argv) > 1):
#     citydata = sys.argv[1]
# else:
#     citydata = 'guizhou'

# root = ''
root = '/Users/fengdong/Downloads/lte_flow01'

trainworkpath = root + '/flowPredictCity/lte_flow/dataforCityFive/trainDataForCity5Min_end/'
predictworkpath = root + '/flowPredictCity/lte_flow/dataforCityFive/predictFlow_city/'
warnningpath = root + '/flowPredictCity/lte_flow/dataforCityFive/warnningdata/'

if not os.path.exists(warnningpath):
    os.mkdir(warnningpath)
citys = os.listdir(trainworkpath)

for x in citys:
    business = os.listdir(trainworkpath + x)
    if not os.path.exists(predictworkpath + x):
        os.mkdir(predictworkpath + x)
    for y in business:

        f0 = open(trainworkpath + x + '/' + y).readlines()
        f1 = open(predictworkpath + x + '/' + 'line_' + y).readlines()

        data_train = f0[-1].split(',')[4]

        predictall = f1[-2].split(',')[0]

        data_day = predictall.split(':')[0]
        data_predict = predictall.split(':')[1]

        filename = warnningpath + x + '/'
        if not os.path.exists(filename):
            os.mkdir(filename)

        if y.count('congjiang') > 0 or y.count('jianhe') > 0 or y.count('liping') > 0 or y.count('jinhaihu') > 0 or y.count(
                'guian') > 0:
            print('这是不稳定的区县')
        else:
            print('正常----------------------------')
