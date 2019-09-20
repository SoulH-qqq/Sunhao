import pandas as pd
import csv
import os
import xlwt
import xlrd

#def mergeCSV():

pathdir = './Data/MySQL/'
list = os.listdir(pathdir)
index = 0
race={}
print( list)
#将所有种race加到race字典中
for i in range(0,len(list)):
    with open(pathdir + list[i], 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = [row['Race'] for row in reader]
        for j in range(0, len(rows)):
            if rows[j] in race.values():
                continue
            else:
                race[index] = rows[j]
                index = index + 1
    print(len(race))
length=len(race)

#创建合并的csv
workbook=xlwt.Workbook()
#创建一个sheet
sheet=workbook.add_sheet('sheet1',cell_overwrite_ok=True)#第二参数用于确认同一个cell单元是否可以重设值
#创建第一行
row0 = [0 for i in range(len(list)+1)]
row0=['Race','pct','r10','r20','r30','r40','r50','r60','r70','r80','r90','r100',\
         'm1r10','m1r20','m1r30','m1r40','m1r50','m1r60','m1r70','m1r80','m1r90','m1r100',\
         'm2r10','m2r20','m2r30','m2r40','m2r50','m1r60','m2r70','m2r80','m2r90','m2r100',\
         'm3r10','m3r20','m3r30','m3r40','m3r50','m3r60','m3r70','m3r80','m3r90','m3r100']
for i in range(len(row0)):
    sheet.write(0,i,row0[i])
print(row0)

#写入第一列
for i in range(0,length):
    sheet.write(i+1,0,race[i])

#写入其他列
#先将其他列全置为0
for i in range(0,length):
    for j in range(0,len(list)):
        sheet.write(i+1,j+1,0)


for p in range(1,len(row0)):
    with open(pathdir + row0[p]+'.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        rowR = []
        rowV = []
        for row in reader:
            rowR.append(row['Race'])
            rowV.append(row['colum2'])
    for i in range(0, len(rowR)):
        for it, val in race.items():
            if val == rowR[i]:
                # print(it)
                break
        sheet.write(it + 1,p, rowV[i])
    csvfile.close()
    print(row0[p])

workbook.save(pathdir+'MySQL.xls')




