import os

import xlwt
import xlrd
import pandas as pd

# 将文本文件转换为Excel再转换为CSV文件
def toCSV(filePath):
    workboot=xlwt.Workbook()
    #创建一个sheet
    sheet=workboot.add_sheet('sheet1',cell_overwrite_ok=True)#第二参数用于确认同一个cell单元是否可以重设值。
    row0 = ['Race', 'colum2']
    #生成第一行
    for i in range(len(row0)):
        sheet.write(0,i,row0[i])

    #对filePath进行处理
    f=open(filePath)
    index=1
    for line in f:
        tmp=line.replace('\t\t','\n')
        data=tmp.split('\n')
        if data[1]=="null":
            continue
        if data[1]==''or data[0]=="null":
            continue
        sheet.write(index,0,data[0])
        sheet.write(index,1,float(data[1])/10000)
        index=index+1
        # print(index)
    workboot.save(filePath+'.xls')
    # 利用pandas把excel转为csv
    data_xls = pd.read_excel(filePath+'.xls', index_col=0)
    data_xls.to_csv(filePath + '.csv', encoding='utf-8')

    # 对数据按照col2进行排序
    train = pd.read_csv(filePath + '.csv', parse_dates=True)
    train.sort_values(by='colum2', ascending=False, inplace=True)
    train.to_csv(filePath + '.csv', encoding='utf-8', index=False)


pathdir='./Data/MySQL1/'
list=os.listdir(pathdir)
for i in range(0,len(list)):
    path=os.path.join(pathdir,list[i])
#    print(path)
    toCSV(path)





