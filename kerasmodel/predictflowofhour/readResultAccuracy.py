import sys

# 加入预测地市
if (len(sys.argv) > 1):
    citydata = sys.argv[1]
else:
    citydata = 'guizhou'

root = ''
root = '/Users/fengdong/Downloads/lte_flow'

f_train = open(root + '/flowPredict/lte_flow/trainDataForReal/lteFlowOfReal_' + citydata + '.csv')
f_predict = open(root + '/flowPredict/lte_flow/predictFlow_real/predictFlow_' + citydata + '.csv')

f0 = f_train.readlines()
f1 = f_predict.readlines()

data0 = []
data1 = []
days = []

f_len = len(f0)

print(f_len)
for i in range(0, 24):
    # data0.append(f0[f_len -i].strip().split()[-1])

    alldata = f0[f_len - 24 + i].strip().split(',')
    flow = alldata[-1]
    # print(alldata[0] + ','+ flow)
    data0.append(flow)
    days.append(alldata[0])

print('-------------\n')
data = f1[-1]
for i in data.strip().split(','):
    if i != '':
        data1.append(i)
        # print(i)

for i in range(len(data1)):
    print('---' + str(i))
    print(data1[i])

print('------')
print(len(data0))
print('-------------')
print(len(data1))

filename = root + '/flowPredict/lte_flow/predictFlow_real/predictAccuracyOf' + citydata + 'Real.csv'

with open(filename, 'a+') as f:
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
