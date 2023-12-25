import random
import os
import time


def rollDice(sides):
  roll = random.randint(1, sides)
  return roll


def stats(dice1, dice2, add):
  health = int(rollDice(dice1) * rollDice(dice2) / 2 + add)
  return health


def characterCreator():

  while True:
    name = input("Name Your Legend:\n")
    type = input("Character Type (Human, Elf, Wizard, Orc):\n")
    print(name + "\n")

    health = stats(6, 12, 10)
    print("HEALTH: " + str(health))

    strength = stats(6, 12, 12)
    print("STRENGTH: " + str(strength))

    next = input("Create another character? (y/n):\n")

    if next == "y":
      continue
    else:
      break
    time.sleep(1)
    os.system("clear")


characterCreator()
