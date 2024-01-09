import random

unique_dict = set()

while len(unique_dict) < 8:
  unique_num = random.randint(0, 90)
  unique_dict.add(unique_num)

unique_list = list(unique_dict)

bingo = [[None, None, None], [None, "BINGO", None], [None, None, None]]

count = 0
for i in range(3):
  for j in range(3):
    if bingo[i][j] != "BINGO":
      bingo[i][j] = unique_list[count]
      count += 1
  print(f"{bingo[i][0]:^5} | {bingo[i][1]:^5} | {bingo[i][2]:^5}")
  if i < 2:
    print("---------------------")
