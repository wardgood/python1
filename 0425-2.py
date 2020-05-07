score = int(input('請輸入考試分數 (1-100)：'))

if score > 100:
    print('請勿亂輸入！')
# elif score >= 90 and score <= 100:
#     print('成績：A+')
# elif score >= 80 and score < 90:
#     print('成績：B+')
elif score >= 70 and score < 80:
    print('成績：B')
else:
    print('成績：C')
print("測試")