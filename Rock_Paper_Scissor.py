import random
try:
    opponent=random.choice([0,1,2])
    youstr=input("Enter Your Choice : ")
    youdict={"r":0 , "p":1 , "s":2}
    you=youdict[youstr] #Choice will covert to number
    reversedict={0:"Rock",1:"Paper",2:"Scissor"} #Number will covert 
    #Now we have 2 numbers
    print(f"You choose {reversedict[you]}\nOpponent choose {reversedict[opponent]}")
    if(opponent==you):
        print("Its a draw")
    else:
        if(opponent==0 and you==1):
            print("You Win")
        elif(opponent==0 and you==2):
            print("Opponent Wins")
        elif(opponent==1 and you==0):
            print("Opponent Wins")
        elif(opponent==1 and you==2):
            print("You Win")
        elif(opponent==2 and you==0):
            print("You Win")
        elif(opponent==2 and you==1):
            print("Opponent Wins")
except Exception as e:
    print("Something Went Wrong ! Please Enter 'r or 'p' or 's' not" ,e)