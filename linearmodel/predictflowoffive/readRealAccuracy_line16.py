import sys
import os
import sys

# sys.path.append(r"/Users/fengdong/Downloads/lte_flow01/flowPredictCity/flowPredict/contrastdata.py")
#
# import contrastdata as con

con = {
    "citydata": {
        'anshun': '安顺',
        'bijie': '毕节',
        'duyun': '都匀',
        'guian': '贵安',
        'guiyang': '贵阳',
        'guizhou': '贵州',
        'kaili': '凯里',
        'liupanshui': '六盘水',
        'tongren': '铜仁',
        'xingyi': '兴义',
        'zunyi': '遵义'

    },

    'citycode': {
        '贵州': '85 ',
        '贵安': '850',
        '贵阳': '851',
        '遵义': '852',
        '安顺': '853',
        '都匀': '854',
        '凯里': '855',
        '铜仁': '856',
        '毕节': '857',
        '六盘水': '858',
        '兴义': '859',

    },

    'quxiandata': {
        'duyun': '都匀市',
        'fuquan': '福泉市',
        'libo': '荔波县',
        'luodian': '罗甸县',
        'wengan': '瓮安县',
        'huishui': '惠水县',
        'dushan': '独山县',
        'changshun': '长顺县',
        'pingtang': '平塘县',
        'guiding': '贵定县',
        'longli': '龙里县',
        'sandu': '三都县',
        'hezhang': '赫章县',
        'zhijin': '织金县',
        'bijie': '毕节市',
        'weining': '威宁县',
        'qianxi': '黔西县',
        'jinsha': '金沙县',
        'jinhaihu': '金海湖新区',
        'nayong': '纳雍县',
        'dafang': '大方县',
        'rongjiang': '榕江县',
        'kaili': '凯里市',
        'huangping': '黄平县',
        'danzhai': '丹寨县',
        'tianzhu': '天柱县',
        'jianhe': '剑河县',
        'majiang': '麻江县',
        'jinping': '锦屏县',
        'leishan': '雷山县',
        'sanhui': '三穗县',
        'zhenyuan': '镇远县',
        'taijiang': '台江县',
        'liping': '黎平县',
        'yingong': '岑巩县',
        'congjiang': '从江县',
        'shibing': '施秉县',
        'liuzhi': '六枝县',
        'panzhou': '盘州市',
        'shuicheng': '水城县',
        'zhongshan': '钟山区',
        'guian': '贵安新区',
        'kaiyang': '开阳县',
        'xiaohe': '小河区',
        'huaxi': '花溪区',
        'xifeng': '息烽县',
        'baiyun': '白云区',
        'yunyan': '云岩区',
        'qingzhen': '清镇市',
        'wudang': '乌当区',
        'guanshan': '观山湖区',
        'xiuwen': '修文县',
        'nanming': '南明区',
        'guanling': '关岭县',
        'xixiu': '西秀区',
        'ziyun': '紫云县',
        'puding': '普定县',
        'pingba': '平坝县',
        'zhenning': '镇宁县',
        'bozhou': '播州区',
        'meitan': '湄潭县',
        'honghuag': '红花岗区',
        'fenggang': '凤冈县',
        'wuchuan': '务川县',
        'daozhen': '道真县',
        'chishui': '赤水市',
        'xinpu': '新蒲新区',
        'xishui': '习水县',
        'renhuai': '仁怀市',
        'zhengan': '正安县',
        'huichuan': '汇川区',
        'suiyang': '绥阳县',
        'tongzi': '桐梓县',
        'yuqing': '余庆县',
        'zhenfeng': '贞丰县',
        'qinglong': '晴隆县',
        'xingren': '兴仁县',
        'puan': '普安县',
        'wangmo': '望谟县',
        'xingyi': '兴义市',
        'anlong': '安龙县',
        'ceheng': '册亨县',
        'songtao': '松桃县',
        'jiangkou': '江口县',
        'wanshan': '万山区',
        'yinjiang': '印江县',
        'shiqian': '石阡县',
        'bijiang': '碧江区',
        'yanhe': '沿河县',
        'dejiang': '德江县',
        'yuping': '玉屏县',
        'sinan': '思南县',

    },

    'businessdata' :{
        'down': '浏览下载',
        'comic': '动漫',
        'finance': '财经',
        'antivirus': '安全杀毒',
        'other': '其他',
        'pay': '支付',
        'pan': '网盘云服务',
        'travel': '出行旅游',
        'appshop': '应用商店',
        'video': '视频',
        'imps': '即时通信',
        'shopping': '购物',
        'newbuss': '新业务',
        'redp': '红包业务',
        'game': '游戏',
        'mail': '邮箱',
        'navi': '导航',
        'live': '视频直播',
        'read': '阅读',
        'music': '音乐',
        'weibo': '微博',
        'voip': 'VoIP业务',
        'ptop': 'P2P业务',
        'mms': '彩信',
    }
}

