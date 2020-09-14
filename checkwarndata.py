import os

root = ''
root = '/Users/fengdong/Downloads/lte_flow01'
path = root + '/flowPredictCity/lte_flow/dataforCityFive/predictFlow_city'
dirlist = os.listdir(path)

warnpath = root + '/flowPredict/lte_flow/dataforCityFive/warnningdata/'

for city in dirlist:
    citydata = os.listdir(path + '/' + city)
    # print(citydata)
    for i in citydata:

        if i.count('line'):
            # print(i)
            f = open(path + '/' + city + '/' + i).readlines()
            for j in f:
                if j != '':
                    theacc = j.split(':')
                    print(theacc)
                    day = theacc[0]
                    acc = theacc[1]
                    # print (acc)
                    accdata = float(acc[:4])
                    # print(accdata)
                    if accdata < 0.7:
                        with open(warnpath + i, 'a+') as wf:
                            wf.write(str(day) + ':' + str(accdata))
                            wf.write('\n')
                        print(day)
                        print(acc)
