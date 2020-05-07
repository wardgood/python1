"""
# 建立函數

def pl():                  # 建立pl()函數
   # print("\n====================\n")
   #print("====================")
    print("++++++++++++++++++++")

def p2():
    print("====================")

list1=[20,30,50,77,88]
print(list1[0])
pl()                        # 呼叫pl()函數 
print(list1[2])
pl()
p2()
print(list1[4])
p2()

"""
"""
def pay(money):
    money=money*1.05
    return(money)

x=int(input("請輸入金額:")
spay = pay(x)
p1()
print("毛利:",spay)
p1()
print("加上營收20000後",spay+20000)
"""
"""
#溫度轉換  華氏=攝氏*(9/5)+32  攝氏=(華氏-32)*5/5

def F2C(f):
    f=(f-32)*5/9
    return f
x=F2C(212)
print("計算結果",x)
"""
"""
# 計算面積

def area(w,h):
    calc=w*h
    return calc
x=int(input("請輸入X:"))
y=int(input("請輸入Y:"))
a=area(x,y)
print(a)
"""

# 輸半徑 計算圓面積(pi*r*r)及周長(pi*r)
def calc(r):
     pi=3.14159
     area=pi*r*r
     length=pi*r
     return area,length  # 同時return多個值


r=float(input("輸入半徑"))
area,length=calc(r)
print("你輸入的半徑為:{},面積為:{},園週長為:{}".format(r,area,length))

