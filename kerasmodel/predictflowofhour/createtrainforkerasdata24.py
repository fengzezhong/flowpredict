import sys

# 加入预测地市
if (len(sys.argv) > 1):
    citydata = sys.argv[1]
else:
    citydata = 'guizhou'

root = ''
# root = '/Users/fengdong/Downloads/lte_flow'

file_in = root + '/flowPredict/lte_flow/trainDataForFiveToHour/lteFlowOfFiveMin_' + citydata + '.csv'
file_out = root + '/flowPredict/lte_flow/realline/kerasdata_train_' + citydata + '24.csv'

# 用于生成之前批量导入的5分钟数据
line_num = 0

with open(file_in, 'r') as f_in:
    with open(file_out, 'w') as f_out:
        for line in f_in:
            line_num += 1
            if line_num == 1:
                f_out.write('日期,编码,地区,流量\n')
            else:

                f_out.write(line)
