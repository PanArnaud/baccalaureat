import time
import string
import random

categories = ['girl_name', 'boy_name', 'job', 'color']
players = []
scorePlayers = []
chrono = 120

print("Welcome")
time.sleep(1)
print("Let's set up the game...")

try:
   nbPlayers = int(raw_input("How many people will play ? "))
except ValueError:
   print("That's not a valid value!")

for i in range(1, nbPlayers + 1):
    player = raw_input("Enter a name for player " + str(i) + ": ")
    players.append(player)

print("Time to play !")
time.sleep(1)
print("And we play with the letter...")
time.sleep(1)
letter = random.choice(string.letters)
print(letter + "!")

for player in players:
    print(player + " it's your turn !")
    for category in categories:
        raw_input(category + ": ")
