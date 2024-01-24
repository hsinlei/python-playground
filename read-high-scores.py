import os, time

f = open("high.score", "r")
count = 0
max = 0
winner = ""
while True:
  contents = f.readline().split()
  count += 1
  if contents == "":
    break

  if count == 5:
    print("Current leader is " + winner + " " + str(max))
    break

  if int(contents[1]) > max:
    max = int(contents[1])
    winner = contents[0]

time.sleep(4)
os.system("clear")
