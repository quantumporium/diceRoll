import random


diceRoll = True

def showDice():
    diceNumber = int(random.randrange(6))
    dice = ['-', '-', '-', '|', diceNumber, '|', '-', '-', '-']

    show = print(f'{dice[0]}{dice[1]}{dice[2]}\n{dice[3]}{dice[4]}{dice[5]}\n{dice[6]}{dice[7]}{dice[8]}')

    return show

while diceRoll:
    showDice()

    whantRoll = input("do you whant to roll the dice again (yes\\no) ")

    if whantRoll.upper() == 'YES' or whantRoll.upper() == 'Y':
        print("you decided to roll the dice again: ")
    else:
        print("the input you type is not recognized so the the sotwar will close: ")
        diceRoll = False
