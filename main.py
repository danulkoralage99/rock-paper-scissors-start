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

user_choice = int(input("What do yu choose? 0 for rock, 1 for paper and 2 siccors"))

computer_choice = random.randint(0,2)

if user_choice == 0:
  print("You chose:")
  print(rock)
elif user_choice == 1:
  print("You chose:")
  print(paper)
else:
  print("You chose:")
  print(scissors)


if computer_choice == 0:
  print("Computer chose:")
  print(rock)
elif computer_choice == 1:
  print("Computer chose:")
  print(paper)
else:
  print("Computer chose:")
  print(scissors)


if user_choice == 0 and computer_choice == 1:
  print("Computer won!")
elif user_choice == 0 and computer_choice == 2:
  print("You won!")
elif user_choice == 1 and computer_choice == 0:
  print("You won!")
elif user_choice == 1 and computer_choice == 2:
  print("Computer won!")
elif user_choice == 2 and computer_choice == 0:
  print("Computer won!")
elif user_choice == 2 and computer_choice == 1:
  print("You won!")
else:
  print("It's a draw try again!")


