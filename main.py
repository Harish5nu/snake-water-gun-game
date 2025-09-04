'''
1 for snake
-1 for water
0 for gun
'''

import random
computer= random.choice([-1, 0, 1])
youstr=input("Enter your choice W or S or G :")
youDict={"s":1, "w":-1,"g":0}
reverseDict={1 :"snake",-1 : "water",0: "Gun"}
you=youDict[youstr]    
print(f"You choose {reverseDict[you]} and Computer choose {reverseDict[computer]}")

# if(computer==-1 and you==1):
#     print("You win.")
# elif(computer==-1 and you==0):
#     print("You lose.")



# elif(computer==1 and you==-1):
#     print("You lose")
# elif(computer==1 and you==0):
#     print("You win")


# elif(computer==0 and you==-1):
#     print("You win")
# elif(computer==0 and you==1):
#     print("You lose")

# elif(computer==you):
#     print("Game draw")
if(computer==you):
    print("Game draw")
elif((computer-you)==-1 or  (computer-you)==2):
    print("You lose.")
else:
    print("You win")