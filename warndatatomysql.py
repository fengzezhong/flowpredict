import pymysql
import os
import codecs
import csv

root = '/Users/fengdong/Downloads/alarmData/'
apppath = root + 'dataForApp/warnningdata/guizhou/'
citypath = root + 'dataForCity/warnningdata/'

applist = os.listdir(apppath)


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


warnsql = 'insert into warnning_data values(%s,%s,%s,%s,%s,%s,%s,%s)'

conn = get_conn()
cur = conn.cursor()

for i in applist:
    warndata = []
    if i.count('line_') > 0:
        line = open(apppath + i).readlines()[-1].strip()
        data = line.split(',')

        warndata.append(data[0].split(':')[1])
        warndata.append(data[3].split(':')[1])
        warndata.append('业务')
        warndata.append(data[1].split(':')[1])
        warndata.append('')
        warndata.append(data[2].split(':')[1])
        warndata.append(data[4].split(':')[1])
        warndata.append(data[5].split(':')[1])

        insert(cur, sql=warnsql, args=tuple(warndata))
        print(warndata)

citylist = os.listdir(citypath)
for i in citylist:
    countydat = os.listdir(citypath + i)
    for j in countydat:
        warndata = []
        if j.count('line_') > 0:
            # print(j)
            line = open(citypath + i + '/' + j).readlines()[-1].strip()
            data = line.split(',')
            # print(data)
            warndata.append(data[0].split(':')[1])
            warndata.append(data[3].split(':')[1])
            warndata.append('区县')
            warndata.append(data[1].split(':')[1])
            warndata.append(data[2].split(':')[1])
            warndata.append('')
            warndata.append(data[4].split(':')[1])
            warndata.append(data[5].split(':')[1])

            insert(cur, sql=warnsql, args=tuple(warndata))
            print(warndata)

conn.commit()
cur.close()
conn.close()
