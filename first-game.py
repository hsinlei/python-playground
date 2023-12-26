import random
import os
import time


def rollDice(sides):
  roll = random.randint(1, sides)
  return roll


def stats(dice1, dice2, add):
  stat = int(rollDice(dice1) * rollDice(dice2) / 2 + add)
  return stat


def characterCreator():
  round = 1
  name = input("Name Your Legend:\n")
  type = input("Character Type (Human, Elf, Wizard, Orc):\n")
  print("\n" + name)
  health_1 = stats(6, 12, 10)
  print("HEALTH: " + str(health_1))
  strength_1 = stats(6, 12, 12)
  print("STRENGTH: " + str(strength_1))

  next = input("Who are they battling?\n\n Name your Legend:")
  type = input("Character Type (Human, Elf, Wizard, Orc):\n")

  print("\n" + next)
  health_2 = stats(6, 12, 10)
  print("HEALTH: " + str(health_2))
  strength_2 = stats(6, 12, 12)
  print("STRENGTH: " + str(strength_2))
  time.sleep(3)
  os.system("clear")

  while True:
    print("⚔️ BATTLE TIME ⚔️")
    c1 = rollDice(6)
    c2 = rollDice(6)
    damage = abs(strength_1 - strength_2) + 1
    if c1 > c2:
      health_2 -= damage
    elif c2 > c1:
      health_1 -= damage
    print(name + "\n Health:" + str(health_1))
    print(next + "\n Health:" + str(health_2))
    round += 1
    if health_1 < 1:
      print("Oh no " + name + " has died after" + str(round) + "rounds!")
      break
    elif health_2 < 1:
      print("Oh no " + next + " has died after" + str(round) + "rounds!")
      break
    else:
      print("And they're both standing for the next round!")
      continue
    time.sleep(1)
    os.system("clear")


characterCreator()