import os

root = ''
# root = '/Users/fengdong/Downloads/lte_flow01/flowPredictApp'
path = root + '/flowPredict/lte_flow/'


# 判断是否保存了一个月的5分钟数据
def get_onemonth(filePath):
    applist = os.listdir(filePath)
    for i in applist:
        print(i)
        f = open(filePath + i).readlines()
        if len(f) > 5760:
            fin = open(filePath + i, 'r')
            a = fin.readlines()
            fout = open(filePath + i, 'w')
            b = ''.join(a[len(a) - 5760:])
            fout.write(b)


dirlist = os.listdir(path)

if 'dataforAppFive' in dirlist:
    ospath = path + 'dataforAppFive/'
    list = os.listdir(ospath)
    if 'predictFlow_app' in list:
        filepath = ospath + 'predictFlow_app' + '/'
        applist = os.listdir(filepath)
        for i in applist:
            lastpath = filepath + i + '/'
            print(lastpath)

            get_onemonth(lastpath)
    if 'warnningdata' in list:
        filepath = ospath + 'warnningdata' + '/'
        applist = os.listdir(filepath)
        for i in applist:
            lastpath = filepath + i + '/'
            print(lastpath)

            get_onemonth(lastpath)


elif 'dataforCityFive' in dirlist:
    ospath = path + 'dataforAppFive/'
    list = os.listdir(ospath)
    if 'predictFlow_city' in list:
        filepath = ospath + 'predictFlow_city' + '/'
        applist = os.listdir(filepath)
        for i in applist:
            lastpath = filepath + i + '/'
            print(lastpath)

            get_onemonth(lastpath)
    if 'warnningdata' in list:
        filepath = ospath + 'warnningdata' + '/'
        applist = os.listdir(filepath)
        for i in applist:
            lastpath = filepath + i + '/'
            print(lastpath)

            get_onemonth(lastpath)
elif 'dataforFive' in dirlist:
    ospath = path + 'dataforAppFive/'
    list = os.listdir(ospath)
    if 'predictFlow_five' in list:
        filepath = ospath + 'predictFlow_five' + '/'
        applist = os.listdir(filepath)
        for i in applist:
            lastpath = filepath + i + '/'
            print(lastpath)

            get_onemonth(lastpath)
    if 'warnningdata' in list:
        filepath = ospath + 'warnningdata' + '/'
        applist = os.listdir(filepath)
        for i in applist:
            lastpath = filepath + i + '/'
            print(lastpath)

            get_onemonth(lastpath)
