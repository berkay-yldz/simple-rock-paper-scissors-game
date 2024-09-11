import random

rock = """    _______   
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices = [rock, paper, scissors]

user_decision = int(input("rock, paper, scissors... (0, 1, 2): "))

user_choice = choices[user_decision]

random_int = random.randint(0, 2)
machine_choice = choices[random_int]

print(f"Your choice:\n{user_choice}\nMachine choice:\n{machine_choice}")

if user_choice == machine_choice:
    print("Equal...")
elif user_decision == 0:
    if random_int == 1:
        print("You lost.")
    elif random_int == 2:
        print("You Win!")
elif user_decision == 1:
    if random_int == 0:
        print("You win!")
    elif random_int == 2:
        print("You lost.")
elif user_decision == 2:
    if random_int == 0:
        print("You lost.")
    elif random_int == 1:
        print("You win!")
