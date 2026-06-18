import random

print("-----Stone-Paper-Sisor Game-----")
print("1 = Stone \n2 = Paper \n3 = Sisor")

user_name = input("Enter user name:")
print (f"user name : {user_name}")


user = int(input ("Enter your choice {1/2/3} :"))
computer= random.randint(1,3)
print('you chose:',user)
print('computer chose:',computer)
#conditions 

if user == computer :
    print ("it's a Draw🤝")

elif (user == 1 and computer == 2):
    print("Computer wins 😔")  

elif (user == 1 and computer == 3):
    print(f"{user_name} wins 🎉")

elif (user == 2 and computer == 1):
    print(f"{user_name} wins 🎉 ")  

elif (user == 2 and computer == 3):
    print("Computer wins 😔")

elif (user == 3 and computer == 2):
    print(f"{user_name} wins🎉")  

elif (user == 3 and computer == 1):
    print("Computer wins 😔")
    
    
print("----------END OF GAME----------")