import os

Race={}
dirpath='C:\\Users\\asus\\Desktop\\Race数据\\mysqllog\\r100\\'
list=os.listdir(dirpath)

for i in range(len(list)):
    f = open(dirpath + list[i])
    next(f)
    lines = f.readlines()
    for line in lines:
        if line != '\n':
            data = line.split("\t\t")
            key = data[0]
            key = hex(int(key[4:]))
            value = data[1]
            value = int(value[6:])
            if key in Race.keys():
                Race[key] += value
            else:
                Race[key] = value
    f.close()
print(len(Race))

Race_order=sorted(Race.items(),key=lambda x:x[1],reverse=True)
file = "./Data/MySQL/r100"
f = open(file, "w")
for i in range(len(Race_order)):
    k=str(Race_order[i][0])
    v=str(Race_order[i][1])
    f.writelines(k+'\t\t'+v+'\n')
f.close()

