print("Hello, Welcome to the game. ")
score = 0

answer = input("Do you want to play game. ")
if answer.lower() == "yes":
    print("Let's go for the game. ")
else:
    print("Ok, never mind. ")

answer = input("What is the full form of CPU. ")
if answer.lower() == "central processing unit":
    print("Correct! ")
    score += 1
else:
    print("Incorrect! ")

answer = input("What is the full form of GPU. ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print('Incorrect!')

answer = input("What is the full form of RAM. ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the full form of PSU. ")
if answer.lower() == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!") 
    
Total_score = score
print('Game is over. ')
print("You got = " + str(Total_score) + " score in your quiz game. " )
print("You got = " + str((Total_score / 4) * 100) + " %. " )