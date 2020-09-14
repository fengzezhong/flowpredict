import sys
import os

# # 加入预测地市
# if (len(sys.argv) > 1):
#     citydata = sys.argv[1]
# else:
#     citydata = 'guizhou'

root = ''
# root = '/Users/fengdong/Downloads/lte_flow01'

file_in_path = root + '/flowPredictCity/lte_flow/dataforCityFive/trainDataForCity5Min/'
file_out_path = root + '/flowPredictCity/lte_flow/dataforCityFive/trainDataForCity5Min_end/'
pathlist = os.listdir(file_in_path)

if not os.path.exists(file_out_path):
    os.mkdir(file_out_path)
pathlist_end = os.listdir(file_out_path)

for city in pathlist:

    dirname = file_in_path + city
    dirname_end = file_out_path + city

    if not os.path.exists(dirname_end):
        os.mkdir(dirname_end)

    files = os.listdir(dirname)

    for yewu in files:
        line_num = 0

        with open(dirname + '/' + yewu, 'r') as f_in:
            with open(dirname_end + '/' + yewu, 'w') as f_out:
                for line in f_in:
                    line_num += 1
                    if line_num == 1:
                        print('11111111111')
                        f_out.write('日期,编码,地区,业务类型,流量\n')
                    else:
                        allday = line.strip().split(',')[0]

                        # 跳过度0点到7点数据
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

                        f_out.write(line)
