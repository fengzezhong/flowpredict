# import pandas as pd
import codecs
import os

root = ''

root = '/Users/fengdong/Downloads/lte_flow01'
osPath = root + '/flowPredictCity/lte_flow/'

# /Users/fengdong/Downloads/lte_flow01/flowPredictCity
print('指定目录：' + osPath)
dirlist = os.listdir(osPath)


# 判断是否保存了一个月的5分钟数据
def get_onemonth(path, applist):
    for i in applist:
        print(i)
        f = open(path + i).readlines()
        if len(f) > 5760:
            fin = open(path + i, 'r')
            a = fin.readlines()
            fout = open(path + i, 'w')
            b = ''.join(a[len(a) - 5760:])
            fout.write(b)


def getofonetoeight(line):
    alldata = line.strip().split(',')
    allday = alldata[0]
    if not (allday[8:10] == '00' or allday[8:10] == '01' or allday[8:10] == '02'
            or allday[8:10] == '03' or allday[8:10] == '04' or allday[8:10] == '05'
            or allday[8:10] == '06' or allday[8:10] == '07' or allday[8:10] == '08'):
        pass


hourFile = []
dayFile = []
realHourFile = []
fiveMinFile = []
appfiveMinFile = []
cityfiveMinFile = []

for j in dirlist:  # 遍历指定目录

    if j.count('APP_FLOW_REAL_5MIN') > 0 and j.count('old') == 0:  # 5分钟应用数据
        fileName = j.split('_')[-1].split('.')[0]
        appfiveMinFile.append(fileName)

    elif j.count('CITY_FLOW_REAL_5MIN') > 0 and j.count('old') == 0:  # 5分钟地市数据
        fileName = j.split('_')[-1].split('.')[0]
        cityfiveMinFile.append(fileName)

    elif j.count('LTE_FLOW_REAL_5MIN') > 0 and j.count('old') == 0:  # 5分钟实时数据
        fileName = j.split('_')[-1].split('.')[0]
        fiveMinFile.append(fileName)

    elif j.count('LTE_FLOW_HOUR') > 0 and j.count('old') == 0:  # 小时汇总数据
        # if (j.count('HOUR') > 0):  # 提取小时粒度数据
        fileName = j.split('_')[-1].split('.')[0]
        hourFile.append(fileName)

    elif j.count('LTE_FLOW_DAY_') > 0 and j.count('old') == 0:  # 天汇总数据数据
        # elif (j.count('DAY') > 0):  # 提取小时粒度数据
        fileName = j.split('_')[-1].split('.')[0]
        dayFile.append(fileName)

    elif j.count('LTE_FLOW_REAL_HOUR') > 0 and j.count('old') == 0:  # 5分钟小时汇总数据
        # elif (j.count('REAL') > 0):
        fileName = j.split('_')[-1].split('.')[0]
        realHourFile.append(fileName)

hourFile.sort()
dayFile.sort()
realHourFile.sort()
fiveMinFile.sort()
appfiveMinFile.sort()
cityfiveMinFile.sort()

osAppPath = osPath + 'dataforFive/trainDataForFiveMin/'
if os.path.exists(osAppPath):
    # 保留一个月的5分钟数据（除去晚12点-早8点）
    applist = os.listdir(osAppPath)
    get_onemonth(osAppPath, applist)

# osAppPath = osPath + 'dataforAppFive/trainDataForApp5Min/'
# if os.path.exists(osAppPath):
#     # 保留一个月的5分钟数据（除去晚12点-早8点）
#     applist = os.listdir(osAppPath)
#     get_onemonth(osAppPath, applist)
#
# osCityPath1 = osPath + 'dataforCityFive/trainDataForCity5Min/'
# if os.path.exists(osCityPath1):
#     # 保留一个月的5分钟数据（除去晚12点-早8点）
#     applist = os.listdir(osCityPath1)
#     get_onemonth(osCityPath1, applist)
#
# osCityPath2 = osPath + 'dataforCityFive/trainDataForCity5Min_bak/'
# if os.path.exists(osCityPath2):
#     # 保留一个月的5分钟数据（除去晚12点-早8点）
#     applist = os.listdir(osCityPath2)
#     get_onemonth(osCityPath2, applist)
#
# osFivePath = osPath + 'dataforFive/trainDataForFiveMin/'
# if os.path.exists(osFivePath):
#     # 保留一个月的5分钟数据（除去晚12点-早8点）
#     applist = os.listdir(osFivePath)
#     get_onemonth(osFivePath, applist)


