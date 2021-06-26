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
gameList=[rock,paper,scissors]
print("Welcome to the rock, paper and scissors game!")
user=int(input("Type in a choice 0,1,2 which stands for rock, paper, scissors respectively: "))
if user>2 or user<0:
  print("Invalid number")
else:
  print(f"Your choice:\n{gameList[user]}")
  computer=random.randint(0,2)
  print(f"Computer chose:\n{gameList[computer]}")
  if user==0 and computer==1:
    print("Computer won!")
  elif user==0 and computer==2:
    print("You won!")
  elif user==1 and computer==0:
    print("You won!")
  elif user==1 and computer==2:
    print("Computer won!")
  elif user==2 and computer==0:
    print("Computer won!")
  elif user==2 and computer==1:
    print("You won!")
  elif user==computer:
    print("Game Draw")
