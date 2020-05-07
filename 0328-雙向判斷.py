chinese = input ("國文分數:")
eng = input ("英文分數:")
math = input ("數學分數:")
chinese,eng,math=int(chinese),int(eng),int(math)

if (chinese and eng <40) :
    print("留校查看")
else :
    print("過關")

