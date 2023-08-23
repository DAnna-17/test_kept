from pyxlsb import open_workbook as open_xlsb

df = []
d1 = []
t = []
for i in range(16):
    t.append([])

def f():
    a = 0
    with open_xlsb('Table.xlsb') as wb:
        with wb.get_sheet(1) as sheet:
            for row in sheet.rows():
                n = 0
                a += 1
                for item in row:
                    t[n].append(item.v )
                    n += 1
    #print(t[0])
f()
print(t[0][:10])

n = 0

x = []
for i in range(50000):
    x.append('')

for i in t:
    print(9999)
    for k in range(len(i)):
        c = i.count(i[k])
        if c == 1:
            x[k] += str(n) + ' '
        elif c < 1:
            x[k] += 'wtf' + ' '
        else:
            x[k] += 'no' + ' '
        if x[k] == 'no no no no no no no no no no no no no no no ':
            print(k)
    n += 1


with open('text.txt', 'w') as f:
    f.write('\n'.join(x))
