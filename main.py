import random
'''
1 for rock
-1 for paper
0 for scisssors '''

computer = random.choice([-1,0,1])
u = input("enter ur choice:")
youDict = {"r": 1,"p": -1,"s": 0}
reverseDict = {1:"rock", -1 : "paper", 0:"scissors"}

you = youDict[u]

print(f"computer chose {reverseDict[computer]}")

if(computer == you):
    print("its a draw")

else: 
 if(computer == -1 and you == 1):
    print("you loose")
 elif(computer == -1 and you == 0):
    print("you win")
 elif(computer == 1 and you == -1):
    print("you win")
 elif(computer == 1 and you == 0):
    print("you loose")
 elif(computer == 0 and you == -1):
    print("you loose")
 elif(computer == 0 and you == 1):
    print("you win")
 else:
    print("sth went wrong")












