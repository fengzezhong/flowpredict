import os
import codecs

root = ''
root = '/Users/fengdong/Downloads/lte_flow01'
# osPath = os.path.dirname(os.path.dirname(os.getcwd())) + '/lte_flow/'
osPath = root + '/flowPredict/lte_flow/'

# osPath = './'
print("当前目录：" + os.getcwd())
print('指定目录：' + osPath)
print(type(osPath))


# 获取文件分类
def transfor_city(osPath):
    # for j in dirlist:  # 遍历指定目录
    #     f = open(osPath + j)

    f = open(osPath + 'LTE_FLOW_REAL_TOTAL.csv')
    liens = f.readlines()
    copyPath = 'copyPath/'
    for i in liens:
        i = i.strip()
        if (i.count("贵州") > 0):
            # print(i)
            with codecs.open(osPath + copyPath + 'lteFlowOfHour_guizhou.csv', 'a+', encoding='utf-8') as f0:
                f0.write(i + ',' + '85' + '\n')
        elif (i.count("贵安新区") > 0):
            with codecs.open(osPath + copyPath + 'lteFlowOfHour_guian.csv', 'a+', encoding='utf-8') as f0:
                f0.write(i + ',' + '850' + '\n')
        elif (i.count("贵阳") > 0):
            with codecs.open(osPath + copyPath + 'lteFlowOfHour_guiyang.csv', 'a+', encoding='utf-8') as f0:
                f0.write(i + ',' + '851' + '\n')
        elif (i.count("遵义") > 0):
            with codecs.open(osPath + copyPath + 'lteFlowOfHour_zunyi.csv', 'a+', encoding='utf-8') as f0:
                f0.write(i + ',' + '852' + '\n')
        elif (i.count("安顺") > 0):
            with codecs.open(osPath + copyPath + 'lteFlowOfHour_anshun.csv', 'a+', encoding='utf-8') as f0:
                f0.write(i + ',' + '853' + '\n')
        elif (i.count("都匀") > 0):
            with codecs.open(osPath + copyPath + 'lteFlowOfHour_duyun.csv', 'a+', encoding='utf-8') as f0:
                f0.write(i + ',' + '854' + '\n')
        elif (i.count("凯里") > 0):
            with codecs.open(osPath + copyPath + 'lteFlowOfHour_kaili.csv', 'a+', encoding='utf-8') as f0:
                f0.write(i + ',' + '855' + '\n')
        elif (i.count("铜仁") > 0):
            with codecs.open(osPath + copyPath + 'lteFlowOfHour_tongren.csv', 'a+', encoding='utf-8') as f0:
                f0.write(i + ',' + '856' + '\n')
        elif (i.count("毕节") > 0):
            with codecs.open(osPath + copyPath + 'lteFlowOfHour_bijie.csv', 'a+', encoding='utf-8') as f0:
                f0.write(i + ',' + '857' + '\n')
        elif (i.count("六盘水") > 0):
            with codecs.open(osPath + copyPath + 'lteFlowOfHour_liupanshui.csv', 'a+', encoding='utf-8') as f0:
                f0.write(i + ',' + '858' + '\n')
        elif (i.count("兴义") > 0):
            with codecs.open(osPath + copyPath + 'lteFlowOfHour_xingyi.csv', 'a+', encoding='utf-8') as f0:
                f0.write(i + ',' + '859' + '\n')


# 找到最近一个小时的数据
def getonehourdata(osPath):
    # print(osPath)
    # print(type(osPath))

    path = osPath + 'trainDataForFiveMin/'
    dirlist = os.listdir(path)
    print('目录里的目录和文件:' + str(dirlist))

    for j in dirlist:  # 遍历指定目录

        print(j)
        f = open(path + j)
        oo = 0

        for i in f.readlines():

            i = i.strip()
            if oo == 0:
                day = str(i.split(',')[0])
                code = str(i.split(',')[1])
                diqu = str(i.split(',')[2])
                print(day)
                # print('--------------------' + diqu)
                with codecs.open(osPath + 'trainDataForFiveToHourMiddle/' + j, 'a+',
                                 encoding='utf-8') as f0:
                    f0.write(day + ',' + code + ',' + diqu + ',')

            if oo < 12:
                # print(oo)
                print(i)

                data = str(float(i.split(',')[-1]))

                # print(data)

                with codecs.open(osPath + 'trainDataForFiveToHourMiddle/' + j, 'a+',
                                 encoding='utf-8') as f0:
                    f0.write(data + ',')

                oo += 1

            if oo == 12:
                with codecs.open(osPath + 'trainDataForFiveToHourMiddle/' + j, 'a+',
                                 encoding='utf-8') as f0:
                    f0.write('\n')

                oo = 0
                continue
        with codecs.open(osPath + 'trainDataForFiveToHourMiddle/' + j, 'a+',
                         encoding='utf-8') as f0:
            f0.write('\n')

        # os.rename(path + j, osPath + 'oldfivetohour/trainDataForFiveMin/' + 'old_' + j)


# 计算并得到最终小时数据
def get_trainData(osPath):
    path = osPath + 'trainDataForFiveToHourMiddle/'
    list = os.listdir(path)
    # print('目录里的目录和文件:' + str(list))

    for j in list:  # 遍历指定目录
        f = open(path + j)
        for i in f.readlines():

            data = i.strip().split(',')

            print('data ' + str(data))
            if (len(data) > 1):
                day = data[0]
                code = data[1]
                diqu = data[2]
                flow = 0.0
                if (len(data) > 11):
                    for index in range(len(data) - 3):

                        if data[index + 3] != '':
                            testflow = data[index + 3]
                            print(testflow)
                            flow = float(testflow) + flow
                            print(flow)
                    with codecs.open(osPath + 'trainDataForFiveToHour/' + j, 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(day + ',' + code + ',' + diqu + ',' + str(round(flow, 2)) + '\n')

        # os.rename(osPath + j, osPath + 'oldfivetohour/trainDataForFiveToHourMiddle/' + 'old_' + j)
        os.rename(path + j, osPath + 'oldfivetohour/trainDataForFiveToHourMiddle/' + 'old_' + j)


# 获取原始数据,并加工为各城市分类数据
# transfor_city(osPath)

# 从分类的数据提取一个小时数据
getonehourdata(osPath)

# 制作训练数据
# get_trainData(osPath)
