def main():
    import random
    rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
    paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
    scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
    choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    Choice = [rock, paper, scissors]
    print(Choice[choice])
    computer = random.randint(0,2)
    print("Computer chose: \n")
    print(Choice[computer])
    if choice >= 3 or choice < 0:
        print("You enetred an invalid number, please try again.")
    elif choice == 0 and computer == 2:
        print("You win!")
    elif computer == 0 and choice == 2:
        print("You lose")
    elif computer > choice:
        print("You lose")
    elif choice > computer:
        print("You win!")
    elif choice == computer:
        print("It's a draw")        
main()