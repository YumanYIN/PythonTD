from keras.models import Sequential
from keras.layers import Dense, LSTM, MaxPool1D, Flatten
from keras import Model
import numpy


def lstm(data, num):
    data = numpy.expand_dims(data, 0)
    data = numpy.expand_dims(data, 2)

    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=(120, 1)))
    model.add(LSTM(16, return_sequences=True))
    model.add(LSTM(10))

    predicted = model.predict(data)
    print(numpy.reshape(predicted, (predicted.size,)))

    print(model.summary())


if __name__ == '__main__':
    lstm(numpy.random.normal(size=120), 10)
