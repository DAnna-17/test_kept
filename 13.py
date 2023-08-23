from pyxlsb import open_workbook as open_xlsb

df = []
d1 = []
t = []
for i in range(15):
    t.append([])

def f():
    a = 0
    with open_xlsb('Table.xlsb') as wb:
        with wb.get_sheet(1) as sheet:
            for row in sheet.rows():
                for i in row:
                    d1.append(row[i].v)
    #print(t[0])
f()
print(t[0][:10])
y = []
for i in range(15):
    y.append([])
n = 0

x = []
for i in range(100000):
    x.append('')

for i in t:
    print(9999)
    for k in range(len(i)):
        if i.count(i[k]) == 1:
            print(i.count(i[k]))
            x[k] += str(n) + ' '
    n += 1


with open('text.txt', 'w') as f:
    f.write('\n'.join(x))