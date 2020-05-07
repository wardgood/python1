def getWinner(user, pc):
    user_score = user
    pc_score = pc

    if user_score > 10.5 and pc_score > 10.5:
        return None

    if user_score <= 10.5 and pc_score > 10.5:
        return 'user'

    if user_score > 10.5 and pc_score <= 10.5:
        return 'pc'

    if user_score == pc_score:
        return 'Equal'

    if user_score > pc_score:
        return 'user'
    else:
        return 'pc'

user= int(input("user:"))
pc=int(input("pc:"))
print("贏家:", getWinner(user, pc))