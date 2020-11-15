import readExcel
import CopieCorbone
from Models import cnn1d, lstm, handle_data, draw_training_and_validation_loss, draw_training_and_validation_error, draw_close_value, draw_prediction_total
# from TP9.CopieCorbone import cc


if __name__ == '__main__':
    # result = readExcel.read_excel("DAT_XLSX_EURUSD_M1_2018.xlsx", 20)
    # readExcel.draw_curve(result)
    # CopieCorbone.cc(result)

    r = readExcel.read_excel("DAT_XLSX_EURUSD_M1_2018.xlsx", 600, readExcel.Type.ALL_DATA)
    data = [[r[i][1]/2, r[i][2]/2, r[i][3]/2, r[i][4]/2] for i in range(0, 600)]
    x_train, y_train, x_test, y_test = handle_data(data)
    # model = cnn1d([5, 4, 1])
    model = lstm([5, 4, 1])
    history = model.fit(x_train, y_train, batch_size=128, epochs=35, validation_split=0.2, verbose=2)
    history_dict = history.history

    """r = readExcel.read_excel("DAT_XLSX_EURUSD_M1_2018.xlsx", 1200)
    data = [r[i][1] for i in range(0, 1200)]
    LSTM.lstm(data)"""

    draw_training_and_validation_loss(history_dict)
    draw_training_and_validation_error(history_dict)

    trainScore = model.evaluate(x_train, y_train, verbose=0)
    testScore = model.evaluate(x_test, y_test, verbose=0)
    p = model.predict(x_test)
    p1 = model.predict(x_train)

    draw_close_value(p, y_test)
    draw_prediction_total(y_train, y_test, p, p1)
