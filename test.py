# path = '/Users/fengdong/Downloads/lte_flow01/flowPredictCity/lte_flow/dataforCityFive/oldFlow_cityfive/old_CITY_FLOW_REAL_5MIN_201908040505.csv'

# line = open(path).readlines()
#
# # def getofonetoeight(line):
# for i in line:
#     alldata = i.strip().split(',')
#     allday = alldata[0]
#     if not (allday[8:10] == '00' or allday[8:10] == '01' or allday[8:10] == '02' \
#             or allday[8:10] == '03' or allday[8:10] == '04' or allday[8:10] == '05' \
#             or allday[8:10] == '06' or allday[8:10] == '07' or allday[8:10] == '08'):
#         print('这是过滤的')
#
#     else:
#         print(i)

import os

path = '/Users/fengdong/Downloads/lte_flow01/flowPredictCity/lte_flow/dataforAppFive/trainDataForApp5Min_end/anshun/'

list = os.listdir(path)
for qu in list:
    # print(qu)
    # xianlist = os.listdir(path + '/' + qu)
    # for i in xianlist:
    xian = qu.split('_')[-1].split('.')[0]
    print(xian)
    # line = open(path).readlines()
    # for i in line:
    #     print(i)
