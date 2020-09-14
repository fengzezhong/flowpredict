import os
import datetime

# 加入预测地市
# if len(sys.argv) > 1:
#     citydata = sys.argv[1]
# else:
#     citydata = 'guizhou'

root = ''
root = '/Users/fengdong/Downloads/lte_flow01/flowPredictCity'

trainworkpath = root + '/flowPredict/lte_flow/dataforCityFive/trainDataForCity5Min_end/'
traindatapath = root + '/flowPredict/lte_flow/dataforCityFive/citytraindata/'
preparedatapath = root + '/flowPredict/lte_flow/dataforCityFive/citypreparedata/'

if not os.path.exists(preparedatapath):
    os.mkdir(preparedatapath)
if not os.path.exists(traindatapath):
    os.mkdir(traindatapath)

citys = os.listdir(trainworkpath)

# 用于生成之前批量导入的5分钟数据
for x in citys:
    business = os.listdir(trainworkpath + x)
    if not os.path.exists(traindatapath + x):
        os.mkdir(traindatapath + x)
    if not os.path.exists(preparedatapath + x):
        os.mkdir(preparedatapath + x)
    for y in business:
        line_num = 0
        print(trainworkpath + x + '/' + y)
        f = open(trainworkpath + x + '/' + y).readlines()
        f_len = len(f)

        day = f[-1].strip().split(',')[0]
        print('day:' + day)
        code = f[-1].strip().split(',')[1]
        diqu = f[-1].strip().split(',')[2]
        flow = '0'

        thistime = datetime.datetime.strptime(str(day), '%Y%m%d%H%M')

        with open(preparedatapath + x + '/' + y, 'w') as f_out:
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

        with open(trainworkpath + x + '/' + y, 'r') as f_in:
            with open(traindatapath + x + '/' + y, 'w') as f_out:
                for line in f_in:
                    line_num += 1
                    if line_num == 1:
                        f_out.write('日期,编码,地区,流量,月份,天,小时\n')
                    else:
                        alldata = line.strip().split(',')
                        allday = alldata[0]
                        if allday[8:10] == '00':
                            continue
                        elif allday[8:10] == '01':
                            continue
                        elif allday[8:10] == '02':
                            continue
                        elif allday[8:10] == '03':
                            continue
                        elif allday[8:10] == '04':
                            continue
                        elif allday[8:10] == '05':
                            continue
                        elif allday[8:10] == '06':
                            continue
                        elif allday[8:10] == '07':
                            continue
                        elif allday[8:10] == '08':
                            continue

                        code = alldata[1]
                        diqu = alldata[2]
                        flow = (alldata[4])
                        mouth = allday[4:6]
                        day = allday[6:8]
                        hour = allday[8:10]
                        print(allday)
                        print(flow)
                        f_out.write(allday + ',')
                        f_out.write(code + ',')
                        f_out.write(diqu + ',')
                        f_out.write(flow + ',')
                        f_out.write(mouth + ',')
                        f_out.write(day + ',')
                        f_out.write(hour + '\n')

