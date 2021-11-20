import random

def compare_numbers(number, user_guess):
    number=list(str(number))
    user_guess=str(user_guess)
    cow=0
    bull=0
    cowbull=list()
    for i in range(len(user_guess)):
        if user_guess[i] in number:
            if user_guess[i]==number[i]:
                bull+=1
            else:
                cow+=1
    cowbull.extend([cow,bull])
            
    return cowbull

def repeat(num):
    for i in num:
        repeat=0
        for j in num:
            if i==j:
                repeat+=1
            if repeat>1:  
                return True
    return False

playing = True #gotta play the game
while True:
    number = str(random.randint(1000,9999))#random 4 digit number
    if not repeat(number):
        break
guesses = 0

print("Let's play a game of Cowbull!") #explanation
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number that exists in the sequence but is in wrong place, you get a cow. For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print()
print("Type exit at any prompt to exit.")

while playing:
    user_guess = input("Give me your best guess!: ")
        
    if user_guess == "exit":
        break
    else:
        if len(user_guess)==4:
            if repeat(user_guess):
                print('Do not enter repeating numbers')
                print()
                continue
            else:
                print('game')
                cowbullcount = compare_numbers(number,user_guess)
                guesses+=1
        else:
            print('Your guess should be only 4 digit long.')
            print()
            continue
    print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")
    print()
    if cowbullcount[1]==4:
        playing = False
        print("You win the game after " + str(guesses) + "guesses! The number was "+str(number))
        break #redundant exit
    else:
        print("Your guess isn't quite right, try again.")


    