# 加入预测地市
# if (len(sys.argv) > 1):
#     citydata = sys.argv[1]
# else:
#     citydata = 'guizhou'

root = ''
root = '/Users/fengdong/Downloads/lte_flow01/flowPredictCity'

# f_train = open(root + '/flowPredict/lte_flow/trainDataForFiveMin_end/linedata_train_five_' + citydata + '16.csv')
# f_predict = open(root + '/flowPredict/lte_flow/predictFlow_five/predictData_five_' + citydata + '_line16.csv')

trainworkpath = root + '/flowPredict/lte_flow/dataforCityFive/trainDataForCity5Min_end/'
predictworkpath = root + '/flowPredict/lte_flow/dataforCityFive/predictFlow_city/'
warnningpath = root + '/flowPredict/lte_flow/dataforCityFive/warnningdata/'

if not os.path.exists(warnningpath):
    os.mkdir(warnningpath)
citys = os.listdir(trainworkpath)

for x in citys:
    business = os.listdir(trainworkpath + x)
    if not os.path.exists(predictworkpath + x):
        os.mkdir(predictworkpath + x)
    for y in business:

        print(y)
        if y.count('congjiang') > 0 or y.count('jianhe') > 0 or y.count('liping') > 0 or y.count(
                'jinhaihu') > 0 or y.count('guian') > 0:
            print('----------111111111----------------')
        else:
            print('callphone')
        f0 = open(trainworkpath + x + '/' + y).readlines()
        f1 = open(predictworkpath + x + '/' + 'line_' + y).readlines()

        data_train = f0[-1].split(',')[4]
        # print(data_train)
        # '201911151130,854,黔南,都匀市,240870.25'
        # print(f0)
        # print(f1)
        predictall = f1[-2].split(',')[0]

        data_day = predictall.split(':')[0]
        data_predict = predictall.split(':')[1]

        # filename = root + '/flowPredict/lte_flow/predictFlow_five/predictAccuracyOf_five_' + citydata + 'line16.csv'
        filename = warnningpath + x + '/'
        if not os.path.exists(filename):
            os.mkdir(filename)

        with open(filename + 'line_' + y, 'a+') as f:
            flow0 = float(data_train)
            flow1 = float(data_predict)

            if flow0 > flow1:
                arrc = round(flow1 / flow0, 2)
                if arrc < 1:
                    # print(data_day[0:4] + '年' + data_day[4:6] + '月' + data_day[6:8] + '日' + data_day[
                    #                                                                         8:10] + '时' + data_day[
                    #                                                                                       10:13] + '分')
                    quxian = y.split('_')[-1].split('.')[0]
                    msg = '地区:' + con['citydata'][x] + ',' + '区县:' + con['quxiandata'][quxian] + ',' + data_day + ': ' + str(
                        arrc) + '\n'
                    f.write(msg)
                    # print('地区:' + x + ',' +  '区县:' + y + ',' + data_day + ': ' + str(arrc))
                    # client.service.SendIvrData(now, now, '流量预测', 1, 10, 1, 2, sendtime, sendtime, 9000, '13984819884','13984819884', msg, 1, 60, 0, '', '82516', '1', '')
            elif flow0 < flow1:
                arrc = round(flow0 / flow1, 2)
                if arrc < 1:
                    quxian = y.split('_')[-1].split('.')[0]
                    msg = '地区:' + con['citydata'][x] + ',' + '区县:' + con['quxiandata'][quxian] + ',' + data_day + ': ' + str(
                        arrc) + '\n'
                    f.write(msg)
                    # print('地区:' + x + ',' +  '区县:' + y + ',' + data_day + ': ' + str(arrc))
                    # client.service.SendIvrData(now, now, '流量预测', 1, 10, 1, 2, sendtime, sendtime, 9000, '13984819884','13984819884', msg, 1, 60, 0, '', '82516', '1', '')
            else:
                print('1')
                f.write('地区:' + x + ',' + '区县:' + y.split('_')[-1].split('.')[0] + ',' + data_day + ': ' + str(
                    '1.0') + '\n')
