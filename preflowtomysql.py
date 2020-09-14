import os
import contrastdata

import pymysql
import os
import codecs
import csv

root = '/Users/fengdong/Downloads/lte_flow01/flowPredictCity'
path = root + '/flowPredict/lte_flow/lostdata/'

list = os.listdir(path)


def get_conn():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='flowPredict', charset='utf8')
    return conn


def insert(cur, sql, args):
    cur.execute(sql, args)


def read_csv_to_mysql(filename, sql):
    with codecs.open(filename=filename, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        print(reader)
        head = next(reader)
        conn = get_conn()
        cur = conn.cursor()

        for item in reader:
            print(item)

            args = tuple(item)
            # print(args)
            # cur.execute(sql=sql, args=args)
            insert(cur, sql=sql, args=args)

        conn.commit()
        cur.close()
        conn.close()


appsql = 'insert into predict_App_flow_five values(%s,%s,%s,%s,%s)'
citysql = 'insert into predict_City_flow_five values(%s,%s,%s,%s,%s)'
ltesql = 'insert into predict_LTE_flow_five values(%s,%s,%s,%s)'

conn = get_conn()
cur = conn.cursor()

if 'dataforAppFive' in list:

    filepath = path + '/dataforAppFive'
    filelist = os.listdir(filepath)
    if 'predictFlow_app' in filelist:

        apppath = path + '/dataforAppFive' + '/predictFlow_app'
        applist = os.listdir(apppath)
        for i in applist:

            cityname = contrastdata.citydata[i]
            citycode = contrastdata.citycode[contrastdata.citydata[i]]

            citypath = path + '/dataforAppFive' + '/predictFlow_app' + '/' + i
            citylist = os.listdir(citypath)

            for j in citylist:
                if j.count('line') > 0:
                    predictdata = []
                    appname = contrastdata.businessdata[j.split('_')[-1].split('.')[0]]

                    f = open(citypath + '/' + j).readlines()
                    pdata = f[-1].split(',')[0].split(':')
                    # pdata = f[-2].split(',')[0].split(':')

                    if len(pdata):

                        predictdata.append(pdata[0])
                        predictdata.append(citycode)
                        predictdata.append(cityname)
                        predictdata.append(appname)
                        predictdata.append(pdata[1])

                        args = tuple(predictdata)
                        # print(args)

                        # insert(cur, sql=appsql, args=args)
                        # cur.execute(sql=appsql, args=args)

if 'dataforCityFive' in list:

    filepath = path + '/dataforCityFive'
    filelist = os.listdir(filepath)
    print(filelist)
    if 'predictFlow_city' in filelist:

        apppath = path + '/dataforCityFive' + '/predictFlow_city'
        applist = os.listdir(apppath)
        for i in applist:

            # print(i)
            cityname = contrastdata.citydata[i]
            citycode = contrastdata.citycode[contrastdata.citydata[i]]

            citypath = path + '/dataforCityFive' + '/predictFlow_city' + '/' + i
            citylist = os.listdir(citypath)

            for j in citylist:
                if j.count('line') > 0:

                    # print(j)
                    predictdata = []
                    appname = contrastdata.quxiandata[j.split('_')[-1].split('.')[0]]

                    f = open(citypath + '/' + j).readlines()
                    pdata = f[-1].split(',')[0].split(':')
                    # pdata = f[-2].split(',')[0].split(':')

                    if len(pdata):
                        predictdata.append(pdata[0])
                        predictdata.append(citycode)
                        predictdata.append(cityname)
                        predictdata.append(appname)
                        predictdata.append(pdata[1])

                        args = tuple(predictdata)
                        print(args)

                        # insert(cur, sql=citysql, args=args)
                        # cur.execute(sql=appsql, args=args)

if 'dataforFive' in list:

    filepath = path + '/dataforFive'
    filelist = os.listdir(filepath)

    if 'predictFlow_five' in filelist:

        apppath = path + '/dataforFive' + '/predictFlow_five'
        applist = os.listdir(apppath)

        for j in applist:

            if j.count('line_') > 0:

                cityname = contrastdata.citydata[j.split('_')[-1].split('.')[0]]
                citycode = contrastdata.citycode[cityname]

                citypath = path + '/dataforFive' + '/predictFlow_five' + '/' + j

                predictdata = []

                f = open(citypath).readlines()
                pdata = f[-1].split(',')[0].split(':')
                # pdata = f[-2].split(',')[0].split(':')

                if len(pdata):
                    predictdata.append(pdata[0])
                    predictdata.append(citycode)
                    predictdata.append(cityname)
                    predictdata.append(pdata[1])

                    args = tuple(predictdata)
                    print(args)

                    insert(cur, sql=ltesql, args=args)
conn.commit()
cur.close()
conn.close()
# print(j)

# print(applist)
