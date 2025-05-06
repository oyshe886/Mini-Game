import random
computer = random.choice([-1,0,1])
youstr=input("Enter Your Choice: ")
youDict={"s":1 , "w":-1 ,"g":0}
you=youDict[youstr] #choice will convert to number
# Now we have 2 numbers,computer and you
reverseDict={1:"Snake",-1:"Water",0:"Gun"} 
#to convert numbers into word
print(f"You Choose {reverseDict[you]}\nComputer Choose {reverseDict[computer]}")
if(computer==you):
    print("It's a draw")
else:
    if(computer==1 and you==-1):
        print("Computer Wins")
    elif(computer==-1 and you==1):
        print("You Win")
    elif(computer==1 and you==0):
        print("You Win")
    elif(computer==0 and you==1):
        print("Computer Wins")
    elif(computer==-1 and you==0):
        print("Computer Wins")
    elif(computer==0 and you==-1):
        print("You Win")
    else:
        print("Something Went Wrong!")
        
