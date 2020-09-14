#!/bin/bash
# copy data from home/flow_user
mv  /home/flow_user/lte_flow/*  /flowPredict/lte_flow/

# 提取数据并生成训练集
python3 /flowPredict/kerasmodel/predictflowofhour/theTrainDataCount.py

# 预测流量并写入文件
python3 /flowPredict/kerasmodel/predictflowofhour/testAndTrainData_real.py lteFlowOfReal_guizhou
