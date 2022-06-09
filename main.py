import random as rd

result = ["rock", "paper", "scissors"]

user_input = input("Rock, paper, or scissors? Select R, P, or S: ")
user_input = user_input.upper()
print("You selected: " + user_input)

final = rd.choice(result)
print("The computer chose: " + final)

while True:
    if user_input == "R":
        if final == "rock":
            print("You tied!")
            user_input = input("Rock, paper, or scissors? Select R, P, or S: ")
            user_input = user_input.upper()
            print("You selected: " + user_input)
            final = rd.choice(result)
            print("The computer chose: " + final)
            continue
       
        elif final == "paper":
            print("You lost!")
        else:
            print("You won!")
        break
    elif user_input == "P":
        if final == "paper":
            print("You tied!")
            user_input = input("Rock, paper, or scissors? Select R, P, or S: ")
            user_input = user_input.upper()
            print("You selected: " + user_input)
            final = rd.choice(result)
            print("The computer chose: " + final)
            continue
        elif final == "rock":
            print("You won!")
        else:
            print("You lost!")
        break
    elif user_input == "S":
        if final == "scissors":
            print("You tied!")
            user_input = input("Rock, paper, or scissors? Select R, P, or S: ")
            user_input = user_input.upper()
            print("You selected: " + user_input)
            final = rd.choice(result)
            print("The computer chose: " + final)
            continue
        elif final == "rock":
            print("You lost!")
        else:
            print("You won!")
        break
    else:
        print("Invalid input. Try again.")
        user_input = input("Rock, paper, or scissors? Select R, P, or S: ")
        user_input = user_input.upper()
        print("You selected: " + user_input)
        final = rd.choice(result)