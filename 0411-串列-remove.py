fruit = ["banana","apple","orange","lemon","pieapple"]
print(fruit)
while True :
    arm = input("請輸入多餘不要的水果:")
    if (arm==""):
      break
    n=fruit.count(arm)
    if (n > 0):
        fruit.remove(arm)
        print ("己刪除",arm)
    else:
        print("沒有這種水果喔~~")
    print(fruit)


