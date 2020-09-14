import sys

# 加入预测地市
if (len(sys.argv) > 1):
    citydata = sys.argv[1]
else:
    citydata = 'guizhou'

root = ''
# root = '/Users/fengdong/Downloads/lte_flow'

file_in = root + '/flowPredict/lte_flow/trainDataForFiveToHour/lteFlowOfFiveMin_' + citydata + '.csv'
file_out = root + '/flowPredict/lte_flow/realline/kerasdata_train_' + citydata + '16.csv'

# 用于生成之前批量导入的5分钟数据
line_num = 0

with open(file_in, 'r') as f_in:
    with open(file_out, 'w') as f_out:
        for line in f_in:
            line_num += 1
            if line_num == 1:
                f_out.write('日期,编码,地区,流量\n')
            else:
                allday = line.strip().split(',')[0]
                # 跳过度0点到7点数据
                if allday[8:10] == '00':
                    continue
                if allday[8:10] == '01':
                    continue
                if allday[8:10] == '02':
                    continue
                if allday[8:10] == '03':
                    continue
                if allday[8:10] == '04':
                    continue
                if allday[8:10] == '05':
                    continue
                if allday[8:10] == '06':
                    continue
                if allday[8:10] == '07':
                    continue

                f_out.write(line)
