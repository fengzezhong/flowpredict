import numpy
import matplotlib.pyplot as plt
from pandas import read_csv
import math
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
import codecs
import os
import sys

# 加入预测地市
if (len(sys.argv) > 1):
    citydata = sys.argv[1]
else:
    citydata = 'anshun'

root = ''
# root = '/Users/fengdong/Downloads/lte_flow'

# load the dataset

print(root + '/flowPredict/lte_flow/realline/kerasdata_train_' + citydata + '24.csv')
# dataframe = read_csv('../../lte_flow/trainDataForHour/lteFlowOfHour_guizhou.csv', usecols=[3], engine='python', skipfooter=0)
dataframe = read_csv(root + '/flowPredict/lte_flow/realline/kerasdata_train_' + citydata + '24.csv', usecols=[3],
                     engine='python',
                     skipfooter=0)
dataset = dataframe.values / 1024
# 将整型变为float
dataset = dataset.astype('float32')

print(dataset)
plt.plot(dataset)
plt.show()


# X is the number of passengers at a given time (t) and Y is the number of passengers at the next time (t + 1).
# convert an array of values into a dataset matrix
def create_dataset(dataset, look_back=1):
    dataX, dataY = [], []
    for i in range(len(dataset) - look_back - 1):
        a = dataset[i:(i + look_back), 0]
        dataX.append(a)
        dataY.append(dataset[i + look_back, 0])
    return numpy.array(dataX), numpy.array(dataY)


# fix random seed for reproducibility
numpy.random.seed(7)

# normalize the dataset
scaler = MinMaxScaler(feature_range=(0, 1))
dataset = scaler.fit_transform(dataset)

# split into train and test sets
train_size = int(len(dataset) * 0.8)
test_size = len(dataset) - train_size
train, test = dataset[0:train_size, :], dataset[train_size:len(dataset), :]

# use this function to prepare the train and test datasets for modeling
look_back = 1
trainX, trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test, look_back)

# reshape input to be [samples, time steps, features]
trainX = numpy.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
testX = numpy.reshape(testX, (testX.shape[0], 1, testX.shape[1]))

# create and fit the LSTM network
model = Sequential()
model.add(LSTM(4, input_shape=(1, look_back)))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(trainX, trainY, epochs=10, batch_size=1, verbose=2)

print(model.__doc__)
# make predictions
trainPredict = model.predict(trainX)
testPredict = model.predict(testX)
# print(testPredict)

# invert predictions
trainPredict = scaler.inverse_transform(trainPredict)
trainY = scaler.inverse_transform([trainY])
testPredict = scaler.inverse_transform(testPredict)
# print(testPredict)

testY = scaler.inverse_transform([testY])

trainScore = math.sqrt(mean_squared_error(trainY[0], trainPredict[:, 0]))
print('Train Score: %.2f RMSE' % (trainScore))
testScore = math.sqrt(mean_squared_error(testY[0], testPredict[:, 0]))
print('Test Score: %.2f RMSE' % (testScore))

# shift train predictions for plotting
trainPredictPlot = numpy.empty_like(dataset)
trainPredictPlot[:, :] = numpy.nan
trainPredictPlot[look_back:len(trainPredict) + look_back, :] = trainPredict

print(testPredict[-1][0])
osPath = os.path.dirname(os.path.dirname(os.getcwd()))
print(osPath)
print(trainPredict[-1][0])
print(trainPredict[-2][0])

# dirlist = os.listdir(osPath)
for i in range(-24, 0):
    with codecs.open(root + '/flowPredict/lte_flow/realline/predictData' + citydata + '_keras24.csv', 'a+') as f0:
        f0.write(str(testPredict[i][0]) + ' , ')
    i -= 1
with codecs.open(root + '/flowPredict/lte_flow/realline/predictData' + citydata + '_keras24.csv', 'a+') as f0:
    f0.write('\n')
# for i in range(len(testPredict)):
#     for j in range(len(testPredict[i])):
#         print(testPredict[i][j])
# shift test predictions for plotting
testPredictPlot = numpy.empty_like(dataset)
testPredictPlot[:, :] = numpy.nan
testPredictPlot[len(trainPredict) + (look_back * 2) + 1:len(dataset) - 1, :] = testPredict

# plot baseline and predictions
plt.plot(scaler.inverse_transform(dataset))
plt.plot(trainPredictPlot, color='g')
plt.plot(testPredictPlot, color='b')
plt.show()

print(testPredict)
print(trainPredict)
