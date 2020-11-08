from datetime import date
from xlrd import open_workbook,xldate_as_tuple
from xlwt import Workbook
import pandas as pd
import matplotlib.pyplot as plt
import pylab


def read_excel(filename, num):
    with open_workbook(filename) as workbook:
        worksheet = workbook.sheet_by_index(0)
        # date_cell = xldate_as_tuple(worksheet.cell_value(0, 0), workbook.datemode)
        # non_date_cell = worksheet.cell_value(0, 1)
        # print(date_cell, non_date_cell)
        result = []
        # for row_index in range(worksheet.nrows):
        for row_index in range(num):
            result.append([])
            date_cell = xldate_as_tuple(worksheet.cell_value(row_index, 0), workbook.datemode)
            # date_cell = date(*date_cell[:3]).strftime('%Y/%m/%d')
            non_date_cell = worksheet.cell_value(row_index, 4)
            result[row_index].append(date_cell)
            result[row_index].append(non_date_cell)
    return result


def draw_curve(data):
    data_length = len(data)
    x = [str(data[i][0][2])+'/'+str(data[i][0][1])+'/'+str(data[i][0][0])+' '+str(data[i][0][3])+':'+str(data[i][0][4]) for i in range(0, data_length)]
    y = [data[i][1] for i in range(0, data_length)]
    plt.plot(x, y, 'ro-')
    plt.title('Close - Time')
    plt.xlabel('time')
    plt.ylabel('close')
    pylab.xticks(rotation=45)
    plt.legend()
    plt.show()
