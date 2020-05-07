# n = 83  # 隻
# f = 240  # 總腳數
#
ans = 47
min = 0
max = 100
count=0
while True:
    guess = int(input('請輸入數字 %d ~ %d :' % (min, max)))
    count += 1
    if guess == ans:
        print('恭喜答對')

        break;
    else:
        pass
print("guess timer",count)