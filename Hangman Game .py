time_6 = '''
  +---+
  |   |
      |
      |
      |
      |
========='''

time_5 = '''
  +---+
  |   |
  O   |
      |
      |
      |
========='''

time_4 = '''
  +---+
  |   |
  O   |
  |   |
      |
      |
========='''

time_3 = '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
========='''

time_2 =  '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
========='''

time_1 = '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========='''

import time
import random
distances = []
words = ["good", "bad", "ugly"]
random_word = random.choice(words)
for x in random_word:
  distances.append("_")
print(" ".join(distances))
times = 6
print(time_6)
while "_" in distances:
  if times > 0:
    guessed = input("Please guess a letter: ").lower()
    for position in range(len(random_word)):
        if random_word[position] == guessed:
          distances[position] = guessed
    if guessed in distances:
      print(f"You have {times} lives left")
      print(" ".join(distances))
    else:
      times -= 1
      print(f"You have {times} lives left")
      print(" ".join(distances))
    if times == 6:
      print(time_6)
    elif times == 5:
      print(time_5)
    elif times == 4:
      print(time_4)
    elif times == 3:
      print(time_3)
    elif times == 2:
      print(time_2)
    elif times == 1:
      print(time_1)
  else:
    print("You lose")
    print('''
           +---+
           |   |
           O   |
          /|\  |
          / \  |
               |
         =========''')
    time.sleep(2)
    break
if "_" not in distances:
  print("You win")
  time.sleep(2)