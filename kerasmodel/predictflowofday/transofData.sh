#!/bin/bash

# 移动上传的数据到工作目录
cp -r /home/flow_user/lte_flow/* /flowPredict/lte_flow/

# 提取数据并生成训练集
python3 /flowPredict/kerasmodel/predictflowofday/theTrainDataCount.py
#执行天粒度预测

#执行小时粒度预测
