from keras.models import Sequential
from keras.layers import Dense, Convolution1D, MaxPool1D, Flatten
from keras import Model
import numpy


def cnn1d(data, num):
    data = numpy.expand_dims(data, 0)
    data = numpy.expand_dims(data, 2)

    model = Sequential()
    model.add(Convolution1D(1, 5, input_shape=(num, 1), activation="relu", name="convolution_1d_layer"))
    # model.add(Convolution1D(32, 3,))
    model.add(MaxPool1D(pool_size=5, strides=1, padding="valid", name="max_pooling_layer"))
    model.add(Flatten(name="reshape_layer"))
    model.add(Dense(5, bias_initializer="random_normal", use_bias=True, name="full_connect_layer"))

    output = Model(inputs=model.input, outputs=model.get_layer('full_connect_layer').output).predict(data)
    print(output)

    print(model.summary())


if __name__ == '__main__':
    cnn1d(numpy.random.normal(size=25), 25)