for j in cityfiveMinFile:  # 遍历指定目录

    fn = 'CITY_FLOW_REAL_5MIN_' + j + '.csv'  # 每次测试均需要更改 CITY_FLOW_REAL_5MIN_201908050940.csv
    f = open(osPath + fn)

    for i in f.readlines():

        if i.split(',')[0]:
            if i.count("贵州") > 0:
                trainPath = 'dataforCityFive/trainDataForCity5Min/guizhou/'
                if not os.path.exists(osPath + trainPath):
                    os.mkdir(osPath + trainPath)

                with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_guizhou.csv', 'a+', encoding='utf-8') as f0:
                    f0.write(i)
            elif i.count("贵安新区") > 0:
                trainPath = 'dataforCityFive/trainDataForCity5Min/guian/'
                if not os.path.exists(osPath + trainPath):
                    os.mkdir(osPath + trainPath)
                if i.count('贵安新区'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_guian.csv', 'a+', encoding='utf-8') as f0:
                        f0.write(i)
            elif i.count("贵阳") > 0:
                trainPath = 'dataforCityFive/trainDataForCity5Min/guiyang/'
                if not os.path.exists(osPath + trainPath):
                    os.mkdir(osPath + trainPath)
                if i.count('云岩区'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_guiyang_yunyan.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('南明区'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_guiyang_nanming.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('观山湖区'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_guiyang_guanshan.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('小河区'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_guiyang_xiaohe.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('清镇市'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_guiyang_qingzhen.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('花溪区'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_guiyang_huaxi.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('白云区'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_guiyang_baiyun.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('乌当区'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_guiyang_wudang.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('开阳县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_guiyang_kaiyang.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('修文县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_guiyang_xiuwen.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('息烽县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_guiyang_xifeng.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)

            elif i.count("遵义") > 0:
                trainPath = 'dataforCityFive/trainDataForCity5Min/zunyi/'
                if not os.path.exists(osPath + trainPath):
                    os.mkdir(osPath + trainPath)
                if i.count('仁怀市'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_zunyi_renhuai.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('红花岗区'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_zunyi_honghuag.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('播州区'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_zunyi_bozhou.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('汇川区'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_zunyi_huichuan.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('习水县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_zunyi_xishui.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('桐梓县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_zunyi_tongzi.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('新蒲区'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_zunyi_xinpu.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('绥阳县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_zunyi_suiyang.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('正安县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_zunyi_zhengan.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('湄潭县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_zunyi_meitan.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('凤冈县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_zunyi_fenggang.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('赤水市'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_zunyi_chishui.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('务川县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_zunyi_wuchuan.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('道真县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_zunyi_daozhen.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('余庆县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_zunyi_yuqing.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)

            elif i.count("安顺") > 0:
                trainPath = 'dataforCityFive/trainDataForCity5Min/anshun/'
                if not os.path.exists(osPath + trainPath):
                    os.mkdir(osPath + trainPath)
                if i.count('西秀区'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_anshun_xixiu.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('普定县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_anshun_puding.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('镇宁县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_anshun_zhenning.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('平坝县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_anshun_pingba.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('紫云县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_anshun_ziyun.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('关岭县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_anshun_guanling.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)

            elif i.count("黔南") > 0:
                trainPath = 'dataforCityFive/trainDataForCity5Min/duyun/'
                if not os.path.exists(osPath + trainPath):
                    os.mkdir(osPath + trainPath)
                if i.count('都匀市'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_qiannan_duyun.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('瓮安县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_qiannan_wengan.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('惠水县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_qiannan_huishui.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('福泉市'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_qiannan_fuquan.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('龙里县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_qiannan_longli.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('独山县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_qiannan_dushan.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('罗甸县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_qiannan_luodian.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('贵定县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_qiannan_guiding.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('平塘县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_qiannan_pingtang.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('三都县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_qiannan_sandu.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('长顺县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_qiannan_changshun.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('荔波县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_qiannan_libo.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)

            elif i.count("黔东南") > 0:
                trainPath = 'dataforCityFive/trainDataForCity5Min/kaili/'
                if not os.path.exists(osPath + trainPath):
                    os.mkdir(osPath + trainPath)
                if i.count('凯里市'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_qiandongnan_kaili.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('黎平县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_qiandongnan_liping.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('榕江县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_qiandongnan_rongjiang.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('从江县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_qiandongnan_congjiang.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('天柱县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_qiandongnan_tianzhu.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('黄平县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_qiandongnan_huangping.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('镇远县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_qiandongnan_zhenyuan.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('剑河县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_qiandongnan_jianhe.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('三穗县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_qiandongnan_sanhui.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('锦屏县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_qiandongnan_jinping.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('岑巩县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_qiandongnan_yingong.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('雷山县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_qiandongnan_leishan.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('丹寨县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_qiandongnan_danzhai.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('施秉县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_qiandongnan_shibing.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('麻江县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_qiandongnan_majiang.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('台江县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_qiandongnan_taijiang.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)

            elif i.count("铜仁") > 0:
                trainPath = 'dataforCityFive/trainDataForCity5Min/tongren/'
                if not os.path.exists(osPath + trainPath):
                    os.mkdir(osPath + trainPath)
                if i.count('碧江区'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_tongren_bijiang.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('松桃县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_tongren_songtao.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('德江县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_tongren_dejiang.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('沿河县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_tongren_yanhe.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('思南县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_tongren_sinan.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('印江县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_tongren_yinjiang.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('石阡县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_tongren_shiqian.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('江口县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_tongren_jiangkou.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('玉屏县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_tongren_yuping.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('万山区'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_tongren_wanshan.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)


            elif i.count("毕节") > 0:
                trainPath = 'dataforCityFive/trainDataForCity5Min/bijie/'
                if not os.path.exists(osPath + trainPath):
                    os.mkdir(osPath + trainPath)
                if i.count('毕节市'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_bijie_bijie.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('威宁县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_bijie_weining.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('织金县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_bijie_zhijin.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('黔西县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_bijie_qianxi.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('大方县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_bijie_dafang.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('赫章县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_bijie_hezhang.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('金沙县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_bijie_jinsha.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('纳雍县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_bijie_nayong.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('金海湖新区'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_bijie_jinhaihu.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)

            elif i.count("六盘水") > 0:
                trainPath = 'dataforCityFive/trainDataForCity5Min/liupanshui/'
                if not os.path.exists(osPath + trainPath):
                    os.mkdir(osPath + trainPath)
                if i.count('盘州'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_liupanshui_panzhou.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('钟山区'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_liupanshui_zhongshan.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('水城县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_liupanshui_shuicheng.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('六枝县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_liupanshui_liuzhi.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)

            elif i.count("黔西南") > 0:
                trainPath = 'dataforCityFive/trainDataForCity5Min/xingyi/'
                if not os.path.exists(osPath + trainPath):
                    os.mkdir(osPath + trainPath)
                if i.count('兴义市'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_qianxinan_xingyi.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('兴仁市'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_qianxinan_xingren.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('安龙县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_qianxinan_anlong.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('贞丰县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_qianxinan_zhenfeng.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('普安县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_qianxinan_puan.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('望谟县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_qianxinan_wangmo.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('晴隆县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_qianxinan_qinglong.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('册亨县'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfCity5Min_qianxinan_ceheng.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)

    os.rename(osPath + fn, osPath + 'dataforCityFive/oldFlow_cityfive/' + 'old_' + fn)

for j in appfiveMinFile:  # 遍历指定目录

    fn = 'APP_FLOW_REAL_5MIN_' + j + '.csv'  # 每次测试均需要更改
    try:
        f = open(osPath + fn)

        for i in f.readlines():

            if i.count("贵州") > 0:
                # print(i)
                trainPath = 'dataforAppFive/trainDataForApp5Min/guizhou/'
                if not os.path.exists(osPath + trainPath):
                    os.mkdir(osPath + trainPath)
                if i.count('网盘云服务'):

                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guizhou_pan.csv', 'a+',
                                     encoding='utf-8') as f0:
                        # getout_oneToeight(i, f0)
                        f0.write(i)
                elif i.count('P2P业务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guizhou_ptop.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('出行旅游'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guizhou_travel.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('邮箱'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guizhou_mail.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('音乐'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guizhou_music.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('微博'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guizhou_weibo.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('财经'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guizhou_finance.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('浏览下载'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guizhou_down.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('视频直播'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guizhou_live.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('VoIP业务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guizhou_voip.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('导航'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guizhou_navi.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('阅读'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guizhou_read.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('支付'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guizhou_pay.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('应用商店'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guizhou_appshop.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('游戏'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guizhou_game.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('购物'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guizhou_shopping.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('视频'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guizhou_video.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('安全杀毒'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guizhou_antivirus.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('即时通信'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guizhou_imps.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('动漫'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guizhou_comic.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('彩信'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guizhou_mms.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('红包业务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guizhou_redp.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('新业务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guizhou_newbuss.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('其他'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guizhou_other.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)

            elif i.count("贵安新区") > 0:
                trainPath = 'dataforAppFive/trainDataForApp5Min/guian/'
                if not os.path.exists(osPath + trainPath):
                    os.mkdir(osPath + trainPath)
                if i.count('网盘云服务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guian_pan.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('P2P业务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guian_ptop.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('出行旅游'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guian_travel.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('邮箱'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guian_mail.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('音乐'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guian_music.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('微博'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guian_weibo.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('财经'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guian_finance.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('浏览下载'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guian_down.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('视频直播'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guian_live.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('VoIP业务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guian_voip.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('导航'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guian_navi.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('阅读'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guian_read.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('支付'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guian_pay.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('应用商店'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guian_appshop.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('游戏'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guian_game.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('购物'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guian_shopping.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('视频'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guian_video.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('安全杀毒'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guian_antivirus.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('即时通信'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guian_imps.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('动漫'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guian_comic.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('彩信'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guian_mms.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('红包业务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guian_redp.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('新业务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guian_newbuss.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('其他'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guian_other.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)

            elif i.count("贵阳") > 0:
                trainPath = 'dataforAppFive/trainDataForApp5Min/guiyang/'
                if not os.path.exists(osPath + trainPath):
                    os.mkdir(osPath + trainPath)
                if i.count('网盘云服务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guiyang_pan.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('P2P业务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guiyang_ptop.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('出行旅游'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guiyang_travel.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('邮箱'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guiyang_mail.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('音乐'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guiyang_music.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('微博'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guiyang_weibo.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('财经'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guiyang_finance.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('浏览下载'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guiyang_down.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('视频直播'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guiyang_live.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('VoIP业务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guiyang_voip.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('导航'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guiyang_navi.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('阅读'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guiyang_read.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('支付'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guiyang_pay.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('应用商店'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guiyang_appshop.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('游戏'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guiyang_game.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('购物'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guiyang_shopping.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('视频'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guiyang_video.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('安全杀毒'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guiyang_antivirus.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('即时通信'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guiyang_imps.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('动漫'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guiyang_comic.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('彩信'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guiyang_mms.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('红包业务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guiyang_redp.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('新业务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guiyang_newbuss.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('其他'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_guiyang_other.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
            elif i.count("遵义") > 0:
                trainPath = 'dataforAppFive/trainDataForApp5Min/zunyi/'
                if not os.path.exists(osPath + trainPath):
                    os.mkdir(osPath + trainPath)
                if i.count('网盘云服务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_zunyi_pan.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('P2P业务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_zunyi_ptop.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('出行旅游'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_zunyi_travel.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('邮箱'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_zunyi_mail.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('音乐'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_zunyi_music.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('微博'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_zunyi_weibo.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('财经'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_zunyi_finance.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('浏览下载'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_zunyi_down.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('视频直播'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_zunyi_live.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('VoIP业务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_zunyi_voip.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('导航'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_zunyi_navi.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('阅读'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_zunyi_read.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('支付'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_zunyi_pay.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('应用商店'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_zunyi_appshop.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('游戏'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_zunyi_game.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('购物'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_zunyi_shopping.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('视频'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_zunyi_video.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('安全杀毒'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_zunyi_antivirus.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('即时通信'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_zunyi_imps.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('动漫'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_zunyi_comic.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('彩信'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_zunyi_mms.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('红包业务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_zunyi_redp.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('新业务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_zunyi_newbuss.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('其他'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_zunyi_other.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
            elif i.count("安顺") > 0:
                trainPath = 'dataforAppFive/trainDataForApp5Min/anshun/'
                if not os.path.exists(osPath + trainPath):
                    os.mkdir(osPath + trainPath)
                if i.count('网盘云服务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_anshun_pan.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('P2P业务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_anshun_ptop.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('出行旅游'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_anshun_travel.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('邮箱'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_anshun_mail.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('音乐'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_anshun_music.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('微博'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_anshun_weibo.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('财经'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_anshun_finance.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('浏览下载'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_anshun_down.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('视频直播'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_anshun_live.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('VoIP业务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_anshun_voip.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('导航'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_anshun_navi.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('阅读'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_anshun_read.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('支付'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_anshun_pay.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('应用商店'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_anshun_appshop.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('游戏'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_anshun_game.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('购物'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_anshun_shopping.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('视频'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_anshun_video.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('安全杀毒'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_anshun_antivirus.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('即时通信'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_anshun_imps.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('动漫'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_anshun_comic.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('彩信'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_anshun_mms.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('红包业务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_anshun_redp.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('新业务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_anshun_newbuss.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('其他'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_anshun_other.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
            elif i.count("黔南") > 0:
                trainPath = 'dataforAppFive/trainDataForApp5Min/duyun/'
                if not os.path.exists(osPath + trainPath):
                    os.mkdir(osPath + trainPath)
                if i.count('网盘云服务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qiannan_pan.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('P2P业务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qiannan_ptop.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('出行旅游'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qiannan_travel.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('邮箱'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qiannan_mail.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('音乐'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qiannan_music.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('微博'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qiannan_weibo.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('财经'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qiannan_finance.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('浏览下载'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qiannan_down.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('视频直播'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qiannan_live.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('VoIP业务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qiannan_voip.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('导航'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qiannan_navi.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('阅读'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qiannan_read.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('支付'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qiannan_pay.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('应用商店'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qiannan_appshop.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('游戏'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qiannan_game.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('购物'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qiannan_shopping.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('视频'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qiannan_video.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('安全杀毒'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qiannan_antivirus.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('即时通信'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qiannan_imps.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('动漫'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qiannan_comic.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('彩信'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qiannan_mms.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('红包业务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qiannan_redp.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('新业务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qiannan_newbuss.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('其他'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qiannan_other.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
            elif i.count("黔东南") > 0:
                trainPath = 'dataforAppFive/trainDataForApp5Min/kaili/'
                if not os.path.exists(osPath + trainPath):
                    os.mkdir(osPath + trainPath)
                if i.count('网盘云服务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qiandongnan_pan.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('P2P业务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qiandongnan_ptop.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('出行旅游'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qiandongnan_travel.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('邮箱'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qiandongnan_mail.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('音乐'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qiandongnan_music.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('微博'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qiandongnan_weibo.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('财经'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qiandongnan_finance.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('浏览下载'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qiandongnan_down.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('视频直播'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qiandongnan_live.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('VoIP业务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qiandongnan_voip.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('导航'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qiandongnan_navi.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('阅读'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qiandongnan_read.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('支付'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qiandongnan_pay.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('应用商店'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qiandongnan_appshop.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('游戏'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qiandongnan_game.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('购物'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qiandongnan_shopping.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('视频'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qiandongnan_video.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('安全杀毒'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qiandongnan_antivirus.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('即时通信'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qiandongnan_imps.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('动漫'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qiandongnan_comic.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('彩信'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qiandongnan_mms.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('红包业务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qiandongnan_redp.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('新业务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qiandongnan_newbuss.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('其他'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qiandongnan_other.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
            elif i.count("铜仁") > 0:
                trainPath = 'dataforAppFive/trainDataForApp5Min/tongren/'
                if not os.path.exists(osPath + trainPath):
                    os.mkdir(osPath + trainPath)
                if i.count('网盘云服务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_tongren_pan.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('P2P业务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_tongren_ptop.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('出行旅游'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_tongren_travel.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('邮箱'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_tongren_mail.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('音乐'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_tongren_music.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('微博'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_tongren_weibo.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('财经'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_tongren_finance.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('浏览下载'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_tongren_down.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('视频直播'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_tongren_live.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('VoIP业务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_tongren_voip.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('导航'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_tongren_navi.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('阅读'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_tongren_read.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('支付'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_tongren_pay.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('应用商店'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_tongren_appshop.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('游戏'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_tongren_game.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('购物'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_tongren_shopping.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('视频'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_tongren_video.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('安全杀毒'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_tongren_antivirus.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('即时通信'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_tongren_imps.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('动漫'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_tongren_comic.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('彩信'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_tongren_mms.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('红包业务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_tongren_redp.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('新业务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_tongren_newbuss.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('其他'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_tongren_other.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
            elif i.count("毕节") > 0:
                trainPath = 'dataforAppFive/trainDataForApp5Min/bijie/'
                if not os.path.exists(osPath + trainPath):
                    os.mkdir(osPath + trainPath)
                if i.count('网盘云服务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_bijie_pan.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('P2P业务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_bijie_ptop.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('出行旅游'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_bijie_travel.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('邮箱'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_bijie_mail.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('音乐'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_bijie_music.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('微博'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_bijie_weibo.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('财经'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_bijie_finance.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('浏览下载'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_bijie_down.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('视频直播'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_bijie_live.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('VoIP业务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_bijie_voip.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('导航'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_bijie_navi.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('阅读'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_bijie_read.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('支付'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_bijie_pay.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('应用商店'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_bijie_appshop.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('游戏'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_bijie_game.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('购物'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_bijie_shopping.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('视频'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_bijie_video.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('安全杀毒'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_bijie_antivirus.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('即时通信'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_bijie_imps.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('动漫'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_bijie_comic.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('彩信'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_bijie_mms.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('红包业务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_bijie_redp.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('新业务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_bijie_newbuss.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('其他'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_bijie_other.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
            elif i.count("六盘水") > 0:
                trainPath = 'dataforAppFive/trainDataForApp5Min/liupanshui/'
                if not os.path.exists(osPath + trainPath):
                    os.mkdir(osPath + trainPath)
                if i.count('网盘云服务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_liupanshui_pan.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('P2P业务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_liupanshui_ptop.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('出行旅游'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_liupanshui_travel.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('邮箱'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_liupanshui_mail.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('音乐'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_liupanshui_music.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('微博'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_liupanshui_weibo.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('财经'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_liupanshui_finance.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('浏览下载'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_liupanshui_down.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('视频直播'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_liupanshui_live.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('VoIP业务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_liupanshui_voip.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('导航'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_liupanshui_navi.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('阅读'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_liupanshui_read.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('支付'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_liupanshui_pay.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('应用商店'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_liupanshui_appshop.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('游戏'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_liupanshui_game.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('购物'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_liupanshui_shopping.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('视频'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_liupanshui_video.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('安全杀毒'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_liupanshui_antivirus.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('即时通信'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_liupanshui_imps.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('动漫'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_liupanshui_comic.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('彩信'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_liupanshui_mms.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('红包业务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_liupanshui_redp.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('新业务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_liupanshui_newbuss.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('其他'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_liupanshui_other.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
            elif i.count("黔西南") > 0:
                trainPath = 'dataforAppFive/trainDataForApp5Min/xingyi/'
                if not os.path.exists(osPath + trainPath):
                    os.mkdir(osPath + trainPath)
                if i.count('网盘云服务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qianxinan_pan.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('P2P业务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qianxinan_ptop.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('出行旅游'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qianxinan_travel.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('邮箱'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qianxinan_mail.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('音乐'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qianxinan_music.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('微博'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qianxinan_weibo.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('财经'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qianxinan_finance.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('浏览下载'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qianxinan_down.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('视频直播'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qianxinan_live.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('VoIP业务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qianxinan_voip.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('导航'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qianxinan_navi.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('阅读'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qianxinan_read.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('支付'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qianxinan_pay.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('应用商店'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qianxinan_appshop.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('游戏'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qianxinan_game.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('购物'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qianxinan_shopping.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('视频'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qianxinan_video.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('安全杀毒'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qianxinan_antivirus.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('即时通信'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qianxinan_imps.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('动漫'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qianxinan_comic.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('彩信'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qianxinan_mms.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('红包业务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qianxinan_redp.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('新业务'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qianxinan_newbuss.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
                elif i.count('其他'):
                    with codecs.open(osPath + trainPath + 'lteFlowOfApp5Min_qianxinan_other.csv', 'a+',
                                     encoding='utf-8') as f0:
                        f0.write(i)
    except Exception as e:
        print(e)

    os.rename(osPath + fn, osPath + 'dataforAppFive/oldFlow_appfive/' + 'old_' + fn)

for j in fiveMinFile:  # 遍历指定目录

    fn = 'LTE_FLOW_REAL_5MIN_' + j + '.csv'  # 每次测试均需要更改
    f = open(osPath + fn)

    for i in f.readlines():

        trainPath = 'dataforFive/trainDataForFiveMin/'

        if i.split(',')[0]:

            if i.count("贵州") > 0:
                # print(i)
                with codecs.open(osPath + trainPath + 'lteFlowOfFiveMin_guizhou.csv', 'a+', encoding='utf-8') as f0:
                    f0.write(i)
            elif i.count("贵安新区") > 0:
                with codecs.open(osPath + trainPath + 'lteFlowOfFiveMin_guian.csv', 'a+', encoding='utf-8') as f0:
                    f0.write(i)
            elif i.count("贵阳") > 0:
                with codecs.open(osPath + trainPath + 'lteFlowOfFiveMin_guiyang.csv', 'a+', encoding='utf-8') as f0:
                    f0.write(i)
            elif i.count("遵义") > 0:
                with codecs.open(osPath + trainPath + 'lteFlowOfFiveMin_zunyi.csv', 'a+', encoding='utf-8') as f0:
                    f0.write(i)
            elif i.count("安顺") > 0:
                with codecs.open(osPath + trainPath + 'lteFlowOfFiveMin_anshun.csv', 'a+', encoding='utf-8') as f0:
                    f0.write(i)
            elif i.count("都匀") > 0:
                with codecs.open(osPath + trainPath + 'lteFlowOfFiveMin_duyun.csv', 'a+', encoding='utf-8') as f0:
                    f0.write(i)
            elif i.count("凯里") > 0:
                with codecs.open(osPath + trainPath + 'lteFlowOfFiveMin_kaili.csv', 'a+', encoding='utf-8') as f0:
                    f0.write(i)
            elif i.count("铜仁") > 0:
                with codecs.open(osPath + trainPath + 'lteFlowOfFiveMin_tongren.csv', 'a+', encoding='utf-8') as f0:
                    f0.write(i)
            elif i.count("毕节") > 0:
                with codecs.open(osPath + trainPath + 'lteFlowOfFiveMin_bijie.csv', 'a+', encoding='utf-8') as f0:
                    f0.write(i)
            elif i.count("六盘水") > 0:
                with codecs.open(osPath + trainPath + 'lteFlowOfFiveMin_liupanshui.csv', 'a+', encoding='utf-8') as f0:
                    f0.write(i)
            elif i.count("兴义") > 0:
                with codecs.open(osPath + trainPath + 'lteFlowOfFiveMin_xingyi.csv', 'a+', encoding='utf-8') as f0:
                    f0.write(i)

    os.rename(osPath + fn, osPath + 'dataforFive/oldFlow_five/' + 'old_' + fn)

for j in hourFile:  # 遍历指定目录

    fn = 'LTE_FLOW_HOUR_' + j + '.csv'  # 每次测试均需要更改
    f = open(osPath + fn)

    for i in f.readlines():

        trainPath = 'dataforHour/trainDataForHour/'
        if i.split(',')[0]:
            if i.count("贵州") > 0:
                # print(i)
                with codecs.open(osPath + trainPath + 'lteFlowOfHour_guizhou.csv', 'a+', encoding='utf-8') as f0:
                    f0.write(i)
            elif i.count("贵安新区") > 0:
                with codecs.open(osPath + trainPath + 'lteFlowOfHour_guian.csv', 'a+', encoding='utf-8') as f0:
                    f0.write(i)
            elif i.count("贵阳") > 0:
                with codecs.open(osPath + trainPath + 'lteFlowOfHour_guiyang.csv', 'a+', encoding='utf-8') as f0:
                    f0.write(i)
            elif i.count("遵义") > 0:
                with codecs.open(osPath + trainPath + 'lteFlowOfHour_zunyi.csv', 'a+', encoding='utf-8') as f0:
                    f0.write(i)
            elif i.count("安顺") > 0:
                with codecs.open(osPath + trainPath + 'lteFlowOfHour_anshun.csv', 'a+', encoding='utf-8') as f0:
                    f0.write(i)
            elif i.count("都匀") > 0:
                with codecs.open(osPath + trainPath + 'lteFlowOfHour_duyun.csv', 'a+', encoding='utf-8') as f0:
                    f0.write(i)
            elif i.count("凯里") > 0:
                with codecs.open(osPath + trainPath + 'lteFlowOfHour_kaili.csv', 'a+', encoding='utf-8') as f0:
                    f0.write(i)
            elif i.count("铜仁") > 0:
                with codecs.open(osPath + trainPath + 'lteFlowOfHour_tongren.csv', 'a+', encoding='utf-8') as f0:
                    f0.write(i)
            elif i.count("毕节") > 0:
                with codecs.open(osPath + trainPath + 'lteFlowOfHour_bijie.csv', 'a+', encoding='utf-8') as f0:
                    f0.write(i)
            elif i.count("六盘水") > 0:
                with codecs.open(osPath + trainPath + 'lteFlowOfHour_liupanshui.csv', 'a+', encoding='utf-8') as f0:
                    f0.write(i)
            elif i.count("兴义") > 0:
                with codecs.open(osPath + trainPath + 'lteFlowOfHour_xingyi.csv', 'a+', encoding='utf-8') as f0:
                    f0.write(i)

    os.rename(osPath + fn, osPath + 'dataforHour/oldFlow_hour/' + 'old_' + fn)

for j in dayFile:  # 遍历指定目录

    fn = 'LTE_FLOW_DAY_' + j + '.csv'  # 每次测试均需要更改
    f = open(osPath + fn)

    for i in f.readlines():

        trainPath = 'dataforDay/trainDataForDay/'
        if i.split(',')[0]:
            if i.count("贵州") > 0:
                # print(i)
                with codecs.open(osPath + trainPath + 'lteFlowOfDay_guizhou.csv', 'a+', encoding='utf-8') as f0:
                    f0.write(i)
            elif i.count("贵安新区") > 0:
                with codecs.open(osPath + trainPath + 'lteFlowOfDay_guian.csv', 'a+', encoding='utf-8') as f0:
                    f0.write(i)
            elif i.count("贵阳") > 0:
                with codecs.open(osPath + trainPath + 'lteFlowOfDay_guiyang.csv', 'a+', encoding='utf-8') as f0:
                    f0.write(i)
            elif i.count("遵义") > 0:
                with codecs.open(osPath + trainPath + 'lteFlowOfDay_zunyi.csv', 'a+', encoding='utf-8') as f0:
                    f0.write(i)
            elif i.count("安顺") > 0:
                with codecs.open(osPath + trainPath + 'lteFlowOfDay_anshun.csv', 'a+', encoding='utf-8') as f0:
                    f0.write(i)
            elif i.count("都匀") > 0:
                with codecs.open(osPath + trainPath + 'lteFlowOfDay_duyun.csv', 'a+', encoding='utf-8') as f0:
                    f0.write(i)
            elif i.count("凯里") > 0:
                with codecs.open(osPath + trainPath + 'lteFlowOfDay_kaili.csv', 'a+', encoding='utf-8') as f0:
                    f0.write(i)
            elif i.count("铜仁") > 0:
                with codecs.open(osPath + trainPath + 'lteFlowOfDay_tongren.csv', 'a+', encoding='utf-8') as f0:
                    f0.write(i)
            elif i.count("毕节") > 0:
                with codecs.open(osPath + trainPath + 'lteFlowOfDay_bijie.csv', 'a+', encoding='utf-8') as f0:
                    f0.write(i)
            elif i.count("六盘水") > 0:
                with codecs.open(osPath + trainPath + 'lteFlowOfDay_liupanshui.csv', 'a+', encoding='utf-8') as f0:
                    f0.write(i)
            elif i.count("兴义") > 0:
                with codecs.open(osPath + trainPath + 'lteFlowOfDay_xingyi.csv', 'a+', encoding='utf-8') as f0:
                    f0.write(i)

    os.rename(osPath + fn, osPath + 'dataforDay/oldFlow_day/' + 'old_' + fn)

for j in realHourFile:  # 遍历指定目录

    if j.count('TOTAL') > 0:
        fn = 'LTE_FLOW_REAL_' + j + '.csv'  # 每次测试均需要更改
    else:
        fn = 'LTE_FLOW_REAL_HOUR_' + j + '.csv'  # 每次测试均需要更改
    f = open(osPath + fn)

    for i in f.readlines():

        trainPath = 'dataforReal/trainDataForReal/'
        if i.split(',')[0]:
            if i.count("贵州") > 0:
                # print(i)
                with codecs.open(osPath + trainPath + 'lteFlowOfReal_guizhou.csv', 'a+', encoding='utf-8') as f0:
                    f0.write(i)
            elif i.count("贵安新区") > 0:
                with codecs.open(osPath + trainPath + 'lteFlowOfReal_guian.csv', 'a+', encoding='utf-8') as f0:
                    f0.write(i)
            elif i.count("贵阳") > 0:
                with codecs.open(osPath + trainPath + 'lteFlowOfReal_guiyang.csv', 'a+', encoding='utf-8') as f0:
                    f0.write(i)
            elif i.count("遵义") > 0:
                with codecs.open(osPath + trainPath + 'lteFlowOfReal_zunyi.csv', 'a+', encoding='utf-8') as f0:
                    f0.write(i)
            elif i.count("安顺") > 0:
                with codecs.open(osPath + trainPath + 'lteFlowOfReal_anshun.csv', 'a+', encoding='utf-8') as f0:
                    f0.write(i)
            elif i.count("都匀") > 0:
                with codecs.open(osPath + trainPath + 'lteFlowOfReal_duyun.csv', 'a+', encoding='utf-8') as f0:
                    f0.write(i)
            elif i.count("凯里") > 0:
                with codecs.open(osPath + trainPath + 'lteFlowOfReal_kaili.csv', 'a+', encoding='utf-8') as f0:
                    f0.write(i)
            elif i.count("铜仁") > 0:
                with codecs.open(osPath + trainPath + 'lteFlowOfReal_tongren.csv', 'a+', encoding='utf-8') as f0:
                    f0.write(i)
            elif i.count("毕节") > 0:
                with codecs.open(osPath + trainPath + 'lteFlowOfReal_bijie.csv', 'a+', encoding='utf-8') as f0:
                    f0.write(i)
            elif i.count("六盘水") > 0:
                with codecs.open(osPath + trainPath + 'lteFlowOfReal_liupanshui.csv', 'a+', encoding='utf-8') as f0:
                    f0.write(i)
            elif i.count("兴义") > 0:
                with codecs.open(osPath + trainPath + 'lteFlowOfReal_xingyi.csv', 'a+', encoding='utf-8') as f0:
                    f0.write(i)

    os.rename(osPath + fn, osPath + 'dataforReal/oldFlow_real/' + 'old_' + fn)
