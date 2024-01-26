myStuff = []

f = open("Stuff.mine", "r")
myStuff = eval(f.read())
f.close()

while True:
  pizza_num = int(input("How many pizzas? > "))
  size_num = int(input("What size? > "))

  try:
    cost = pizza_num * size_num
    name = input("Name please > ")
    print(f"Thanks {name}, your pizzas will cost {cost}")
    break
  except Exception as err:
    print("You must input a numerical character, try again.\n" + err)
    continue
row = [name, cost]
myStuff.append(row)

f = open("Stuff.mine", "w")
f.write(str(myStuff))
f.close()
