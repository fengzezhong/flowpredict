import pymysql
import os
import codecs
import csv

# path = '/Users/fengdong/Downloads/lte_flow01/flowPredictCity/lte_flow/'
path = '/Users/fengdong/Downloads/lte_flow01/flowPredictCity/flowPredict/lte_flow/lostdata/'
list = os.listdir(path)


def get_conn():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='flowPredict', charset='utf8')
    return conn


def insert(cur, sql, args):
    cur.execute(sql, args)


def read_csv_to_mysql(filename, sql):
    conn = get_conn()
    cur = conn.cursor()

    # f = open(filename).readlines()
    #
    # for i in f:
    #     print(i)

    with codecs.open(filename=filename, mode='rb', encoding='utf-8') as f:
        reader = csv.reader(f)
        # print(reader)
        # head = next(reader)

        # lines = f.readlines()

        i = 0
        print(filename)
        for item in reader:
            i = i + 1
            if i > 1:

                # print(item)
                args = tuple(item)
                insert(cur, sql=sql, args=args)
                print(args)

    conn.commit()
    cur.close()
    conn.close()


for i in list:
    # print(path+i)
    if os.path.isfile(path + i):
        # print(path + i)
        # f = open(path + i).readlines()
        if i.count('APP_FLOW_REAL_5MIN'):
            sql = 'insert into App_flow_five values(%s,%s,%s,%s,%s)'
        elif i.count('CITY_FLOW_REAL_5MIN'):
            sql = 'insert into City_flow_five values(%s,%s,%s,%s,%s)'
        elif i.count('LTE_FLOW_REAL_5MIN'):
            sql = 'insert into LTE_flow_five values(%s,%s,%s,%s)'

        read_csv_to_mysql(path + i, sql)

    # elif os.path.isdir(path+i):
    #     print(path+i)
