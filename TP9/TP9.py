import readExcel
import CopieCorbone
import CNN1D
import LSTM
# from TP9.CopieCorbone import cc


if __name__ == '__main__':
    # result = readExcel.read_excel("DAT_XLSX_EURUSD_M1_2018.xlsx", 20)
    # readExcel.draw_curve(result)
    # CopieCorbone.cc(result)

    """r = readExcel.read_excel("DAT_XLSX_EURUSD_M1_2018.xlsx", 120)
    data = [r[i][1] for i in range(0, 120)]
    CNN1D.cnn1d(data, 120)"""

    r = readExcel.read_excel("DAT_XLSX_EURUSD_M1_2018.xlsx", 120)
    data = [r[i][1] for i in range(0, 120)]
    LSTM.lstm(data, 120)
