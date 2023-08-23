import pandas as pd
from pyxlsb import open_workbook as open_xlsb

df = []
d1 = []
a = []

def f(n):
    with open_xlsb('Table.xlsb') as wb:
        with wb.get_sheet(1) as sheet:
            for row in sheet.rows():
                df.append([row[1].v, row[2].v, row[12].v])


    for i in df:
        if df.count(i) > 1:
            print('auga')
            break
f([0])
