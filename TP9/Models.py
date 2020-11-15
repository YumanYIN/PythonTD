from keras.models import Sequential
from keras.layers import Dense, Conv1D, MaxPooling1D, Flatten, Dropout, LSTM
from keras import Model
import numpy
import matplotlib.pyplot as plt


def handle_data(data):
    result = []
    time_steps = 6
    for i in range(len(data) - time_steps):
        result.append(data[i:i + time_steps])
    result = numpy.array(result)
    train_size = int(0.8 * len(result))
    train = result[:train_size, :]
    x_train = train[:, :-1]
    y_train = train[:, -1][:, -1]
    x_test = result[train_size:, :-1]
    y_test = result[train_size:, -1][:, -1]
    x_train = x_train.reshape(x_train.shape[0], x_train.shape[1], x_train.shape[2])
    x_test = x_test.reshape(x_test.shape[0], x_test.shape[1], x_test.shape[2])
    # return train
    return x_train, y_train, x_test, y_test


def lstm(data):
    model = Sequential()
    # model.add(LSTM(128, input_shape=(data[0], data[1]), return_sequences=True))
    model.add(LSTM(64, input_shape=(data[0], data[1]), return_sequences=False))
    model.add(Dropout(0.5))
    # model.add(Dense(16, activation="relu", kernel_initializer="uniform"))
    # model.add(Dropout(0.2))
    model.add(Dense(1, activation="relu", kernel_initializer="uniform"))
    model.compile(loss='mse', optimizer='adam', metrics=['mae'])
    print(model.summary())
    return model


def cnn1d(data):
    model = Sequential()
    model.add(Dense(128, input_shape=(data[0], data[1])))
    model.add(Conv1D(filters=112, kernel_size=1, padding='valid', activation='relu', kernel_initializer='uniform'))
    model.add(MaxPooling1D(pool_size=2, padding='valid'))
    model.add(Conv1D(filters=64, kernel_size=1, padding='valid', activation='relu', kernel_initializer='uniform'))
    model.add(MaxPooling1D(pool_size=1, padding='valid'))
    model.add(Dropout(0.2))
    model.add(Flatten())
    model.add(Dense(100, activation='relu', kernel_initializer='uniform'))
    model.add(Dense(1, activation='relu', kernel_initializer='uniform'))
    model.compile(loss='mse', optimizer='adam', metrics=['mae'])
    print(model.summary())
    return model


def draw_training_and_validation_loss(history_dict):
    loss_values = history_dict['loss']
    val_loss_values = history_dict['val_loss']
    loss_values50 = loss_values[0:150]
    val_loss_values50 = val_loss_values[0:150]
    epochs = range(1, len(loss_values50) + 1)
    plt.plot(epochs, loss_values50, 'b', color='blue', label='Training loss')
    plt.plot(epochs, val_loss_values50, 'b', color='red', label='Validation loss')
    plt.rc('font', size=18)
    plt.title('Training and validation loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.xticks(epochs)
    fig = plt.gcf()
    fig.set_size_inches(15, 7)
    # fig.savefig('img/tcstest&validationlosscnn.png', dpi=300)
    plt.show()


def draw_training_and_validation_error(history_dict):
    mae = history_dict['mae']
    vmae = history_dict['val_mae']
    epochs = range(1, len(mae) + 1)
    plt.plot(epochs, mae, 'b', color='blue', label='Training error')
    plt.plot(epochs, vmae, 'b', color='red', label='Validation error')
    plt.title('Training and validation error')
    plt.xlabel('Epochs')
    plt.ylabel('Error')
    plt.legend()
    plt.xticks(epochs)
    fig = plt.gcf()
    fig.set_size_inches(15, 7)
    # fig.savefig('img/tcstest&validationerrorcnn.png', dpi=300)
    plt.show()


def draw_close_value(p, y_test):
    plt.plot(p, color='red', label='prediction')
    plt.plot(y_test, color='blue', label='y_test')
    plt.xlabel('No. of Trading Minutes')
    plt.ylabel('Close Value (scaled)')
    plt.legend(loc='upper left')
    fig = plt.gcf()
    fig.set_size_inches(15, 5)
    # fig.savefig('img/tcstestcnn.png', dpi=300)
    plt.show()


# len(y_train)=475, len(y_test)=119, len(p1)=475, len(y)=119
def draw_prediction_total(y_train, y_test, p, p1):
    Y = numpy.concatenate((y_train, y_test), axis=0)
    P = numpy.concatenate((p1, p), axis=0)
    # plotting the complete Y set with predicted values on x_train and x_test(variable p1 & p respectively given above)
    # for
    plt.plot(P[:380], color='red', label='prediction on training samples')
    # for validating samples
    z = numpy.array(range(380, 475))
    plt.plot(z, P[380:475], color='black', label='prediction on validating samples')
    # for testing samples
    x = numpy.array(range(475, 594))
    plt.plot(x, P[475:], color='green', label='prediction on testing samples(x_test)')

    plt.plot(Y, color='blue', label='Y')
    plt.legend(loc='upper left')
    fig = plt.gcf()
    fig.set_size_inches(20, 12)
    plt.show()


if __name__ == '__main__':
    cnn1d(numpy.random.normal(size=25), 25)
