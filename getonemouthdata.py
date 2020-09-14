import os

root = ''

root = '/Users/fengdong/Downloads/lte_flow01'
osPath = root + '/flowPredictCity/lte_flow/'


# print('指定目录：' + osPath)
# dirlist = os.listdir(osPath)


# 判断是否保存了一个月的5分钟数据
def get_onemonth(path, applist):
    for i in applist:
        # print(i)
        f = open(path + i).readlines()
        if len(f) > 5760:
            fin = open(path + i, 'r')
            a = fin.readlines()
            fout = open(path + i, 'w')
            b = ''.join(a[len(a) - 5760:])
            fout.write(b)


osFivePath = osPath + 'dataforFive/trainDataForFiveMin/'
if os.path.exists(osFivePath):
    # 保留一个月的5分钟数据（除去晚12点-早8点）
    list = os.listdir(osFivePath)
    print(osFivePath)
    print(list)
    get_onemonth(osFivePath, list)

osAppPath = osPath + 'dataforAppFive/trainDataForApp5Min/'
if os.path.exists(osAppPath):
    # 保留一个月的5分钟数据（除去晚12点-早8点）
    list = os.listdir(osAppPath)
    for i in list:
        applist = os.listdir(osAppPath + i)
        path = osAppPath + i + '/'
        print(path)
        print(applist)
        get_onemonth(path, applist)

osCityPath1 = osPath + 'dataforCityFive/trainDataForCity5Min/'
if os.path.exists(osCityPath1):
    # 保留一个月的5分钟数据（除去晚12点-早8点）
    list = os.listdir(osCityPath1)
    for i in list:
        citylist = os.listdir(osCityPath1 + i)
        path = osCityPath1 + i + '/'
        get_onemonth(path, citylist)

osCityPath2 = osPath + 'dataforCityFive/trainDataForCity5Min_bak/'
if os.path.exists(osCityPath2):
    # 保留一个月的5分钟数据（除去晚12点-早8点）
    list = os.listdir(osCityPath2)
    for i in list:
        citylist = os.listdir(osCityPath2 + i)
        path = osCityPath2 + i + '/'
        get_onemonth(path, citylist)
