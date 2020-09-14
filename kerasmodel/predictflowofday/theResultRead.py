file = open('结果集测试.csv')
f = file.readlines()
predict = 0
for i in f:
    data = i.split(',')
    # print(data)
    if (float(data[1]) > float(data[2])):
        predict = float(data[2]) / float(data[1])
    if (float(data[1]) < float(data[2])):
        predict = float(data[1]) / float(data[2])

    print(predict)
