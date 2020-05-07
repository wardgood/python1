# import qrcode as q
# img=q.make("https://pypi.org/project/qrcode/")

# img.save("my.jpg")
# img.show("my.jpg")

# from qsqrcode.qrcode import Qrcode

# qr = Qrcode('test it')
# qr.generate('testpic/test.png')

# import os
# file="xyz.txt"
# if os.path.exists(file):
#     os.remove(file)
#     print("del ok")
# else:
#     print ("no file")

# folder="ggg"
# if os.path.exists(folder):
#     os.rmdir(folder)
#     print("建立")
# else:
#     os.mkdir(folder)
#     print("存在")

# import os
# file="myfile.txt"
# if os.path.exists(file):
#     os.remove(file)
# else:
#     print(file,"檔案未建立")

# import os
# fname=input("new creat filename")
# fname=fname+".py"
# if not os.path.exists(fname):
#     f=open(fname,"w")
#     f.close()
# else:
#     print("now had")

# import os
# c_path=os.path.dirname(__file__)
# f=os.walk(c_path)
# for x,y,z in f:
#     print("dirname:",x)
#     print("subdir:",y)


# content='''hello python
# 中文字測試
# welcome
# '''

# f=open('file1.txt','w')
# f.write(content)
# f.close()

# f=open('file1.txt','r')

# for line in f:
#     print(line)

# f.close

import os,csv
#csv read
with open('2016gold.csv','r',encoding='utf-8-sig') as csvfile :
   #csv.reader(csvfile)
    x=list(csv.reader(csvfile))
    for row in x:
        if(row[0]=="成長率"):
print(row[0],row[1])
   