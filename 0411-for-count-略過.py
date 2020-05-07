"""
count =0
for x in range(30):
    if(x%2==0):
        continue
    else:
        print(x)
"""
"""
count =0
for x in range(30):
    if(x%3==0):
        continue
        count+=1
    else:
        print(x)
"""

count =0
for x in range(30):
    if(x%3==0):
        count+=1
        continue
        
    else:
        print(x)
