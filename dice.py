import random

act = 1
while act != 0:
    resoult = random.randint(1,6)
    print("The resoult is : ", resoult)
    act = input('Please tap any key to roll dices again, to exit tap 0: \n')
    act = int(act)
    if (act == 0):
        act = 0
    elif(act != 0):
        act = 1
