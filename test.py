with open('fiveMindata5.csv', 'w') as f:
    f.write('day,city,flow' + '\n')
    for i in range(5):

        with open('townlteFlowOfFiveMin.csv', 'r') as fi:
            lines = fi.readlines()
            for line in lines:
                citys = line.split(',')
                f.write(citys[0] + ',' + citys[1] + '_' + str(i) + ',' + citys[2])
            f.write('\n')