#!/bin/bash

# 将上传的数据移动到工作目录
#mv  /home/flow_user/lte_flow/*  /flowPredict/lte_flow/

# 提取数据并生成训练集
#python3  /flowPredict/theTrainDataCount.py

# 计算准确率低于70%的值
#python3 /flowPredict/checkwarndata.py


##生成16小时的训练数据
#python3 /flowPredict/kerasmodel/predictflowoffive/createtrainforkerasdata16.py
##训练并预测16小时数据
#python3 /flowPredict/kerasmodel/predictflowoffive/testAndTrainData16.py
##准确率对比并生成写入数据
#python3 /flowPredict/kerasmodel/predictflowoffive/readResultAccuracy16.py


#### 16小时数据加工及预测和写入数据(多元线性模型)
# root = '/Users/fengdong/Downloads/lte_flow01/flowPredictCity/'

#生成训练数据
python3 /Users/fengdong/Downloads/lte_flow01/flowPredictCity/flowPredict/linearmodel/predictflowoffive/createtrainforlinerdata16.py
#生成16小时预测集
python3 /Users/fengdong/Downloads/lte_flow01/flowPredictCity/flowPredict/linearmodel/predictflowoffive/createpredictdata16.py
#训练并预测数据(写入预测文件)
python3 /Users/fengdong/Downloads/lte_flow01/flowPredictCity/flowPredict/linearmodel/predictflowoffive/testPredictFlow16.py
# 计算准确率并写入文件
python3 /Users/fengdong/Downloads/lte_flow01/flowPredictCity/flowPredict/linearmodel/predictflowoffive/readRealAccuracy_line16.py


