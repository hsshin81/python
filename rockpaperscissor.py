import random

def main():
    user_choice = get_user()
    comp_choice = get_comp()
    compare_choice(user_choice, comp_choice)

def get_comp():
    return random.choice(["Rock", "Paper", "Scissor"])

def get_user():
    return input("Rock, Paper, or Scissor? ")
    
def compare_choice(user, comp):
    if user == comp:
        print("User: ", user, "Comp: ", comp, "You tied.")
        main()
    elif user == "Rock" and comp == "Paper":
        print("User: ", user, "Comp: ", comp, "You lose.")
    elif user == "Rock" and comp == "Scissor":
        print("User: ", user, "Comp: ", comp, "You win.")
    elif user == "Paper" and comp == "Rock":
        print("User: ", user, "Comp: ", comp, "You win.")
    elif user == "Paper" and comp == "Scissor":
        print("User: ", user, "Comp", comp, "You lose.")
    elif user == "Scissor" and comp == "Rock":
        print("User: ", user, "Comp: ", comp, "You lose.")
    elif user == "Scissor" and comp == "Paper":
        print("User: ", user, "Comp: ", comp, "You win.")

main()