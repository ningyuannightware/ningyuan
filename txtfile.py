#开发人员：王宁
#开发时间： 2022/11/4 14:08

import os

"""
创建指定文件名的空txt文件
"""
filedir="E:\cloud2"
filelist= os.listdir(filedir)
with open("test.txt","w+") as txt:
    for num,i in enumerate( filelist):
        oldname=os.path.join(filedir,i)
        filename=".".join(i.split(".")[:-1])
        print(oldname)
        txt.write(oldname+'\r\n')

filedir="E:\cloud2"
filelist= os.listdir(filedir)
for num,i in enumerate( filelist):
    oldname=os.path.join(filedir,i)
    filename=".".join(i.split(".")[:-1])
   # midlename="smoke002_"
    # print(filename[4:])
    newname=os.path.join(filedir,filename+"."+"txt")
    file = open(newname,'w')
    file.close()
    print(newname)
    # os.rename(oldname,newname)