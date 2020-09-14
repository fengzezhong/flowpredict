# import pandas as pd
import codecs
import os

# pd_data = pd.read_csv(file)
# print(pd_data)


osPath = os.path.dirname(os.getcwd()) + '/lte_flow/'
print(osPath)
dirlist = os.listdir(osPath)
for j in dirlist:
    if (j.count('DAY') > 0 and j.count('old') == 0):
        # print(j)
        f = open(osPath + j)
        line_num = 0
        for i in f.readlines():
            line_num += 1
            if (line_num != 1):
                trainPath = 'trainDataForDay/'
                if (i.count("贵州") > 0):
                    with codecs.open(osPath + trainPath + 'lteFlowOfDay_guizhou.csv', 'a+', 'utf-8') as f0:
                        f0.write(i)
                elif (i.count("贵安新区") > 0):
                    with codecs.open(osPath + trainPath + 'lteFlowOfDay_guian.csv', 'a+', 'utf-8') as f0:
                        f0.write(i)
                elif (i.count("贵阳") > 0):
                    with codecs.open(osPath + trainPath + 'lteFlowOfDay_guiyang.csv', 'a+', 'utf-8') as f0:
                        f0.write(i)
                elif (i.count("遵义") > 0):
                    with codecs.open(osPath + trainPath + 'lteFlowOfDay_zunyi.csv', 'a+', 'utf-8') as f0:
                        f0.write(i)
                elif (i.count("安顺") > 0):
                    with codecs.open(osPath + trainPath + 'lteFlowOfDay_anshun.csv', 'a+', 'utf-8') as f0:
                        f0.write(i)
                elif (i.count("都匀") > 0):
                    with codecs.open(osPath + trainPath + 'lteFlowOfDay_duyun.csv', 'a+', 'utf-8') as f0:
                        f0.write(i)
                elif (i.count("凯里") > 0):
                    with codecs.open(osPath + trainPath + 'lteFlowOfDay_kaili.csv', 'a+', 'utf-8') as f0:
                        f0.write(i)
                elif (i.count("铜仁") > 0):
                    with codecs.open(osPath + trainPath + 'lteFlowOfDay_tongren.csv', 'a+', 'utf-8') as f0:
                        f0.write(i)
                elif (i.count("毕节") > 0):
                    with codecs.open(osPath + trainPath + 'lteFlowOfDay_bijie.csv', 'a+', 'utf-8') as f0:
                        f0.write(i)
                elif (i.count("六盘水") > 0):
                    with codecs.open(osPath + trainPath + 'lteFlowOfDay_liupanshui.csv', 'a+', 'utf-8') as f0:
                        f0.write(i)
                elif (i.count("兴义") > 0):
                    with codecs.open(osPath + trainPath + 'lteFlowOfDay_xingyi.csv', 'a+', 'utf-8') as f0:
                        f0.write(i)

        os.rename(osPath + j, osPath + 'oldFlow_day/' + 'old_' + j)


    elif (j.count('HOUR') > 0 and j.count('old') == 0):
        f = open(osPath + j)
        line_num = 0
        for i in f.readlines():
            line_num += 1
            if (line_num != 1):
                trainPath = 'trainDataForHour/'
                if (i.count("贵州") > 0):
                    with codecs.open(osPath + trainPath + 'lteFlowOfHour_guizhou.csv', 'a+', 'utf-8') as f0:
                        f0.write(i)
                elif (i.count("贵安新区") > 0):
                    with codecs.open(osPath + trainPath + 'lteFlowOfHour_guian.csv', 'a+', 'utf-8') as f0:
                        f0.write(i)
                elif (i.count("贵阳") > 0):
                    with codecs.open(osPath + trainPath + 'lteFlowOfHour_guiyang.csv', 'a+', 'utf-8') as f0:
                        f0.write(i)
                elif (i.count("遵义") > 0):
                    with codecs.open(osPath + trainPath + 'lteFlowOfHour_zunyi.csv', 'a+', 'utf-8') as f0:
                        f0.write(i)
                elif (i.count("安顺") > 0):
                    with codecs.open(osPath + trainPath + 'lteFlowOfHour_anshun.csv', 'a+', 'utf-8') as f0:
                        f0.write(i)
                elif (i.count("都匀") > 0):
                    with codecs.open(osPath + trainPath + 'lteFlowOfHour_duyun.csv', 'a+', 'utf-8') as f0:
                        f0.write(i)
                elif (i.count("凯里") > 0):
                    with codecs.open(osPath + trainPath + 'lteFlowOfHour_kaili.csv', 'a+', 'utf-8') as f0:
                        f0.write(i)
                elif (i.count("铜仁") > 0):
                    with codecs.open(osPath + trainPath + 'lteFlowOfHour_tongren.csv', 'a+', 'utf-8') as f0:
                        f0.write(i)
                elif (i.count("毕节") > 0):
                    with codecs.open(osPath + trainPath + 'lteFlowOfHour_bijie.csv', 'a+', 'utf-8') as f0:
                        f0.write(i)
                elif (i.count("六盘水") > 0):
                    with codecs.open(osPath + trainPath + 'lteFlowOfHour_liupanshui.csv', 'a+', 'utf-8') as f0:
                        f0.write(i)
                elif (i.count("兴义") > 0):
                    with codecs.open(osPath + trainPath + 'lteFlowOfHour_xingyi.csv', 'a+', 'utf-8') as f0:
                        f0.write(i)

        os.rename(osPath + j, osPath + 'oldFlow_hour/' + 'old_' + j)
