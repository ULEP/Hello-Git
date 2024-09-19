import random
seed=int(input("输入一个无符号整数作为种子"))                            #引入种子


def f(x):                                                           #定义投骰子的函数
    code_1 = random.randint(1,7)
    code_2 = random.randint(1,7)
    mark = code_1 + code_2
    return mark



sum=f(seed)                                                        #第一轮投掷
if sum == 7 or sum == 11:
    print(f'点数为{sum},您获胜了,游戏结束')
    input()
elif sum == 2 or sum == 3 or sum == 12 :
    print(f'点数为{sum},您失败了,游戏结束')
    input()
else:                                                             #后续轮次投掷，用while循环直至和数为7或点数等于和数
    while True:
        roll=f(seed)
        sum +=roll
        if sum == 7 :
            print('点数为7,您失败了,游戏结束')
            break
        elif roll==sum :
            print(f'点数为{sum},您获胜了，游戏结束')
            break
        else :
            print(f'点数为{sum},游戏继续')










